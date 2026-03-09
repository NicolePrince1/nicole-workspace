# Google Ads API Basic Access Application — Oviond

## Company Information
- **Company Name:** Oviond (Pty) Ltd
- **Website:** https://oviond.com
- **Manager Account ID:** 638-795-6297

## Use Case Description

We are applying for Basic Access to manage our own Google Ads account (290-615-4258) programmatically via the Google Ads API. This is for **internal use only** — we are not building a tool for third parties.

### What we will use the API for:

1. **Performance Reporting** — Automated retrieval of campaign, ad group, and keyword performance metrics (impressions, clicks, conversions, cost, CPA, ROAS) for internal marketing dashboards and analysis.

2. **Campaign Optimization** — Programmatic bid adjustments, keyword management (pausing underperforming keywords, adding negatives), and budget allocation changes based on performance data.

3. **Audit & Quality Control** — Automated checks for wasted spend (zero-conversion keywords), broken conversion tracking, policy violations, and optimization opportunities.

### Scope of access:
- **Read operations:** Campaign, ad group, keyword, and conversion data via GoogleAdsService.Search (GAQL queries)
- **Write operations:** Campaign/keyword status changes (pause/enable), bid adjustments, budget updates via mutate operations
- **Single account:** We only need to manage our own Oviond account under our own manager account

## Technical Implementation

- **Authentication:** OAuth 2.0 via service account with domain-wide delegation, impersonating an authorized Google Workspace user (nicole@oviond.com)
- **GCP Project:** oviond-workspace-cli (project number: 480335022137)
- **API Version:** v21 (latest)
- **Client:** Direct REST API calls (no SDK)
- **Rate limiting:** We will respect all API rate limits and quotas. Expected volume is very low — tens of queries per day for reporting, occasional mutate operations for optimization.

## OAuth Scopes Required
- `https://www.googleapis.com/auth/adwords`

## Data Handling
- All data is used internally for marketing optimization
- No data is shared with third parties
- No end-user data is collected or stored beyond standard Google Ads metrics
- Credentials are stored securely with encryption at rest

## Contact
- **Primary contact:** info@oviond.com
- **Technical contact:** nicole@oviond.com
