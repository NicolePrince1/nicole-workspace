# Oviond Attribution Hub

A Railway-ready internal Next.js app that treats Stripe as lifecycle truth and stitches attribution data onto real business events before sending them to Meta, GA4, and Google Ads.

## The model

### Stripe is truth

The hub no longer asks the app to decide whether a conversion happened.

Instead:

- `trial_started` comes from Stripe `customer.subscription.created` when the subscription is `trialing`
- `subscription_started` comes from Stripe subscription lifecycle changes when the account becomes paid/active
- `invoice_paid` comes from Stripe `invoice.paid`
- `subscription_cancelled` comes from Stripe subscription cancellation/deletion
- `trial_expired` is derived from Stripe subscription lifecycle changes when a trial ends without becoming active paid

### The app captures attribution

Oviond should send attribution captures into the hub before or around signup:

- `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`
- `fbclid`, `fbc`, `fbp`
- `gclid`, `gbraid`, `wbraid`
- landing page, page path, page location, referrer
- email / user ID / account ID / Stripe customer ID / Stripe subscription ID when available

### The hub stitches the two together

When a Stripe lifecycle event arrives, the hub finds the best matching attribution capture in this order:

1. `stripe_customer_id`
2. `stripe_subscription_id`
3. `user_id`
4. `account_id`
5. `email`

The most recent reasonable match wins. That stitched lifecycle event is what gets delivered downstream.

## What it does

- stores Stripe lifecycle events in Postgres
- stores attribution captures separately in Postgres
- stitches attribution onto Stripe truth on ingest and replay
- fans stitched events out to Meta, GA4, and Google Ads adapters
- shows lifecycle volume, attribution match rate, and recent delivery attempts in a dashboard
- provides replay tooling for re-dispatching stored lifecycle events

## Stack

- Next.js App Router
- TypeScript
- Tailwind CSS v4
- `postgres` for Railway Postgres
- `stripe` for webhook verification
- `zod` for schema validation

## Local development

```bash
npm install
npm run dev
```

Open <http://localhost:3000>

## Required environment variables

### Core

```bash
DATABASE_URL=postgres://...
INGEST_API_KEY=replace-with-long-random-string
ADMIN_TOKEN=replace-with-long-random-string
```

### Stripe

```bash
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

### Meta Conversions API

```bash
META_PIXEL_ID=338809875265876
META_ACCESS_TOKEN=...
```

### GA4 Measurement Protocol

```bash
GA4_MEASUREMENT_ID=G-XXXXXXXXXX
GA4_API_SECRET=...
```

### Google Ads adapter scaffold

This project intentionally remains a **refresh-token scaffold** for now.

Workspace-standard Google Ads operations are service-account-first, but this app has not been migrated to that model yet. Its local adapter/env wiring still expects the older refresh-token shape below, and the scaffold should be treated as project-local until a deliberate service-account migration is done.

```bash
GOOGLE_ADS_CUSTOMER_ID=1234567890
GOOGLE_ADS_DEVELOPER_TOKEN=...
GOOGLE_ADS_REFRESH_TOKEN=...
GOOGLE_ADS_CONVERSION_ACTION_ID=...
GOOGLE_ADS_LOGIN_CUSTOMER_ID=...
```

## Railway deploy

1. Create or open the Railway project.
2. Add a Postgres service.
3. Deploy this app as a Node/Next service.
4. Set the environment variables above.
5. Open the deployed URL and log in with `ADMIN_TOKEN`.

Notes:
- the schema bootstraps itself with `CREATE TABLE IF NOT EXISTS`
- no separate migration tool is required for the MVP
- secrets stay server-side only

## API

### Health check

```bash
GET /api/health
```

Returns runtime + database readiness.

### Capture attribution

```bash
curl -X POST http://localhost:3000/api/attribution/capture \
  -H "Authorization: Bearer $INGEST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "customer@example.com",
    "stripe_customer_id": "cus_123",
    "utm_source": "meta",
    "utm_medium": "paid-social",
    "utm_campaign": "remarketing_usa_free_trial_test",
    "fbclid": "fbclid-value",
    "fbc": "fb.1...",
    "fbp": "fb.1...",
    "landing_page": "https://v2.oviond.com/signup",
    "page_path": "/signup",
    "page_location": "https://v2.oviond.com/signup?utm_source=meta",
    "referrer": "https://facebook.com/",
    "raw_payload": {
      "trigger": "signup_page_loaded"
    }
  }'
```

### Stripe webhook

```bash
POST /api/stripe/webhook
```

Verifies the Stripe signature and records mapped lifecycle events.

### Manual lifecycle ingest

```bash
curl -X POST http://localhost:3000/api/ingest \
  -H "Authorization: Bearer $INGEST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "event_type": "trial_started",
    "event_id": "stripe_evt_test_123",
    "source": "manual-backfill",
    "stripe_customer_id": "cus_123",
    "stripe_subscription_id": "sub_123",
    "user_email": "customer@example.com",
    "billing_model": "free_trial",
    "trial_days": 15,
    "raw_payload": {
      "reason": "backfill"
    }
  }'
```

### Replay a stored lifecycle event

```bash
curl -X POST http://localhost:3000/api/internal/replay \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"eventId": "stripe_evt_test_123"}'
```

## Downstream mapping

### Meta

- `trial_started` -> `StartTrial`
- `subscription_started` -> `Subscribe`
- `invoice_paid` -> `Purchase`

### GA4

GA4 receives the Stripe lifecycle event names directly over Measurement Protocol.

### Google Ads

Google Ads delivery remains scaffolded and disabled-safe until production Ads API access is fully confirmed.

Important: this repository's Google Ads adapter is still a refresh-token scaffold by design. That is a project-specific exception, not the main workspace standard. Do not read this README as the canonical Google Ads auth pattern for the broader workspace.

## Recommended Oviond wiring

1. Capture attribution as early as possible.
2. Include stable IDs when you have them:
   - Stripe customer ID
   - Stripe subscription ID
   - user/account ID
   - email
3. Let Stripe webhooks declare lifecycle truth.
4. Avoid treating page views, button clicks, or raw form submits as conversion truth.

## Quality checks

Run before deploy:

```bash
npm run lint
npm run build
```
