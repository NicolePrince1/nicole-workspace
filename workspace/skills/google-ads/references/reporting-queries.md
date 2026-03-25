# Reporting queries for Oviond Google Ads

Use these GAQL queries with `ads_query.js` after auth is healthy.

## Quick account summary

```sql
SELECT
  customer.id,
  customer.descriptive_name,
  customer.currency_code,
  customer.time_zone
FROM customer
LIMIT 1
```

## Campaign performance — last 30 days

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion,
  metrics.ctr,
  metrics.average_cpc
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
```

## Budget pacing — today

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  metrics.cost_micros,
  metrics.clicks,
  metrics.conversions
FROM campaign
WHERE segments.date DURING TODAY
  AND campaign.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
```

## Search terms — last 30 days

```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 200
```

## Wasted spend keywords — last 90 days

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.criterion_id,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM keyword_view
WHERE segments.date DURING LAST_90_DAYS
  AND metrics.cost_micros > 5000000
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

## Winning keywords — last 30 days

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.criterion_id,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.search_impression_share
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.conversions > 0
ORDER BY metrics.conversions_value DESC
LIMIT 200
```

## Device split — last 30 days

```sql
SELECT
  segments.device,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion,
  metrics.conversions_value
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

## Geo split — last 30 days

```sql
SELECT
  geographic_view.country_criterion_id,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM geographic_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

## Conversion tracking health

```sql
SELECT
  conversion_action.id,
  conversion_action.name,
  conversion_action.type,
  conversion_action.status,
  conversion_action.primary_for_goal,
  conversion_action.category,
  conversion_action.counting_type
FROM conversion_action
ORDER BY conversion_action.name
```

## Disapproved / limited ads

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_ad.ad.id,
  ad_group_ad.ad.type,
  ad_group_ad.status,
  ad_group_ad.policy_summary.approval_status,
  ad_group_ad.policy_summary.review_status
FROM ad_group_ad
WHERE ad_group_ad.status != 'REMOVED'
ORDER BY campaign.name, ad_group.name
LIMIT 200
```

## Helpful command patterns

Inline query:

```bash
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_query.js "SELECT campaign.name, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_7_DAYS"
```

Query from file:

```bash
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_query.js --file ./query.sql
```

Pretty output:

```bash
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_query.js --file ./query.sql --format pretty
```

## Analysis reminders

- `cost_micros / 1_000_000` = account currency units
- do not compare CPAs without checking conversion quality and volume
- use longer windows for sparse campaigns
- verify conversion tracking before making aggressive optimization calls
