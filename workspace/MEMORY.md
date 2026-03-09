# MEMORY.md

## Identity and role

- I am Nicole Prince, VP of Marketing at Oviond.
- Chris Irwin is my boss.
- My remit covers marketing, strategy, delivery, research, positioning, growth planning, and execution support for Oviond.

## Oviond business context

- Oviond is a B2B SaaS reporting platform built primarily for marketing agencies.
- Brand/product direction: simple, clear, easy, uncluttered reporting for agencies; quick to set up; low learning curve; something agencies can set up and largely forget.
- GTM motion today: mostly self-serve SaaS, with some sales-led support for larger accounts.
- Ideal customer profile: small to medium-sized marketing agencies.
- Common switch sources: manual reporting, AgencyAnalytics, Looker Studio, Swydo, and similar reporting tools.
- Main reasons customers choose Oviond: simplicity, lower pricing, white-label reporting.
- Main reasons prospects say no: product can feel unpolished, missing integrations, weak initial setup/onboarding, or early perception that the product does not work.
- Growth target: move from about $28.5k MRR to $100k MRR by Dec 2026.

## Stripe context

- Chris provided a restricted Stripe key for read-only analysis.
- I created a reusable local skill at `skills/stripe-reader/` with a packaged artifact at `skills/dist/stripe-reader.skill`.
- The Stripe helper script is `skills/stripe-reader/scripts/stripe_snapshot.py`.
- The key works for billing reads like subscriptions, customers, and invoices, but does not have permission for `/account`.
- Do not store raw Stripe keys in tracked files or git.
- Preferred long-term setup: place the key in OpenClaw Envars as `STRIPE_SECRET_KEY`.

## Current Stripe learnings

- My first API probe confirmed access but did not yet reconstruct trustworthy MRR.
- The first sample from the API showed many `trialing`, `active`, and `paused` subscriptions, suggesting activation/reactivation is likely important.
- Chris shared a Stripe dashboard screenshot showing the real business picture more clearly: around $28k MRR, 312 active subscriptions, 2,030 customers, and meaningful payments volume.
- Trust the Stripe dashboard over the current script for MRR until the Stripe skill is improved.
- Next Stripe work should focus on full pagination, paid-vs-trial separation, plan mix, paused/reactivation opportunity, and churn-risk views.
