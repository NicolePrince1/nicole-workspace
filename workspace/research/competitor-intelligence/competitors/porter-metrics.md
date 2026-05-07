# Porter Metrics

Last verified: 2026-05-07
Priority: Tier 2
Category: Connector/report automation
Source category: [Connector and report-automation substitutes](../categories/connector-report-automation.md)

---

## 3. Porter Metrics

Sources: pricing, connectors, templates.

- https://portermetrics.com/en/pricing/
- https://portermetrics.com/en/connectors/
- https://portermetrics.com/en/templates/

### Positioning
Porter Metrics positions around no-code marketing reporting automation for Looker Studio, Google Sheets, Power BI, and BigQuery. The connectors page says it connects 26+ marketing platforms in minutes, with data blending, multi-account support, and 30+ data sources.

### Pricing / scaling metric
Porter’s public pricing says “Start free. Pay per data source account.” It defines a data source account as an ad account, property, business profile, store, account, or 10 locations.

- Public calculator showed $12.50/mo billed annually for 1 account.
- All plans include 20+ data sources and templates, data blending/cross-channel reports, unlimited historical data/users/reports, AI Query Builder + alerts/notifications, support.
- Free forever plan after trial limits: 3 data source accounts and 30-day data history.
- Pricing table scales down per-account as accounts rise, with annual billing about 16.6% off.

Important gates: data source accounts and data history on free plan. Porter explicitly avoids per-destination fees in its connector messaging.

### Source/connectors limits
The connectors page says 26 ready-to-use integrations / 30+ data sources across paid media, analytics, social, ecommerce, CRM, and email. It emphasizes automatic mapping of dates/campaigns/metrics and multi-account blending.

### Destination support
Porter says “All destinations included”: Data Studio/Looker Studio, Google Sheets, Power BI, BigQuery, Slack, and Zapier are part of every plan.

### Agency templates / white-label / client reporting relevance
Porter is agency-relevant because of multi-account workflows, Looker Studio/Sheets templates, and low per-account pricing. It names agencies, freelancers, and in-house teams as users and says it is trusted by 1,500+ marketing teams in 60 countries. However, it is still a connector/template layer, not a full white-label client reporting workspace.

### API posture
Porter now signals BigQuery and MCP in pricing/navigation. Public pricing did not surface a full management API posture. Best interpreted as pragmatic connector + destination + AI/MCP rather than full API platform.

### AI / automation posture
AI Query Builder + alerts and notifications are listed as included. Pricing/navigation mentions MCP. Strong “AI in the workflow” for query/alerts, less enterprise-governance heavy.

### Strengths
- Very simple and agency-friendly account-based pricing.
- All destinations included.
- Unlimited users/reports/history on paid plan.
- Good for small agencies/freelancers using Looker Studio/Sheets.

### Weaknesses / exploitable gaps
- Much narrower connector breadth than Supermetrics/Funnel/Coupler/Windsor.
- Client-reporting UX depends on external destinations.
- White-label/custom domain/client portal not central.
- Per-account pricing can still rise with many client accounts, although it discounts at scale.

### DIY-workflow implications
Porter makes the DIY path cheaper and simpler, especially for Looker Studio agencies. But agencies still own dashboard design, client access, white labeling, and operational QA.

### Oviond counter-position
“Porter is a smart connector choice for Looker Studio-heavy agencies. Oviond should position as the agency reporting system, not just the data pipe: branded client reporting, unified delivery, and core agency features without stitching reports across Google tools.”

---
