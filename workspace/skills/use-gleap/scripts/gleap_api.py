#!/usr/bin/env python3
"""Minimal Gleap API helper for skill-driven operations.

Usage examples:
  python3 scripts/gleap_api.py probe
  python3 scripts/gleap_api.py request GET /tickets --query limit=3 --query sort=-updatedAt
  python3 scripts/gleap_api.py request PUT /tickets/TICKET_ID --data '{"status":"DONE"}'

Credentials are read from env by default:
  GLEAP_API_KEY
  GLEAP_PROJECT_ID
  GLEAP_BASE_URL (optional, defaults to https://api.gleap.io/v3)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Iterable

DEFAULT_BASE_URL = "https://api.gleap.io/v3"
DEFAULT_TIMEOUT = 30


class GleapApiError(RuntimeError):
    pass


def _require(value: str | None, label: str) -> str:
    if value:
        return value
    raise GleapApiError(f"Missing {label}. Set the env var or pass the flag explicitly.")


def _parse_pairs(values: Iterable[str] | None, label: str) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for raw in values or []:
        if "=" not in raw:
            raise GleapApiError(f"Invalid {label} '{raw}'. Expected KEY=VALUE.")
        key, value = raw.split("=", 1)
        pairs.append((key, value))
    return pairs


def _load_json_data(raw: str | None) -> Any:
    if raw is None:
        return None
    if raw.startswith("@"):
        with open(raw[1:], "r", encoding="utf-8") as handle:
            return json.load(handle)
    return json.loads(raw)


def _normalize_path(path: str) -> str:
    return "/" + path.lstrip("/")


def gleap_request(
    method: str,
    path: str,
    *,
    api_key: str,
    project_id: str,
    base_url: str = DEFAULT_BASE_URL,
    query: list[tuple[str, str]] | None = None,
    data: Any = None,
    headers: list[tuple[str, str]] | None = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> Any:
    url = base_url.rstrip("/") + _normalize_path(path)
    if query:
        url += "?" + urllib.parse.urlencode(query, doseq=True)

    request_headers = {
        "Authorization": f"Bearer {api_key}",
        "Project": project_id,
        "Accept": "application/json",
        "User-Agent": "OpenClaw-Gleap-Skill/1.0",
    }
    for key, value in headers or []:
        request_headers[key] = value

    body: bytes | None = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        request_headers["Content-Type"] = "application/json"

    request = urllib.request.Request(
        url,
        data=body,
        headers=request_headers,
        method=method.upper(),
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = response.read().decode("utf-8")
            if not payload.strip():
                return None
            content_type = response.headers.get("Content-Type", "")
            if "json" in content_type.lower() or payload.strip().startswith(("{", "[")):
                return json.loads(payload)
            return payload
    except urllib.error.HTTPError as exc:
        body_text = exc.read().decode("utf-8", errors="replace")
        raise GleapApiError(
            f"HTTP {exc.code} {exc.reason} for {method.upper()} {path}\n{body_text}"
        ) from exc
    except urllib.error.URLError as exc:
        raise GleapApiError(f"Request failed for {method.upper()} {path}: {exc}") from exc


def _extract_count(payload: Any) -> int | None:
    if isinstance(payload, list):
        return len(payload)
    if isinstance(payload, dict):
        for key in ("totalCount", "count", "total", "length"):
            value = payload.get(key)
            if isinstance(value, int):
                return value
        for key in ("tickets", "items", "data", "results", "users", "teams"):
            value = payload.get(key)
            if isinstance(value, list):
                return len(value)
    return None


def _extract_ticket_list(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        tickets = payload.get("tickets")
        if isinstance(tickets, list):
            return [item for item in tickets if isinstance(item, dict)]
        data = payload.get("data")
        if isinstance(data, list):
            return [item for item in data if isinstance(item, dict)]
    return []


def cmd_request(args: argparse.Namespace) -> int:
    api_key = _require(args.api_key or os.getenv("GLEAP_API_KEY"), "GLEAP_API_KEY")
    project_id = _require(
        args.project_id or os.getenv("GLEAP_PROJECT_ID"), "GLEAP_PROJECT_ID"
    )
    base_url = args.base_url or os.getenv("GLEAP_BASE_URL") or DEFAULT_BASE_URL

    payload = gleap_request(
        args.method,
        args.path,
        api_key=api_key,
        project_id=project_id,
        base_url=base_url,
        query=_parse_pairs(args.query, "query argument"),
        data=_load_json_data(args.data),
        headers=_parse_pairs(args.header, "header argument"),
        timeout=args.timeout,
    )
    if args.raw and isinstance(payload, str):
        print(payload)
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=args.sort_keys))
    return 0


def cmd_probe(args: argparse.Namespace) -> int:
    api_key = _require(args.api_key or os.getenv("GLEAP_API_KEY"), "GLEAP_API_KEY")
    project_id = _require(
        args.project_id or os.getenv("GLEAP_PROJECT_ID"), "GLEAP_PROJECT_ID"
    )
    base_url = args.base_url or os.getenv("GLEAP_BASE_URL") or DEFAULT_BASE_URL

    targets: list[tuple[str, str, list[tuple[str, str]] | None]] = [
        ("permissions", "/users/me/permissions", None),
        ("users", "/projects/users", None),
        ("teams", "/teams", None),
        ("ticket_count", "/tickets/ticketscount", None),
        (
            "sample_tickets",
            "/tickets",
            [
                ("limit", str(args.ticket_limit)),
                ("sort", "-updatedAt"),
                ("ignoreArchived", "true"),
            ],
        ),
    ]
    if not args.skip_helpcenter:
        targets.append(("helpcenter_collections", "/helpcenter/collections/all", None))
    if not args.skip_unified_inbox:
        targets.append(
            (
                "unified_inbox",
                "/users/unified-inbox",
                [("limit", str(args.inbox_limit))],
            )
        )

    results: dict[str, Any] = {}
    errors: dict[str, str] = {}

    for name, path, query in targets:
        try:
            results[name] = gleap_request(
                "GET",
                path,
                api_key=api_key,
                project_id=project_id,
                base_url=base_url,
                query=query,
                timeout=args.timeout,
            )
        except GleapApiError as exc:
            errors[name] = str(exc)

    tickets = _extract_ticket_list(results.get("sample_tickets"))
    statuses = sorted({t.get("status") for t in tickets if t.get("status")})
    types = sorted({t.get("type") for t in tickets if t.get("type")})
    priorities = sorted({t.get("priority") for t in tickets if t.get("priority")})
    teams = results.get("teams") if isinstance(results.get("teams"), list) else []
    users = results.get("users") if isinstance(results.get("users"), list) else []
    permissions = results.get("permissions") if isinstance(results.get("permissions"), dict) else {}

    summary = {
        "base_url": base_url,
        "project_id": project_id,
        "auth": {
            "permissions_ok": "permissions" in results,
            "roles": permissions.get("roles", []),
            "permissions_count": len(permissions.get("permissions", []) or []),
        },
        "users": {
            "count": len(users),
            "sample": users[: min(5, len(users))],
        },
        "teams": {
            "count": len(teams),
            "sample": teams[: min(5, len(teams))],
        },
        "tickets": {
            "count_payload": results.get("ticket_count"),
            "sample_count": len(tickets),
            "observed_statuses": statuses,
            "observed_types": types,
            "observed_priorities": priorities,
            "sample": tickets[: min(3, len(tickets))],
        },
        "helpcenter": {
            "accessible": "helpcenter_collections" in results,
            "collection_count": _extract_count(results.get("helpcenter_collections")),
        },
        "unified_inbox": {
            "accessible": "unified_inbox" in results,
            "count": _extract_count(results.get("unified_inbox")),
        },
        "errors": errors,
    }

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if not errors else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Gleap API helper")
    parser.add_argument("--api-key")
    parser.add_argument("--project-id")
    parser.add_argument("--base-url")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)

    subparsers = parser.add_subparsers(dest="command", required=True)

    request_parser = subparsers.add_parser("request", help="Perform an arbitrary Gleap API request")
    request_parser.add_argument("method", choices=["GET", "POST", "PUT", "PATCH", "DELETE"])
    request_parser.add_argument("path", help="API path like /tickets or tickets/123")
    request_parser.add_argument("--query", action="append", help="Repeatable KEY=VALUE query param")
    request_parser.add_argument("--header", action="append", help="Repeatable KEY=VALUE extra header")
    request_parser.add_argument(
        "--data",
        help="Inline JSON string or @path/to/file.json",
    )
    request_parser.add_argument("--raw", action="store_true", help="Print raw text responses")
    request_parser.add_argument("--sort-keys", action="store_true")
    request_parser.set_defaults(func=cmd_request)

    probe_parser = subparsers.add_parser(
        "probe", help="Run safe read-only checks to discover live Gleap shape"
    )
    probe_parser.add_argument("--ticket-limit", type=int, default=3)
    probe_parser.add_argument("--inbox-limit", type=int, default=5)
    probe_parser.add_argument("--skip-helpcenter", action="store_true")
    probe_parser.add_argument("--skip-unified-inbox", action="store_true")
    probe_parser.set_defaults(func=cmd_probe)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except GleapApiError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON input: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
