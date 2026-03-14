#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone

BASE = "https://api.stripe.com/v1"
API_VERSION = "2024-06-20"
REVENUE_STATUSES = {"active", "past_due", "unpaid"}


def stripe_key():
    key = os.environ.get("STRIPE_SECRET_KEY") or os.environ.get("STRIPE")
    if not key:
        raise SystemExit("Missing Stripe key. Set STRIPE_SECRET_KEY or STRIPE.")
    return key


def api_get(path, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {stripe_key()}")
    req.add_header("Stripe-Version", API_VERSION)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(body)
            message = payload.get("error", {}).get("message", body)
        except Exception:
            message = body
        raise RuntimeError(f"stripe_error {exc.code} on {path}: {message}")


def paginate(path, base_params=None):
    params = list(base_params or [])
    starting_after = None
    while True:
        query = list(params)
        query.append(("limit", "100"))
        if starting_after:
            query.append(("starting_after", starting_after))
        data = api_get(path, query)
        rows = data.get("data", [])
        for row in rows:
            yield row
        if not data.get("has_more") or not rows:
            break
        starting_after = rows[-1]["id"]


def ts_to_iso(ts):
    if not ts:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def month_bounds(now=None):
    now = now or datetime.now(timezone.utc)
    start_this = datetime(now.year, now.month, 1, tzinfo=timezone.utc)
    if now.month == 1:
        start_last = datetime(now.year - 1, 12, 1, tzinfo=timezone.utc)
    else:
        start_last = datetime(now.year, now.month - 1, 1, tzinfo=timezone.utc)
    return now, start_this, start_last


def amount_to_monthly(amount_cents, interval, interval_count):
    if amount_cents is None:
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
    return (amount_cents / 100.0) / months if months else 0.0


def tier_amount_cents(price, quantity):
    quantity = quantity or 0
    tiers = price.get("tiers") or []
    if not tiers:
        return None
    mode = price.get("tiers_mode")
    if mode == "volume":
        for tier in tiers:
            up_to = tier.get("up_to")
            if up_to is None or quantity <= up_to:
                return (tier.get("flat_amount") or 0) + ((tier.get("unit_amount") or 0) * quantity)
        return None
    if mode == "graduated":
        total = 0
        remaining = quantity
        lower = 0
        for tier in tiers:
            up_to = tier.get("up_to")
            flat_amt = tier.get("flat_amount") or 0
            unit_amt = tier.get("unit_amount") or 0
            if up_to is None:
                units = max(remaining, 0)
            else:
                tier_capacity = max(up_to - lower, 0)
                units = min(max(remaining, 0), tier_capacity)
            if units > 0 or flat_amt:
                total += flat_amt + (unit_amt * units)
            remaining -= units
            if up_to is not None:
                lower = up_to
            if remaining <= 0:
                break
        return total
    return None


def subscription_item_monthly_amount(item):
    price = item.get("price") or {}
    recurring = price.get("recurring") or {}
    quantity = item.get("quantity") or 1
    if price.get("billing_scheme") == "tiered":
        cents = tier_amount_cents(price, quantity)
    else:
        cents = (price.get("unit_amount") or 0) * quantity
    return amount_to_monthly(cents, recurring.get("interval"), recurring.get("interval_count"))


def price_label(price):
    product = price.get("product")
    product_name = product.get("name") if isinstance(product, dict) else None
    return product_name or price.get("nickname") or price.get("lookup_key") or price.get("id") or "unknown"


def load_prices():
    prices = {}
    for price in paginate("/prices", [("active", "true"), ("expand[]", "data.product"), ("expand[]", "data.tiers")]):
        prices[price["id"]] = price
    return prices


def load_customers():
    return list(paginate("/customers"))


def load_invoices(status=None, expand_lines=True):
    params = []
    if status:
        params.append(("status", status))
    if expand_lines:
        params.append(("expand[]", "data.lines.data.price"))
    return list(paginate("/invoices", params))


def load_subscriptions(prices_by_id):
    subs = []
    for sub in paginate("/subscriptions", [("status", "all"), ("expand[]", "data.items.data.price")]):
        for item in ((sub.get("items") or {}).get("data") or []):
            price = item.get("price") or {}
            if price.get("id") in prices_by_id:
                item["price"] = prices_by_id[price["id"]]
        subs.append(sub)
    return subs


def customer_signup_counts(customers):
    _, start_this, start_last = month_bounds()
    this_count = 0
    last_count = 0
    for customer in customers:
        created = customer.get("created") or 0
        if created >= int(start_this.timestamp()):
            this_count += 1
        elif int(start_last.timestamp()) <= created < int(start_this.timestamp()):
            last_count += 1
    return {
        "this_month": this_count,
        "last_month": last_count,
        "delta": this_count - last_count,
        "delta_pct": round(((this_count - last_count) / last_count) * 100, 2) if last_count else None,
    }


def invoice_revenue_counts(invoices):
    _, start_this, start_last = month_bounds()
    out = {"this_month_paid_revenue": 0.0, "this_month_paid_invoices": 0, "last_month_paid_revenue": 0.0, "last_month_paid_invoices": 0}
    for inv in invoices:
        if inv.get("status") != "paid":
            continue
        created = inv.get("created") or 0
        amount_paid = (inv.get("amount_paid") or 0) / 100.0
        if created >= int(start_this.timestamp()):
            out["this_month_paid_revenue"] += amount_paid
            out["this_month_paid_invoices"] += 1
        elif int(start_last.timestamp()) <= created < int(start_this.timestamp()):
            out["last_month_paid_revenue"] += amount_paid
            out["last_month_paid_invoices"] += 1
    out["this_month_paid_revenue"] = round(out["this_month_paid_revenue"], 2)
    out["last_month_paid_revenue"] = round(out["last_month_paid_revenue"], 2)
    return out


def paid_customer_acquisition(invoices):
    _, start_this, start_last = month_bounds()
    first_paid = {}
    for inv in invoices:
        if inv.get("status") != "paid":
            continue
        customer = inv.get("customer")
        created = inv.get("created") or 0
        amount_paid = inv.get("amount_paid") or 0
        if not customer or amount_paid <= 0:
            continue
        if customer not in first_paid or created < first_paid[customer]:
            first_paid[customer] = created
    this_count = sum(1 for ts in first_paid.values() if ts >= int(start_this.timestamp()))
    last_count = sum(1 for ts in first_paid.values() if int(start_last.timestamp()) <= ts < int(start_this.timestamp()))
    return {
        "this_month": this_count,
        "last_month": last_count,
        "delta": this_count - last_count,
        "delta_pct": round(((this_count - last_count) / last_count) * 100, 2) if last_count else None,
    }


def latest_paid_invoice_by_subscription(invoices):
    latest = {}
    for inv in invoices:
        if inv.get("status") != "paid" or (inv.get("amount_paid") or 0) <= 0:
            continue
        sub_id = inv.get("subscription")
        created = inv.get("created") or 0
        if not sub_id:
            continue
        if sub_id not in latest or created > (latest[sub_id].get("created") or 0):
            latest[sub_id] = inv
    return latest


def invoice_monthly_amount(inv):
    monthly = 0.0
    for line in ((inv.get("lines") or {}).get("data") or []):
        if line.get("type") != "subscription":
            continue
        amount = line.get("amount") or 0
        recurring = ((line.get("price") or {}).get("recurring") or {})
        monthly += amount_to_monthly(amount, recurring.get("interval"), recurring.get("interval_count"))
    return monthly


def subscription_metrics(subs, invoices):
    status_counts = Counter()
    mrr = 0.0
    valuation_methods = Counter()
    plan_mix = defaultdict(lambda: {"subscriptions": 0, "mrr": 0.0})
    canceled_this_month = 0
    _, start_this, _ = month_bounds()
    latest_invoice_map = latest_paid_invoice_by_subscription(invoices)

    for sub in subs:
        status = sub.get("status") or "unknown"
        status_counts[status] += 1
        canceled_at = sub.get("canceled_at")
        if canceled_at and canceled_at >= int(start_this.timestamp()):
            canceled_this_month += 1
        items = ((sub.get("items") or {}).get("data") or [])
        sub_monthly = 0.0
        valued = False
        for item in items:
            monthly = subscription_item_monthly_amount(item)
            price = item.get("price") or {}
            if monthly > 0:
                valued = True
                sub_monthly += monthly
                label = price_label(price)
                plan_mix[label]["subscriptions"] += 1
                plan_mix[label]["mrr"] += monthly
        if not valued and status in REVENUE_STATUSES:
            inv = latest_invoice_map.get(sub.get("id"))
            inferred = invoice_monthly_amount(inv) if inv else 0.0
            if inferred > 0:
                sub_monthly = inferred
                valued = True
                valuation_methods["latest_paid_invoice"] += 1
            else:
                valuation_methods["unvalued"] += 1
        elif valued:
            valuation_methods["subscription_items"] += 1
        else:
            valuation_methods["zero_or_trial"] += 1
        if status in REVENUE_STATUSES:
            mrr += sub_monthly

    plan_mix_rows = [{"plan": name, "subscriptions": vals["subscriptions"], "mrr": round(vals["mrr"], 2)} for name, vals in sorted(plan_mix.items(), key=lambda kv: (-kv[1]["mrr"], kv[0]))]
    return {
        "subscription_status_counts": dict(status_counts),
        "estimated_mrr": round(mrr, 2),
        "valuation_methods": dict(valuation_methods),
        "canceled_this_month": canceled_this_month,
        "plan_mix": plan_mix_rows,
    }


def delinquency_metrics(subs, invoices):
    delinquent = []
    invoice_status = Counter(inv.get("status") or "unknown" for inv in invoices)
    latest_open_by_customer = {}
    for inv in invoices:
        customer = inv.get("customer")
        created = inv.get("created") or 0
        if customer and inv.get("status") in {"open", "uncollectible", "draft"}:
            if customer not in latest_open_by_customer or created > (latest_open_by_customer[customer].get("created") or 0):
                latest_open_by_customer[customer] = inv
    for sub in subs:
        status = sub.get("status")
        if status not in {"past_due", "unpaid"}:
            continue
        customer = sub.get("customer")
        delinquent.append({
            "subscription_id": sub.get("id"),
            "customer_id": customer,
            "status": status,
            "current_period_end": ts_to_iso(sub.get("current_period_end")),
            "latest_open_invoice_status": (latest_open_by_customer.get(customer) or {}).get("status"),
            "latest_open_invoice_amount_due": ((latest_open_by_customer.get(customer) or {}).get("amount_due") or 0) / 100.0,
        })
    return {"invoice_status_counts": dict(invoice_status), "delinquent_subscriptions": delinquent, "delinquent_count": len(delinquent)}


def data_quality(elapsed):
    return {
        "key_source": "STRIPE_SECRET_KEY or STRIPE",
        "mrr_method": "Active/past_due/unpaid subscriptions valued from recurring subscription items with tiered-price support; falls back to latest paid recurring invoice when needed.",
        "notes": [
            "Excludes zero-value trial subscriptions from MRR.",
            "Uses full pagination; not limited to the first 100 objects.",
            "Restricted keys may block some account-level endpoints; this script does not depend on /account.",
        ],
        "elapsed_seconds": round(elapsed, 2),
    }


def build_snapshot():
    start = time.time()
    prices = load_prices()
    customers = load_customers()
    invoices = load_invoices(expand_lines=True)
    subs = load_subscriptions(prices)
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "customers": {"total": len(customers), "signups": customer_signup_counts(customers), "paid_acquisition": paid_customer_acquisition(invoices)},
        "subscriptions": subscription_metrics(subs, invoices),
        "revenue": invoice_revenue_counts(invoices),
        "delinquency": delinquency_metrics(subs, invoices),
    }
    out["data_quality"] = data_quality(time.time() - start)
    return out


def build_signups():
    start = time.time()
    customers = load_customers()
    invoices = load_invoices(status="paid", expand_lines=False)
    out = {"total": len(customers), "signups": customer_signup_counts(customers), "paid_acquisition": paid_customer_acquisition(invoices)}
    out["data_quality"] = data_quality(time.time() - start)
    return out


def build_revenue():
    start = time.time()
    invoices = load_invoices(status="paid", expand_lines=False)
    out = invoice_revenue_counts(invoices)
    out["data_quality"] = data_quality(time.time() - start)
    return out


def build_mrr_or_plans(include_plans=False):
    start = time.time()
    prices = load_prices()
    subs = load_subscriptions(prices)
    invoices = load_invoices(status="paid", expand_lines=True)
    subm = subscription_metrics(subs, invoices)
    out = {
        "estimated_mrr": subm["estimated_mrr"],
        "valuation_methods": subm["valuation_methods"],
        "subscription_status_counts": subm["subscription_status_counts"],
        "canceled_this_month": subm["canceled_this_month"],
    }
    if include_plans:
        out["plan_mix"] = subm["plan_mix"]
    out["data_quality"] = data_quality(time.time() - start)
    return out


def build_delinquency():
    start = time.time()
    prices = load_prices()
    subs = load_subscriptions(prices)
    invoices = load_invoices(expand_lines=False)
    out = delinquency_metrics(subs, invoices)
    out["data_quality"] = data_quality(time.time() - start)
    return out


def main():
    parser = argparse.ArgumentParser(description="Read-only Stripe analytics for Oviond")
    parser.add_argument("mode", nargs="?", default="snapshot", choices=["snapshot", "mrr", "signups", "revenue", "plans", "delinquency"])
    args = parser.parse_args()
    if args.mode == "snapshot":
        out = build_snapshot()
    elif args.mode == "mrr":
        out = build_mrr_or_plans(include_plans=False)
    elif args.mode == "signups":
        out = build_signups()
    elif args.mode == "revenue":
        out = build_revenue()
    elif args.mode == "plans":
        out = build_mrr_or_plans(include_plans=True)
    elif args.mode == "delinquency":
        out = build_delinquency()
    else:
        out = build_snapshot()
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
