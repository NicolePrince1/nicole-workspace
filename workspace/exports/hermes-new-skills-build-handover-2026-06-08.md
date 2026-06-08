# Hermes New Skills Build Handover — Oviond / Nicole Rebuild

**Prepared for:** Hermes, new Nicole agent, Chris Irwin  
**Prepared by:** Nicole Prince  
**Date:** 2026-06-08  
**Purpose:** Define the skills Hermes should build fresh for the new Nicole agent, using Hermes best practice, current provider documentation, and Oviond-specific operating needs.  
**Important instruction:** Do **not** blindly copy Nicole’s old skills. Use them only as a historical template for what worked, what we needed, and how Oviond uses each platform. Hermes must research each provider’s current documentation and build clean, durable, well-tested skills from scratch.

---

## 1. Prime directive for Hermes

Hermes should build a fresh skill system for the new Nicole agent.

The old Nicole skills and handover docs explain:

- what platforms Oviond uses,
- how Nicole previously connected,
- what workflows mattered,
- what guardrails existed,
- what business questions Chris asks,
- what mistakes to avoid.

But Hermes must create new skills using:

- Hermes best practice,
- provider-current documentation,
- robust authentication handling,
- clear read/write boundaries,
- typed/structured outputs where possible,
- smoke tests / auth doctors,
- least-privilege API use,
- safe mutation workflows,
- Oviond-specific business context.

Do not build thin wrappers that merely “hit an endpoint.” Build operator skills that help Nicole make good decisions.

---

## 2. Global skill architecture rules

Every provider skill should include:

### 2.1 Skill brief

Each skill must have:

- purpose,
- when to use it,
- when **not** to use it,
- required credentials / env vars,
- provider docs links,
- auth model,
- read operations,
- write operations,
- guardrails,
- smoke tests,
- common failures,
- Oviond-specific operating playbook,
- output standards.

### 2.2 Auth doctor

Every API-backed skill should have an auth doctor command or function that checks:

- credential presence,
- credential shape without printing secrets,
- token/API reachability,
- account/property/container IDs,
- read smoke test,
- write capability only if safe to validate,
- actionable error messages.

Output should be JSON-friendly, e.g.:

```json
{
  "ok": true,
  "credentialPresent": true,
  "accountVisible": true,
  "resourceCount": 3,
  "errors": []
}
```

### 2.3 Read-first, write-carefully

Default stance:

- Read-only unless Chris explicitly asks for a write.
- For risky writes: preview → validate/dry-run → summarize blast radius → ask approval → apply.
- For destructive actions: prefer archive/trash/disable over delete.
- For external communications/publishing/spend: require explicit Chris approval.

### 2.4 Provider docs first

Hermes must visit and use current official docs for each provider before building.

Do not rely only on old Nicole scripts. APIs change.

### 2.5 Railway env vars

Chris said all API keys are in Railway env vars for Hermes.

Hermes should:

- read credentials from Railway/env/secrets according to Hermes runtime best practice,
- never hard-code keys,
- never commit keys,
- never print keys,
- report missing env vars by name only,
- support alternate env var names if existing Railway config uses older naming.

### 2.6 Output format standard

Each skill should provide both:

1. Human-readable summaries for Chris / Nicole.
2. Structured JSON for downstream agent workflows.

Example:

```text
Summary: Stripe MRR is down $X vs prior 7 days; past_due is Y.
Evidence: invoice count, paid amount, date range.
Next: prioritize delinquency rescue for high-value monthly accounts.
```

And JSON:

```json
{
  "status": "attention",
  "metric": "past_due_count",
  "value": 43,
  "threshold": 20
}
```

---

## 3. Oviond context every skill must know

### Business

Oviond is a B2B SaaS reporting platform built mainly for marketing agencies.

Primary ICP:

- small to medium-sized marketing agencies.

Growth goal:

- move from roughly `$28.5k MRR` to `$100k MRR` by Dec 2026.

Core positioning:

> Agency reporting that finally feels simple.

Durable shorthand:

> Invisible, dependable, and done.

### Current strategic constraints

- Retention and activation are as important as acquisition.
- Tracking has historically been polluted.
- GA4 mixes marketing site, app, white-label report domains, and dev traffic.
- Paid media must remain off until the new website/app is live, tracking is verified, and Chris explicitly reauthorizes ads.
- Stripe/app truth beats ad-platform vanity conversions.
- Gleap support signal is growth signal.
- Sequenzy is the lifecycle rebuild path.
- MailerLite and Loops are retired from active lifecycle operations, but may be needed for archive/reference/migration intelligence.
- Sanity + Astro is the marketing site/content future.
- Supabase/Postgres/API/MCP is the product/platform future.

### Canonical business events

Use these as the baseline event dictionary unless live product truth says otherwise:

- `signup_started`
- `email_verified`
- `trial_started`
- `subscription_started`
- `invoice_paid`
- `trial_expired`
- `subscription_cancelled`

Rule:

> Backend/app truth decides whether conversion happened. GTM, GA4, Meta, and Google Ads are downstream observers. Stripe is revenue truth.

---

## 4. Required skills overview

Hermes should build these skills fresh:

1. `dataforseo` — keyword/SERP/competitor research
2. `sequenzy` — lifecycle email and SaaS automation
3. `mailerlite-archive` — retired platform archive/migration reference
4. `gleap` — support, customer signal, help center, roadmap friction
5. `meta` — Meta Ads / Facebook / Instagram analytics and safe operations
6. `google-ads` — Google Ads reporting and safe operations
7. `stripe` — MRR, invoices, trials, churn, delinquency, billing truth
8. `sanity` — CMS/content operating system for new marketing site
9. `google-analytics` — GA4 reporting with host/event caution
10. `google-search-console` — SEO query/page performance
11. `google-tag-manager` — GTM audit and controlled container operations
12. `google-workspace` — Gmail, Drive, Calendar, Docs, Sheets as Nicole
13. `supabase-oviond-api` — product/app/growth intelligence layer
14. `postiz` — social publishing rail
15. `railway` — infrastructure/env/deployment operations
16. `oviond-content-engine` — editorial/content strategy orchestration
17. `oviond-design-director` — creative direction and brand QA
18. `oviond-screenshot-director` — product screenshots/docs/launch visuals
19. `website-seo` — technical/on-page SEO for Sanity/Astro
20. `content-quality-auditor` — publish-readiness / E-E-A-T / quality gate

The first 13 are the highest priority for operational rebuild.

---

# 5. Skill briefs

---

## 5.1 `dataforseo` skill

### Purpose

Use DataForSEO for live SERP, keyword, ranking, competitor, search-volume, and content-gap research.

This skill helps Nicole answer:

- What keywords should Oviond target?
- Which competitor pages rank for agency reporting terms?
- What SERP features / intent patterns exist?
- Which pages should Sanity/Astro content target?
- Which comparison pages are worth building?
- How do Oviond’s rankings and competitors move over time?

### Provider docs Hermes must read

Hermes should read current DataForSEO docs for:

- Authentication
- SERP API
- Keywords Data API
- DataForSEO Labs API
- Rank Tracker API if available/needed
- Appendix/user data endpoint
- Rate limits / task pricing / batching

Likely docs root:

- `https://docs.dataforseo.com/`

### Credential/env

Known local note:

- Preferred env var: `DATA_FOR_SEO`
- Accepted format previously: `login:password` or pre-encoded Basic Auth token

Hermes should detect and support both formats safely.

### Current known state

Nicole had live DataForSEO verified on 2026-05-12 via:

- `/v3/appendix/user_data`
- Google organic live SERP smoke test

### Required operations

Read/reporting:

- auth doctor / account balance check
- live Google organic SERP query
- keyword suggestions
- keyword volume / CPC / competition where available
- competitor domain keyword overlap
- top-ranking page extraction
- SERP feature detection
- country/language-specific query research
- batch keyword research with rate-limit handling

Oviond workflows:

- agency reporting keyword research
- competitor comparison page planning
- reporting templates hub expansion
- page-2-to-page-1 opportunity validation
- content briefs for Sanity
- SEO movement triangulation with GSC

### Guardrails

- Do not burn credits with giant unbounded batches.
- Always estimate or state task volume before big runs.
- Cache repeated SERP results where useful.
- Prefer targeted batches.
- Do not print credentials.

### Output standard

For keyword research:

```json
{
  "query": "agency reporting tool",
  "country": "US",
  "intent": "commercial",
  "serp_competitors": [],
  "recommended_action": "comparison page / product landing page / blog / no action"
}
```

---

## 5.2 `sequenzy` skill

### Purpose

Operate Sequenzy for lifecycle email, subscriber management, SaaS automation, transactional messaging, events, campaign metrics, and retention workflows.

Sequenzy is Oviond’s active lifecycle rebuild path.

### Provider docs Hermes must read

Hermes should read current Sequenzy docs and inspect live API behavior carefully because old Nicole learned that:

- the API has broader reads than docs suggest,
- it needs an explicit `User-Agent`,
- some endpoints/envelopes are inconsistent.

Read docs for:

- auth
- subscribers/contacts
- tags
- attributes/properties
- events
- lists/audiences
- campaigns
- sequences/automations
- templates
- transactional email
- metrics/reporting
- webhooks
- rate limits

### Credential/env

Known env var:

- `SEQUENZY_API_KEY`

### Current known state

- Sequenzy read access worked.
- It is the future lifecycle platform.
- MailerLite and Loops are retired.

### Required operations

Read:

- auth doctor
- list subscribers
- get subscriber profile
- list tags/attributes/events
- list sequences/automations
- list campaigns
- list templates
- metrics: sends, opens, clicks, bounces, unsubscribes
- sequence health checks
- deliverability checks

Writes, with approval/preview:

- create/update subscriber
- add/remove tags
- set attributes
- emit lifecycle events
- draft campaigns
- draft sequences
- activate/pause automations only with approval
- transactional sends only with explicit approval or pre-approved operational trigger

Oviond lifecycle flows to support:

1. Trial started
2. Email verification
3. First login / activation nudge
4. First client/report setup
5. Data-source connection guidance
6. Day 3 check-in
7. Day 7 progress nudge
8. Day 10/13/14/15 trial-expiry urgency
9. Trial rescue / extension path
10. Past-due rescue
11. Churned customer win-back
12. Annual plan conversion
13. Client-limit upgrade
14. Integration failure / report-delivery issue messaging if product data exists

### Guardrails

- Do not blast lists without Chris approval.
- Do not activate automations without approval and QA.
- Do not import dirty old MailerLite/Loops logic blindly.
- Respect unsubscribes and suppression lists.
- Treat deliverability seriously.
- Use Stripe/app truth for billing lifecycle triggers, not guessed statuses.

### Output standard

Lifecycle health report should include:

- active sequences
- drafts
- missing flows
- bounce/open anomalies
- recommended next build
- risk level

---

## 5.3 `mailerlite-archive` skill

### Purpose

MailerLite is retired from active operations, but Hermes should build a limited archive/reference skill if API credentials exist.

This skill is **not** for relaunching MailerLite lifecycle. It is for:

- historical campaign analysis,
- old subscriber/list/group reference,
- migration intelligence,
- learning what worked/failed,
- extracting useful copy/assets/segments.

### Provider docs Hermes must read

Read current MailerLite docs for:

- auth/API version
- subscribers
- groups/segments
- campaigns
- automations
- stats/reports
- exports
- rate limits

Likely docs root:

- `https://developers.mailerlite.com/`

### Credential/env

Hermes should inspect Railway env vars for likely keys:

- `MAILERLITE_API_KEY`
- or legacy naming

Do not assume key exists.

### Required operations

Read-only by default:

- auth doctor
- list groups/segments
- list subscribers / counts
- list campaigns and metrics
- list automations if API supports
- export campaign copy/subject lines
- identify old trial/reactivation/upgrade flows

Potential writes:

- none by default.

### Oviond context

Old lifecycle references included:

- trial onboarding sequence
- reactivation/scrub automations
- annual upgrade / client-limit groups that were empty or historical

But the durable decision is:

> MailerLite and Loops are retired. Sequenzy is the rebuild path.

### Guardrails

- Do not send from MailerLite.
- Do not reactivate MailerLite automations.
- Do not sync stale lists into Sequenzy without cleaning and Chris approval.
- Respect unsubscribes/suppression.

---

## 5.4 `gleap` skill

### Purpose

Operate Gleap for support signal, tickets/conversations, tracker tickets, help center content, sessions, customer friction, and retention/product insight.

Gleap is not just a support inbox. For Oviond it is a growth intelligence source.

### Provider docs Hermes must read

Read current Gleap docs for:

- API auth
- conversations/messages
- tickets
- tracker tickets / roadmap
- users/companies
- help center articles/collections
- sessions/events if available
- metrics/reporting
- webhooks
- rate limits

Likely docs root:

- `https://docs.gleap.io/`

### Credential/env

Hermes should inspect Railway env vars for Gleap keys. Do not print.

Likely old skill used local helper paths but new build should use Hermes secret handling.

### Current known state

- Gleap access was operational.
- Tracker-ticket endpoint was empty in April validation; verify live.
- Support looked Michelle-dependent historically.
- Gleap has noisy inbound email; filter vendor/newsletter/internal QA noise.

### Required operations

Read:

- auth doctor
- list conversations/tickets
- fetch full conversation
- search conversations by terms
- list users/companies if available
- list tracker tickets/roadmap items
- list help center collections/articles
- support metrics: volume, response, status, tags
- recent sentiment sweep

Writes, with approval:

- draft help center articles
- update help center content
- add tags/internal notes
- create tracker ticket
- reply to customer only with explicit approval unless a workflow is pre-approved

Oviond workflows:

- identify top activation blockers
- identify connector/data trust issues
- identify report delivery pain
- identify API/MCP questions
- collect customer language for positioning
- prioritize docs and product fixes
- launch support war-room sweeps
- churn-risk signal from support friction

### Key June 2026 customer themes

- data trust and connector confidence
- report delivery confidence
- API/MCP/AI readiness
- setup/admin friction
- dashboard/report polish
- white-label/custom domain trust infrastructure

### Guardrails

- Do not expose customer private data in public outputs.
- Do not message customers as Nicole without approval.
- Summarize themes; avoid dumping raw conversations unless Chris asks and context is private.
- Treat API results as directional if noisy.

---

## 5.5 `meta` skill

### Purpose

Audit, report, and safely operate Oviond’s Meta presence across Facebook Page, Instagram, and Meta Ads.

Primary marketing use:

- confirm ads-off hold,
- analyze spend/performance,
- inspect campaigns/ad sets/ads/creatives,
- plan remarketing/creative improvements,
- eventually apply safe changes with approval.

### Provider docs Hermes must read

Read current Meta docs for:

- Marketing API
- Graph API auth
- ad accounts/campaigns/ad sets/ads
- insights endpoint
- breakdowns/fields
- creative objects
- custom audiences
- pages/Instagram accounts if needed
- permissions/app review
- rate limits

Docs root:

- `https://developers.facebook.com/docs/marketing-apis/`
- `https://developers.facebook.com/docs/graph-api/`

### Credential/env

Hermes should inspect Railway env vars for Meta token(s), ad account IDs, app IDs.

Do not print tokens.

### Current known state

- Meta access configured.
- USA remarketing campaigns remained paused in late April/May 2026.
- Previous broad remarketing was noisy.
- Tighter Facebook-only previous-visitor remarketing with stronger image creative looked cleaner.
- Ads-off hold is active.

### Required operations

Read:

- auth doctor
- account visibility
- campaign/ad set/ad inventory
- delivery status
- insights by date range
- spend/impressions/clicks/landing page views
- conversion events if available
- creative inventory and previews
- audience setup inspection
- Page/Instagram high-level status where relevant

Writes, with strict approval:

- pause campaigns/ad sets/ads
- create draft campaigns/ad sets/ads
- update budgets/bids/status
- upload creatives
- create/edit custom audiences

### Guardrails

Standing ads-off hold:

> Until the new website is live, tracking is confirmed, and Chris explicitly reauthorizes ads, Meta work must stay read-only or protective pause-only.

Do not:

- unpause campaigns,
- increase budgets,
- launch new spend,
- optimize against polluted events,
- call traffic healthy based on cheap clicks alone.

### Oviond reporting standard

Always separate:

- spend,
- impressions,
- clicks,
- landing page views,
- actual trial/signup quality,
- Stripe/app conversion truth.

---

## 5.6 `google-ads` skill

### Purpose

Audit, report, and safely operate Oviond’s Google Ads account.

Primary use:

- confirm ads-off hold,
- pull campaign/search-term/keyword/conversion reporting,
- audit conversion actions,
- protect spend,
- prepare paid relaunch plans,
- eventually apply validated changes.

### Provider docs Hermes must read

Read current Google Ads API docs for:

- auth models
- developer token
- manager/client account linkage
- GAQL
- GoogleAdsService search/searchStream
- mutate operations
- validate-only
- conversion actions
- campaign/ad group/keyword criteria
- recommendations/experiments where useful
- rate limits/errors

Docs root:

- `https://developers.google.com/google-ads/api/docs/start`

### Credential/env

Known current mapping:

```text
MCC: 638-795-6297
Target account: 290-615-4258
Developer token env: GOOGLE_ADS_DEVELOPER_TOKEN
Preferred service-account credential source: GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT
```

Hermes should inspect Railway env vars for exact keys.

### Current known state

- Production API access works.
- Historical audits showed USA PMAX was the only clearly proven engine.
- Display was waste-risk.
- South Africa can only be supervised/tactical if Chris directs it.
- Judge real free-trial quality, not cheap traffic or inflated platform conversions.
- Ads-off hold active.

### Required operations

Read:

- auth doctor
- accessible customers
- manager/client linkage check
- campaign inventory/status
- spend/impressions/clicks/conversions by date
- search term reporting
- keyword reporting
- asset/ad reporting
- conversion action audit
- budget/status audit
- geo/device/network breakdowns

Writes, strict approval:

- validate-only mutations
- pause/enable campaigns/ad groups/ads/keywords
- budget changes
- negative keywords
- campaign/ad creation
- conversion action updates

### Guardrails

- No enabling/relaunching/spend-driving mutations during ads-off hold.
- Protective pausing is allowed if needed, but validate and explain.
- Always use validate-only before writes.
- Do not optimize using polluted GA4 conversion events.
- Tie paid decisions to Stripe/app signup/trial/paid truth.

### Historical campaign context

Historical approved USA Search campaign:

```text
Name: USA | Search | Trial | Core Intent | 2026-04-03
Campaign ID: 23720451302
Budget: R250/day
Target: USA-only Search
No Display
No Search Partners
Buyer-intent exact/phrase keywords
Junk-intent negatives
```

This is historical only, not current approval to run.

---

## 5.7 `stripe` skill

### Purpose

Read Stripe billing data for MRR, revenue, trials, invoices, subscriptions, cancellations, plan mix, delinquency, churn risk, and reactivation opportunities.

Stripe is the finance/revenue source of truth.

### Provider docs Hermes must read

Read current Stripe docs for:

- authentication
- pagination
- customers
- subscriptions
- invoices
- charges/payment intents as needed
- products/prices
- trials
- subscription statuses
- cancellations
- webhooks/events
- test/live mode handling
- rate limits

Docs root:

- `https://docs.stripe.com/api`

### Credential/env

Known preferred env var:

- `STRIPE_SECRET_KEY`

Hermes should detect live/test key mode and report without exposing key.

### Current known state

- Stripe read-only access exists.
- Primary operational read: invoice-backed normalized MRR.
- Dashboard numbers remain finance-grade tie-breaker.

### Required operations

Read:

- auth doctor
- current MRR / normalized MRR
- active paying customers
- active trials
- trials expiring within next 3 days
- paid invoices last 7/30 days
- prior-period comparisons
- past_due count
- subscription statuses
- cancellations/churn
- plan/product/price mix
- ARPU
- new vs expansion vs churn if possible
- lapsed/reactivation candidate lists

Writes:

- none by default.
- Any billing/customer/subscription write needs explicit Chris approval and high caution.

### Heartbeat support

The skill must support:

- Trial Health Check
- Revenue Pulse
- past_due threshold alert >20
- rolling 7-day paid invoice comparison

### Guardrails

- Handle pagination completely.
- Separate trialing vs paid.
- Do not confuse invoice revenue with MRR without normalization.
- Do not expose customer private data in broad summaries.
- Do not perform billing writes unless explicitly approved.

---

## 5.8 `sanity` skill

### Purpose

Operate Sanity CMS as Oviond’s marketing content operating system.

Old WordPress site is migrating to Sanity + Astro. Sanity should become Nicole’s structured surface for:

- pages,
- blog posts,
- comparison pages,
- customer stories,
- SEO metadata,
- taxonomy,
- redirects/content governance,
- launch messaging.

### Provider docs Hermes must read

Read current Sanity docs for:

- Content Lake API
- GROQ
- mutations/transactions
- datasets/projects
- auth tokens and permissions
- schema/content types
- assets/images
- migration scripts
- releases/drafts if used
- webhooks

Docs root:

- `https://www.sanity.io/docs`

### Credential/env

Hermes should inspect Railway env vars for:

- Sanity project ID
- dataset
- API token
- studio URL/config if available

Likely names may include:

- `SANITY_PROJECT_ID`
- `SANITY_DATASET`
- `SANITY_API_TOKEN`

But do not assume.

### Current known state

- Website/CMS direction: WordPress → Sanity + Astro.
- Treat Sanity as Oviond’s marketing operating system.
- Detailed audit exists:
  - `research/sanity-audit-2026-05-12/oviond-sanity-astro-strategy-read.md`

### Required operations

Read:

- auth doctor
- project/dataset check
- list document types
- fetch pages/posts
- fetch slugs/routes
- fetch SEO fields
- fetch taxonomy/category/tag structure
- detect drafts/unpublished content
- detect missing metadata
- inspect redirects if modeled
- content inventory export

Writes, approval/preview:

- create/update drafts
- update SEO metadata
- create comparison pages
- create blog posts
- update taxonomy
- upload assets
- publish content only with approval

### Oviond workflows

- launch page QA
- metadata cleanup
- taxonomy cleanup
- comparison page buildout
- customer story modeling
- redirect integrity checks
- editorial governance
- content calendar execution

### Guardrails

- Never overwrite published content blindly.
- Prefer drafts and preview links.
- Preserve slugs unless redirect plan exists.
- Before publishing, run SEO/content QA.
- Do not break Astro routes.

---

## 5.9 `google-analytics` skill

### Purpose

Query and analyze Oviond GA4 data safely.

### Provider docs Hermes must read

Read:

- GA4 Data API
- GA4 Admin API
- dimensions/metrics compatibility
- quotas
- authentication/service-account impersonation

Docs:

- `https://developers.google.com/analytics/devguides/reporting/data/v1`
- `https://developers.google.com/analytics/devguides/config/admin/v1`

### Credential/auth

Use Google Workspace service-account impersonation where appropriate.

Known helper historically:

- `/data/.openclaw/secrets/gws-analytics-token.js`

### Current warning

`Oviond Website + App` mixes:

- `www.oviond.com`
- app/product usage
- white-label customer report domains
- dev/localhost traffic

Never treat top-level GA4 as clean acquisition truth.

### Required operations

Read:

- auth doctor
- property discovery
- traffic by host
- landing pages by host
- source/medium by host
- signup-style events by host/source
- event counts by name
- country/device reports with host filters
- conversion action investigation
- daily trend reports

### Guardrails

- Segment by hostname.
- Do not use polluted conversions as final truth.
- Prefer backend/app and Stripe for real conversion/revenue truth.
- State caveats clearly.

---

## 5.10 `google-search-console` skill

### Purpose

Query Oviond Search Console for SEO performance.

### Provider docs Hermes must read

Read:

- Search Console API / Search Analytics
- Sites/list
- Query dimensions
- Date ranges
- Row limits/pagination behavior

Docs:

- `https://developers.google.com/webmaster-tools/search-console-api-original/`

### Credential/auth

Use Google Workspace service-account impersonation.

Known property:

```text
sc-domain:oviond.com
```

Known helper historically:

- `/data/.openclaw/secrets/gws-gsc-token.js`

### Required operations

Read:

- auth doctor
- property visibility
- top queries
- top pages
- query+page pairs
- branded vs non-branded split
- country/device breakdown
- position buckets
- week-over-week movement
- page-specific keyword set

### Heartbeat support

SEO Movement check:

- pull top 10 non-brand queries
- compare to stored baseline
- flag drops >3 positions

### Guardrails

- Store baselines cleanly.
- Do not overreact to tiny impressions.
- Separate brand and non-brand.
- Use DataForSEO for SERP validation when needed.

---

## 5.11 `google-tag-manager` skill

### Purpose

Audit, diagnose, and safely manage Oviond GTM accounts/containers/workspaces/tags/triggers/variables.

### Provider docs Hermes must read

Read:

- Tag Manager API
- Accounts/containers/workspaces
- Tags/triggers/variables
- Versions/publishing
- Permissions
- Quotas/errors

Docs:

- `https://developers.google.com/tag-platform/tag-manager/api/v2`

### Credential/auth

Use Google Workspace service-account impersonation.

Known GTM facts:

```text
Account: Oviond / accounts/6002040978
Main container: www.oviond.com and v2.oviond.com / GTM-WXRJGTK / containers/32460546
Server container: www.oviond.com - Server / GTM-WGXKZQH / containers/65118591
```

### Required operations

Read:

- auth doctor
- list accounts/containers/workspaces
- export tags/triggers/variables
- audit firing rules
- inspect GA4/Ads/Meta tags
- identify host filters
- identify old/polluted conversion tags

Writes, strict approval:

- create workspace
- edit tags/triggers/variables
- create version
- publish version

### Guardrails

- Never publish without diff/audit.
- Use workspaces, not blind default edits.
- Summarize what will fire more/less/stop firing.
- Fix host filters/site injection where appropriate, not reporting views only.

---

## 5.12 `google-workspace` skill

### Purpose

Operate Gmail, Drive, Calendar, Docs, Sheets, Tasks, and Contacts as Nicole.

### Separate handover doc

Use the dedicated Google Workspace rebuild document:

- `exports/hermes-google-workspace-rebuild-instructions-2026-06-08.md`

### Required architecture

```text
Google Cloud service account
+ domain-wide delegation
+ impersonation of nicole@oviond.com
+ scoped OAuth tokens
```

### Required operations

Read:

- auth doctor
- Gmail profile/search/read
- Drive upload/download/search/share
- Calendar list/read
- Docs export/read
- Sheets get/update with approval
- Contacts lookup

Writes, approval:

- send Gmail
- create calendar events
- share Drive externally
- edit Sheets/Docs

### Guardrails

- Never send external email without approval.
- Never expose secrets.
- Confirm actions were actually executed before claiming completion.
- If Drive upload works as robot account, auth is wrong; it must act as `nicole@oviond.com`.

---

## 5.13 `supabase-oviond-api` skill

### Purpose

Create the growth/product intelligence bridge between Nicole and Oviond’s new app/backend.

Oviond is moving toward:

- Supabase/Postgres/Supabase Auth
- Stripe retained
- API-first React frontend
- Oviond REST API
- MCP/AI-first direction

This skill should expose clean, read-first app truth for growth decisions.

### Provider docs Hermes must read

Read:

- Supabase JS/API docs
- PostgREST docs
- Supabase Auth admin docs
- Edge Functions if used
- Database access and RLS docs
- Oviond API docs / internal API docs if available
- MCP/API docs if Oviond has them

Docs:

- `https://supabase.com/docs`

### Credential/env

Hermes should inspect Railway env vars for:

- Supabase URL
- service role key
- anon key
- database URL
- Oviond API key/token
- MCP/API credentials

Use least privilege. Prefer read-only credentials for Nicole where possible.

### Required operations

Read:

- auth doctor
- active trials
- trial activation milestones
- signup source/UTM
- email verified
- first login
- first client created
- first data source connected
- first dashboard/report created
- scheduled report configured
- report shared/exported
- data-source health
- integration failures
- churn-risk usage indicators
- customer/account profile

Writes:

- none by default unless specific internal tools are approved.

### Growth intelligence outputs

This skill should power:

- trial health check
- activation funnel baseline
- churn-risk views
- lifecycle triggers for Sequenzy
- support prioritization with Gleap
- paid traffic quality validation

### Guardrails

- Read-only by default.
- Respect PII and customer privacy.
- Do not bypass RLS/security casually.
- Do not mutate production app data without explicit approval.
- Treat backend/app truth as the conversion source of truth.

---

## 5.14 `postiz` skill

### Purpose

Operate Postiz as Oviond’s social publishing rail.

Nicole owns strategy and content judgment; Postiz handles drafts, scheduling, publishing, media, and analytics collection.

### Provider docs Hermes must read

Read current Postiz docs for:

- API auth
- posts/drafts
- channels/accounts
- media upload
- scheduling
- analytics
- webhooks
- rate limits

Docs/site:

- `https://postiz.com/`
- Use current API docs if published.

### Credential/env

Hermes should inspect Railway env vars for Postiz API keys/base URL.

### Required operations

Read:

- auth doctor
- connected channels
- scheduled posts
- drafts
- recent published posts
- analytics if available

Writes, approval:

- create drafts
- upload media
- schedule posts
- publish posts

### Oviond workflows

- blog → LinkedIn/X/Facebook adaptation
- launch announcement drafts
- weekly social calendar
- content repurposing
- performance feedback loop

### Guardrails

- Do not publish without approval.
- Prefer drafts first.
- Keep channel-specific formatting.
- LinkedIn is primary; X secondary; Facebook selective.

---

## 5.15 `railway` skill

### Purpose

Operate Railway infrastructure for Oviond/OpenClaw/Hermes deployments, services, env vars, logs, metrics, domains, and deployment diagnostics.

### Provider docs Hermes must read

Read Railway docs for:

- projects/services/environments
- deployments/logs
- variables
- domains
- databases
- object storage
- GraphQL/API/CLI
- rate limits

Docs:

- `https://docs.railway.com/`

### Credential/env

Hermes likely has Railway access and env vars. Do not expose tokens.

### Required operations

Read:

- auth doctor
- list projects/services/environments
- deployment status
- logs
- env var names only
- service health
- domains
- metrics if available

Writes, approval:

- add/update env vars
- restart/deploy service
- change domains
- provision services/databases/storage

### Guardrails

- Do not edit env vars blindly.
- Never print env var values.
- Before restarts/config changes, explain risk and get approval unless Chris explicitly asks.
- Prefer safe diff/preview.

---

## 5.16 `oviond-content-engine` skill

### Purpose

Own Oviond’s content strategy and production workflow.

This is not a provider API skill only. It is Nicole’s editorial operating brain.

### Inputs

- Oviond positioning
- GSC data
- DataForSEO research
- Sanity content inventory
- competitor intelligence
- Gleap customer language
- launch priorities
- product updates

### Required operations

- topic selection
- content briefs
- blog outlines
- full blog drafts
- LinkedIn/X/Facebook adaptations
- content calendar
- source asset repurposing
- performance review
- Sanity draft coordination
- Postiz draft coordination

### Guardrails

- Avoid generic SaaS fluff.
- Every content piece needs an audience, point of view, and business purpose.
- Comparison content should be fair, not publicly nasty.
- Use content-quality auditor before important publish.

---

## 5.17 `oviond-design-director` skill

### Purpose

Create Oviond creative direction, prompts, visual QA, and design-system consistency.

### Required operations

- creative briefs
- image prompt packages
- design QA
- social/paid/web/blog visual direction
- brand consistency checks
- asset specs
- design handoff notes

### Brand facts

Palette:

```text
Primary: #0000FF
Secondary: #0A0B5C
Tertiary: #5676FF
Neutral: #FFFFFF
Ink: #000000
Surface soft: #D5E4FF
Font: Inter
```

Creative feeling:

- clean
- modern
- digital
- calm
- commercial
- uncluttered
- product-trust-building

### Guardrails

- Prefer overlay-safe / text-free generated visuals.
- Avoid generic office scenes.
- Avoid noisy startup fluff.
- Nicole should QA final output.

---

## 5.18 `oviond-screenshot-director` skill

### Purpose

Capture, annotate, QA, and manage product screenshots for help docs, launch materials, social, ads, and product explainers.

### Required operations

- screenshot brief
- capture checklist
- annotation guidance
- style consistency
- product state QA
- image naming/storage
- docs/help-center handoff

### Guardrails

- No broken/dirty UI screenshots.
- Avoid exposing private customer data.
- Use clean demo data.
- Screenshots should build trust, not show clutter.

---

## 5.19 `website-seo` skill

### Purpose

Technical and on-page SEO system for the Sanity/Astro marketing site.

### Required operations

- title/meta description optimization
- H1/H2 hierarchy
- schema recommendations
- internal linking plans
- redirect checks
- content gap analysis
- Core Web Vitals guidance
- comparison page strategy
- reporting template hub strategy

### Inputs

- Sanity content inventory
- GSC data
- DataForSEO SERP data
- competitor intelligence
- Astro route map

### Guardrails

- SEO should support useful content, not keyword stuffing.
- Preserve redirects and slugs.
- Segment brand/non-brand.

---

## 5.20 `content-quality-auditor` skill

### Purpose

Audit content quality, E-E-A-T, publish readiness, and fix plans.

### Required operations

- 80-item quality scoring or Hermes-equivalent robust framework
- veto checks
- evidence/support checks
- clarity and audience fit
- originality/point-of-view checks
- practical fix plan

### Guardrails

- Do not pass thin content.
- If content is not publish-ready, say so.
- Prefer fewer better pieces over more generic pieces.

---

## 6. Priority build sequence

Hermes should not build everything randomly. Recommended sequence:

### Phase 1 — Business truth and safety

1. `stripe`
2. `google-workspace`
3. `google-analytics`
4. `google-search-console`
5. `google-tag-manager`
6. `google-ads`
7. `meta`

Reason:

- These protect measurement, revenue truth, and ads-off safety.

### Phase 2 — Customer and lifecycle system

8. `gleap`
9. `sequenzy`
10. `mailerlite-archive`
11. `supabase-oviond-api`

Reason:

- These power activation, retention, support signal, and lifecycle automation.

### Phase 3 — Content and launch growth

12. `sanity`
13. `dataforseo`
14. `website-seo`
15. `oviond-content-engine`
16. `content-quality-auditor`
17. `postiz`

Reason:

- These turn the new site into a growth/content machine.

### Phase 4 — Creative and operations

18. `oviond-design-director`
19. `oviond-screenshot-director`
20. `railway`

Reason:

- These round out launch/design/infra work.

Railway may move earlier if Hermes needs it to inspect env vars.

---

## 7. Cross-skill workflows Hermes should support

### 7.1 Launch tracking verification

Skills:

- `google-tag-manager`
- `google-analytics`
- `supabase-oviond-api`
- `stripe`
- `google-ads`
- `meta`

Goal:

- prove visit → signup → email verified → trial → paid is trackable and not polluted.

### 7.2 Trial activation rescue

Skills:

- `stripe`
- `supabase-oviond-api`
- `sequenzy`
- `gleap`
- `google-workspace`

Goal:

- identify near-expiry/high-risk trials and trigger the right rescue path.

### 7.3 Churn and delinquency rescue

Skills:

- `stripe`
- `gleap`
- `sequenzy`
- `google-workspace`

Goal:

- reduce past_due and voluntary churn.

### 7.4 SEO/content production loop

Skills:

- `google-search-console`
- `dataforseo`
- `sanity`
- `website-seo`
- `oviond-content-engine`
- `content-quality-auditor`
- `postiz`

Goal:

- find opportunity → brief content → draft → QA → publish → repurpose → measure.

### 7.5 Customer friction → product/docs fixes

Skills:

- `gleap`
- `supabase-oviond-api`
- `sanity`
- `oviond-screenshot-director`
- `website-seo`

Goal:

- turn repeated support pain into better docs, better screenshots, and product priorities.

### 7.6 Paid relaunch decision

Skills:

- `stripe`
- `supabase-oviond-api`
- `google-analytics`
- `google-tag-manager`
- `google-ads`
- `meta`
- `dataforseo`
- `oviond-design-director`

Goal:

- relaunch paid only when tracking and funnel truth justify it.

---

## 8. Skill acceptance checklist

For each skill, Hermes should not mark it complete until:

- [ ] official provider docs were reviewed,
- [ ] auth doctor exists,
- [ ] credentials are loaded from secure env/secret source,
- [ ] no secrets are printed,
- [ ] read smoke test passes,
- [ ] write path is guarded or disabled,
- [ ] common error messages are actionable,
- [ ] Oviond-specific account/property/resource IDs are discovered or configurable,
- [ ] output includes human summary and structured JSON,
- [ ] at least one real Oviond workflow is tested,
- [ ] docs/SKILL.md explains when to use it and guardrails.

---

## 9. What Hermes should not do

- Do not copy old Nicole skills verbatim.
- Do not build shallow endpoint wrappers without operator context.
- Do not assume old API behavior still works.
- Do not expose secrets.
- Do not relaunch ads.
- Do not publish content/social posts without approval.
- Do not send email without approval.
- Do not treat GA4 conversions as clean truth without segmentation.
- Do not revive MailerLite as the active lifecycle platform.
- Do not mutate Stripe billing data unless explicitly approved.
- Do not edit Sanity published content without preview/diff.

---

## 10. Source materials for Hermes

Hermes should use these local handover/source docs as context, not as code to copy blindly:

- `exports/nicole-prince-handover-for-new-agent-2026-06-08.md`
- `exports/hermes-google-workspace-rebuild-instructions-2026-06-08.md`
- `MEMORY.md`
- `STRATEGY-Q2-Q4-2026.md`
- `projects/oviond-growth-operating-system.md`
- `launch/nicole-launch-checklist-2026-06-09.md`
- `DESIGN.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `research/sanity-audit-2026-05-12/oviond-sanity-astro-strategy-read.md`
- `research/supabase-growth-machine-2026-05-05.md`
- `research/gleap-customer-sentiment-2026-06-02/gleap-customer-sentiment-sweep-2026-06-02.md`
- `research/competitor-intelligence/`
- old skills under `skills/*/SKILL.md` only as historical template

---

## 11. Final instruction to Hermes

Hermes: build Nicole’s new skills fresh.

Use provider docs. Use Railway env vars. Use the old Nicole handovers only to understand Oviond’s workflows and previous working patterns.

The goal is not to recreate old scripts. The goal is to give the new Nicole a clean, durable, safe, deeply useful operating system for Oviond growth.

If a skill can only read, build it read-only first. If a skill can write, make the write path impossible to trigger accidentally. If a platform affects money, customers, public content, email, ads, or production systems, default to preview and approval.

Above all: help Chris grow Oviond with truth, not noise.
