# Google Looker / Conversational Analytics / Gemini

Last verified: 2026-05-07
Priority: Watchlist
Category: AI/BI analytics threat
Source category: [AI-native and agentic analytics threats](../categories/ai-native-threats.md)

---

## Threat type 8: Google Looker / Conversational Analytics / Gemini

### Positioning

Looker remains governed BI with semantic modeling. Google is adding Conversational Analytics, measured in data tokens, where an LLM processes questions, context, answers, generated API/SQL queries, and visualizations. Source: https://cloud.google.com/looker/pricing

### Pricing

- Looker platform pricing is sales-led: Standard/Enterprise/Embed editions require contacting sales.
- Standard edition includes one production instance, 10 Standard Users, 2 Developer Users, upgrades, up to 1,000 query-based API calls/month and 1,000 admin API calls/month.
- Enterprise includes up to 100,000 query API calls/month; Embed includes up to 500,000 query API calls/month.
- Conversational Analytics token quotas: Viewer 1M input/20K output monthly; Standard 2M/40K; Developer 4M/80K. Unlimited access through Sept 30, 2026 within fair use; quota enforcement/overage starts Oct 1, 2026. Source: https://cloud.google.com/looker/pricing

### Capabilities

- Governed dashboards/Looks/Explore/LookML/API/scheduling.
- Conversational Analytics can generate natural-language responses, API/SQL queries, and visualizations.

### Data connection model

- Semantic model/data warehouse first. Looker Studio remains the lower-cost adjacent tool, often fed by Sheets/connectors.

### API/MCP/agent posture

- Strong API posture; conversational analytics tokenization shows Google expects natural-language BI to become a normal usage surface.
- Google’s official GA MCP and Google Ads MCP work reinforce the broader Google-agent trend.

### Reporting-output quality

- Strong where LookML/semantic model exists.
- Too much setup for most small agencies unless they already live in Looker.

### What Oviond must defend

- Agencies do not want to buy/model/maintain enterprise BI to answer client marketing questions.

---
