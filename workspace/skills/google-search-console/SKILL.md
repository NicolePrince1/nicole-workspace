---
name: google-search-console
description: "Query Oviond's Google Search Console data — keyword rankings, search impressions, clicks, CTR, page performance, and index coverage."
metadata:
  {
    "openclaw":
      {
        "emoji": "🔍",
      },
  }
---

# Google Search Console Skill — Oviond

Query SEO data for oviond.com via the Search Console API.

## Account Details

- **Property:** sc-domain:oviond.com (domain-level, full user access)
- **Auth:** Service account impersonation of nicole@oviond.com
- **Token helper:** `/data/.openclaw/secrets/gws-gsc-token.js`

## Query Runner

```bash
node /data/.openclaw/workspace/skills/google-search-console/scripts/gsc_query.js <report_json>
```

## API Endpoint

All queries use POST to:
```
https://searchconsole.googleapis.com/webmasters/v3/sites/sc-domain%3Aoviond.com/searchAnalytics/query
```

## Common Reports

### Top Keywords (Last 30 Days)
```json
{
  "startDate": "30daysAgo",
  "endDate": "today",
  "dimensions": ["query"],
  "rowLimit": 50
}
```

### Top Pages
```json
{
  "startDate": "30daysAgo",
  "endDate": "today",
  "dimensions": ["page"],
  "rowLimit": 25
}
```

### Keywords by Page (Specific URL)
```json
{
  "startDate": "30daysAgo",
  "endDate": "today",
  "dimensions": ["query"],
  "dimensionFilterGroups": [{
    "filters": [{
      "dimension": "page",
      "operator": "contains",
      "expression": "/pricing/"
    }]
  }],
  "rowLimit": 25
}
```

### Country Breakdown
```json
{
  "startDate": "30daysAgo",
  "endDate": "today",
  "dimensions": ["country"],
  "rowLimit": 20
}
```

### Device Breakdown
```json
{
  "startDate": "30daysAgo",
  "endDate": "today",
  "dimensions": ["device"],
  "rowLimit": 5
}
```

### Daily Trend
```json
{
  "startDate": "30daysAgo",
  "endDate": "today",
  "dimensions": ["date"],
  "rowLimit": 30
}
```

### Query + Page Combo (Where Does Each Query Land)
```json
{
  "startDate": "30daysAgo",
  "endDate": "today",
  "dimensions": ["query", "page"],
  "rowLimit": 50
}
```

### Search Appearance (Rich Results, etc.)
```json
{
  "startDate": "30daysAgo",
  "endDate": "today",
  "dimensions": ["searchAppearance"],
  "rowLimit": 10
}
```

### Branded vs Non-Branded
Run two queries:
1. Branded: filter `query contains "oviond"`
2. Non-branded: filter `query notContains "oviond"`

```json
{
  "startDate": "30daysAgo",
  "endDate": "today",
  "dimensions": ["query"],
  "dimensionFilterGroups": [{
    "filters": [{
      "dimension": "query",
      "operator": "notContains",
      "expression": "oviond"
    }]
  }],
  "rowLimit": 25
}
```

### Position Bucket Analysis
Query all keywords, then programmatically bucket by position:
- Position 1-3: Top of page
- Position 4-10: Page 1
- Position 11-20: Page 2 (low-hanging fruit!)
- Position 21+: Deep

## Current SEO Snapshot (as of 2026-03-09)

**Top Brand Queries:**
- "oviond" — 596 clicks, pos 1.8, 62.9% CTR
- "oviond login" — 16 clicks, pos 1.0, 94.1% CTR
- "oviond pricing" — 11 clicks, pos 1.0, 68.8% CTR

**Top Non-Brand Queries:**
- "digital marketing report" — 8 clicks, 1,707 impr, pos 7.6 (page 1!)
- "pros and cons of influencer marketing" — 8 clicks, 155 impr, pos 1.9
- "ai tools for digital marketing free" — 6 clicks, 56 impr, pos 4.2

**Top Content Pages:**
- Homepage — 730 clicks, 28.7K impressions
- Influencer marketing pros/cons — 97 clicks, 12.7K impressions
- Excel marketing dashboard templates — 87 clicks, 13.9K impressions
- Client onboarding checklist — 76 clicks, 40.4K impressions (huge impression volume!)
- Free AI tools for agencies — 50 clicks, 14.4K impressions

**Key Opportunities:**
- "client onboarding checklist" page has 40K impressions but only 76 clicks (pos 18.1) — move to page 1 = massive traffic lift
- "content in social media marketing" — 30K impressions, 36 clicks (pos 12.3) — page 2, close to page 1
- "importance of paid advertising" — 13.7K impressions, 14 clicks (pos 24.4) — needs work but high volume
- "digital marketing reporting" — 13.5K impressions, 24 clicks (pos 14.5) — core topic, should rank top 5

## Response Fields

Each row in the API response contains:
- `keys` — array of dimension values
- `clicks` — number of clicks
- `impressions` — number of impressions
- `ctr` — click-through rate (0-1, multiply by 100 for %)
- `position` — average ranking position

## Date Ranges

- Use `YYYY-MM-DD` format
- Data available up to ~2-3 days ago (Search Console has a delay)
- Max range: 16 months of history

## Output Formatting (Slack)

```
*SEO Overview — oviond.com (Last 30 Days)*

*Top Non-Brand Keywords:*
• "digital marketing report" — 8 clicks, 1,707 impr, pos 7.6 🎯
• "ai tools for digital marketing" — 6 clicks, 56 impr, pos 4.2
• "client onboarding checklist" — 4 clicks, 40K impr, pos 18.1 ⚠️ (huge opportunity)

*Quick Wins (High impressions, position 8-20):*
• /client-onboarding-checklist/ — 40K impr, pos 18 → optimize for page 1
• /content-in-social-media-marketing/ — 30K impr, pos 12 → close to page 1
• /digital-marketing-reporting-explained/ — 13.5K impr, pos 14.5
```
