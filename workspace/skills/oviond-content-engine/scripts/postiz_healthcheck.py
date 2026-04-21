#!/usr/bin/env python3
import json
import os
import sys
import urllib.error
import urllib.request

USER_AGENT = "OpenClaw-Nicole/1.0"
DEFAULT_API_URL = "https://api.postiz.com"


def request_json(url, headers, timeout=20):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", "replace")
        return resp.status, dict(resp.headers), json.loads(body)


def request_text(url, headers, timeout=20):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", "replace")
        return resp.status, dict(resp.headers), body


def main():
    api_key = os.environ.get("POSTIZ_API_KEY", "")
    api_url = os.environ.get("POSTIZ_API_URL", DEFAULT_API_URL).rstrip("/")
    mcp_url = os.environ.get("POSTIZ_MCP_URL") or os.environ.get("POSTIZ_MCP_UR", "")
    mcp_token = os.environ.get("POSTIZ_MCP_BEARER_TOKEN", "")

    warnings = []
    errors = []

    if os.environ.get("POSTIZ_MCP_UR"):
        warnings.append("Found legacy POSTIZ_MCP_UR. The canonical variable name is POSTIZ_MCP_URL, and the old typo should be removed once POSTIZ_MCP_URL is confirmed working.")

    if not api_key:
        errors.append("Missing POSTIZ_API_KEY")

    result = {
        "ok": False,
        "env": {
            "apiKeyPresent": bool(api_key),
            "apiUrl": api_url,
            "mcpUrl": mcp_url or None,
            "mcpTokenPresent": bool(mcp_token),
        },
        "warnings": warnings,
        "errors": errors,
        "api": None,
        "integrations": None,
        "mcp": None,
    }

    if errors:
        print(json.dumps(result, indent=2))
        return 1

    api_headers = {
        "Authorization": api_key,
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }

    try:
        status, _, body = request_json(f"{api_url}/public/v1/is-connected", api_headers)
        result["api"] = {
            "status": status,
            "connected": bool(body.get("connected")),
        }
    except urllib.error.HTTPError as e:
        result["api"] = {
            "status": e.code,
            "error": e.read().decode("utf-8", "replace"),
        }
        print(json.dumps(result, indent=2))
        return 1
    except Exception as e:
        result["api"] = {
            "error": f"{type(e).__name__}: {e}",
        }
        print(json.dumps(result, indent=2))
        return 1

    if not result["api"]["connected"]:
        result["errors"].append("Postiz API did not report connected=true")
        print(json.dumps(result, indent=2))
        return 1

    try:
        status, _, integrations = request_json(f"{api_url}/public/v1/integrations", api_headers)
        result["integrations"] = {
            "status": status,
            "count": len(integrations),
            "items": [
                {
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "platform": item.get("identifier"),
                    "profile": item.get("profile"),
                    "disabled": item.get("disabled"),
                }
                for item in integrations
            ],
        }
    except urllib.error.HTTPError as e:
        result["integrations"] = {
            "status": e.code,
            "error": e.read().decode("utf-8", "replace"),
        }
    except Exception as e:
        result["integrations"] = {
            "error": f"{type(e).__name__}: {e}",
        }

    if mcp_url and mcp_token:
        mcp_headers = {
            "Authorization": f"Bearer {mcp_token}",
            "Accept": "application/json, text/event-stream",
            "User-Agent": USER_AGENT,
        }
        try:
            status, headers, body = request_text(mcp_url, mcp_headers)
            result["mcp"] = {
                "status": status,
                "contentType": headers.get("Content-Type"),
                "reachable": True,
                "note": body[:300],
            }
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            reachable = e.code in (400, 401, 405)
            note = body[:500]
            if e.code == 400 and "session ID" in body:
                note = "MCP endpoint is reachable and authenticated enough to demand a valid session handshake."
            result["mcp"] = {
                "status": e.code,
                "contentType": e.headers.get("Content-Type"),
                "reachable": reachable,
                "note": note,
            }
        except Exception as e:
            result["mcp"] = {
                "reachable": False,
                "error": f"{type(e).__name__}: {e}",
            }
    else:
        result["mcp"] = {
            "reachable": False,
            "note": "Missing POSTIZ_MCP_URL/POSTIZ_MCP_BEARER_TOKEN",
        }

    result["ok"] = bool(result["api"]["connected"]) and bool(result["mcp"]["reachable"])
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
