# Connector and report-automation substitutes

Canonical category research document. Last verified: 2026-05-07.

Source detail also retained at `raw/connector-report-automation.md`.

---

# Connector / report-automation substitutes for Oviond

Last verified: 2026-05-07

Scope: Supermetrics, Funnel.io, Porter Metrics, Dataslayer, Coupler.io, Windsor.ai, Improvado, plus Adverity as an obvious enterprise connector-layer competitor.

Strategic frame: these vendors are not classic agency-reporting platforms. They substitute for Oviond when an agency decides to assemble reporting infrastructure from connectors + Looker Studio / Sheets / Power BI / warehouse + templates / AI. The competitive pressure is strongest where they promise breadth, data freshness, and “bring your own BI.” The exploitable gap is that agencies still own the reporting system design, client delivery layer, QA, white-label experience, and ongoing dashboard maintenance.

---

## Snapshot comparison

| Vendor | Core wedge | Pricing/scaling metric | Connector breadth | Destinations | Agency/client-reporting relevance | AI/API posture |
|---|---|---:|---:|---|---|---|
| Supermetrics | Marketing intelligence/data movement into BI, spreadsheets, warehouses, AI | Package + destination + data sources + accounts/users; extras available | Large marketing connector catalog; premium/early-access connectors visible | Looker Studio, Sheets, Excel, Power BI; Enterprise adds Snowflake/BigQuery and more | Strong DIY agency stack; not white-label client portal-first | Data API/MCP in packages; Management API only Enterprise |
| Funnel.io | Marketing data hub for modeling, reporting, exporting | Plan tiers by connectors, reporting solutions, export solutions | 121 Starter / 579 Business / 590 Enterprise connectors | Funnel dashboards, reporting solutions, export destinations | Strong for data teams/agencies with budget; overkill for simple client reporting | Funnel AI positioning; measurement add-on; custom integrations on higher plans |
| Porter Metrics | Low-cost marketing connectors for Looker Studio/Sheets/Power BI/BigQuery | Pay per data source account | 26+ / 30+ marketing sources | Looker Studio/Data Studio, Google Sheets, Power BI, BigQuery, Slack, Zapier | Explicitly agency-friendly: multi-account, templates, 1,500+ marketers | AI query builder, alerts, notifications; new MCP signal |
| Dataslayer | Supermetrics alternative for automated reporting | Plan by destination, users, accounts per connector, enterprise rows | 50+ sources listed | Sheets, Looker Studio, BigQuery, API Query Manager, Power BI, S3, Redshift, Excel, Snowflake, DBs, GCS | Good DIY stack; less native agency reporting/white-label emphasis | AI Chat, Alerts Agent, Looker Analyzer, MCP, GPT |
| Coupler.io | Broad no-code data integration + dashboards | Accounts, destinations, users, rows/run, refresh, AI quota | 400+ data sources | Looker Studio, Sheets, BigQuery, Power BI, Excel, Snowflake, Postgres, Redshift, JSON, Tableau, Qlik, monday, CSV | Pro adds team & client workspaces; agency/enterprise custom | AI data analysis, AI Agent/Insights quotas, integrations with Claude/ChatGPT/OpenClaw/Cursor/etc. |
| Windsor.ai | No-code ELT/BI/AI connectors with all sources/destinations included | Data sources, accounts, destination tasks, MAR rows, refresh | 325+ sources | BI, spreadsheets, warehouses, DBs, file storage, Python, Windsor MCP | Explicit agencies tab; auto-add accounts on Professional | Windsor MCP for ChatGPT/Claude/Copilot/etc.; API rate limits published |
| Improvado | Enterprise marketing data pipeline + governance + AI analytics | Custom quote; unique rows/year, sync frequency, credits, recipes, add-ons | 500+ supported sources | 18+ destinations; hosted/managed/owned storage; direct push | Enterprise agency solution; experts/custom dashboards; not SMB self-serve | AI Agent add-on; Management API; governance/monitoring add-ons |
| Adverity | Enterprise-grade marketing data foundation + intelligence | Fully customized quote | Very broad marketing connector library | BI, warehouse, DB, file/datalake destinations | Enterprise/agencies; data quality/governance more than client portal | AI built-in / Adverity Intelligence; no transparent self-serve API pricing found |

---

## 1. Supermetrics

Sources: pricing, connectors, API/product pages.

- https://supermetrics.com/pricing
- https://supermetrics.com/connectors
- https://supermetrics.com/products/supermetrics-api
- https://supermetrics.com/blog/ai-ready-marketing-data

### Positioning
Supermetrics positions as a leading “Marketing Intelligence Platform” and a simple way to gather granular data from marketing sources into reporting, BI, warehouse, and AI workflows. Its API page says users can “pull live data from all your marketing platforms into your own tools, dashboards, and AI workflows — through a single, consistent API.”

### Pricing / scaling metric
Pricing is package-led with multiple gates:

- Starter: from €39/mo yearly / €49 monthly; 1 core destination, 3 data sources, 1 user, 3 accounts per data source, weekly Google Sheets refresh.
- Growth: from €159/mo yearly / €199 monthly; 1 core destination, 7 data sources, 2 users, 7 accounts per data source, daily Sheets refresh, one custom data import config.
- Pro: from €399/mo yearly / €499 monthly; 1 core destination, 10 data sources, 3 users, 10 accounts per data source, hourly Sheets refresh, Storage Basic add-on.
- Enterprise: custom; choose core and DWH destinations, all data sources, custom user/account limits, on-demand refreshes, warehousing/storage, Management API, multiple teams, residency controls, premium support.

Important gates: destinations, selected data sources, accounts per source, users, refresh frequency, data warehousing, Management API, custom import, teams, support.

### Source/connectors limits
The connectors page lists a large catalog across SEO, paid media, social, app analytics, web analytics, ecommerce, email/SMS, sales, affiliate, retail media, reviews, and other categories. It marks some connectors as “Premium” or “Early access,” reinforcing that connector access can be gated by package/extra.

### Destination support
Core destination choices surfaced on pricing include ChatGPT/Claude/Microsoft Copilot, Looker Studio, Google Sheets, Excel, Power BI. Enterprise adds DWH destinations such as Snowflake and BigQuery. Pricing also references Data API & MCP access.

### Agency templates / white-label / client reporting relevance
Supermetrics is highly relevant to agencies already comfortable with Looker Studio/Sheets/Power BI. It supplies the data layer and some dashboards/templates, but it is not primarily a client-reporting portal or white-label agency reporting platform. Agencies still need to design templates, handle client access, manage report QA, and maintain BI assets.

### API posture
Strong. “Data API access” appears across packages, while “Management API access” is Enterprise. Supermetrics API is explicitly positioned for custom applications and AI workflows.

### AI / automation posture
Strong and current. Pricing includes AI destinations (ChatGPT, Claude, Copilot) and “Data API & MCP access.” Its AI-ready marketing-data content frames Supermetrics as the foundation for trusted AI outputs through centralization, freshness, governance, and quality checks.

### Strengths
- Category awareness and trust; claims 200,000+ companies.
- Deep marketing connector breadth.
- Familiar destinations for marketers and analysts.
- Strong API/MCP/AI story.
- Enterprise controls for governance, storage, data residency, support.

### Weaknesses / exploitable gaps
- Pricing is multi-dimensional and potentially confusing: package + destination + data sources + accounts + users + extras.
- Starter/Growth/Pro include only one core destination by default.
- Agencies still need to operate the reporting layer in external tools.
- White-label/client-portal experience is not the center of the product.

### DIY-workflow implications
Supermetrics is a powerful “build your own stack” choice. It lowers connector pain but leaves agencies with dashboard architecture, branding, client permissions, insight narration, and maintenance burden.

### Oviond counter-position
“Supermetrics is great if your agency wants to build and maintain a BI stack. Oviond is for agencies that want client reporting infrastructure already packaged: client-count pricing, core features included, white label and custom domains without plan archaeology, and reporting that feels done rather than assembled.”

---

## 2. Funnel.io

Sources: pricing, connectors, templates.

- https://funnel.io/pricing
- https://funnel.io/all-data-sources
- https://funnel.io/templates

### Positioning
Funnel positions as a marketing data hub: connect and model all marketing data, send it to dashboards/exports/warehouses, and support reporting, measurement, and activation. Pricing copy says it serves “companies of all sorts and sizes, from tech startup to global media agency.”

### Pricing / scaling metric
The pricing page shows three tiers:

- Starter: starts from €180/mo billed annually; 121 connectors; Funnel dashboards and 3 reporting solutions; no export destinations; measurement unavailable.
- Business: starts from €720/mo billed annually; 579 connectors; advanced Data Hub capabilities; custom integrations; Measurement as add-on; Funnel dashboards and 6 reporting solutions; 26 export solutions.
- Enterprise: custom; 590 connectors; enterprise governance/compliance; custom integrations; Measurement add-on; 6 reporting solutions; 27 export solutions.

Important gates: connector count, advanced data hub, custom integrations, export destinations, measurement add-on, governance/compliance.

### Source/connectors limits
Funnel claims an industry-leading connector library and says custom connectors are available for Business and Enterprise customers. Its FAQ distinguishes core connectors from custom connectors and says custom connector requests are picked up within two working days and usually take two to eight weeks depending on complexity.

### Destination support
Business/Enterprise include export destinations; Starter does not. The pricing page lists “reporting solutions” and “export solutions”; embedded destination data includes Looker Studio/Data Studio and Postgres among BI/export options.

### Agency templates / white-label / client reporting relevance
Funnel is relevant to larger agencies that want a central data hub and can justify platform/data-ops spend. It offers dashboard templates such as a GA4 dashboard template. It is less obviously a white-label client reporting portal and more a data/modeling/reporting operations layer.

### API posture
Custom integrations and export destinations are gated to higher plans. Public pricing does not present a simple self-serve API-first package in the same way Supermetrics/Windsor do.

### AI / automation posture
Funnel has Funnel AI navigation/product positioning and a broader marketing intelligence narrative. Measurement is an add-on. Automation strength is in data hub modeling, exports, and recurring reporting workflows.

### Strengths
- Mature marketing data hub with modeling and export focus.
- Strong connector breadth at Business/Enterprise.
- Better suited for centralized teams than one-off dashboards.
- Custom connector process and partner ecosystem.

### Weaknesses / exploitable gaps
- Starting price is high for smaller agencies.
- Starter excludes export destinations and measurement.
- Business plan jump is significant.
- Complex data-hub language can feel heavyweight compared with “client reports done.”

### DIY-workflow implications
Funnel is a serious DIY reporting-infrastructure path: strong for teams that want to own their data model, but it makes reporting feel like an analytics/data-ops program rather than a simple agency deliverable.

### Oviond counter-position
“Funnel is powerful when reporting is a data-platform project. Oviond should win agencies that want less platform ceremony: onboard clients, connect data, brand the experience, automate delivery, and keep pricing easy to understand.”

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

## 4. Dataslayer

Sources: pricing, connectors, destinations, AI.

- https://www.dataslayer.ai/pricing
- https://www.dataslayer.ai/connectors-dataslayer
- https://www.dataslayer.ai/destinations
- https://www.dataslayer.ai/ai-insights

### Positioning
Dataslayer calls itself “the smartest alternative for automated reporting” with all marketing metrics in one place and transparent pricing. It is a direct Supermetrics-style substitute for marketers who want connector automation into common reporting destinations.

### Pricing / scaling metric
Public pricing extraction was noisy, but the page clearly structures plans around destination, users, accounts per connector, scheduling, and enterprise-destination row volume:

- Starter: select 1 core destination or 1 enterprise destination; 1 user; 3 accounts per connector; daily schedule; unlimited rows in core destinations; 5K monthly rows in enterprise destinations.
- Advanced: 10 users; 50 accounts per connector; hourly schedule; 100K enterprise rows.
- Pro: unlimited users; 100 accounts per connector; hourly schedule/custom hours; dedicated account manager; 2M enterprise rows.
- Custom: custom connectors, users, accounts, rows.
- Free: 1 connector, 1 user, 1 account, manual daily refresh.

The page showed “20€/monthly billed annually” repeated across paid tiers, likely a rendering/extraction issue; treat exact tier prices as requiring manual verification before publication.

### Source/connectors limits
Connector page lists 50+ marketing and analytics sources, including GA4, Google Ads, Facebook/Instagram, Snapchat, Bing, Criteo, DV360, Search Console, YouTube, LinkedIn, TikTok, Stripe, WooCommerce, Shopify, Pinterest, Amazon Ads, Klaviyo, HubSpot, Reddit Ads, AppsFlyer, databases, CSV/XML/JSON, and roadmap items.

### Destination support
Destination page includes Google Sheets, Data Studio/Looker Studio, BigQuery, API Query Manager, Power BI, Amazon S3, Redshift, Morpheus MMM, Excel, Snowflake, databases (MySQL/PostgreSQL/MSSQL/Oracle/MariaDB), and Google Cloud Storage.

### Agency templates / white-label / client reporting relevance
Dataslayer is relevant for agencies using Looker Studio/Sheets/Power BI, with Pro explicitly “best for agencies and advanced marketing.” It does not appear to center native white-label client portals or custom domains.

### API posture
API Query Manager is a named destination; MCP is also explicitly promoted. The API posture is useful for pushing data into tools, but pricing is more destination/row/account based than platform API-management led.

### AI / automation posture
Very strong AI messaging:

- Dataslayer AI Chat with pre-configured MCP and direct access to marketing data.
- Alerts Agent for 24/7 KPI monitoring/anomaly detection.
- AI Looker Studio Analyzer Chrome extension.
- Dataslayer MCP for ChatGPT, Claude, Mistral, and others.
- Dataslayer GPT in the ChatGPT marketplace.

### Strengths
- Clear Supermetrics alternative positioning.
- Strong destination range for both BI and data warehouses.
- Aggressive AI/MCP posture.
- Agency/pro plan framing.

### Weaknesses / exploitable gaps
- Pricing extraction/page presentation is confusing enough to require caution.
- Connector breadth narrower than Coupler/Windsor/Improvado/Adverity.
- The reporting output still depends on external BI/spreadsheet destinations.
- White-label/client delivery not central.

### DIY-workflow implications
Dataslayer is a modern DIY connector+AI layer. It gives agencies more data/AI capability but does not remove the need to construct and maintain the actual reporting experience.

### Oviond counter-position
“Dataslayer leans into AI data access. Oviond should not fight that head-on; position API/MCP as background infrastructure while making the main promise client-reporting clarity: the agency gets branded reports and dependable delivery without becoming a BI/AI workflow integrator.”

---

## 5. Coupler.io

Sources: pricing.

- https://www.coupler.io/pricing
- https://www.coupler.io/sources
- https://www.coupler.io/destinations

### Positioning
Coupler.io positions as a no-code data integration and automation platform with broad sources, dashboards, transformations, and AI data analysis. It is broader than marketing-only reporting, but marketing connectors and dashboard templates make it a real substitute.

### Pricing / scaling metric
Pricing is highly explicit and multi-dimensional:

- Free: $0; 1 account, 1 user, 1 data source, 1 destination, manual refresh, 100 rows/run.
- Starter: $24/mo annually or $32 monthly; 3 accounts, 1 destination, daily refresh, 1 user, 5,000 rows/run, dashboard templates, AI data analysis.
- Active: $99/mo annually or $132 monthly; 15 accounts, 3 destinations, daily refresh, unlimited users/data volume, transformations, advanced dashboards, AI data analysis.
- Pro: $199/mo annually or $259 monthly; 50 accounts, unlimited destinations, hourly refresh, team & client workspaces, automations, account manager.
- Agency & Enterprise: custom; custom accounts/destinations, 15-minute refresh, custom sources/dashboards, priority support, SLA, onboarding.

Important gates: accounts, destinations, refresh frequency, users, rows/run/data volume, workspaces, automations, support/SLA, AI quota.

### Source/connectors limits
The pricing page says 400+ data sources and lists a very broad catalog across ads, analytics, ecommerce, CRM, finance, support, productivity, databases, files, and APIs.

### Destination support
Pricing lists Looker Studio, Google Sheets, BigQuery, Power BI, Excel, Snowflake, PostgreSQL, Redshift, JSON, Tableau, Qlik, monday.com, and CSV.

### Agency templates / white-label / client reporting relevance
Coupler has dashboard templates and “team & client workspaces” from Pro upward. This makes it more agency-relevant than generic ETL tools, but still not a dedicated white-label reporting platform. Custom dashboards and agency features are strongest on Pro/custom tiers.

### API posture
Coupler supports JSON among destinations and lists webhooks under transformations/extras in the pricing comparison. Public pricing does not foreground a management API; it is more no-code integration than API platform.

### AI / automation posture
Pricing includes AI data analysis across paid plans and lists AI integrations with Claude, ChatGPT, OpenClaw, Cursor, Perplexity, and Gemini. AI Agent and AI Insights are quota-gated by plan.

### Strengths
- Very broad connector catalog.
- Transparent pricing and free plan.
- Strong destination breadth.
- Team/client workspaces and automations on Pro.
- AI quotas visible.

### Weaknesses / exploitable gaps
- Broadness can dilute agency-reporting specificity.
- Starter is constrained by 1 user, 1 destination, 5,000 rows/run.
- Client workspaces are not available until Pro.
- Agencies must still manage report design and client presentation in external tools/custom dashboards.

### DIY-workflow implications
Coupler is a good “cheap-to-start, broad-to-scale” DIY option. It can become a maze of accounts/destinations/row limits/workspaces as agencies scale.

### Oviond counter-position
“Coupler is compelling for teams that want a general data automation tool. Oviond should win where the buyer’s job is agency reporting, not data plumbing: fewer knobs, clearer client-count pricing, and the reporting layer included.”

---

## 6. Windsor.ai

Sources: pricing, homepage/data-source positioning.

- https://windsor.ai/pricing/
- https://windsor.ai/
- https://windsor.ai/data-field/all/
- https://windsor.ai/destinations/windsor-mcp-for-ai-insights/

### Positioning
Windsor.ai positions as a no-code data integration platform for BI, databases, and AI tools: “Connect any data source. Analyze it anywhere. Get insights with AI.” It claims 325+ business platforms, BI/spreadsheet/warehouse/AI destinations, and no-code sync in 1 minute.

### Pricing / scaling metric
Pricing scales by selected data sources, accounts, destination tasks, refresh frequency, and monthly active rows (MAR) for warehouse/database destinations:

- Free trial/Forever Free: 30-day trial; then free plan with 1 user, 1 data source, 1 account. Trial includes 10 data sources, 15 accounts, 5 destination tasks, 30-day history limit.
- Basic: $19/mo annually / $23 monthly; unlimited users, 3 data sources, 75 accounts, 5 destination tasks, daily sync, 5M MAR included.
- Standard: $99/mo annually / $118 monthly; unlimited users, 7 sources, 75 accounts, unlimited destination tasks, daily/hourly sync, 7.5M MAR.
- Plus: $249/mo annually / $299 monthly; 10 sources, 200 accounts, 10M MAR.
- Professional: $499/mo annually / $598 monthly; 14 sources, 500 accounts, auto-add all accounts, 15-min sync, 50M MAR.
- Enterprise: up to 200 sources, up to 50,000 accounts, invoice, dedicated manager, custom connector development, onboarding, SSO.

Important gates: data-source count, account count, destination task count, refresh interval, MAR volume, auto-add accounts, custom connector, SSO/invoicing.

### Source/connectors limits
Windsor says all plans include access to all data sources/destinations, but each plan limits the number of data sources selected and accounts. It claims 325+ sources.

### Destination support
Pricing FAQ lists Power BI, Looker Studio, Google Sheets, Excel, BigQuery, Snowflake, Tableau, PostgreSQL, MySQL, Python, Amazon S3, Azure Blob, Azure SQL, Redshift, Databricks, Microsoft Fabric, and Windsor MCP server. Insert destinations have MAR limits.

### Agency templates / white-label / client reporting relevance
Windsor explicitly speaks to agencies: automate cross-platform client dashboards, manage hundreds of accounts from a single workspace, unlimited users and data blending on every plan, onboard clients quickly, scale to more clients without technical headcount. Professional’s “auto-add all accounts” is specifically described as designed for agencies. No strong native white-label portal/custom-domain story found in fetched sources.

### API posture
Pricing FAQ publishes API rate limits: 600 requests/minute and 10,000 requests/day. External authentication links allow clients/teammates to connect data without sharing credentials. Custom connector development is Enterprise/immediate or feature request queue.

### AI / automation posture
Strong. Windsor MCP connects data to ChatGPT, Claude, Copilot, Gemini, Perplexity, Cursor, Manus, and other LLMs. All plans include access to Windsor MCP for AI analysis. Homepage strongly frames AI insights and scheduled automation.

### Strengths
- All connectors/destinations included conceptually; plan limits are source/account/task based.
- Transparent pricing and useful free/trial plan.
- Explicit agency messaging.
- Strong AI/MCP posture.
- Broad destination set and warehouse support.

### Weaknesses / exploitable gaps
- Plan math is still complex: sources + accounts + tasks + MAR + refresh.
- Basic/Standard cap source count even with 325+ available.
- MAR billing for warehouse/database destinations can surprise non-technical agencies.
- Client-facing reporting/white-label layer remains external.

### DIY-workflow implications
Windsor is one of the strongest substitutes because it combines breadth, transparent pricing, agency language, and MCP. But it still frames success around connecting data “anywhere,” not delivering agency-branded reporting as a managed client experience.

### Oviond counter-position
“Windsor is a credible data-infrastructure substitute. Oviond should contrast on operational simplicity: no MAR math, no source/task planning, no external BI assembly — just agency reporting infrastructure with core features included.”

---

## 7. Improvado

Sources: pricing, agencies page.

- https://improvado.io/pricing
- https://improvado.io/solutions/agencies

### Positioning
Improvado is an enterprise marketing data platform for extraction/loading, transformation, governance, reporting, and AI. It is built for larger companies and agencies with complex data needs, not SMB self-serve reporting.

### Pricing / scaling metric
Pricing is fully tailored / demo-led with plan names Growth, Advanced, Enterprise. Public comparison exposes the scaling levers:

- Unique rows/year: up to 200M, 600M, or 1B.
- Sync frequency: up to twice daily, four times daily, or custom depending on tier.
- Unlimited data sources/accounts and 500+ pre-built sources across tiers.
- Custom sources/destinations use credits.
- Initial historical data: 2 years or max depending on tier.
- Direct push can be add-on/gated.
- Concurrent data destinations: 2 or unlimited depending on tier.
- Customization credits: 240/480/960.
- Recipes/dashboards, governance, AI Agent, custom dashboards, premium support, and 24/7 support are gated/add-on in multiple places.

### Source/connectors limits
500+ supported sources; custom source connectors available with credits. Agency page says “missing something? We’ll build a connector for it.”

### Destination support
18+ pre-built destinations, custom destinations with credits, flexible storage options (hosted, managed, owned), direct push to destinations, data warehouses including Snowflake/Google BigQuery/MS SQL/Databricks for ELT/AI perimeter use.

### Agency templates / white-label / client reporting relevance
Agency page highlights 500+ integrated platforms, 15+ ready-made data recipes, and report prep via prompts. Improvado is highly agency-relevant for enterprise agencies, especially where data modeling/governance/custom dashboards matter. It is not positioned as a simple white-label client portal for smaller agencies.

### API posture
Strong enterprise API posture: Improvado Management API lets customers manage an instance without logging into the UI, including source/account connections, automations, and product integration.

### AI / automation posture
AI Agent is an add-on positioned as an autonomous marketing analytics teammate that can automate up to 99.5% of analytics routines/reporting and save 30 hours/week. Governance modules include KPI health, naming conventions, budget pacing, brand safety, and alerts. Agency page promotes prompt-based charts/dashboards/docs/code.

### Strengths
- Enterprise-grade breadth, governance, security, support.
- Strong custom connector/destination story.
- AI and data governance much deeper than SMB tools.
- Good for complex agency/brand data operations.

### Weaknesses / exploitable gaps
- No transparent pricing; sales-led.
- Add-on/credit model is complex.
- Heavy enterprise posture may intimidate smaller/mid-market agencies.
- Reporting delivery likely requires implementation/pro services and external BI choices.

### DIY-workflow implications
Improvado is the “enterprise build it properly” substitute. It helps agencies professionalize data ops, but reporting becomes a data program with contracts, credits, add-ons, and implementation scope.

### Oviond counter-position
“Improvado is for enterprise-grade marketing data operations. Oviond should not chase that complexity; it should own the mid-market agency need: polished reporting infrastructure, clear pricing, fast implementation, and enough API/MCP depth without enterprise procurement drag.”

---

## 8. Adverity (obvious additional competitor)

Sources: pricing, connectors, destinations, AI/intelligence pages.

- https://www.adverity.com/pricing
- https://www.adverity.com/data-connectors
- https://www.adverity.com/data-destinations
- https://www.adverity.com/adverity-intelligence/analyze

### Positioning
Adverity positions as an enterprise-grade marketing data foundation and intelligence platform. Navigation separates Adverity Data (connect/orchestrate/manage) from Adverity Intelligence (analyze/collaborate/activate). It emphasizes accurate, consistent data at scale and AI-powered marketing insights.

### Pricing / scaling metric
Pricing is fully custom. The pricing page says Adverity does not stick to rigid pricing plans and instead provides a customized quote tailored to each client.

### Source/connectors limits
Adverity’s connector page lists a very large marketing connector library across search, CRM, SEO, DSP/SSP, ad servers, analytics, ecommerce/retail, databases, files/datalakes, social, affiliate, call analytics, and more. It credibly competes on enterprise connector breadth.

### Destination support
Destination page includes business intelligence, CRM, database, DMP, file/datalake, social advertising, and web analytics categories. Visible destinations include Google BigQuery, Google Sheets, Looker Studio, Microsoft Excel, Microsoft Fabric, OneDrive, databases/warehouses, and other BI/file outputs.

### Agency templates / white-label / client reporting relevance
Adverity has agency and enterprise solution navigation and agency case-study relevance. It is better understood as enterprise data infrastructure and intelligence for agencies/brands, not a lightweight white-label client reporting product.

### API posture
Public fetched pages did not expose clear self-serve API pricing. Product navigation and data-platform positioning imply integration depth, but public posture is sales-led/enterprise rather than transparent API package.

### AI / automation posture
Adverity has “AI Built-In” and Adverity Intelligence. The Analyze page title/source content positions “AI-Powered Marketing Insights and Data Analysis.” Intelligence modules include analyze, collaborate, and activate.

### Strengths
- Enterprise credibility and breadth.
- Strong data quality/governance posture.
- Large connector/destination catalog.
- AI/intelligence narrative beyond simple connectors.

### Weaknesses / exploitable gaps
- Fully custom pricing increases friction.
- Enterprise language and implementation heft may be overkill for agencies wanting fast reporting.
- Not a simple agency-client reporting platform.

### DIY-workflow implications
Adverity is less DIY for SMB agencies and more “enterprise data platform as substitute.” It can displace agency reporting platforms when the client/agency wants centralized governed marketing data, but at the cost of complexity and procurement.

### Oviond counter-position
“Adverity is for enterprise marketing data maturity. Oviond should be the clear agency reporting layer: faster to buy, easier to explain, and purpose-built for client-facing reporting rather than enterprise data governance.”

---

## Cross-market patterns

### Pricing patterns that create Oviond opportunity

- Connector tools rarely price by the agency mental model of “clients.” They price by sources, accounts, destinations, users, rows, refreshes, tasks, credits, MAR, or custom quotes.
- Many “all connectors/destinations included” claims still have secondary limits: data-source count, account count, destination tasks, row volume, refresh, support, SSO, custom connectors.
- AI/MCP is becoming table stakes in the connector layer. Oviond should not over-index launch messaging on MCP alone; make it a confidence feature behind the main simplicity promise.

### Feature gates to watch

- White label/custom domains are usually not central in this category.
- Client workspaces appear in Coupler Pro and agency-oriented messaging in Windsor, but not as the core experience.
- API/Management API is often Enterprise or buried.
- Refresh frequency is a common upsell: daily → hourly → 15-min/on-demand.
- Destination breadth is a common upsell: single destination or no exports on low tiers.
- Connector breadth may be gated by core/custom/premium/early access categories.

### Strength of DIY substitute by agency segment

- Small Looker Studio agencies: Porter, Dataslayer, Coupler Starter/Active, Windsor Basic/Standard.
- Scaling performance agencies: Supermetrics Growth/Pro, Windsor Plus/Professional, Coupler Pro, Funnel Starter/Business.
- Enterprise agencies/data teams: Funnel Business/Enterprise, Improvado, Adverity, Supermetrics Enterprise.

---

## Implications for Oviond

1. **Lead with “agency reporting infrastructure,” not “connector breadth.”** Connector vendors will almost always win raw breadth. Oviond wins if the buyer wants a finished client-reporting operation.

2. **Make pricing contrast painfully clear.** The market is full of source/account/destination/user/row/task/MAR/credit logic. Oviond’s client-count slider and included core features are a real positioning asset.

3. **Treat API/MCP as power under the hood.** Competitors are rapidly adding AI chats, MCP, GPTs, and agents. Oviond should show it is modern without making agencies feel they need to design AI workflows to get value.

4. **Exploit the white-label gap.** Most connector tools feed Looker Studio, Sheets, Power BI, and warehouses. They do not naturally solve branded client portals, custom domains, agency templates, client access, report delivery, and stakeholder-ready presentation.

5. **Position against “BI assembly fatigue.”** The strongest copy angle is not “we have more integrations.” It is: “Stop stitching together connectors, dashboards, permissions, templates, and client delivery. Oviond gives agencies the reporting layer already assembled.”

6. **Use positive competitive language.** Public messaging should acknowledge DIY stacks as valid for data teams, then frame Oviond as the better fit when reporting is an agency deliverable that must be repeatable, branded, and low-maintenance.

7. **Product proof points to emphasize:** all core features included, white label/custom domains, agency templates, client management, automated report delivery, simple scaling by clients, dependable data connections, and API/MCP availability for advanced users.
