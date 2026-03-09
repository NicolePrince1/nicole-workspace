---
name: google-ads
description: "Query, audit, and optimize the Oviond Google Ads account via the Google Ads API (v21). Read campaign/keyword/ad group performance, manage bids, pause/enable entities, find wasted spend, and run optimization audits."
metadata:
  {
    "openclaw":
      {
        "emoji": "📊",
      },
  }
---

# Google Ads Skill — Oviond

Manage the Oviond Google Ads account via the Google Ads API v21.

## Account Details

- **Manager Account:** 638-795-6297 (Oviond MCC)
- **Oviond Ads Account:** 290-615-4258
- **Developer Token:** stored in env `GOOGLE_ADS_DEVELOPER_TOKEN`
- **Auth:** Service account impersonation of nicole@oviond.com via `GOOGLE_ADS_TOKEN` env var

## Authentication

Before any API call, get an access token:

```bash
# Generate token (uses service account → nicole@oviond.com impersonation)
export GOOGLE_ADS_TOKEN=$(node /data/.openclaw/secrets/gws-ads-token.js)
```

## GAQL Query Runner

Use the helper script for all queries:

```bash
# Read query
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_query.js "SELECT campaign.name, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC"

# Mutate operation (writes)
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_mutate.js <operation_json_file>
```

## Common GAQL Queries

### Campaign Performance (Last 30 Days)
```sql
SELECT
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion,
  metrics.conversions_value
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
```

### Keyword Performance
```sql
SELECT
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  campaign.name,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion,
  metrics.search_impression_share
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

### Wasted Spend (Zero-Conversion Keywords)
```sql
SELECT
  ad_group_criterion.keyword.text,
  campaign.name,
  metrics.cost_micros,
  metrics.clicks,
  metrics.impressions
FROM keyword_view
WHERE metrics.conversions = 0
  AND metrics.cost_micros > 5000000
  AND segments.date DURING LAST_90_DAYS
ORDER BY metrics.cost_micros DESC
```

### Ad Group Performance
```sql
SELECT
  ad_group.name,
  campaign.name,
  ad_group.status,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion
FROM ad_group
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
```

### Search Terms Report
```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

### Conversion Actions
```sql
SELECT
  conversion_action.name,
  conversion_action.type,
  conversion_action.status,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion
FROM conversion_action
WHERE segments.date DURING LAST_30_DAYS
```

### Daily Spend Trend
```sql
SELECT
  segments.date,
  metrics.cost_micros,
  metrics.clicks,
  metrics.impressions,
  metrics.conversions
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY segments.date DESC
```

### Geographic Performance
```sql
SELECT
  geographic_view.country_criterion_id,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM geographic_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 20
```

### Device Performance
```sql
SELECT
  segments.device,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
```

## Mutate Operations

### Pause a Campaign
```json
{
  "operations": [{
    "update": {
      "resourceName": "customers/2906154258/campaigns/{CAMPAIGN_ID}",
      "status": "PAUSED"
    },
    "updateMask": "status"
  }]
}
```

### Pause a Keyword
```json
{
  "operations": [{
    "update": {
      "resourceName": "customers/2906154258/adGroupCriteria/{AD_GROUP_ID}~{CRITERION_ID}",
      "status": "PAUSED"
    },
    "updateMask": "status"
  }]
}
```

### Update Campaign Budget
```json
{
  "operations": [{
    "update": {
      "resourceName": "customers/2906154258/campaignBudgets/{BUDGET_ID}",
      "amountMicros": "50000000"
    },
    "updateMask": "amountMicros"
  }]
}
```

## Audit Checklist

Run these queries in sequence for a full account health check:

1. **Campaign overview** — status, spend, conversions, CPA
2. **Wasted spend** — zero-conversion keywords with significant cost
3. **Search terms** — irrelevant queries eating budget
4. **Conversion tracking** — all actions active and firing
5. **Device split** — mobile vs desktop performance gaps
6. **Geographic** — spending in wrong regions
7. **Daily trend** — spend pacing and anomalies

## Output Formatting

When reporting to Slack (no markdown tables), use bullet lists:

```
*Campaign Performance (Last 30 Days)*

• *Branded Search* — $2,450 spend, 89 conversions, $27.53 CPA ✅
• *Competitor Terms* — $1,800 spend, 12 conversions, $150 CPA ⚠️
• *Display Remarketing* — $950 spend, 3 conversions, $316 CPA ❌

*Recommendations:*
1. Increase Branded Search budget — strong ROI
2. Review Competitor Terms — CPA 5x target
3. Pause Display Remarketing — below threshold
```

## Notes

- `cost_micros` = cost in micros (divide by 1,000,000 for dollars)
- All currency is in the account's currency (check `customer.currency_code`)
- GAQL dates: `DURING LAST_30_DAYS`, `DURING LAST_7_DAYS`, `DURING TODAY`, or `BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'`
- Rate limits: 15,000 requests per day for Basic Access
- Always confirm with user before mutate operations (pausing, budget changes)
