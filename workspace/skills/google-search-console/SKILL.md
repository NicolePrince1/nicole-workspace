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
• "keyword one" — X clicks, Y impr, pos Z 🎯
• "keyword two" — X clicks, Y impr, pos Z
• "keyword three" — X clicks, Y impr, pos Z ⚠️

*Quick Wins (High impressions, position 8-20):*
• /page-one/ — X impr, pos Y → optimize for page 1
• /page-two/ — X impr, pos Y → close to page 1
• /page-three/ — X impr, pos Y
```
