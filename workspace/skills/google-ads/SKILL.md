---
name: google-ads
description: Query, diagnose, and operate Oviond's Google Ads account via the Google Ads API using a service-account-first workflow with an explicit OAuth refresh-token fallback. Use when auditing auth blockers, validating access, pulling campaign/search-term/keyword/conversion reporting, preparing optimization plans, or safely applying Google Ads account changes after validation.
---

# Google Ads Skill — Oviond

Operate Oviond's Google Ads account with a **service-account-first** setup and a documented **OAuth refresh-token fallback**.

Default Oviond mapping:
- manager account (MCC): `638-795-6297`
- target ads account: `290-615-4258`
- developer token: env `GOOGLE_ADS_DEVELOPER_TOKEN`
- preferred service-account credential source: env `GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT`

Stable operator rule:
- prefer durable references to the active credential source and account mapping over hard-coding a specific GCP project name or service-account email unless a task explicitly requires that level of diagnostics

## Core workflow

### 1) Diagnose auth first

Before trusting any report or planning writes, run:

```bash
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_auth_doctor.js --json
```

If auth is blocked, read:
- `references/service-account-setup.md`
- `references/errors.md`

Do not pretend reporting works if the auth doctor fails.

Optional auth-mode override when testing fallback auth:

```bash
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_auth_doctor.js --auth-mode oauth-refresh-token --json
```

### 2) Run reporting queries

Use the query runner for GAQL reporting. It uses `searchStream` so larger report pulls do not require manual pagination.

Inline query:

```bash
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_query.js "SELECT campaign.name, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_7_DAYS"
```

Query from file:

```bash
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_query.js --file ./query.sql
```

For reusable query patterns, read `references/reporting-queries.md`.

### 3) Plan and execute maintenance

For optimization cadence and guardrails, read `references/operating-rhythm.md`.

Default mutation flow:
1. inspect with reporting queries
2. prepare mutation JSON
3. run validate-only first
4. review output
5. only then apply a real write if approved

Example:

```bash
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_mutate.js campaigns ./pause-campaign.json --validate-only
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_mutate.js campaigns ./pause-campaign.json --apply
```

## Scripts

### `ads_auth_doctor.js`

Purpose:
- verify developer token presence
- mint an access token from the selected auth mode
- inspect the backing Cloud project when using a service account
- test `customers:listAccessibleCustomers`
- test a target account query
- test manager → client linkage query

### `ads_query.js`

Purpose:
- run GAQL queries against the default Oviond Ads account
- return structured JSON for analysis or downstream automation

Helpful flags:
- `--file ./query.sql`
- `--customer-id <id>`
- `--login-customer-id <id>`
- `--format pretty`

### `ads_mutate.js`

Purpose:
- run mutate operations safely
- default to validate-only mode
- require explicit `--apply` for real writes

## Guardrails

- prefer the service-account path over human refresh tokens unless the service-account route proves impossible after proper setup
- treat `GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT` as the canonical credential entry point unless a specific task proves otherwise
- if you need the fallback path, force it explicitly with `GOOGLE_ADS_AUTH_MODE=oauth-refresh-token`
- do not assume Google Workspace-style domain-wide delegation is the right model here
- do not bake transient GCP incident details into the main skill instructions; keep this file stable and move volatile auth history into `MEMORY.md` or targeted troubleshooting notes
- do not apply risky writes without validation
- do not call the account healthy until the auth doctor passes end-to-end
- for high-impact changes, summarize the intended changeset and the business reason before applying

## References

- `references/service-account-setup.md` — setup workflow and targeted auth troubleshooting
- `references/reporting-queries.md` — reusable GAQL query library
- `references/operating-rhythm.md` — daily/weekly/monthly optimization cadence
- `references/errors.md` — operator translation for common failures
