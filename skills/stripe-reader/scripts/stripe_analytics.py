#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_BASE = "https://api.stripe.com/v1"
API_VERSION = "2024-06-20"
REVENUE_STATUSES = {"active", "past_due", "unpaid"}
CACHE_DIR = Path(os.environ.get("STRIPE_READER_CACHE_DIR", "/data/.openclaw/db/stripe-reader"))
DEFAULT_CACHE_TTLS = {
    "snapshot": 900,
    "mrr": 300,
    "plans": 300,
    "revenue": 180,
    "signups": 600,
    "delinquency": 300,
}


def stripe_key():
    key = os.environ.get("STRIPE_SECRET_KEY") or os.environ.get("STRIPE")
    if not key:
        raise SystemExit("Missing STRIPE_SECRET_KEY/STRIPE")
    return key


def api_get(path, params=None):
    url = API_BASE + path
    if params:
        url += "?" + urlencode(params, doseq=True)
    req = Request(url)
    req.add_header("Authorization", f"Bearer {stripe_key()}")
    req.add_header("Stripe-Version", API_VERSION)
    with urlopen(req, timeout=90) as resp:
        return json.loads(resp.read().decode())


def paginate(path, params=None):
    base = list(params or [])
    starting_after = None
    while True:
        query = list(base)
        query.append(("limit", "100"))
        if starting_after:
            query.append(("starting_after", starting_after))
        payload = api_get(path, query)
        rows = payload.get("data") or []
        for row in rows:
            yield row
        if not payload.get("has_more") or not rows:
            break
        starting_after = rows[-1]["id"]


def month_bounds(now=None):
    now = now or datetime.now(timezone.utc)
    start_this = datetime(now.year, now.month, 1, tzinfo=timezone.utc)
    if now.month == 1:
        start_last = datetime(now.year - 1, 12, 1, tzinfo=timezone.utc)
    else:
        start_last = datetime(now.year, now.month - 1, 1, tzinfo=timezone.utc)
    return now, start_this, start_last


def ts_to_iso(ts):
    if not ts:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def amount_to_monthly(amount_cents, interval, interval_count):
    count = interval_count or 1
    if amount_cents is None:
        return 0.0
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


def period_seconds_to_months(start_ts, end_ts):
    if not start_ts or not end_ts or end_ts <= start_ts:
        return None
    return ((end_ts - start_ts) / 86400.0) / 30.4375


def tier_amount(price, quantity):
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
                cap = max(up_to - lower, 0)
                units = min(max(remaining, 0), cap)
            if units > 0 or flat_amt:
                total += flat_amt + unit_amt * units
            remaining -= units
            if up_to is not None:
                lower = up_to
            if remaining <= 0:
                break
        return total
    return None


def cache_file(mode):
    return CACHE_DIR / f"{mode}.json"


def default_ttl(mode):
    return DEFAULT_CACHE_TTLS.get(mode, 300)


def decorate_cache(payload, mode, *, used, ttl_seconds, path, age_seconds=0):
    if isinstance(payload, dict):
        payload["cache"] = {
            "used": used,
            "mode": mode,
            "path": str(path),
            "ttl_seconds": ttl_seconds,
            "age_seconds": round(age_seconds, 2),
        }
    return payload


def load_cached(mode, ttl_seconds):
    if ttl_seconds is None or ttl_seconds <= 0:
        return None
    path = cache_file(mode)
    if not path.exists():
        return None
    age = time.time() - path.stat().st_mtime
    if age > ttl_seconds:
        return None
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return None
    return decorate_cache(payload, mode, used=True, ttl_seconds=ttl_seconds, path=path, age_seconds=age)


def write_cache(mode, payload, ttl_seconds):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = cache_file(mode)
    path.write_text(json.dumps(payload, indent=2) + "\n")
    return decorate_cache(payload, mode, used=False, ttl_seconds=ttl_seconds, path=path, age_seconds=0)


def load_price(price_id, price_cache, expand_product=True, expand_tiers=True):
    if not price_id:
        return {}
    if price_id not in price_cache:
        params = []
        if expand_product:
            params.append(("expand[]", "product"))
        if expand_tiers:
            params.append(("expand[]", "tiers"))
        price_cache[price_id] = api_get(f"/prices/{price_id}", params)
    return price_cache[price_id]


def load_customers(created_gte=None, created_lte=None):
    params = []
    if created_gte is not None:
        params.append(("created[gte]", str(created_gte)))
    if created_lte is not None:
        params.append(("created[lte]", str(created_lte)))
    return list(paginate("/customers", params))


def load_invoices(status=None, expand_lines=False, created_gte=None, created_lte=None):
    params = []
    if status:
        params.append(("status", status))
    if created_gte is not None:
        params.append(("created[gte]", str(created_gte)))
    if created_lte is not None:
        params.append(("created[lte]", str(created_lte)))
    if expand_lines:
        params.append(("expand[]", "data.lines.data"))
    return list(paginate("/invoices", params))


def load_invoices_for_statuses(statuses, expand_lines=False, created_gte=None, created_lte=None):
    rows = []
    for status in statuses:
        rows.extend(load_invoices(status=status, expand_lines=expand_lines, created_gte=created_gte, created_lte=created_lte))
    return rows


def load_subscriptions(statuses=None, price_cache=None, expand_latest_invoice_lines=False):
    statuses = list(statuses or ["all"])
    price_cache = price_cache if price_cache is not None else {}
    rows = []
    base_params = [("expand[]", "data.items.data.price")]
    if expand_latest_invoice_lines:
        base_params.append(("expand[]", "data.latest_invoice.lines.data"))
    for status in statuses:
        params = [("status", status)] + list(base_params)
        for sub in paginate("/subscriptions", params):
            for item in ((sub.get("items") or {}).get("data") or []):
                price_obj = item.get("price") or {}
                price_id = price_obj if isinstance(price_obj, str) else price_obj.get("id")
                if price_id:
                    item["price"] = load_price(price_id, price_cache, expand_product=True, expand_tiers=True)
            rows.append(sub)
    return rows


def load_subscription_status_snapshot():
    counts = Counter()
    canceled_this_month = 0
    _, start_this, _ = month_bounds()
    for sub in paginate("/subscriptions", [("status", "all")]):
        status = sub.get("status") or "unknown"
        counts[status] += 1
        canceled_at = sub.get("canceled_at") or 0
        if canceled_at and canceled_at >= int(start_this.timestamp()):
            canceled_this_month += 1
    return dict(counts), canceled_this_month


def customer_signup_counts(customers):
    now, start_this, start_last = month_bounds()
    this_month = 0
    last_month = 0
    for customer in customers:
        created = customer.get("created") or 0
        if created >= int(start_this.timestamp()):
            this_month += 1
        elif created >= int(start_last.timestamp()):
            last_month += 1
    return {
        "this_month": this_month,
        "last_month": last_month,
        "window": {
            "this_month_start": start_this.isoformat(),
            "last_month_start": start_last.isoformat(),
            "now": now.isoformat(),
        },
    }


def paid_customer_acquisition(invoices):
    now, start_this, start_last = month_bounds()
    first_paid_by_customer = {}
    for inv in invoices:
        if inv.get("status") != "paid" or (inv.get("amount_paid") or 0) <= 0:
            continue
        customer = inv.get("customer")
        created = inv.get("created") or 0
        if not customer:
            continue
        if customer not in first_paid_by_customer or created < first_paid_by_customer[customer]:
            first_paid_by_customer[customer] = created
    this_month = 0
    last_month = 0
    for created in first_paid_by_customer.values():
        if created >= int(start_this.timestamp()):
            this_month += 1
        elif created >= int(start_last.timestamp()):
            last_month += 1
    return {
        "this_month": this_month,
        "last_month": last_month,
        "window": {
            "this_month_start": start_this.isoformat(),
            "last_month_start": start_last.isoformat(),
            "now": now.isoformat(),
        },
    }


def invoice_revenue_counts(invoices):
    now, start_this, start_last = month_bounds()
    this_month = 0.0
    last_month = 0.0
    this_count = 0
    last_count = 0
    for inv in invoices:
        if inv.get("status") != "paid":
            continue
        created = inv.get("created") or 0
        amount = (inv.get("amount_paid") or 0) / 100.0
        if created >= int(start_this.timestamp()):
            this_month += amount
            this_count += 1
        elif created >= int(start_last.timestamp()):
            last_month += amount
            last_count += 1
    return {
        "paid_revenue": {
            "this_month": round(this_month, 2),
            "last_month": round(last_month, 2),
            "this_month_paid_invoices": this_count,
            "last_month_paid_invoices": last_count,
        },
        "window": {
            "this_month_start": start_this.isoformat(),
            "last_month_start": start_last.isoformat(),
            "now": now.isoformat(),
        },
    }


def price_label(price):
    product = price.get("product") or {}
    if isinstance(product, dict) and product.get("name"):
        return product.get("name")
    if price.get("nickname"):
        return price.get("nickname")
    if price.get("lookup_key"):
        return price.get("lookup_key")
    return price.get("id") or "unknown_price"


def subscription_item_monthly_amount(item):
    price = item.get("price") or {}
    recurring = price.get("recurring") or {}
    quantity = item.get("quantity") or 1
    if price.get("billing_scheme") == "tiered":
        amount_cents = tier_amount(price, quantity) or 0
    else:
        amount_cents = (price.get("unit_amount") or 0) * quantity
    return amount_to_monthly(amount_cents, recurring.get("interval"), recurring.get("interval_count"))


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


def invoice_line_monthly_amount(line):
    if line.get("type") != "subscription":
        return 0.0
    details = ((line.get("parent") or {}).get("subscription_item_details") or {})
    if details.get("proration"):
        return 0.0
    amount = line.get("amount_excluding_tax")
    if amount is None:
        amount = line.get("amount") or 0
    discount_total = sum((entry.get("amount") or 0) for entry in (line.get("discount_amounts") or []))
    net_amount = amount - discount_total
    if net_amount <= 0:
        return 0.0
    period = line.get("period") or {}
    months = period_seconds_to_months(period.get("start"), period.get("end"))
    if months:
        return (net_amount / 100.0) / months
    recurring = ((line.get("price") or {}).get("recurring") or {})
    return amount_to_monthly(net_amount, recurring.get("interval"), recurring.get("interval_count"))


def invoice_monthly_amount(inv):
    monthly = 0.0
    for line in ((inv.get("lines") or {}).get("data") or []):
        monthly += invoice_line_monthly_amount(line)
    return monthly


def latest_invoice_monthly_amount(sub):
    latest_invoice = sub.get("latest_invoice") or {}
    if not isinstance(latest_invoice, dict):
        return 0.0
    return invoice_monthly_amount(latest_invoice)


def subscription_metrics(subs, status_counts=None, canceled_this_month=0, fallback_paid_invoices=None):
    status_counts = status_counts or Counter(sub.get("status") or "unknown" for sub in subs)
    mrr = 0.0
    valuation_methods = Counter()
    plan_mix = defaultdict(lambda: {"subscriptions": 0, "mrr": 0.0})
    latest_paid_map = latest_paid_invoice_by_subscription(fallback_paid_invoices or [])

    for sub in subs:
        status = sub.get("status") or "unknown"
        items = ((sub.get("items") or {}).get("data") or [])
        item_monthly_total = 0.0
        item_plan_rows = []
        for item in items:
            monthly = subscription_item_monthly_amount(item)
            if monthly > 0:
                label = price_label(item.get("price") or {})
                item_plan_rows.append((label, monthly))
                item_monthly_total += monthly

        if status not in REVENUE_STATUSES:
            if item_monthly_total > 0:
                valuation_methods["non_revenue_or_trial_with_items"] += 1
            else:
                valuation_methods["zero_or_trial"] += 1
            continue

        invoice_backed = latest_invoice_monthly_amount(sub)
        if invoice_backed > 0:
            sub_monthly = invoice_backed
            valuation_methods["latest_invoice"] += 1
        elif item_monthly_total > 0:
            sub_monthly = item_monthly_total
            valuation_methods["subscription_items_fallback"] += 1
        else:
            paid_fallback = invoice_monthly_amount(latest_paid_map.get(sub.get("id")) or {})
            if paid_fallback > 0:
                sub_monthly = paid_fallback
                valuation_methods["latest_paid_invoice_fallback"] += 1
            else:
                sub_monthly = 0.0
                valuation_methods["unvalued"] += 1

        mrr += sub_monthly
        for label, monthly in item_plan_rows:
            plan_mix[label]["subscriptions"] += 1
            plan_mix[label]["mrr"] += monthly

    plan_mix_rows = [
        {
            "plan": name,
            "subscriptions": vals["subscriptions"],
            "mrr": round(vals["mrr"], 2),
        }
        for name, vals in sorted(plan_mix.items(), key=lambda kv: (-kv[1]["mrr"], kv[0]))
    ]
    return {
        "subscription_status_counts": dict(status_counts),
        "estimated_mrr": round(mrr, 2),
        "mrr_included_statuses": sorted(REVENUE_STATUSES),
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
    return {
        "invoice_status_counts": dict(invoice_status),
        "delinquent_subscriptions": delinquent,
        "delinquent_count": len(delinquent),
    }


def data_quality(elapsed):
    return {
        "key_source": "STRIPE_SECRET_KEY or STRIPE",
        "mrr_method": "Canonical MRR uses latest-invoice recurring subscription lines normalized to monthly and net of line-level discounts where available; falls back to current subscription-item pricing with archived-price/tier fetch support, then latest paid recurring invoice if needed.",
        "notes": [
            "Canonical MRR includes active, past_due, and unpaid subscriptions by default.",
            "Plan mix still comes from current subscription-item pricing, so it may not sum exactly to invoice-backed MRR when discounts or invoice-specific adjustments exist.",
            "Revenue windows use paid invoices only and are restricted to the needed date range for speed.",
            "Restricted keys may block some account-level endpoints; this script does not depend on /account.",
        ],
        "elapsed_seconds": round(elapsed, 2),
    }


def finalize(mode, start, payload):
    payload.setdefault("generated_at", datetime.now(timezone.utc).isoformat())
    payload["data_quality"] = data_quality(time.time() - start)
    return payload


def build_snapshot():
    start = time.time()
    now, _, start_last = month_bounds()
    price_cache = {}
    status_counts, canceled_this_month = load_subscription_status_snapshot()
    customers = load_customers()
    paid_invoices_all = load_invoices(status="paid", expand_lines=False)
    paid_invoices_recent = [
        inv for inv in paid_invoices_all if (inv.get("created") or 0) >= int(start_last.timestamp())
    ]
    revenue_subs = load_subscriptions(statuses=sorted(REVENUE_STATUSES), price_cache=price_cache, expand_latest_invoice_lines=True)
    delinquency_context_invoices = load_invoices_for_statuses(["open", "uncollectible", "draft"], expand_lines=False)
    out = {
        "customers": {
            "total": len(customers),
            "signups": customer_signup_counts(customers),
            "paid_acquisition": paid_customer_acquisition(paid_invoices_all),
        },
        "subscriptions": subscription_metrics(revenue_subs, status_counts=status_counts, canceled_this_month=canceled_this_month),
        "revenue": invoice_revenue_counts(paid_invoices_recent),
        "delinquency": delinquency_metrics(revenue_subs, delinquency_context_invoices),
        "snapshot_scope": {
            "customer_total_scope": "all customers",
            "revenue_scope": "paid invoices this month vs last month",
            "mrr_scope": "latest invoice-backed recurring value across active/past_due/unpaid subscriptions",
        },
    }
    return finalize("snapshot", start, out)


def build_signups():
    start = time.time()
    customers = load_customers()
    paid_invoices = load_invoices(status="paid", expand_lines=False)
    out = {
        "total": len(customers),
        "signups": customer_signup_counts(customers),
        "paid_acquisition": paid_customer_acquisition(paid_invoices),
    }
    return finalize("signups", start, out)


def build_revenue():
    start = time.time()
    _, _, start_last = month_bounds()
    invoices = load_invoices(status="paid", expand_lines=False, created_gte=int(start_last.timestamp()))
    out = invoice_revenue_counts(invoices)
    return finalize("revenue", start, out)


def build_mrr_or_plans(include_plans=False):
    start = time.time()
    price_cache = {}
    status_counts, canceled_this_month = load_subscription_status_snapshot()
    subs = load_subscriptions(statuses=sorted(REVENUE_STATUSES), price_cache=price_cache, expand_latest_invoice_lines=True)
    subm = subscription_metrics(subs, status_counts=status_counts, canceled_this_month=canceled_this_month)
    out = {
        "estimated_mrr": subm["estimated_mrr"],
        "mrr_included_statuses": subm["mrr_included_statuses"],
        "valuation_methods": subm["valuation_methods"],
        "subscription_status_counts": subm["subscription_status_counts"],
        "canceled_this_month": subm["canceled_this_month"],
    }
    if include_plans:
        out["plan_mix"] = subm["plan_mix"]
    return finalize("plans" if include_plans else "mrr", start, out)


def build_delinquency():
    start = time.time()
    price_cache = {}
    subs = load_subscriptions(statuses=sorted(REVENUE_STATUSES), price_cache=price_cache, expand_latest_invoice_lines=False)
    invoices = load_invoices_for_statuses(["open", "uncollectible", "draft"], expand_lines=False)
    out = delinquency_metrics(subs, invoices)
    return finalize("delinquency", start, out)


def main():
    parser = argparse.ArgumentParser(description="Read-only Stripe analytics for Oviond")
    parser.add_argument("mode", nargs="?", default="snapshot", choices=["snapshot", "mrr", "signups", "revenue", "plans", "delinquency"])
    parser.add_argument("--live", action="store_true", help="Bypass cached output and refresh from Stripe.")
    parser.add_argument("--cache-ttl", type=int, default=None, help="Override cache TTL in seconds. Use 0 to disable cache.")
    args = parser.parse_args()

    ttl = default_ttl(args.mode) if args.cache_ttl is None else args.cache_ttl
    if not args.live:
        cached = load_cached(args.mode, ttl)
        if cached is not None:
            json.dump(cached, sys.stdout, indent=2)
            sys.stdout.write("\n")
            return

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

    out = write_cache(args.mode, out, ttl)
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
