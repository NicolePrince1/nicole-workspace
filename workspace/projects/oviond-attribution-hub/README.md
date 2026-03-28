# Oviond Attribution Hub

A Railway-ready internal Next.js app that turns Oviond into the source of truth for attribution.

## What it does

- records canonical business events in Postgres
- treats the event ledger as truth
- fans those events out to downstream platforms
- shows delivery attempts for Meta, GA4, and Google Ads
- ingests verified Stripe webhooks into the same ledger
- provides a replay endpoint so stored events can be re-sent after credentials/config change

## Canonical events

The app is built around these event types:

- `signup_started`
- `email_verified`
- `trial_started`
- `subscription_started`
- `invoice_paid`
- `trial_expired`
- `subscription_cancelled`

## Architecture

1. Oviond backend emits a canonical event to `POST /api/ingest`
2. the event is validated with `zod`
3. the event is stored in Postgres
4. inline dispatch attempts are made to:
   - Meta Conversions API
   - GA4 Measurement Protocol
   - Google Ads adapter scaffold
5. every downstream attempt is logged in `delivery_attempts`
6. Stripe webhook events can also create canonical events directly

## Stack

- Next.js App Router
- TypeScript
- Tailwind CSS v4
- `postgres` package for Railway Postgres
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

```bash
GOOGLE_ADS_CUSTOMER_ID=1234567890
GOOGLE_ADS_DEVELOPER_TOKEN=...
GOOGLE_ADS_REFRESH_TOKEN=...
GOOGLE_ADS_CONVERSION_ACTION_ID=...
GOOGLE_ADS_LOGIN_CUSTOMER_ID=...
```

### Stripe

```bash
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

## Railway deploy

1. Create a new Railway project.
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

### Ingest canonical event

```bash
curl -X POST http://localhost:3000/api/ingest \
  -H "Authorization: Bearer $INGEST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "event_type": "trial_started",
    "event_id": "trial_123",
    "source": "oviond-app",
    "user_id": "user_123",
    "user_email": "customer@example.com",
    "account_id": "account_123",
    "plan_name": "Agency",
    "trial_days": 15,
    "billing_model": "free_trial",
    "session_source": "meta",
    "session_medium": "paid-social",
    "session_campaign": "remarketing_usa_free_trial_test",
    "fbclid": "fbclid-value",
    "fbp": "fb.1...",
    "fbc": "fb.1...",
    "page_path": "/signup",
    "page_location": "https://v2.oviond.com/signup",
    "raw_payload": {
      "trigger": "signup_api_success"
    }
  }'
```

### Stripe webhook

```bash
POST /api/stripe/webhook
```

Verifies the Stripe signature and records mapped canonical events.

### Replay a stored event

```bash
curl -X POST http://localhost:3000/api/internal/replay \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"eventId": "trial_123"}'
```

## Meta mapping

Current mapping:

- `signup_started` -> `Lead`
- `email_verified` -> `CompleteRegistration`
- `trial_started` -> `StartTrial`
- `subscription_started` -> `Subscribe`
- `invoice_paid` -> `Purchase`

The adapter sends the same `event_id` to support browser/server dedupe later.

## GA4 mapping

GA4 receives the canonical event names directly over Measurement Protocol.

## Google Ads status

The Google Ads adapter is intentionally scaffolded but not live-uploading yet.

Why:
- the app can already validate whether the right config is present
- it can show which events are eligible for Google Ads delivery
- it can log replay attempts later
- but it avoids pretending delivery succeeded before account/API access is fully confirmed

## Recommended Oviond app wiring

The product should emit `trial_started` only when the backend confirms a real trial exists.

Do **not** fire canonical conversion events from:
- page views
- button clicks
- plain form submits
- DOM selector hacks

## Quality checks

Run before deploy:

```bash
npm run lint
npm run build
```
