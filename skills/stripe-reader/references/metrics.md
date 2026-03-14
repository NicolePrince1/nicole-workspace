# Stripe metrics notes

## Purpose

This skill is for reliable read-only Stripe analytics inside the hosted OpenClaw runtime.

## Metric definitions

### Estimated MRR

Estimated MRR is computed from the **current recurring billing state**, not from the first page of subscriptions and not from manual dashboard fallback.

Primary method:
- value `active`, `past_due`, and `unpaid` subscriptions from recurring subscription items
- support both `per_unit` and `tiered` prices
- normalize monthly, yearly, weekly, and daily intervals to monthly values

Fallback method:
- if a revenue-carrying subscription cannot be valued from its subscription items, use the most recent paid recurring invoice lines for that subscription

Exclusions:
- zero-value trial subscriptions
- canceled subscriptions
- one-off invoice items

### Signups

Customer signups are counted from Stripe customer `created` timestamps:
- this month = customers created since the first day of the current UTC month
- last month = customers created in the prior UTC month window

### Paid customer acquisition

Paid acquisition is counted from the **first paid invoice with positive amount** for each customer.

### Revenue

Revenue in the snapshot is **cash collected from paid invoices** in the requested period, using `amount_paid`.

### Delinquency

Delinquency is based on subscription status (`past_due`, `unpaid`) plus current invoice status context where available.

### Plan mix

Plan mix groups recurring value by the best available plan label from:
1. product name
2. price nickname
3. price lookup key
4. price id

## Notes

- This script is designed for restricted-key reality and does not depend on `/account`.
- Tiered pricing is common in this Stripe account, so `price.unit_amount` alone is not reliable.
- Use the JSON output as the source of truth for calculations, then translate it into business language.
