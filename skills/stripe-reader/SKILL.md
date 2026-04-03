---
name: stripe-reader
description: Read and analyze Stripe billing data for SaaS reporting. Use when the user wants current MRR, revenue, new customer signups, paid acquisition, plan mix, delinquency, cancellations, or recurring billing diagnostics from Stripe in read-only mode.
---

# Stripe Reader

Read-only Stripe billing analytics for Oviond.

## What this skill is for

Use this skill when you need:
- current MRR
- paid revenue this month vs last month
- signup counts
- first-paid customer counts
- plan mix
- delinquency / unpaid / past_due visibility
- billing diagnostics

## Operating model

Use the local analytics script:

```bash
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py <mode>
```

Modes:
- `snapshot` — combined business snapshot
- `mrr` — canonical current MRR
- `plans` — current MRR + plan mix
- `revenue` — paid invoice revenue windows
- `signups` — customer signups + first-paid counts
- `delinquency` — current past_due / unpaid / open-invoice view

Optional flags:
- `--live` — bypass cache and refresh from Stripe
- `--cache-ttl <seconds>` — override cache TTL; use `0` to disable cache

## MRR definition

This skill now treats **invoice-backed normalized MRR** as the primary MRR source.

That means:
- use each subscription’s **latest invoice** recurring subscription lines when available
- normalize each recurring line to monthly based on its billed period
- subtract line-level discounts where present
- include `active`, `past_due`, and `unpaid` subscriptions by default

Fallback order:
1. latest invoice recurring lines
2. current subscription-item pricing, including archived prices and tier expansion
3. latest paid recurring invoice if needed

This is materially more accurate for Oviond than pure price math.

## Important interpretation rules

- Treat `estimated_mrr` from this skill as the best local operational MRR read.
- If the user already has a Stripe Dashboard number and needs finance-grade confirmation, prefer the dashboard as the ultimate tie-breaker.
- `plan_mix` is derived from current subscription-item pricing, so it may not sum perfectly to invoice-backed MRR when discounts or invoice-specific adjustments exist.

## Performance / cache

The script now writes cached JSON snapshots under:

- `/data/.openclaw/db/stripe-reader/`

This is for speed only.
Do not commit cache files.

Default TTLs:
- `mrr` / `plans`: 5 minutes
- `revenue`: 3 minutes
- `delinquency`: 5 minutes
- `signups`: 10 minutes
- `snapshot`: 15 minutes

## Guardrails

- Read-only only
- Never mutate Stripe data from this skill
- When reporting MRR, say what method you used if accuracy matters
- When the user asks for “current MRR right now”, prefer `mrr --live`
- When the user asks for a quick heartbeat / status check, cached mode is fine unless freshness is critical
