---
name: stripe-reader
description: Read and analyze Stripe billing data for SaaS reporting. Use when the user wants Stripe revenue, customers, subscriptions, MRR approximations, churn investigation, plan mix, failed payments, or billing diagnostics. Prefer this skill for read-only Stripe analysis and recurring finance snapshots.
---

Use Stripe in read-only mode.

## Workflow

1. Require a Stripe secret or restricted key in the environment as `STRIPE_SECRET_KEY` unless the user explicitly provides a temporary key for one-off testing.
2. Prefer the bundled script `scripts/stripe_snapshot.py` for fast account snapshots.
3. For deeper analysis, extend from the script or call Stripe REST endpoints with the same auth pattern.
4. Do not commit live keys, paste them into tracked files, or echo full secrets back to the user.
5. Summarize findings in business language: MRR trend, active subscriptions, delinquency risk, plan mix, and notable account movements.

## Commands

Quick snapshot:

```bash
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_snapshot.py
```

Use a temporary key for one-off testing without persisting it:

```bash
STRIPE_SECRET_KEY=sk_live_or_rk_live python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_snapshot.py
```

## Outputs

The script returns a compact JSON snapshot with:

- account id
- default currency
- active and trialing subscription counts
- customer count estimate (first page)
- invoice status sample
- recent MRR estimate from active/trialing subscriptions using recurring line items on the first 100 subscriptions

Treat MRR as directional unless a full pagination pass or warehouse source confirms it.
