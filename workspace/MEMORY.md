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

- Stripe access exists for read-only billing analysis.
- I created a reusable local skill at `skills/stripe-reader/` with a packaged artifact at `skills/dist/stripe-reader.skill`.
- The Stripe helper script is `skills/stripe-reader/scripts/stripe_snapshot.py`.
- Current access works for billing reads like subscriptions, customers, and invoices, but not `/account`.
- Do not store raw Stripe keys in tracked files or git.
- Preferred long-term setup: keep the key in OpenClaw Envars as `STRIPE_SECRET_KEY`.

## Google Workspace

- `nicole@oviond.com` is my Google Workspace email address.
- Google Workspace is connected via service-account impersonation with domain-wide delegation in project `oviond-workspace-cli`.
- Credentials and token helpers live in gitignored secret storage under `/data/.openclaw/secrets/`.
- Wrapper: `gws-nicole` — drop-in replacement for `gws` that injects an impersonated token.
- Authorized scopes include Gmail, Calendar, Drive, Sheets, Docs, Contacts, and Tasks.
- The `gws` CLI does not natively support service-account subject impersonation, so the local wrapper/helper approach is used.
- Gmail and Drive access were verified; Drive includes the "Nicole Prince Control" doc.

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

- Meta access is configured for Oviond’s Facebook, Instagram, and Ads assets.
- Access token material is stored in gitignored secret storage under `/data/.openclaw/secrets/`.
- Facebook Page: OVIOND.
- Instagram: `@ovionddigital`.
- Ad account uses ZAR.
- Pixel: Oviond 2024.
- Domain: `oviond.com` is verified.
- Active campaign at last check: "Remarketing USA" (Traffic objective, R350/day).
- Two paused campaigns at last check: "Remarketing Top Countries" and "United States - Free Trial Remarketing".
- Skill at `skills/meta/`.

## Google Analytics

- GA4 skill built at `skills/google-analytics/` with report runner and property discovery scripts.
- Token helper material lives in gitignored secret storage under `/data/.openclaw/secrets/`.
- Analytics scopes were added to the domain-wide delegation setup.
- Analytics Data API and Admin API are enabled in project `oviond-workspace-cli`.
- GA4 property: "Oviond Website + App".
- The Google Analytics setup is fully operational for `nicole@oviond.com`.

## Google Ads

- Oviond’s Google Ads setup is connected under the main manager account, with an additional BizSage sub-account also present.
- The Google Ads developer token exists in secret storage and must not be written into tracked workspace files.
- `nicole@oviond.com` has been added as a user on the Ads account.
- Service-account impersonation works for the `adwords` scope.
- Google Ads API is enabled in project `oviond-workspace-cli`.
- Current blocker: the developer token still needs Basic Access approval before production account access works cleanly (`PROJECT_DISABLED` until then).
- Skill framework built at `skills/google-ads/` with GAQL query runner and mutate scripts.
- Token helper material lives in gitignored secret storage under `/data/.openclaw/secrets/`.
- Cron reminder set for 2026-03-12 to check whether access has been approved.

## Current Stripe learnings

- My first API probe confirmed access but did not yet reconstruct trustworthy MRR.
- The first sample from the API showed many `trialing`, `active`, and `paused` subscriptions, suggesting activation/reactivation is likely important.
- Chris shared a Stripe dashboard screenshot showing the real business picture more clearly: around $28k MRR, 312 active subscriptions, 2,030 customers, and meaningful payments volume.
- Trust the Stripe dashboard over the current script for MRR until the Stripe skill is improved.
- Next Stripe work should focus on full pagination, paid-vs-trial separation, plan mix, paused/reactivation opportunity, and churn-risk views.
