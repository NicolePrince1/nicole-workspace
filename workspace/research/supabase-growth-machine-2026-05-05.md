# Supabase Growth Machine Research — 2026-05-05

## Context

Chris confirmed Oviond is moving the rebuilt core product from MongoDB/Meteor/Meteor Auth/Galaxy to Supabase/Postgres/Supabase Auth, with Stripe statuses locked into Supabase. The new app is API-first, with Swagger/API docs at `docs.oviond.com`, and is launching around the new website/app migration.

This is not just a technical migration. It changes Nicole's operating model: product, billing, account, customer, integration, reporting, and lifecycle truth can now be unified around Postgres + the Oviond REST API.

## Supabase primitives that matter for Oviond

### 1. Postgres as the operating truth layer

Supabase provides a full Postgres database, SQL editor, relationships, backups, table view, and extensions. For Nicole, this means the customer/account/product state can become queryable instead of inferred from scattered systems.

Growth uses:
- Customer health scoring from real product usage.
- Trial activation scoring.
- Churn-risk detection.
- Funnel analytics beyond GA4.
- Agency segmentation by plan, connected data sources, clients, projects, automations, report schedules, and billing state.
- Cohort reporting: signup month, plan, activation depth, integration path, churn timing.

### 2. Supabase Auth + RLS

Supabase Auth supports password, magic link/OTP, OAuth, SSO, JWT-based auth, and integrates with Row Level Security. RLS is critical because the app is multi-tenant and agency/client data is sensitive.

Growth uses:
- Cleaner identity model for lifecycle messaging.
- Safer internal/admin access patterns.
- Better account/team/member-level segmentation.
- Potential enterprise/agency SSO story later.

Guardrail:
- Nicole should not be given broad direct production write access casually. Prefer read-only/reporting views, service-role access only through approved functions, or a dedicated internal API key with scoped permissions.

### 3. Database webhooks and pg_net

Supabase database webhooks can fire on INSERT/UPDATE/DELETE after table changes and are built around async `pg_net`. This is highly relevant because growth/lifecycle actions should respond to real product state.

Growth uses:
- New user/account created → sync/enrich into Sequenzy.
- Stripe status changed in Supabase → lifecycle tag/update.
- Trial expires soon → trigger lifecycle workflow.
- First client created → onboarding milestone.
- First data source connected → activation milestone.
- First project/dashboard/report created → activation milestone.
- Automation scheduled → stronger activation signal.
- Automation failed → trust-risk/support alert.
- Integration disconnected/erroring → churn-risk/support alert.

### 4. Edge Functions

Supabase Edge Functions are globally distributed TypeScript functions for webhooks, third-party integrations, transactional email, small AI tasks, and API orchestration.

Growth uses:
- Receive Stripe/webhook events and normalize into Supabase.
- Send normalized lifecycle events to Sequenzy.
- Create internal endpoints for Nicole dashboards or safe operations.
- Run AI-assisted analysis tasks close to product data.
- Build small internal support/customer-success tools without touching the core app too heavily.

### 5. Cron

Supabase Cron runs recurring SQL, database functions, or HTTP calls; job runs are recorded in Postgres.

Growth uses:
- Daily trial-expiry queue.
- Daily churn-risk refresh.
- Weekly customer-health snapshots.
- Failed automation/integration scans.
- Delinquency and payment-status sync checks.
- Monthly-to-annual conversion candidate lists.

### 6. Realtime

Supabase Realtime can broadcast database changes, presence, and Postgres changes.

Growth/product uses:
- Internal live customer-success dashboards.
- Live support/admin views when key account events happen.
- Future collaborative reporting experiences.

Not the first growth lever, but useful later.

### 7. Storage and Vector/AI capabilities

Supabase Storage supports files, analytics buckets, vector buckets, S3-compatible storage, CDN, image transforms, and RLS-integrated access. Supabase AI docs emphasize pgvector, semantic/keyword/hybrid search, and embeddings.

Growth/product uses:
- Store generated report assets, screenshots, PDFs, and customer-facing media.
- Semantic search over help docs, support tickets, account notes, product events, and report templates.
- AI assistant/RAG layer for internal customer context and eventually customer-facing reporting assistance.
- Pattern discovery from cancellation reasons, support tickets, and product usage notes.

## Oviond API docs quick read

`docs.oviond.com` confirms the new Oviond API is positioned around:
- accounts and usage
- API keys
- activity logs
- clients
- projects/reports/dashboards
- widgets/assets/pages
- automations and automation history
- billing/plans/invoices
- branding
- custom data
- data/integration account queries
- email setup/logs/sending
- folders

This means Oviond is becoming programmable agency-reporting infrastructure, not just a UI app.

## Strategic thesis

The Supabase migration can help Oviond reach $100k MRR if it becomes the source of truth for three systems:

1. **Activation system** — detect exactly where trials get stuck and intervene.
2. **Retention system** — detect trust, integration, automation, billing, and usage risks before cancellation.
3. **Agent/API system** — make Oviond easier for AI agents, internal tools, and partner workflows to operate.

The biggest commercial value is not merely that data is in Postgres. It is that Nicole can stop guessing from GA4/Stripe fragments and start operating from product truth.

## Recommended Nicole access model when ready

Ask Chris for:

1. **Read-only Supabase reporting access**
   - Prefer a dedicated reporting replica/view role or scoped SQL access.
   - Access to sanitized views for accounts, users, plans, Stripe status, trials, subscriptions, clients, projects, data sources, automations, integration health, activity logs, and churn/cancellation fields.

2. **Oviond internal/admin API key**
   - Scoped initially to read-only endpoints.
   - Later allow specific safe actions via dedicated endpoints, not blanket writes.

3. **Event/webhook catalogue**
   - signup/account created
   - trial started/ending/ended
   - Stripe status changed
   - subscription converted/canceled/past_due
   - client created
   - data source connected/disconnected/erroring
   - project/report created
   - automation scheduled/paused/failed/sent
   - user invited/team member added

4. **Schema map / data dictionary**
   - Table names, key relationships, tenant/account boundaries, important timestamps, and status enums.

5. **Safe sandbox/staging project**
   - For building queries, functions, and lifecycle logic without risking production.

6. **Decision on Stripe posture**
   - Recommendation: keep Stripe connector for finance-grade fallback and reconciliation for now; use Supabase as operational customer truth once Stripe statuses are reliably mirrored.
   - Do not disconnect Stripe until Supabase billing mirror has been reconciled against Stripe for MRR, trials, past_due, cancellations, plan mix, and invoice status.

## Priority growth builds after launch

### Phase 1: Read-only intelligence layer

- Build a Supabase/Oviond API read-only skill for Nicole.
- Create daily/weekly SQL views:
  - active trials
  - trials expiring in 3 days
  - activation milestones completed/missing
  - customers past_due
  - customers with no recent product activity
  - customers with integration/automation failures
  - plan mix and MRR health
  - churn candidates and saveable accounts

### Phase 2: Lifecycle automation

- Pipe product/billing events into Sequenzy.
- Build lifecycle sequences around:
  - welcome/setup
  - first client not created
  - no data source connected
  - no report/project created
  - no automation scheduled
  - trial ending soon
  - payment failed/past_due
  - integration failure
  - win-back
  - monthly-to-annual conversion

### Phase 3: Customer-success cockpit

- Combine Supabase product truth + Stripe billing + Gleap support signals.
- Create weekly account health view and priority action list.
- Use this to drive retention work, help-center fixes, product improvements, and messaging.

### Phase 4: AI-agent layer

- Use docs/API + Supabase views to build internal agent workflows:
  - “summarize this account health”
  - “why is this trial stuck?”
  - “which customers are likely to churn?”
  - “which integrations are causing trust risk?”
  - “draft a support/lifecycle message based on account state”
  - “find agencies that look ready for annual conversion”

### Phase 5: Growth experiments

- Build cleaner acquisition cohorts by tying source/landing page/campaign to actual activation and revenue.
- Relaunch ads only when source→signup→activation→MRR can be tied through the new data layer.
- Use product data to generate better landing pages and content: integrations, templates, use cases, comparison pages, and objection-handling pages.

## Biggest risks

- Giving Nicole or any automation too much production write access too early.
- Treating mirrored Stripe status in Supabase as finance-grade truth before reconciliation.
- Building lifecycle spam before activation milestones and event semantics are clean.
- Exposing service-role credentials in unsafe places.
- Polluting production with ad hoc SQL/functions instead of versioned migrations and reviewed views.

## Current recommendation

Keep both Stripe and Supabase initially:
- Supabase becomes the operational/customer/product truth layer.
- Stripe remains finance-grade billing truth and reconciliation fallback.
- Once Supabase mirrors Stripe perfectly over time, we can reduce direct Stripe dependency for day-to-day Nicole operations, but I would not disconnect it yet.

The first build I want after launch is a **Nicole Growth Intelligence Layer**: read-only Supabase/Oviond API access plus a set of canonical views for trial health, activation, churn risk, billing state, and lifecycle triggers.
