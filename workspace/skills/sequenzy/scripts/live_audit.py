#!/usr/bin/env python3
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import OrderedDict

BASE_URL = os.environ.get("SEQUENZY_BASE_URL", "https://api.sequenzy.com/api/v1").rstrip("/")
API_KEY = os.environ.get("SEQUENZY_API_KEY")
USER_AGENT = os.environ.get("SEQUENZY_USER_AGENT", "Nicole-Oviond-Sequenzy-Audit/1.0")
TIMEOUT = int(os.environ.get("SEQUENZY_TIMEOUT_SECONDS", "20"))


def fail(message: str, code: int = 1) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)


if not API_KEY:
    fail("Missing SEQUENZY_API_KEY")


def api_get(path: str, extra_headers: dict | None = None):
    request = urllib.request.Request(f"{BASE_URL}{path}", method="GET")
    request.add_header("Authorization", f"Bearer {API_KEY}")
    request.add_header("Content-Type", "application/json")
    request.add_header("User-Agent", USER_AGENT)
    for key, value in (extra_headers or {}).items():
        request.add_header(key, value)

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            raw = response.read().decode("utf-8", "replace")
            return response.status, dict(response.headers), parse_body(raw)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        return exc.code, dict(exc.headers), parse_body(raw)


def parse_body(raw: str):
    try:
        return json.loads(raw)
    except Exception:
        return raw


def summarize(obj):
    if isinstance(obj, dict):
        summary = OrderedDict()
        summary["type"] = "object"
        summary["keys"] = list(obj.keys())[:20]
        for field in ["success", "error", "message", "currentCompanyId", "companyId"]:
            if field in obj:
                summary[field] = obj[field]
        if "pagination" in obj and isinstance(obj["pagination"], dict):
            summary["pagination"] = {
                key: obj["pagination"].get(key)
                for key in ["page", "limit", "total", "totalPages"]
                if key in obj["pagination"]
            }
        for field in [
            "subscribers",
            "transactional",
            "transactionalEmails",
            "companies",
            "websites",
            "lists",
            "segments",
            "templates",
            "campaigns",
            "sequences",
            "recipients",
            "stats",
            "subscriber",
            "campaign",
            "sequence",
            "template",
        ]:
            if field not in obj:
                continue
            value = obj[field]
            if isinstance(value, list):
                summary[f"{field}_count"] = len(value)
                if value and isinstance(value[0], dict):
                    summary[f"{field}_item_keys"] = list(value[0].keys())[:20]
            elif isinstance(value, dict):
                summary[f"{field}_keys"] = list(value.keys())[:20]
            else:
                summary[field] = value
        return summary
    if isinstance(obj, list):
        summary = OrderedDict(type="array", count=len(obj))
        if obj and isinstance(obj[0], dict):
            summary["item_keys"] = list(obj[0].keys())[:20]
        return summary
    return OrderedDict(type=type(obj).__name__, preview=str(obj)[:300])


report = []


def add(label: str, path: str, extra_headers: dict | None = None):
    status, headers, body = api_get(path, extra_headers=extra_headers)
    report.append(
        OrderedDict(
            label=label,
            path=path,
            status=status,
            content_type=headers.get("Content-Type") or headers.get("content-type"),
            summary=summarize(body),
        )
    )
    return body


subscribers_body = add("REST subscribers", "/subscribers?limit=2")
add("REST transactional", "/transactional")
add("REST metrics", "/metrics")
add("REST stats alias", "/stats")
add("Private account", "/account")
companies_body = add("Private companies", "/companies")
add("Private websites", "/websites")
add("Private lists", "/lists")
add("Private segments", "/segments")
templates_body = add("Private templates", "/templates")
campaigns_body = add("Private campaigns", "/campaigns")
sequences_body = add("Private sequences", "/sequences")
add("Private deliverability health", "/health/deliverability")
add("REST recipient metrics", "/metrics/recipients?limit=1")

sample_email = None
if isinstance(subscribers_body, dict):
    subscribers = subscribers_body.get("subscribers")
    if isinstance(subscribers, list) and subscribers:
        sample_email = subscribers[0].get("email")
if sample_email:
    encoded = urllib.parse.quote(sample_email, safe="")
    add("REST subscriber detail", f"/subscribers/{encoded}")
    add("Private subscriber activity route", f"/subscribers/{encoded}/activity")

for label, body, field, detail_prefix, metrics_prefix in [
    ("campaign", campaigns_body, "campaigns", "/campaigns", "/metrics/campaigns"),
    ("sequence", sequences_body, "sequences", "/sequences", "/metrics/sequences"),
]:
    if not isinstance(body, dict):
        continue
    items = body.get(field)
    if not isinstance(items, list) or not items:
        continue
    identifier = items[0].get("id")
    if not identifier:
        continue
    add(f"Private {label} detail", f"{detail_prefix}/{identifier}")
    add(f"Private {label} stats", f"{detail_prefix}/{identifier}/stats")
    add(f"REST {label} metrics", f"{metrics_prefix}/{identifier}")

if isinstance(templates_body, dict):
    templates = templates_body.get("templates")
    if isinstance(templates, list) and templates:
        template_id = templates[0].get("id")
        if template_id:
            add("Private template detail", f"/templates/{template_id}")

if isinstance(companies_body, dict):
    companies = companies_body.get("companies")
    if isinstance(companies, list) and companies:
        company_id = companies[0].get("id")
        if company_id:
            add("Private templates with x-company-id", "/templates", {"x-company-id": company_id})
            add("Private campaigns with x-company-id", "/campaigns", {"x-company-id": company_id})
            add("Private sequences with x-company-id", "/sequences", {"x-company-id": company_id})

print(json.dumps(report, indent=2))
