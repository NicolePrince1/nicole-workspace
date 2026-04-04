---
name: mailerlite
description: "Manage Oviond's MailerLite account — subscribers, campaigns, automations, groups, forms. Read analytics, manage lists, create and send campaigns, analyze engagement."
metadata:
  {
    "openclaw":
      {
        "emoji": "📧",
      },
  }
---

# MailerLite Skill — Oviond

Manage Oviond's email marketing via the MailerLite REST API.

## Authentication

```bash
# API key is in env var MAILER_LITE
# All requests need these headers:
# Authorization: Bearer $MAILER_LITE
# Content-Type: application/json
# Accept: application/json
```

Base URL: `https://connect.mailerlite.com/api`
Rate limit: 120 requests/minute

**Important:** URL-encode bracket characters in query params. Use `%5B` for `[` and `%5D` for `]`.

## Account Shape

- MailerLite is used as a lifecycle email system with subscribers, groups, automations, campaigns, and forms.
- Expect lifecycle-oriented segments for trial, paying, lapsed, dormant, LTD, and reactivation flows.
- Treat counts and current segment sizes as live data to query at runtime, not as durable skill guidance.

## API Endpoints

### Subscribers

```bash
# List subscribers (paginated via cursor)
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/subscribers?limit=25"

# Filter by status: active, unsubscribed, unconfirmed, bounced, junk
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/subscribers?filter%5Bstatus%5D=active&limit=25"

# Get single subscriber (by ID or email)
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/subscribers/user@example.com"

# Create/upsert subscriber
curl -X POST -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/subscribers" \
  -d '{"email":"user@example.com","fields":{"name":"John","last_name":"Doe"},"groups":["GROUP_ID"]}'

# Delete subscriber
curl -X DELETE -H "Authorization: Bearer $MAILER_LITE" \
  "https://connect.mailerlite.com/api/subscribers/{SUBSCRIBER_ID}"
```

### Groups

```bash
# List all groups
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/groups?limit=50&sort=name"

# Get group subscribers
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/groups/{GROUP_ID}/subscribers?limit=25"

# Create group
curl -X POST -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/groups" \
  -d '{"name":"New Group Name"}'

# Assign subscriber to group
curl -X POST -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/subscribers/{SUBSCRIBER_ID}/groups/{GROUP_ID}"
```

### Campaigns

```bash
# List campaigns (filter by status: sent, draft, ready)
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/campaigns?filter%5Bstatus%5D=sent&limit=25"

# Get campaign details
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/campaigns/{CAMPAIGN_ID}"

# Get campaign subscriber activity
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/campaigns/{CAMPAIGN_ID}/reports/subscriber-activity?limit=25"

# Create campaign
curl -X POST -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/campaigns" \
  -d '{
    "name": "Campaign Name",
    "type": "regular",
    "emails": [{
      "subject": "Email Subject",
      "from_name": "Oviond",
      "from": "hello@oviond.com",
      "reply_to": "hello@oviond.com",
      "content": "<html>Email HTML content</html>"
    }],
    "groups": ["GROUP_ID"],
    "filter": [
      [{"operator": "in_any", "args": ["groups", ["GROUP_ID"]]}]
    ]
  }'

# Schedule campaign
curl -X POST -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/campaigns/{CAMPAIGN_ID}/schedule" \
  -d '{"delivery": "scheduled", "date": "2026-03-15 10:00:00"}'

# Send campaign immediately
curl -X POST -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/campaigns/{CAMPAIGN_ID}/schedule" \
  -d '{"delivery": "instant"}'

# Cancel scheduled campaign
curl -X POST -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/campaigns/{CAMPAIGN_ID}/cancel"
```

### Automations

```bash
# List automations
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/automations?limit=25"

# Get automation details
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/automations/{AUTOMATION_ID}"

# Get automation subscriber activity
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/automations/{AUTOMATION_ID}/activity?limit=25"
```

### Forms

```bash
# List forms (types: popup, embedded, promotion)
curl -s -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/forms/popup?limit=25"
```

### Batch Operations

```bash
# Batch API — up to 20 operations per request
curl -X POST -H "Authorization: Bearer $MAILER_LITE" -H "Content-Type: application/json" \
  "https://connect.mailerlite.com/api/batch" \
  -d '{
    "requests": [
      {"method": "GET", "path": "/api/subscribers?limit=1"},
      {"method": "GET", "path": "/api/groups?limit=50"},
      {"method": "GET", "path": "/api/campaigns?filter%5Bstatus%5D=sent"}
    ]
  }'
```

## Key Automation Types

Common automation categories to inspect:
- trial onboarding
- expired trial re-engagement
- paying customer onboarding
- churn recovery / reactivation
- seasonal or promotional sequences
- LTD upsell or upgrade flows

Query current automation names, statuses, and send volumes at runtime instead of relying on fixed examples in the skill body.

## Subscriber Custom Fields

Oviond syncs rich customer data into MailerLite custom fields:
- `customer_id` — Stripe customer ID
- `active_plan` — Current plan name
- `subscription_status` — trialing, active, canceled, past_due
- `trialing` — true/false
- `is_lifetime_user` — true/false (LTD users)
- `projects_count`, `dashboards_count`, `clients_count` — usage metrics
- `current_period_end` — subscription renewal date
- `amount` — payment amount
- `product_name` — Stripe product name

This means we can segment by subscription status, usage, plan type — very powerful for targeted campaigns.

## Output Formatting (Slack)

```
*MailerLite Overview*

*Lifecycle Groups:*
• Trial Users — X active
• Active Paying — Y active
• Lapsed — Z (reactivation opportunity)
• LTD Users — N
• Dormant — M

*Recent Campaign:*
• Campaign Name — X sent, Y% open, Z% click

*Top Automations:*
• Trial onboarding — X sent
• Reactivation flow — Y sent
• Expired trial win-back — Z sent
```

## Safety Rules

- **Always confirm before sending** any campaign
- **Always confirm before deleting** subscribers
- **Draft campaigns first** — create as draft, show to user, then schedule/send
- **Never bulk-delete** without explicit approval
- Respect rate limit: 120 req/min, use batch endpoint for bulk ops
