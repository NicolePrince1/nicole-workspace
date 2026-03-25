#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any, Callable

from meta_common import DEFAULTS, MetaAPIError, ensure_act_prefix, get_page_token, graph_request, print_json


OperationBuilder = Callable[[dict[str, Any]], str]


OPERATIONS: dict[str, dict[str, Any]] = {
    "create_campaign": {
        "path": lambda spec: f"{ensure_act_prefix(spec.get('account_id') or DEFAULTS['ad_account_id'])}/campaigns",
        "token": "system",
        "supports_validate": True,
        "kind": "ads",
        "requires": [],
    },
    "update_campaign": {
        "path": lambda spec: spec["object_id"],
        "token": "system",
        "supports_validate": True,
        "kind": "ads",
        "requires": ["object_id"],
    },
    "create_adset": {
        "path": lambda spec: f"{ensure_act_prefix(spec.get('account_id') or DEFAULTS['ad_account_id'])}/adsets",
        "token": "system",
        "supports_validate": True,
        "kind": "ads",
        "requires": [],
    },
    "update_adset": {
        "path": lambda spec: spec["object_id"],
        "token": "system",
        "supports_validate": True,
        "kind": "ads",
        "requires": ["object_id"],
    },
    "create_adcreative": {
        "path": lambda spec: f"{ensure_act_prefix(spec.get('account_id') or DEFAULTS['ad_account_id'])}/adcreatives",
        "token": "system",
        "supports_validate": True,
        "kind": "ads",
        "requires": [],
    },
    "create_ad": {
        "path": lambda spec: f"{ensure_act_prefix(spec.get('account_id') or DEFAULTS['ad_account_id'])}/ads",
        "token": "system",
        "supports_validate": True,
        "kind": "ads",
        "requires": [],
    },
    "update_ad": {
        "path": lambda spec: spec["object_id"],
        "token": "system",
        "supports_validate": True,
        "kind": "ads",
        "requires": ["object_id"],
    },
    "create_page_post": {
        "path": lambda spec: f"{spec.get('page_id') or DEFAULTS['page_id']}/feed",
        "token": "page",
        "supports_validate": False,
        "kind": "social",
        "requires": [],
    },
    "create_page_photo": {
        "path": lambda spec: f"{spec.get('page_id') or DEFAULTS['page_id']}/photos",
        "token": "page",
        "supports_validate": False,
        "kind": "social",
        "requires": [],
    },
    "create_instagram_media": {
        "path": lambda spec: f"{spec.get('instagram_account_id') or DEFAULTS['instagram_account_id']}/media",
        "token": "system",
        "supports_validate": False,
        "kind": "social",
        "requires": [],
    },
    "publish_instagram_media": {
        "path": lambda spec: f"{spec.get('instagram_account_id') or DEFAULTS['instagram_account_id']}/media_publish",
        "token": "system",
        "supports_validate": False,
        "kind": "social",
        "requires": [],
    },
}


def load_spec(path: str) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise MetaAPIError("Spec file must contain a JSON object.")
    if "op" not in data:
        raise MetaAPIError("Spec file must include an 'op' field.")
    data.setdefault("params", {})
    if not isinstance(data["params"], dict):
        raise MetaAPIError("Spec file 'params' must be a JSON object.")
    return data


def require_fields(spec: dict[str, Any], fields: list[str]) -> None:
    for field in fields:
        if not spec.get(field):
            raise MetaAPIError(f"Spec for {spec.get('op')} is missing required field: {field}")


def apply_guardrails(spec: dict[str, Any], *, allow_active: bool) -> list[str]:
    warnings: list[str] = []
    params = spec.setdefault("params", {})
    op = spec["op"]

    if op == "create_campaign":
        params.setdefault("special_ad_categories", [])

    if op in {"create_campaign", "update_campaign", "create_adset", "update_adset", "create_ad", "update_ad"}:
        status = str(params.get("status", "")).upper().strip()
        if status == "ACTIVE" and not allow_active:
            params["status"] = "PAUSED"
            warnings.append("Requested ACTIVE status was forced to PAUSED. Re-run with --allow-active if you truly want live delivery.")

    return warnings


def resolve_token(mode: str, spec: dict[str, Any]) -> str | None:
    if mode == "system":
        return None
    if mode == "page":
        return get_page_token(spec.get("page_id") or DEFAULTS["page_id"])
    raise MetaAPIError(f"Unsupported token mode: {mode}")


def build_request(spec: dict[str, Any]) -> dict[str, Any]:
    op = spec["op"]
    operation = OPERATIONS.get(op)
    if not operation:
        raise MetaAPIError(f"Unsupported operation: {op}")

    require_fields(spec, operation.get("requires", []))
    path = operation["path"](spec)
    params = copy.deepcopy(spec.get("params", {}))

    request = {
        "op": op,
        "kind": operation["kind"],
        "supports_validate": operation["supports_validate"],
        "token_mode": operation["token"],
        "path": path,
        "params": params,
    }
    for key in ["account_id", "page_id", "instagram_account_id", "object_id"]:
        if key in spec:
            request[key] = spec[key]
    return request


def add_validate_only(params: dict[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(params)
    existing = merged.get("execution_options")
    if existing is None:
        merged["execution_options"] = ["validate_only"]
        return merged
    if isinstance(existing, list) and "validate_only" not in existing:
        merged["execution_options"] = existing + ["validate_only"]
        return merged
    if isinstance(existing, str) and "validate_only" not in existing:
        merged["execution_options"] = [existing, "validate_only"]
        return merged
    return merged


def preview(request: dict[str, Any], warnings: list[str]) -> dict[str, Any]:
    return {
        "mode": "preview",
        "warnings": warnings,
        "request": request,
        "note": "No live change was sent to Meta.",
    }


def validate(request: dict[str, Any], warnings: list[str]) -> dict[str, Any]:
    if not request["supports_validate"]:
        raise MetaAPIError(
            f"Operation {request['op']} does not support server-side validate_only mode. Use preview before apply."
        )
    token = resolve_token(request["token_mode"], request)
    params = add_validate_only(request["params"])
    response = graph_request(request["path"], params, method="POST", token=token)
    return {
        "mode": "validate",
        "warnings": warnings,
        "request": {**request, "params": params},
        "response": response,
    }


def apply(request: dict[str, Any], warnings: list[str]) -> dict[str, Any]:
    token = resolve_token(request["token_mode"], request)
    response = graph_request(request["path"], request["params"], method="POST", token=token)
    return {
        "mode": "apply",
        "warnings": warnings,
        "request": request,
        "response": response,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Safely preview, validate, and apply Meta ads/social mutations from JSON specs."
    )
    parser.add_argument("mode", choices=["preview", "validate", "apply"])
    parser.add_argument("spec", help="Path to a JSON spec file.")
    parser.add_argument("--allow-active", action="store_true", help="Allow ACTIVE status on ads objects.")
    parser.add_argument(
        "--yes-apply",
        action="store_true",
        help="Required alongside apply mode so live writes are explicit.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.mode == "apply" and not args.yes_apply:
        raise SystemExit("Refusing live Meta write without --yes-apply")

    spec = load_spec(args.spec)
    warnings = apply_guardrails(spec, allow_active=args.allow_active)
    request = build_request(spec)
    request["spec_file"] = args.spec

    if args.mode == "preview":
        result = preview(request, warnings)
    elif args.mode == "validate":
        result = validate(request, warnings)
    else:
        result = apply(request, warnings)

    print_json(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
