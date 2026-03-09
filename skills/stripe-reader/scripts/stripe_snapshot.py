#!/usr/bin/env python3
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from collections import Counter

BASE = "https://api.stripe.com/v1"


def api_get(path, params=None):
    key = os.environ.get("STRIPE_SECRET_KEY")
    if not key:
        raise SystemExit("Missing STRIPE_SECRET_KEY environment variable")
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {key}")
    req.add_header("Stripe-Version", "2024-06-20")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(body)
        except Exception:
            payload = {"error": {"message": body}}
        raise RuntimeError(f"stripe_error {e.code} on {path}: {payload.get('error', {}).get('message', 'unknown error')}")


def amount_to_monthly(amount, interval, interval_count):
    if amount is None:
        return 0.0
    count = interval_count or 1
    if interval == "month":
        months = count
    elif interval == "year":
        months = 12 * count
    elif interval == "week":
        months = (52 / 12) * count
    elif interval == "day":
        months = (365 / 12) * count
    else:
        return 0.0
    if months == 0:
        return 0.0
    return (amount / 100.0) / months


def subscription_monthly_amount(sub):
    total = 0.0
    items = (((sub or {}).get("items") or {}).get("data") or [])
    for item in items:
        price = item.get("price") or {}
        recurring = price.get("recurring") or {}
        quantity = item.get("quantity") or 1
        unit_amount = price.get("unit_amount")
        total += amount_to_monthly(unit_amount or 0, recurring.get("interval"), recurring.get("interval_count")) * quantity
    return total


def safe_get(path, params=None):
    try:
        return api_get(path, params), None
    except Exception as e:
        return None, str(e)


def main():
    start = time.time()
    acct, acct_error = safe_get("/account")
    subs, subs_error = safe_get("/subscriptions", {"status": "all", "limit": 100, "expand[]": "data.items.data.price"})
    customers, customers_error = safe_get("/customers", {"limit": 100})
    invoices, invoices_error = safe_get("/invoices", {"limit": 25})

    sub_status = Counter()
    active_monthly = 0.0
    for sub in (subs or {}).get("data", []):
        status = sub.get("status", "unknown")
        sub_status[status] += 1
        if status in {"active", "trialing", "past_due", "unpaid"}:
            active_monthly += subscription_monthly_amount(sub)

    invoice_status = Counter(inv.get("status", "unknown") for inv in ((invoices or {}).get("data", [])))

    out = {
        "account_id": (acct or {}).get("id"),
        "business_name": ((acct or {}).get("business_profile", {}) or {}).get("name") or ((acct or {}).get("settings", {}) or {}).get("dashboard", {}).get("display_name"),
        "default_currency": (acct or {}).get("default_currency"),
        "country": (acct or {}).get("country"),
        "livemode": (acct or {}).get("livemode"),
        "subscriptions_sample_count": len(((subs or {}).get("data", []))),
        "subscription_status_counts": dict(sub_status),
        "customers_sample_count": len(((customers or {}).get("data", []))),
        "invoice_status_sample": dict(invoice_status),
        "estimated_mrr_from_first_100_subscriptions": round(active_monthly, 2),
        "endpoint_errors": {k: v for k, v in {
            "account": acct_error,
            "subscriptions": subs_error,
            "customers": customers_error,
            "invoices": invoices_error,
        }.items() if v},
        "generated_at": int(time.time()),
        "elapsed_seconds": round(time.time() - start, 2),
    }
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
