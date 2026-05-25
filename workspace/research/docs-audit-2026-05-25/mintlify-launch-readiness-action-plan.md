# Oviond Mintlify Docs Launch Readiness Audit & Action Plan

Prepared for: Chris Irwin and Oviond dev team  
Site audited: https://docs.oviond.com/introduction  
Fresh audit date: 2026-05-25  
Prior audit reviewed: 2026-05-23

## Executive verdict

Do not treat the Mintlify docs as launch-ready yet.

The public docs are structurally in decent shape: the introduction renders, the sitemap and `llms.txt` mostly align, the user-facing intro/quickstart/product sections are much better than the old Gleap-style help-center content, and the docs clearly point toward the right product story: white-label agency reporting, dashboards, data sources, automation, custom domains, API, and MCP.

But the developer/API layer still has trust-breaking issues that must be fixed before launch. The biggest one has not changed since the 23 May audit: `https://docs.oviond.com/api-reference/openapi.json` still publicly serves Mintlify's sample **OpenAPI Plant Store** spec. That is the first thing a technical user, AI crawler, SDK generator, or agent might find, and it makes the API surface look unfinished.

The second problem is that the real OpenAPI file at `/api/openapi.json` is live, but it is being treated inconsistently across the docs surface. It appears as a sitemap/LLM-index item but does not have a markdown page equivalent, so a crawl hits `https://docs.oviond.com/api/openapi.json.md` and gets a 404. That is not as embarrassing as the Plant Store sample, but it tells us raw spec files and human docs pages are mixed together in the Mintlify routing/indexing setup.

The third problem is polish and trust: API pages are still mostly thin generated wrappers, internal implementation/vendor terms still leak into public docs and OpenAPI descriptions, destructive actions often lack proper warning treatment, and several product terms need a single canonical explanation before the team launches the new product/API/MCP story.

## Fresh audit scope

Fresh crawl sources used:

- `https://docs.oviond.com/introduction`
- `https://docs.oviond.com/llms.txt`
- `https://docs.oviond.com/sitemap.xml`
- Markdown endpoints for all indexed docs pages
- HTML samples for introduction, authentication, API overview, quickstart, and delete account
- OpenAPI files:
  - `https://docs.oviond.com/api-reference/openapi.json`
  - `https://docs.oviond.com/api/openapi.json`
  - `https://docs.oviond.com/openapi.json`

Fresh crawl numbers:

- Total indexed URLs: 249
- Sitemap URLs: 248
- LLM index URLs: 249
- API/developer pages: 146
- Non-API/user docs pages: 103
- Fresh findings generated: 240
  - P0: 2
  - P1: 231
  - P2: 7
- Thin pages under audit thresholds: 152
- Pages/spec entries with internal/vendor language: 43
- Destructive/risky pages without a Mintlify warning component: 41

Important caveat: one P0 is a routing/indexing issue for the raw real OpenAPI JSON appearing like a page and returning 404 at `.md`. The truly urgent reputational P0 remains the live Plant Store sample spec.

## What changed since the 23 May audit

The broad picture is mostly unchanged, but the fresh audit shows the docs have moved slightly in the right direction in user-facing sections.

Still unresolved from 23 May:

1. The Plant Store sample OpenAPI spec is still live at `/api-reference/openapi.json`.
2. The real spec is still at `/api/openapi.json`, creating two competing spec surfaces.
3. The OpenAPI spec still uses invalid colon-style path params in many paths, e.g. `/v1/users/:id`, `/v1/clients/:id`, `/v1/automations/:id`.
4. API endpoint pages are still very thin and generated-looking.
5. Public docs/spec still expose internal/vendor terms such as Supabase, S3, SQS, Resend, Vercel, cron scheduler, accounts row, users table, raw_data, client_integrations, resource_type, and Stripe.
6. Destructive actions still need stronger warnings and consequence explanations.
7. Product taxonomy still needs one canonical definition for client, project, report, dashboard, agency report, template, data source, integration, API key, and MCP.

Improvements / better signs:

1. The rendered Introduction page is coherent and has solid Mintlify components: cards and steps.
2. The rendered Quickstart, Authentication, and API Overview pages return valid HTML with sensible titles and descriptions.
3. Non-API pages are not all terrible. Many appear usable as a foundation; the launch risk is now concentrated more heavily in API/reference quality, terminology, and high-risk operations.
4. Sitemap and `llms.txt` still mostly agree, which is good for AI-reader discoverability once the wrong/spec issues are fixed.

## Critical launch blockers — fix first

### P0. Remove the Mintlify Plant Store OpenAPI sample

Current state:

- URL: `https://docs.oviond.com/api-reference/openapi.json`
- Status: 200
- Public title: `OpenAPI Plant Store`
- Server: `http://sandbox.mintlify.com`
- Paths include `/plants` and `/plants/{id}`

Why this blocks launch:

- It is visibly not Oviond.
- It can pollute AI/docs readers and generated client tooling.
- It makes the new API/MCP positioning look unfinished.
- It is the kind of issue a technical buyer screenshots immediately.

Required fix:

- Remove the sample spec from the Mintlify repo/config.
- Either redirect `/api-reference/openapi.json` to the real Oviond spec or return 404 intentionally.
- Prefer one canonical public spec URL. Recommendation: keep `/api/openapi.json` as canonical if endpoint pages already reference it, and redirect `/api-reference/openapi.json` there.
- After deploy, verify with `curl -I` and body inspection that no Plant Store content remains anywhere public.

Acceptance criteria:

- `https://docs.oviond.com/api-reference/openapi.json` no longer returns Plant Store content.
- Searching the deployed docs for `Plant Store`, `sandbox.mintlify.com`, `/plants`, and `NewPlant` returns zero public hits.
- `llms.txt` and `sitemap.xml` do not expose sample-spec URLs.

### P0/P1. Fix canonical OpenAPI routing and indexing

Current state:

- Real spec: `https://docs.oviond.com/api/openapi.json`
- Sample spec: `https://docs.oviond.com/api-reference/openapi.json`
- `/openapi.json` returns 404.
- `/api/openapi.json` appears in the crawl as a URL but does not have a markdown page equivalent, causing `/api/openapi.json.md` to return 404.

Required fix:

- Decide on exactly one canonical OpenAPI URL.
- Configure Mintlify so raw JSON spec files are not treated as human pages.
- If the spec should appear in navigation, create a human page called “OpenAPI Specification” that links to/downloads the raw JSON.
- Do not let raw JSON files appear as broken `.md` docs endpoints.

Acceptance criteria:

- One canonical spec URL exists and is documented.
- Stale/sample spec URLs redirect or disappear.
- `llms.txt` and `sitemap.xml` do not create broken `.md` equivalents for raw JSON assets.
- Endpoint pages are generated from the canonical spec only.

### P0/P1. Fix OpenAPI path parameter syntax

Current state:

The real OpenAPI file contains 102 paths. At least 30 paths still use colon-style parameters, including:

- `/v1/users/:id`
- `/v1/white-label/domains/:domain_id`
- `/v1/clients/:id`
- `/v1/integrations/:client_id`
- `/v1/integrations/:integrationID/profiles/:profileName`
- `/v1/email/domains/:id`
- `/v1/media/:id`
- `/v1/assets/:id`
- `/v1/pdf/status/:job_id`
- `/v1/templates/:id`
- `/v1/themes/:id`
- `/v1/automations/:id`

OpenAPI expects `{id}` style path params, not `:id`.

Required fix:

- Convert every colon path to OpenAPI-valid brace syntax.
- Ensure each path parameter is declared under `parameters` with `in: path`, `required: true`, and a schema.
- Regenerate Mintlify endpoint pages from the corrected spec.

Acceptance criteria:

- Zero paths in the spec match `/:param` format.
- OpenAPI validation passes.
- Mintlify endpoint pages show valid path parameters and request builders.

## High-priority pre-launch fixes

### 1. Normalize REST authentication language

Current state:

- The docs use “Bearer token” and “API key” language interchangeably.
- The OpenAPI spec declares `bearerFormat: JWT`.
- Public examples should consistently use one placeholder and one explanation.

Decision needed from dev/product:

- If Oviond issues opaque API keys, public language should be: “Use your Oviond API key as a Bearer token.” Remove `bearerFormat: JWT`.
- If Oviond issues JWTs, document expiry, renewal, revocation, and token lifecycle properly.

Recommendation:

Use customer-facing API-key language unless these are genuinely customer-managed JWTs.

Standard example:

```bash
curl https://api.oviond.com/v1/users/me \
  -H "Authorization: Bearer $OVIOND_API_KEY"
```

Acceptance criteria:

- One placeholder: `OVIOND_API_KEY`.
- One auth explanation reused across docs.
- OpenAPI security scheme matches the actual token type.
- Authentication page examples match the actual API response envelope.

### 2. Remove internal implementation/vendor language from public docs

Fresh audit found public mentions of:

- Supabase
- S3
- SQS
- Resend
- Vercel
- cron scheduler
- accounts row
- users table
- upstream API
- raw_data
- client_integrations
- resource_type/resource_id
- Stripe in places where billing-provider detail may not be appropriate

This makes docs feel like generated internal engineering notes rather than public product docs.

Rewrite examples:

- “Deletes the accounts row” → “Deletes the account and all associated workspace data.”
- “Purges S3 media files” → “Permanently removes stored media files.”
- “Removes cron scheduler job” → “Stops future scheduled deliveries.”
- “Registers the domain on Vercel” → “Registers the custom domain with Oviond’s domain service.”
- “Queues emails to SQS / Resend” → “Queues email delivery.”
- `user_id`, `resource_type`, `resource_id` → “actor, affected item, and action metadata.”

Acceptance criteria:

- Public docs/spec have zero avoidable internal stack names.
- Vendor names appear only where they are intentionally customer-facing or legally/operationally necessary.
- Engineering details move to private runbooks.

### 3. Upgrade destructive-action pages with proper warnings

Fresh audit found 41 destructive/risky pages without a Mintlify `<Warning>` component.

This includes delete/archive/revoke/bulk-delete style pages across user docs and API docs.

Required template for every destructive action:

```mdx
<Warning>
This action can remove or disable customer-facing data. Confirm the account, permissions, and recovery behavior before continuing.
</Warning>
```

Each destructive page must answer:

1. Who can do this?
2. Is it soft delete, archive, revoke, or permanent delete?
3. Can it be restored? If yes, for how long?
4. What related data is affected?
5. Does it affect billing, automations, scheduled emails, public links, PDFs, templates, integrations, or users?
6. What errors should users expect?
7. What should they do before using the endpoint/action?

Acceptance criteria:

- Every delete/archive/revoke/bulk-delete page has a warning block.
- Delete Account has an especially clear irreversible-action warning.
- API destructive endpoints include example error responses and consequences.

### 4. Expand API endpoint pages beyond generated stubs

Fresh audit still finds most API pages are too thin. Many endpoint pages are 28–40 words plus generated API metadata.

Minimum API endpoint template:

1. What this endpoint does
2. When to use it
3. Method and path
4. Auth and required permission/role
5. Path/query/body params
6. Example cURL request
7. Example JS/TS request
8. Example success response
9. Common errors
10. Side effects/warnings
11. Related endpoints

Prioritize these endpoint groups first:

1. Auth/API keys/users/account
2. Clients/projects/pages/widgets/templates
3. Data sources/integrations/querying data
4. Automations/email/PDF/report delivery
5. White label/custom domains/branding
6. Billing/account deletion
7. MCP/API-adjacent pages

Acceptance criteria:

- Top 30 API pages have real examples and consequences.
- No critical endpoint page is under ~150 useful words excluding generated OpenAPI boilerplate.
- Endpoint examples use the canonical auth placeholder and real response envelope.

### 5. Define product taxonomy once and reuse it everywhere

Problem:

The docs still risk confusing users with overlapping terms: project, report, dashboard, client project, agency project, agency report, template, widget, data source, integration, profile, API key, MCP.

Add a canonical terminology section near Introduction or Quickstart:

- Account/workspace: the agency’s Oviond environment.
- Client: one customer/profile/store/branch being reported on.
- Project: the container for a dashboard or report.
- Report: a paged project intended for client-ready reporting and delivery.
- Dashboard: a live project view for monitoring KPIs.
- Client project: a project tied to one client.
- Agency project/report: an account-level project not tied to one client.
- Template: a reusable project/report structure.
- Data source: a marketing platform or connector type.
- Integration/profile: a connected account/auth profile for a data source.
- API key: a credential used to call Oviond’s API.
- MCP: a way for supported AI clients to operate Oviond through scoped tools.

Acceptance criteria:

- H1s and sidebar labels disambiguate client vs agency pages.
- Duplicate generic headings like “Overview”, “List Projects”, “Add Project”, “Bulk Delete”, and “Widgets” are renamed with context.
- Agency-vs-client reporting has a comparison table.

### 6. Tighten MCP docs before launch

The MCP story is strategically important, but it must be precise.

Required fixes:

- Avoid saying every MCP client supports remote HTTP + OAuth unless that is tested and true.
- Add tested clients and versions.
- Reconcile MCP category/tool counts.
- Add a dedicated MCP safety page:
  - What agents can do
  - What they cannot do
  - Permission inheritance
  - Revoking access
  - Destructive actions and confirmation expectations
  - Audit logs
  - Recommended safe first prompts

Acceptance criteria:

- No overclaim about universal MCP support.
- Safety and revocation are easy to find.
- MCP copy connects to the product strategy without sounding like generic AI fluff.

### 7. Align billing/pricing docs with launch truth

Current risk:

Billing docs may go stale quickly because Oviond is moving toward clearer client-count pricing and grandfathering existing customers.

Required fixes:

- Verify current live pricing and launch pricing with Chris/dev before publishing.
- Make billing docs point to the authoritative pricing page for current prices.
- Explain cancellation, downgrade/upgrade timing, invoices/receipts, tax, failed payments, and grandfathered plans carefully.
- Avoid stale plan-tier language if plans are being simplified.

Acceptance criteria:

- Billing docs do not contradict launch pricing.
- Existing customers/grandfathering are handled carefully if mentioned.
- Pricing examples are either current and approved or avoided.

## Mintlify repo implementation plan

The docs cleanup should be run as a docs-as-code workflow inside the actual Mintlify repo, not as one-off copy editing.

### Step 1 — Add Mintlify-native agent context

Inside the docs repo:

```bash
npx skills add https://mintlify.com/docs
```

If the team uses Claude Code, also install/use Mintlify’s Claude plugin/skill where appropriate.

### Step 2 — Add repo-level rules

Add `CLAUDE.md` at repo root. It should define:

- Oviond terminology
- Tone and writing rules
- Forbidden internal/vendor terms
- API endpoint template
- Destructive-action template
- MCP safety rules
- Mintlify component rules
- Validation gates

Add a custom `skill.md` or `.mintlify/skills/` module for Oviond docs work.

### Step 3 — Fix in PR sequence

Recommended PR order:

1. **PR 1: OpenAPI routing/spec cleanup**
   - Remove Plant Store sample.
   - Choose canonical OpenAPI route.
   - Exclude raw JSON from page-style indexing.
   - Validate spec route after deploy.

2. **PR 2: OpenAPI syntax and auth cleanup**
   - Convert `:id` paths to `{id}`.
   - Fix path params.
   - Normalize auth language and examples.
   - Regenerate API pages.

3. **PR 3: Public language cleanup**
   - Remove internal/vendor terms from docs/spec.
   - Rewrite Delete Account, email, media, custom-domain, automations, data, activity-log descriptions.

4. **PR 4: Destructive-action safety pass**
   - Add warning components and consequence sections to all delete/archive/revoke/bulk-delete pages.

5. **PR 5: API endpoint depth pass**
   - Expand top 30 critical endpoint pages with examples, errors, side effects, related endpoints.

6. **PR 6: Product taxonomy and user-doc polish**
   - Add terminology section/page.
   - Rename duplicate/generic H1s.
   - Add client-vs-agency reporting comparison.
   - Expand the few remaining thin user docs.

7. **PR 7: MCP and billing readiness**
   - Tighten MCP claims and safety docs.
   - Align billing docs to launch pricing truth.

### Step 4 — Validate every PR

Use whichever Mintlify CLI is installed in the repo:

```bash
mintlify dev
mintlify validate
```

or:

```bash
mint dev
mint validate
```

Also run custom checks:

- No `Plant Store`, `sandbox.mintlify.com`, `/plants` sample content.
- No colon-style OpenAPI params.
- No avoidable vendor/internal terms.
- No broken internal links.
- No duplicate high-level H1s without context.
- No destructive page without `<Warning>`.
- `llms.txt`, `llms-full.txt`, sitemap, and `.well-known` skill surfaces are clean after deploy.

## Suggested owner checklist for dev team

### Critical before public launch

- [ ] Remove/redirect Plant Store OpenAPI sample.
- [ ] Confirm one canonical OpenAPI spec URL.
- [ ] Remove raw spec files from docs page indexing or create a proper spec page.
- [ ] Convert all OpenAPI `:param` paths to `{param}`.
- [ ] Validate OpenAPI spec.
- [ ] Normalize REST auth wording and examples.
- [ ] Remove public internal/vendor implementation leaks.
- [ ] Add warnings to destructive actions.
- [ ] Rewrite Delete Account public docs/API description.
- [ ] Expand top API endpoint pages beyond generated stubs.

### Important before launch if time allows

- [ ] Add product terminology section/page.
- [ ] Add client-vs-agency report comparison.
- [ ] Fix duplicate/generic H1s.
- [ ] Align billing docs with launch pricing/grandfathering truth.
- [ ] Add MCP safety/revocation page.
- [ ] Add tested MCP client compatibility notes.

### Post-launch but do not ignore

- [ ] Add screenshots/GIFs to top user workflows.
- [ ] Add docs lint checks to CI.
- [ ] Build support-ticket-to-docs feedback loop from Gleap.
- [ ] Add examples for all API endpoint groups.
- [ ] Maintain generated `llms.txt` and agent skill surfaces as first-class launch surfaces.

## Bottom line for Chris

The docs are not a disaster. They are fixable. But the current API/spec layer still has “unfinished generated docs” fingerprints all over it, and the Plant Store spec is a hard no for launch.

If the dev team fixes the spec routing, OpenAPI syntax, auth consistency, internal leaks, destructive-action warnings, and top endpoint examples, the docs can become launch-safe quickly. After that, the user-doc polish and screenshots can continue in parallel without holding the migration/product launch hostage.
