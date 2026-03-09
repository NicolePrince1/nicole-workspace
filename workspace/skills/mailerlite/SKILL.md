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

## Account Overview

- **Subscribers:** ~9,000+ across all statuses
- **Groups:** 20+ lifecycle-based segments (trial, paying, lapsed, dormant, LTD, reactivation)
- **Automations:** 10+ active workflows (trial onboarding, expired reactivation, paying customer onboarding, churn recovery, reactivation series)
- **Campaigns:** Primarily automation-driven; 1 sent campaign, 1 draft
- **Forms:** 1 popup (exit intent)

### Key Groups (Lifecycle Segments)

| Group | Purpose | Active |
|-------|---------|--------|
| 1.1. Trial Users (0-15 Days) | Active trialing users | ~46 |
| 2.1. Trial Expired - Reactivation (16-68 Days) | Win-back expired trials | ~248 |
| 3.1. Paying Customer Onboarding (0-30 Days) | New customer nurture | ~23 |
| 3.2. Active Paying Customers - All | Current paying base | ~350 |
| 4.1. Lapsed Customer - Reactivation | Cancelled/stale trial recovery | ~1,916 |
| 5.1. Lifetime Free Users | LTD users | ~1,027 |
| 6.1. Dormant Contacts | Cold contacts | ~2,644 |
| 102 - Reach out Then Unsubscribe | Cleanup segment | ~3,179 |

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

## Key Automations

| Automation | Sends | Purpose |
|-----------|-------|---------|
| 101 - Reactivate or Scrub | 31,316 | Main reactivation/cleanup flow |
| 1.1. Trialling Simplified (15 Days) | 10,765 | Trial onboarding sequence |
| 7 Email Reactivation Series Nov 2025 | 14,251 | Reactivation campaign |
| 1.2. Trial Expired Re-Engagement | 8,732 | Expired trial win-back |
| Black Friday 2025 | 6,649 | Seasonal promo |
| 3.1. Paying Customer Onboarding | 2,186 | New customer nurture |
| Trialing Users 3-Step Reward | 1,762 | Trial incentive sequence |
| 4.1. LTD Client Limit Upgrade | 1,142 | LTD upsell flow |

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
• Trial Users (0-15 days) — 46 active
• Active Paying — 350 active
• Lapsed — 1,916 (reactivation opportunity)
• LTD Users — 1,027
• Dormant — 2,644

*Recent Campaign:*
• LTD Upgrade Accelerator — 5,635 sent, 15.4% open, 4.8% click ✅

*Top Automations:*
• Trial Onboarding (15 days) — 10,765 sent
• Reactivate or Scrub — 31,316 sent
• Trial Expired Win-back — 8,732 sent
```

## Safety Rules

- **Always confirm before sending** any campaign
- **Always confirm before deleting** subscribers
- **Draft campaigns first** — create as draft, show to user, then schedule/send
- **Never bulk-delete** without explicit approval
- Respect rate limit: 120 req/min, use batch endpoint for bulk ops
