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

## Google Workspace

- nicole@oviond.com is my Google Workspace email address.
- Connected via service account with domain-wide delegation (project: oviond-workspace-cli).
- Service account: nicole-workspace@oviond-workspace-cli.iam.gserviceaccount.com
- Credentials stored at `/data/.openclaw/secrets/gws-service-account.json` (gitignored).
- Token helper: `/data/.openclaw/secrets/gws-token.js` — generates impersonated OAuth tokens.
- Wrapper: `gws-nicole` — drop-in replacement for `gws` that auto-injects the token.
- Or in scripts: `export GOOGLE_WORKSPACE_CLI_TOKEN=$(node /data/.openclaw/secrets/gws-token.js)`
- Authorized scopes: gmail.modify, gmail.send, calendar, drive, spreadsheets, documents, contacts.readonly, tasks.
- The `gws` CLI (v0.8.1) doesn't natively support service account subject impersonation, so we use the token helper approach.
- Gmail has ~15 messages, Drive has files including "Nicole Prince Control" doc.

## Google Analytics

- GA4 skill built at `skills/google-analytics/` with report runner and property discovery scripts
- Token helper at `/data/.openclaw/secrets/gws-analytics-token.js`
- Needs analytics scopes added to domain-wide delegation: `analytics.readonly` and `analytics`
- Needs Analytics Data API and Admin API enabled in GCP project `oviond-workspace-cli`
- GA4 property ID TBD — will discover via admin API once scopes are authorized
- nicole@oviond.com needs viewer/editor access on the GA4 property

## Google Ads

- Oviond Google Ads account: 290-615-4258 (under manager account 638-795-6297)
- Developer token: `z7adyM4vUm79lJCxNi0Ydg` (currently Test Account level — Basic Access application submitted 2026-03-09)
- nicole@oviond.com has been added as a user on the Ads account
- Service account impersonation works for the `adwords` scope
- GCP project `oviond-workspace-cli` (480335022137) has Google Ads API enabled
- Blocker: developer token needs Basic Access approval to hit production accounts (PROJECT_DISABLED error until then)
- Skill framework built at `skills/google-ads/` with GAQL query runner and mutate scripts
- Token helper at `/data/.openclaw/secrets/gws-ads-token.js`
- Cron reminder set for 2026-03-12 to check if access is approved
- The first developer token Chris gave (`oyZpQqJIpp3QdYanw-JtZA`) was wrong — the real one is `z7adyM4vUm79lJCxNi0Ydg`
- There's also a BizSage Google Ads sub-account (687-473-0709) under the manager

## Current Stripe learnings

- My first API probe confirmed access but did not yet reconstruct trustworthy MRR.
- The first sample from the API showed many `trialing`, `active`, and `paused` subscriptions, suggesting activation/reactivation is likely important.
- Chris shared a Stripe dashboard screenshot showing the real business picture more clearly: around $28k MRR, 312 active subscriptions, 2,030 customers, and meaningful payments volume.
- Trust the Stripe dashboard over the current script for MRR until the Stripe skill is improved.
- Next Stripe work should focus on full pagination, paid-vs-trial separation, plan mix, paused/reactivation opportunity, and churn-risk views.
