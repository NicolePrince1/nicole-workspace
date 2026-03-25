# Meta metrics for Oviond

## Core commercial metrics

- **Spend** — total ad spend in ZAR.
- **Impressions** — total times the ads were served.
- **Clicks** — all clicks, not just landing-page visits.
- **CTR** — clicks ÷ impressions.
- **CPC** — spend ÷ clicks.
- **CPM** — spend ÷ impressions × 1000.

## Funnel actions that matter most

Meta reports most conversion behavior inside `actions` and `cost_per_action_type` arrays.
Do not assume a top-level column exists for the KPI you care about.

Common action types to inspect:
- `link_click`
- `landing_page_view`
- `omni_landing_page_view`
- `lead`
- `purchase`
- `complete_registration`
- `offsite_conversion.custom.<ID>` for custom conversions

## Oviond reporting discipline

For Oviond, prefer this order of truth:
1. **Primary business KPI** named explicitly for the task
2. **Landing page views** for traffic quality
3. **Link clicks** only as a weaker top-of-funnel proxy

When a user says "CPA", immediately clarify or infer which action is the denominator:
- LPV CPA
- lead CPA
- trial-start CPA
- custom conversion CPA
- purchase CPA

If the account uses custom conversions, first run `meta_report.py action-types ...` to discover the actual action names present in reporting.

## Common traps

- High CTR with weak LPV count usually means weak post-click quality.
- Strong LPV volume with weak downstream conversion often means landing-page or offer friction.
- Mixed objectives inside one analysis window can distort CPA comparisons.
- Platform-level spend splits can look healthy while one placement is dragging efficiency.
- Custom conversion action names are account-specific; do not hardcode guesses.
