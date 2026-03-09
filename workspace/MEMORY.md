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

## MailerLite

- API key stored in env var `MAILER_LITE` (added via AlphaClaw Envars)
- Skill at `skills/mailerlite/`
- Account has ~9,000+ subscribers across lifecycle segments
- 20+ groups organized by lifecycle stage (trial, paying, lapsed, dormant, LTD)
- 10+ automations running (trial onboarding, expired reactivation, paying customer nurture, reactivation, churn recovery)
- Rich custom fields synced from Stripe (customer_id, plan, status, usage metrics)
- Key insight: account is heavily automation-driven, only 1 sent campaign vs 10+ automations
- Largest segments: Dormant (2,644), Reach-out-then-unsub (3,179), Lapsed (1,916), LTD users (1,027)
- Top automation by volume: "101 - Reactivate or Scrub" (31,316 sends)

## Meta (Facebook + Instagram)

- System User: Nicole Prince (ID: 61584969418636) — Admin access, non-expiring token
- Business Manager ID: 287659180931920
- Facebook Page: OVIOND (ID: 1700329636926546) — 798 followers, full control
- Instagram: @ovionddigital (ID: 17841415739993320) — 85 followers, 3 posts
- Ad Account: act_286631686227626 (Oviond, currency: ZAR)
- Pixel: Oviond 2024
- Domain: oviond.com verified
- Token stored at `/data/.openclaw/secrets/meta-token.txt` (gitignored)
- Active campaign: "Remarketing USA" (Traffic objective, R350/day)
- 2 paused campaigns: "Remarketing Top Countries" (Sales), "United States - Free Trial Remarketing" (Leads, R300/day)
- Skill at `skills/meta/`

## Google Analytics

- GA4 skill built at `skills/google-analytics/` with report runner and property discovery scripts
- Token helper at `/data/.openclaw/secrets/gws-analytics-token.js`
- Needs analytics scopes added to domain-wide delegation: `analytics.readonly` and `analytics`
- Needs Analytics Data API and Admin API enabled in GCP project `oviond-workspace-cli`
- GA4 property: "Oviond Website + App" — Property ID: 432527276 (Account: Oviond, 109663738)
- All scopes working, APIs enabled, nicole@oviond.com has access — fully operational

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
