#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

USER_AGENT = "OpenClaw-Nicole/1.0"
DEFAULT_API_URL = "https://api.postiz.com"
VALID_TYPES = {"draft", "schedule", "now"}


def die(message, code=1):
    print(json.dumps({"ok": False, "error": message}, indent=2))
    raise SystemExit(code)


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def fetch_json(url, headers):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8", "replace"))


def post_json(url, headers, payload):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8", "replace"))


def normalize_payload(payload, force_draft=False):
    if not isinstance(payload, dict):
        die("Payload must be a JSON object")

    post_type = payload.get("type")
    if post_type not in VALID_TYPES:
        die("Payload must include type of draft, schedule, or now")

    if force_draft:
        payload["type"] = "draft"

    if payload.get("type") == "now":
        die("Refusing type=now by default. Use draft or schedule, or pass --allow-now if you really mean it.")

    if "date" not in payload or not isinstance(payload["date"], str):
        die("Payload must include ISO date string in field 'date'")

    if "shortLink" not in payload or not isinstance(payload["shortLink"], bool):
        die("Payload must include boolean field 'shortLink'")

    if "tags" not in payload or not isinstance(payload["tags"], list):
        die("Payload must include list field 'tags'")

    posts = payload.get("posts")
    if not isinstance(posts, list) or not posts:
        die("Payload must include non-empty list field 'posts'")

    for idx, post in enumerate(posts, start=1):
        if not isinstance(post, dict):
            die(f"posts[{idx}] must be an object")
        integration = post.get("integration", {})
        if not isinstance(integration, dict) or not integration.get("id"):
            die(f"posts[{idx}].integration.id is required")
        value = post.get("value")
        if not isinstance(value, list) or not value:
            die(f"posts[{idx}].value must be a non-empty list")
        for jdx, item in enumerate(value, start=1):
            if not isinstance(item, dict):
                die(f"posts[{idx}].value[{jdx}] must be an object")
            if not isinstance(item.get("content"), str):
                die(f"posts[{idx}].value[{jdx}].content must be a string")
            images = item.get("image", [])
            if not isinstance(images, list):
                die(f"posts[{idx}].value[{jdx}].image must be a list")
        settings = post.get("settings")
        if not isinstance(settings, dict) or not settings.get("__type"):
            die(f"posts[{idx}].settings.__type is required")

    return payload


def integration_map(headers, api_url):
    _, integrations = fetch_json(f"{api_url}/public/v1/integrations", headers)
    return {item["id"]: item for item in integrations}


def validate_integrations(payload, integrations):
    issues = []
    for idx, post in enumerate(payload["posts"], start=1):
        integration_id = post["integration"]["id"]
        settings_type = post["settings"].get("__type")
        integration = integrations.get(integration_id)
        if not integration:
            issues.append(f"posts[{idx}] integration id not found in live Postiz account: {integration_id}")
            continue
        live_type = integration.get("identifier")
        compatible = {
            live_type,
            "linkedin" if live_type == "linkedin-page" else live_type,
            "linkedin-page" if live_type == "linkedin" else live_type,
        }
        if settings_type not in compatible:
            issues.append(
                f"posts[{idx}] settings.__type={settings_type} does not match live integration type={live_type}"
            )
    return issues


def main():
    parser = argparse.ArgumentParser(description="Validate and optionally create a Postiz post from a JSON payload file.")
    parser.add_argument("payload", help="Path to JSON payload file")
    parser.add_argument("--apply", action="store_true", help="Actually send the payload to Postiz")
    parser.add_argument("--allow-now", action="store_true", help="Permit payload type=now")
    parser.add_argument("--force-draft", action="store_true", help="Rewrite payload type to draft before validation")
    parser.add_argument("--pretty", action="store_true", help="Print normalized payload in output")
    args = parser.parse_args()

    api_key = os.environ.get("POSTIZ_API_KEY")
    if not api_key:
        die("Missing POSTIZ_API_KEY")

    api_url = os.environ.get("POSTIZ_API_URL", DEFAULT_API_URL).rstrip("/")
    headers = {
        "Authorization": api_key,
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    payload_path = Path(args.payload)
    if not payload_path.exists():
        die(f"Payload file not found: {payload_path}")

    payload = load_json(payload_path)
    payload = normalize_payload(payload, force_draft=args.force_draft)

    if payload["type"] == "now" and not args.allow_now:
        die("Refusing type=now without --allow-now")

    integrations = integration_map(headers, api_url)
    issues = validate_integrations(payload, integrations)

    result = {
        "ok": len(issues) == 0,
        "mode": "apply" if args.apply else "dry-run",
        "apiUrl": api_url,
        "payloadPath": str(payload_path),
        "postType": payload["type"],
        "issues": issues,
        "postCount": len(payload["posts"]),
    }

    if args.pretty:
        result["payload"] = payload

    if issues:
        print(json.dumps(result, indent=2))
        return 1

    if not args.apply:
        print(json.dumps(result, indent=2))
        return 0

    try:
        status, response = post_json(f"{api_url}/public/v1/posts", headers, payload)
        result["status"] = status
        result["response"] = response
        print(json.dumps(result, indent=2))
        return 0
    except urllib.error.HTTPError as e:
        result["ok"] = False
        result["status"] = e.code
        result["response"] = e.read().decode("utf-8", "replace")
        print(json.dumps(result, indent=2))
        return 1
    except Exception as e:
        result["ok"] = False
        result["response"] = f"{type(e).__name__}: {e}"
        print(json.dumps(result, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
