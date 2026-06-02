# Oviond Docs Launch Audit — 2026-06-02

Site audited: https://docs.oviond.com/introduction  
Compared against: `research/docs-audit-2026-05-25/` and `research/docs-audit-2026-05-23/`  
Audit run: 2026-06-02 08:52 UTC

## Verdict

Do **not** call the docs perfect yet.

The user-facing docs shell is healthier than the API layer: the Introduction, Quickstart, Authentication, API overview, and MCP overview render and read coherently. The docs have the right broad product story: white-label reporting, clients, dashboards/reports, data sources, custom domains, automations, API, and MCP.

But the major launch blockers from last week are still present. The public docs still expose Mintlify’s Plant Store sample OpenAPI spec, the real OpenAPI spec still uses invalid colon-style path parameters, generated API endpoint pages are still thin, internal implementation/vendor language still leaks publicly, and destructive actions still lack consistent warning treatment.

## Fresh crawl scope

- Discovery sources: `llms.txt`, `sitemap.xml`, `robots.txt`, markdown endpoints, rendered HTML fetches, OpenAPI JSON surfaces.
- URLs discovered: 249
- `llms.txt` URLs: 249
- `sitemap.xml` URLs: 248
- Difference: `llms.txt` includes `https://docs.oviond.com/api/openapi.json`; sitemap does not.
- API/developer-classified pages: 155
- Non-API/user docs pages: 94
- Internal broken links found after filtering Cloudflare email-obfuscation links: 0
- External Oviond/app/docs links checked: no failing important external links found.

## Fresh findings summary

Current automated findings: 490

- P0: 3
- P1: 238
- P2: 249

Main categories:

- Live sample OpenAPI spec: 1
- Raw OpenAPI JSON indexed as docs markdown and returning 404: 1
- Invalid OpenAPI colon-path parameter pattern: 30 paths, grouped as 1 P0 finding
- Thin pages: 162 findings; 152 pages still under 120 words
- Internal/vendor leaks: 44 page findings plus OpenAPI-wide leak finding
- Destructive pages missing warning components: 41
- API pages lacking real examples/use-case guidance: still widespread; OpenAPI analysis found 130/144 operations appear to lack examples
- Weak/short meta descriptions: 232 P2 findings
- Introduction too light for a perfect launch entry point: 237 words

## What has been done since last week

Good news first: the basics are stable.

1. The docs site is live and crawlable.
   - `https://docs.oviond.com/introduction` returns 200.
   - `llms.txt`, `sitemap.xml`, and `robots.txt` return 200.
   - The public docs index is consistent enough for AI/docs readers to discover the site.

2. The main Introduction page is coherent.
   - It has a clear H1, a clean product summary, a useful card group, and a simple “How Oviond works” step flow.
   - It links readers to Quick Start, Authentication, Data Sources, Custom Domains, Projects, and API Reference.

3. The Quickstart page is meaningfully better than a placeholder.
   - It gives a practical agency flow: create account, complete onboarding, add client, connect data source, create report, share with client.

4. The API overview and Authentication pages exist and render.
   - They explain base URL, Bearer/API key usage, status codes, and key management.

5. MCP positioning exists.
   - `/mcp/overview` gives a real AI-agent story and routes to connect/auth/tools.

## What has not been fixed

These are materially unchanged from the 2026-05-25 audit.

### P0 — Mintlify Plant Store sample spec is still public

`https://docs.oviond.com/api-reference/openapi.json` still returns:

- title: `OpenAPI Plant Store`
- server: `http://sandbox.mintlify.com`
- paths: `/plants`, `/plants/{id}`

This is still the single most embarrassing launch issue. It can poison AI readers, generated clients, and technical buyer trust.

### P0 — Real OpenAPI spec still has invalid colon-style paths

`https://docs.oviond.com/api/openapi.json` returns the real Oviond Backend API spec, but 30 paths still use colon parameters instead of OpenAPI `{param}` syntax.

Examples:

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

Acceptance criterion: zero paths matching `/:param` in the OpenAPI file.

### P0/P1 — Raw OpenAPI routing is still messy

Current spec route status:

- `/api-reference/openapi.json`: 200, but wrong Plant Store sample
- `/api/openapi.json`: 200, real Oviond spec
- `/openapi.json`: 404
- `/api/openapi.json.md`: 404
- `/api-reference/openapi.json.md`: 404

The real raw spec is still appearing in `llms.txt` as a docs URL, but it has no markdown page equivalent.

### P1 — API endpoint pages are still generated-looking

Example: `/api/clients/update-client` is basically:

- H1: Update Client
- one-line description: “Update a client”
- raw OpenAPI block

It does not explain when to use the endpoint, what fields matter, safe examples, common errors, side effects, or related endpoints.

### P1 — Auth language still needs one canonical truth

Docs say API key as Bearer token, while the OpenAPI security scheme still declares:

```json
{
  "type": "http",
  "scheme": "bearer",
  "bearerFormat": "JWT"
}
```

If these are opaque API keys, remove `bearerFormat: JWT` and standardize on `OVIOND_API_KEY` everywhere. If they are real JWTs, document expiry, refresh, revocation, and lifecycle.

### P1 — Public docs still leak implementation/vendor language

Examples found in live pages/spec:

- Supabase
- S3
- SQS
- Resend
- Vercel
- Stripe
- cron scheduler
- accounts row
- users table
- upstream API
- raw_data
- client_integrations
- resource_type/resource_id/user_id

Example bad page: `/api/account/delete-account` says it deletes users table rows, purges S3 files, cancels Stripe, and deletes Supabase Auth users. That is internal runbook language, not public customer-facing documentation.

### P1 — Destructive actions still lack warning treatment

41 destructive/risky pages still lack a Mintlify `<Warning>` component. These include account delete, archive/delete endpoints, bulk deletes, key revocation, custom data deletion, integration deletion, media deletion, template/theme deletion, and user removal.

### P2 — Meta descriptions are too short across the site

232 pages have short/weak descriptions. This is not a launch blocker by itself, but it hurts search snippets, docs polish, and AI-reader summaries.

## Introduction page assessment

Current Introduction page: good foundation, not perfect.

What works:

- Clear H1 and purpose.
- Good summary: white-label marketing reporting for agencies.
- Good primary routing cards.
- Good simple workflow: connect data sources → build reports → apply brand → automate delivery.
- No obvious internal/vendor leaks on the page itself.

What is missing for “perfect”:

1. Stronger segmentation by reader intent.
   - “I’m an agency operator setting up reports” → Quickstart.
   - “I’m configuring brand/client delivery” → White label/custom domains/automations.
   - “I’m a developer” → API/auth/openapi.
   - “I’m using AI agents” → MCP.

2. More product specificity.
   - Define client, project/report/dashboard, data source, template, automation, custom domain, API key, and MCP in plain English.
   - Right now the Introduction assumes the user already understands the product model.

3. Better “first 10 minutes” path.
   - The page should make the shortest successful path feel obvious: create account → add client → connect data source → create report → share/automate.

4. Stronger agency trust language.
   - Explain that the docs cover branded delivery, scheduled reports, permissions/team workflows, and client-ready reporting.

5. A launch-quality visual/product cue.
   - Add one clean screenshot or product-preview graphic near the top if Mintlify layout allows it.

6. Clearer developer/API warning until API docs are fixed.
   - Do not over-promote API Reference from the intro until the OpenAPI sample/colon-path/API-page quality issues are fixed.

## Recommended launch fix order

### Same day blockers

1. Remove or redirect `/api-reference/openapi.json` so Plant Store is gone.
2. Pick one canonical OpenAPI URL and remove raw spec files from docs-page indexing.
3. Convert all OpenAPI `/:param` paths to `{param}`.
4. Regenerate endpoint pages from the corrected spec.
5. Standardize API auth wording and examples.

### Next polish pass

6. Add warning components and consequence language to all destructive actions.
7. Rewrite public/internal leaks into customer-facing language.
8. Upgrade the top 25 API endpoint pages with real examples and common errors.
9. Add a glossary/product model page and link it from Introduction.
10. Expand Introduction into a better launch doorway with audience-routing and first-10-minutes guidance.

### Final “perfect” pass

11. Bring meta descriptions to 110–160 chars where practical.
12. Add screenshots/product previews to Introduction, Quickstart, white-label/custom domains, automations, and data-source pages.
13. QA mobile/desktop visually after Chromium/browser dependencies are available. I attempted Playwright screenshots, but the local headless browser cannot launch in this container because `libglib-2.0.so.0` is missing.
14. Re-run crawl and acceptance checks after fixes.

## Acceptance checklist for launch-ready docs

- [ ] `Plant Store`, `sandbox.mintlify.com`, `/plants`, and `NewPlant` return zero public matches.
- [ ] One canonical OpenAPI spec URL is documented.
- [ ] `/api-reference/openapi.json` redirects to the canonical Oviond spec or is intentionally gone.
- [ ] No raw JSON spec URL appears as a broken markdown docs page.
- [ ] OpenAPI has zero colon-style path params.
- [ ] OpenAPI security scheme matches actual auth type.
- [ ] Authentication examples use one placeholder: `OVIOND_API_KEY`.
- [ ] `/authentication` response example matches the real `/v1/users/me` envelope and field names.
- [ ] Top API pages include cURL + JS/TS examples, common errors, side effects, and related endpoints.
- [ ] All destructive docs have warning components.
- [ ] Public docs remove internal/vendor implementation language unless truly necessary.
- [ ] Introduction explains who the docs are for, where to start, and how Oviond’s product model works.
- [ ] Pricing/billing docs match the current public pricing strategy before launch.
- [ ] Final crawl reports zero P0s.

## Artifacts

- `summary.json` — crawl/spec summary
- `findings.json` and `findings.csv` — raw findings
- `pages.json` and `pages.csv` — page inventory and page-level metadata
- `internal_links.json` — internal link references and checks
- `external_link_checks.json` — important external link checks
- `raw/md/` — captured markdown pages
- `raw/json/` — captured OpenAPI/spec route responses
- `scripts/crawl_docs_2026_06_02.py` — repeatable audit script
