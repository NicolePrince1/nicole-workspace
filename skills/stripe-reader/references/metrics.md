# Stripe Reader Metrics Notes

## Canonical MRR

Primary metric:
- `estimated_mrr`

Definition:
- invoice-backed normalized MRR across `active`, `past_due`, and `unpaid` subscriptions
- based on the subscription’s latest recurring invoice lines when available
- net of line-level discounts where present
- normalized to monthly based on the billed period length

Fallbacks:
1. latest invoice recurring lines
2. current subscription-item pricing with archived-price + tier expansion support
3. latest paid recurring invoice if required

## Why this is better than pure price math

Pure price math is fragile when the account has:
- archived prices
- tiered prices
- invoice-level discount effects
- billing states where the latest invoice reality differs from the current raw price object

Oviond’s Stripe account has enough of that complexity that invoice-backed MRR is a better operational truth source.

## Plan mix

`plan_mix` is built from current subscription items and price definitions.
That makes it good for:
- plan-family visibility
- relative mix
- spotting which plans are carrying revenue

But it may not equal invoice-backed MRR exactly when discounts or invoice-specific adjustments exist.

## Revenue windows

`revenue` mode uses paid invoices only and compares:
- this month vs last month

## Signups

`signups` mode reports:
- customer signups this month vs last month
- first-paid customer counts this month vs last month

## Delinquency

`delinquency` mode focuses on:
- `past_due` subscriptions
- `unpaid` subscriptions
- latest open / uncollectible / draft invoice context

## Cache semantics

Every mode can return cached data unless `--live` is used.
Outputs include a `cache` block so you can see:
- whether cached data was used
- cache path
- TTL
- cache age

## Recommended usage

For a quick operational check:

```bash
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py mrr
```

For the freshest live read:

```bash
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py mrr --live
```

For a combined commercial snapshot:

```bash
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py snapshot --live
```
