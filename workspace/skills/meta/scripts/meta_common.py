#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

GRAPH_VERSION = "v21.0"
BASE_URL = f"https://graph.facebook.com/{GRAPH_VERSION}/"

DEFAULTS = {
    "business_manager_id": "287659180931920",
    "system_user_id": "61584969418636",
    "page_id": "1700329636926546",
    "instagram_account_id": "17841415739993320",
    "ad_account_id": "286631686227626",
    "domain": "oviond.com",
    "currency": "ZAR",
}

TOKEN_ENV_NAMES = [
    "META_TOKEN",
    "META_ACCESS_TOKEN",
    "META_SYSTEM_USER_TOKEN",
]
TOKEN_PATHS = [
    Path("/data/.openclaw/secrets/meta-token.txt"),
]


@dataclass
class MetaAPIError(RuntimeError):
    message: str
    status: int | None = None
    code: int | None = None
    error_subcode: int | None = None
    error_type: str | None = None
    raw: Any = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "message": self.message,
            "status": self.status,
            "code": self.code,
            "error_subcode": self.error_subcode,
            "type": self.error_type,
            "raw": self.raw,
        }

    def __str__(self) -> str:
        bits = [self.message]
        if self.status:
            bits.append(f"status={self.status}")
        if self.code is not None:
            bits.append(f"code={self.code}")
        if self.error_subcode is not None:
            bits.append(f"subcode={self.error_subcode}")
        return " | ".join(bits)


def load_system_token() -> str:
    for name in TOKEN_ENV_NAMES:
        value = os.getenv(name, "").strip()
        if value:
            return value
    for path in TOKEN_PATHS:
        if path.exists():
            value = path.read_text(encoding="utf-8").strip()
            if value:
                return value
    raise MetaAPIError(
        "No Meta system-user access token found. Set META_TOKEN or provide /data/.openclaw/secrets/meta-token.txt."
    )


def ensure_act_prefix(account_id: str | None = None) -> str:
    raw = str(account_id or DEFAULTS["ad_account_id"])
    return raw if raw.startswith("act_") else f"act_{raw}"


def utc_today() -> date:
    return datetime.now(timezone.utc).date()


def date_window(days: int, *, until: date | None = None) -> tuple[str, str]:
    if days <= 0:
        raise ValueError("days must be > 0")
    end = until or utc_today()
    start = end - timedelta(days=days - 1)
    return start.isoformat(), end.isoformat()


def previous_window(since: str, until: str) -> tuple[str, str]:
    start = date.fromisoformat(since)
    end = date.fromisoformat(until)
    span = (end - start).days + 1
    prev_end = start - timedelta(days=1)
    prev_start = prev_end - timedelta(days=span - 1)
    return prev_start.isoformat(), prev_end.isoformat()


def _coerce_param(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list)):
        return json.dumps(value, separators=(",", ":"))
    return str(value)


def _json_loads_safe(raw: str) -> Any:
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"raw": raw}


def _handle_error(status: int, payload: Any) -> MetaAPIError:
    if isinstance(payload, dict):
        err = payload.get("error", {})
        return MetaAPIError(
            message=err.get("message") or "Meta API request failed",
            status=status,
            code=err.get("code"),
            error_subcode=err.get("error_subcode"),
            error_type=err.get("type"),
            raw=payload,
        )
    return MetaAPIError(message="Meta API request failed", status=status, raw=payload)


def fetch_json_url(url: str, *, timeout: int = 60) -> Any:
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = _json_loads_safe(response.read().decode("utf-8"))
            if response.status >= 400:
                raise _handle_error(response.status, payload)
            return payload
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        payload = _json_loads_safe(body)
        raise _handle_error(exc.code, payload) from exc


def graph_request(
    path: str,
    params: dict[str, Any] | None = None,
    *,
    method: str = "GET",
    token: str | None = None,
    timeout: int = 60,
) -> Any:
    token = token or load_system_token()
    payload = {k: _coerce_param(v) for k, v in (params or {}).items() if v is not None}
    payload["access_token"] = token

    url = urllib.parse.urljoin(BASE_URL, path.lstrip("/"))
    method = method.upper()

    if method == "GET":
        url = f"{url}?{urllib.parse.urlencode(payload)}"
        request = urllib.request.Request(url, method="GET")
        data = None
    else:
        data = urllib.parse.urlencode(payload).encode("utf-8")
        request = urllib.request.Request(url, data=data, method=method)

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            body = _json_loads_safe(raw)
            if response.status >= 400:
                raise _handle_error(response.status, body)
            return body
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        body = _json_loads_safe(raw)
        raise _handle_error(exc.code, body) from exc


def paginate(
    path: str,
    params: dict[str, Any] | None = None,
    *,
    token: str | None = None,
    page_limit: int = 50,
) -> list[dict[str, Any]]:
    token = token or load_system_token()
    merged = dict(params or {})
    if "limit" not in merged:
        merged["limit"] = 100

    first = graph_request(path, merged, token=token)
    rows = list(first.get("data", []))
    paging = first.get("paging", {}) if isinstance(first, dict) else {}
    next_url = paging.get("next")
    pages = 1

    while next_url and pages < page_limit:
        page = fetch_json_url(next_url)
        rows.extend(page.get("data", []))
        paging = page.get("paging", {}) if isinstance(page, dict) else {}
        next_url = paging.get("next")
        pages += 1

    return rows


def get_page_token(
    page_id: str | None = None,
    *,
    system_token: str | None = None,
) -> str:
    data = graph_request(
        str(page_id or DEFAULTS["page_id"]),
        {"fields": "id,name,access_token"},
        token=system_token or load_system_token(),
    )
    token = data.get("access_token")
    if not token:
        raise MetaAPIError("Meta returned no page access token.", raw=data)
    return token


def float_or_none(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def int_or_none(value: Any) -> int | None:
    if value in (None, ""):
        return None
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return None


def action_map(items: Iterable[dict[str, Any]] | None) -> dict[str, float]:
    result: dict[str, float] = {}
    for item in items or []:
        key = item.get("action_type")
        if not key:
            continue
        result[key] = result.get(key, 0.0) + (float_or_none(item.get("value")) or 0.0)
    return result


def clean_action_map(items: Iterable[dict[str, Any]] | None) -> dict[str, float]:
    cleaned: dict[str, float] = {}
    for key, value in action_map(items).items():
        if float(value).is_integer():
            cleaned[key] = int(value)
        else:
            cleaned[key] = round(value, 4)
    return cleaned


def extract_action_value(row: dict[str, Any], action_type: str, *, source: str = "actions") -> float:
    return action_map(row.get(source)).get(action_type, 0.0)


def numeric_delta(current: float | None, previous: float | None) -> dict[str, Any]:
    if current is None or previous is None:
        return {"absolute": None, "percent": None}
    absolute = current - previous
    percent = None if previous == 0 else (absolute / previous) * 100.0
    return {
        "absolute": round(absolute, 4),
        "percent": None if percent is None else round(percent, 2),
    }


def sanitize_row(row: dict[str, Any]) -> dict[str, Any]:
    cleaned = dict(row)
    if "actions" in cleaned:
        cleaned["actions"] = clean_action_map(cleaned.get("actions"))
    if "cost_per_action_type" in cleaned:
        cleaned["cost_per_action_type"] = clean_action_map(cleaned.get("cost_per_action_type"))
    if "outbound_clicks" in cleaned:
        cleaned["outbound_clicks"] = clean_action_map(cleaned.get("outbound_clicks"))
    return cleaned


def print_json(data: Any) -> None:
    json.dump(data, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
