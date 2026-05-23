# Oviond Docs Launch QA — 2026-05-23

## Verdict

**Do not launch the docs site as-is.**

The structure is there and some core pages are promising, but the docs still feel generated/incomplete in too many places. The biggest launch risk is the developer/API surface: a public Mintlify sample OpenAPI file is still live, API endpoint pages are mostly raw generated dumps, auth examples are inconsistent, and internal implementation details leak into public docs.

## Scope crawled

- Site: `https://docs.oviond.com`
- Crawl source: `llms.txt`, `sitemap.xml`, direct markdown endpoints, sampled rendered HTML
- Pages crawled: **249**
- Sitemap paths: **248**
- LLM index items: **249**
- API endpoint/reference pages: **146**
- Non-API/user docs pages: **103**
- Internal link unknown targets: **0**
- Generated findings: **444**
  - P0: **1**
  - P1: **207**
  - P2: **236**

Artifacts:

- `pages.json` / `pages.csv` — crawl inventory
- `findings.json` / `findings.csv` — raw findings
- `internal_links.json` — internal link references and checks
- `taxonomy.json` — page distribution by section
- `raw/pages/` — captured markdown for every indexed page
- `raw/html/` — sampled rendered HTML/meta snapshots

## Skills installed/used

Installed and used docs/content audit support:

1. `website-seo` — broad on-page/technical SEO and site audit checklist.
2. `content-quality-auditor` — publish-readiness/content-quality framework.

I also used a custom crawl script for this specific docs site because the site exposes useful `.md`, `llms.txt`, sitemap, and OpenAPI surfaces.

---

# Priority fixes

## P0 — Must fix before launch

### 1. Wrong public OpenAPI spec is live at `/api-reference/openapi.json`

**Evidence**

`https://docs.oviond.com/api-reference/openapi.json` returns a Mintlify sample spec:

- Title: `OpenAPI Plant Store`
- Server: `http://sandbox.mintlify.com`
- Paths: `/plants`, `/plants/{id}`

**Why this matters**

This is the most embarrassing launch blocker. It signals unfinished docs instantly to technical users and can poison generated SDKs, AI docs readers, and integrations.

**Fix**

- Replace `/api-reference/openapi.json` with the real Oviond spec, or remove/hide it entirely.
- Make one canonical OpenAPI URL.
- Redirect stale/sample spec URLs to the canonical spec.
- Verify no Mintlify sample content remains public.

---

## P1 — Should fix before launch

### 2. Canonical API spec routing is confusing

**Evidence**

- The real spec appears at `/api/openapi.json`.
- Endpoint pages embed `yaml /api/openapi.json ...`.
- A separate `/api-reference/openapi.json` serves sample Plant Store content.
- `/api/openapi.json` is indexed like a page but has no H1 because it is raw JSON.

**Fix**

- Choose one canonical spec URL, ideally `/api/openapi.json` or `/openapi.json`.
- Remove the sample `/api-reference/openapi.json` route or redirect it.
- Exclude raw JSON from docs search/sidebar page rendering.
- Add a human page called “OpenAPI Specification” only if needed.

### 3. OpenAPI path templates are invalid/inconsistent

**Evidence**

The real OpenAPI spec mixes colon-style and brace-style path params:

- Colon-style examples: `/v1/clients/:id`, `/v1/users/:id`
- Brace-style examples: `/v1/projects/{id}`

OpenAPI expects `{id}` style.

**Fix**

- Convert all colon params to OpenAPI-valid `{param}` style.
- Ensure every path param has a matching `in: path` parameter schema.
- Rebuild endpoint pages from the corrected spec.

### 4. API endpoint pages are too thin/generated

**Evidence**

- 146 API pages crawled.
- Most endpoint pages are under 80 words.
- Typical page pattern: H1 + one-line description + raw OpenAPI block.

Examples:

- `/api/health/health-check` — 22 words
- `/api/clients/update-client` — 24 words
- `/api/projects/update-project` — 24 words
- `/api/users/get-user` — mostly raw schema dump

**Fix**

Every endpoint should use a consistent template:

1. What it does
2. Method + path
3. Auth requirement
4. Required permissions
5. Path/query/body params
6. Example request: cURL and JS/TS
7. Example success response
8. Common errors
9. Side effects/warnings
10. Related endpoints

### 5. Auth terminology is inconsistent

**Evidence**

- REST docs say both “Bearer token” and “API key”.
- OpenAPI declares `bearerFormat: JWT`.
- `/authentication` uses `Authorization: Bearer ***` but says replace `YOUR_API_KEY`.

**Fix**

Choose public language:

- If these are opaque API keys: say “API key sent as a Bearer token” and remove `bearerFormat: JWT`.
- If they are JWTs: document expiry, refresh, issuance, and token lifecycle.
- Use one placeholder everywhere: `OVIOND_API_KEY`.

### 6. Auth example response conflicts with the actual schema

**Evidence**

`/authentication` example for `/v1/users/me` returns:

```json
{
  "id": "usr_abc123",
  "email": "you@youragency.com",
  "name": "Your Name",
  "accountId": "acc_xyz789"
}
```

The OpenAPI schema returns an envelope:

```json
{
  "success": true,
  "data": {
    "id": "abc123",
    "account_id": "ov:...",
    "fullname": "Jane Smith"
  }
}
```

**Fix**

Align every public example with the real response envelope and field names.

### 7. Internal implementation details leak into public docs

**Evidence**

Public docs/spec mention internal or vendor-specific terms including:

- Supabase
- S3
- SQS
- Resend
- Vercel
- cron scheduler
- `accounts row`
- `users table`
- `account.onboarding = false`
- `user_id`, `resource_type`, `resource_id`
- “upstream API”

**Fix**

Replace with customer-facing language:

- “stored securely” instead of S3
- “email delivery provider” only if vendor matters
- “domain verification service” instead of Vercel
- “scheduled delivery system” instead of cron scheduler
- “onboarding is marked complete” instead of raw flags
- “actor, item, timestamp” instead of database field names

Move engineering details to private runbooks.

### 8. Destructive actions need stronger warnings

**Evidence**

Delete/archive/bulk-delete pages exist, but destructive API docs are often short and implementation-heavy. Delete account exposes backend details while underexplaining user-facing consequences, permissions, confirmation, recovery, and billing impact.

**Fix**

For every destructive endpoint/page:

- Add clear warning block.
- State who can perform it.
- State whether it is soft delete vs permanent.
- State recovery window, if any.
- State billing/subscription impact.
- State what related data is affected.
- Add example error responses.

### 9. User docs are too thin in many core areas

**Evidence**

73 of 103 non-API pages were flagged as thin/short. Very thin examples:

- `/notifications/view` — 87 words
- `/activity-log/overview` — 97 words
- `/archive/view` — 97 words
- `/company/overview` — 98 words
- `/api-keys/delete` — 100 words
- `/themes/delete` — 105 words
- `/templates/delete` — 109 words

**Fix**

Adopt a minimum user-doc page template:

1. What this feature/action is for
2. When to use it
3. Prerequisites/permissions
4. Steps
5. Expected result
6. Edge cases/troubleshooting
7. Related links

Prioritize: account/company, notifications, archive, billing, projects, agency, templates/themes.

### 10. Projects/reports/dashboards/agency taxonomy is confusing

**Evidence**

Duplicate/generic H1s and mixed wording:

- `/projects/list` and `/agency/list` both use “List Projects”.
- `/projects/add` and `/agency/add` both use “Add Project”.
- Agency docs alternate between “agency report”, “account-level project”, and “project”.
- Report/dashboard/project terms are not defined centrally.

**Fix**

Define terms early in Intro/Quickstart:

- **Project** = container
- **Report** = paged project
- **Dashboard** = live single-scroll project
- **Client project** = project inside a client workspace
- **Agency project/report** = account-level project not tied to one client

Rename page H1s/sidebar labels:

- “Add a Client Project”
- “Add an Agency Report”
- “List Client Projects”
- “List Agency Projects”
- “Share a Client Project”
- “Share an Agency Report”

### 11. Agency vs client data-source model needs one clear explanation

**Evidence**

The distinction exists but is scattered:

- `/agency/add` says agency reports use shared integrations.
- `/projects/widgets` says client project widgets use client-connected sources.
- `/agency/widgets` says client-scoped integrations do not appear.

**Fix**

Create or add a comparison table:

| Area | Client report | Agency report |
| --- | --- | --- |
| Scope | One client | Account-level |
| Data sources | Client-linked integrations | Shared/account integrations |
| Best for | Client reporting | Internal rollups/pitch decks |
| Sharing | Client-facing | Internal/stakeholder/prospect |
| Templates | Client templates | Agency-compatible templates |
| Limitations | Cannot mix other clients | Cannot use client-scoped integrations |

### 12. Billing/pricing docs are vague and may become stale quickly

**Evidence**

- `/billing/plans` says plans have tiers and limits but no pricing/examples.
- `/billing/subscription` says cancellation switches to a “limited free tier”.
- Billing paths vary: `Account → Billing`, `Settings → Billing`, etc.
- LTD add-ons are mentioned without context.

**Fix**

Verify current product truth, then document:

- The authoritative place to see live pricing.
- Upgrade/downgrade timing.
- What happens after cancellation.
- Invoice/tax/receipt handling.
- LTD eligibility and where it applies.
- Enterprise language.
- A single UI path for billing.

Important: this needs alignment with the new planned simple client-count pricing so we do not launch stale plan-tier language.

### 13. MCP docs overclaim and underexplain safety

**Evidence**

- `/mcp/connect` says “Every MCP client supports remote HTTP servers with OAuth.” That is not true.
- `/mcp/overview` says 19 categories.
- `/mcp/tools` says 19 categories, but table lists 18.
- Docs say agents can manage the account directly, including destructive actions, but do not explain confirmation, revocation, audit trails, scopes, or permission inheritance deeply enough.

**Fix**

- Change to: “MCP clients that support remote streamable HTTP with OAuth…”
- Add tested clients and versions.
- Reconcile tool category counts from the MCP registry.
- Add an MCP safety page:
  - What agents can/can’t do
  - Permissions model
  - Destructive actions
  - Revoking access
  - Audit logs
  - Recommended first prompts

---

## P2 — Polish/follow-up fixes

### 14. Quickstart says five steps but has six

**Evidence**

`/quickstart` says “publish your first client report in five steps” but renders six steps:

1. Create account
2. Complete onboarding
3. Add client
4. Connect data source
5. Create report
6. Share with client

**Fix**

Either say “six steps” or merge onboarding into account creation.

### 15. Guides promise screenshots/decision points but are mostly text-only

**Evidence**

`/guides/overview` promises screenshots and decision points, but sampled guides are mostly text walkthroughs.

**Fix**

Either add screenshots/GIF placeholders and decision criteria, or change the promise to “step-by-step walkthroughs.”

### 16. Duplicate/generic H1s hurt search and UX

Examples:

- `Overview` appears on REST API, Guides, MCP.
- `Bulk Delete` appears across agency, clients, media, projects.
- `Widgets` appears in agency and client project docs.

**Fix**

Use context-specific H1s:

- “REST API Overview”
- “MCP Server Overview”
- “Guides Overview”
- “Bulk Delete Clients”
- “Bulk Delete Media”
- “Agency Report Widgets”
- “Client Project Widgets”

### 17. Public `.md` pages include LLM index boilerplate

**Evidence**

Every raw `.md` page begins with:

> Documentation Index — Fetch the complete documentation index at llms.txt

**Fix**

If this only appears in LLM-facing markdown endpoints, it is acceptable. If it appears in rendered human pages or pollutes search/snippets, hide/remove it from human output.

### 18. Some copy reads generated/stubby

**Evidence**

Several pages are mechanically correct but underwritten, e.g. one-line steps like “Click Create. Oviond opens the editor.”

**Fix**

Run a style pass:

- Active voice
- Customer-facing terms
- No internal stack names
- Consistent UI paths
- Clear outcomes
- Add short troubleshooting sections where users may get stuck

---

# What is already working

- No broken internal docs links were found in the crawl.
- Sitemap and `llms.txt` mostly agree.
- Intro, Quickstart, Data Sources, Custom Domains, Widgets, and some Guides pages have a solid foundation.
- The docs are not a total rewrite problem. The core job is launch polish: API cleanup, taxonomy, consistency, and depth.

# Recommended launch sequence

## Phase 1 — Same day / launch blocker cleanup

1. Remove/replace Plant Store spec at `/api-reference/openapi.json`.
2. Fix canonical OpenAPI spec route.
3. Convert OpenAPI colon paths to `{param}` paths.
4. Align REST auth terminology and examples.
5. Remove public internal implementation/vendor leaks from docs/spec.
6. Fix the worst duplicate H1s in API/MCP/Projects/Agency.

## Phase 2 — 1–2 day polish pass

1. Expand the 20 most important thin pages.
2. Add Projects/Reports/Dashboards/Agency terminology page/section.
3. Add Client vs Agency report comparison table.
4. Rewrite billing/pricing docs against current launch truth.
5. Add destructive-action warnings.
6. Add MCP safety/permissions/revocation page.

## Phase 3 — Post-launch quality system

1. Add a docs lint check for:
   - duplicate H1s
   - thin pages
   - broken links
   - internal/vendor terms
   - stale sample content
2. Generate endpoint docs from the canonical OpenAPI spec.
3. Add screenshots/GIFs to top workflows.
4. Track docs gaps from support tickets/Gleap.

# Bottom line

The site is close enough structurally, but not close enough reputationally. Fix the API/spec/auth/internal-leak issues first — those are the things that make a technical buyer instantly lose trust. Then clean up taxonomy and expand thin user docs so the product feels deliberate, not half-generated.
