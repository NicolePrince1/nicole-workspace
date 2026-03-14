---
name: stripe-reader
description: Read and analyze Stripe billing data for SaaS reporting. Use when the user wants current MRR, revenue, new customer signups, paid acquisition, plan mix, delinquency, cancellations, or recurring billing diagnostics from Stripe in read-only mode.
---

Use Stripe in **read-only** mode via the bundled analytics script.

## Default rule

Do not rely on ad hoc first-page Stripe reads or the old snapshot logic.
Use `scripts/stripe_analytics.py` as the canonical Stripe workflow.

## Environment

The script accepts either:
- `STRIPE_SECRET_KEY`
- `STRIPE`

It normalizes those internally. Do not print or store raw keys.

## Core workflow

1. Run the analytics script in the smallest mode that answers the question.
2. Prefer `snapshot` for a full overview.
3. Use specific modes for focused answers.
4. Summarize results in business language after reading the JSON.
5. Keep Stripe usage read-only.

## Commands

Full snapshot:

```bash
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py snapshot
```

Focused modes:

```bash
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py mrr
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py signups
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py revenue
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py plans
python3 /data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py delinquency
```

## What it returns

The rebuilt analytics path is designed to answer:
- estimated current MRR
- subscription status counts
- customer signups this month vs last
- paid customer acquisition this month vs last
- paid invoice revenue this month vs last
- plan mix
- delinquent subscriptions and invoice status mix
- current data-quality notes about the calculation path

## Metric discipline

Read `references/metrics.md` when you need the exact metric definitions or want to explain caveats.

## Guardrails

- Read-only only.
- Do not create, update, refund, cancel, or delete Stripe objects through this skill.
- If a metric looks suspicious, inspect the JSON and explain the limitation instead of bluffing.
