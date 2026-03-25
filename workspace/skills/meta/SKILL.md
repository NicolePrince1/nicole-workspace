---
name: meta
description: Manage Oviond's Meta presence across Facebook Page, Instagram, and Facebook/Instagram Ads. Use when auditing Meta access, diagnosing reporting issues, pulling ad/account/platform/creative performance, reviewing Page or Instagram activity, planning optimizations, or safely preparing and applying campaign/ad set/ad/social changes.
---

# Meta Skill — Oviond

Operate Oviond's Meta stack with reusable scripts instead of ad hoc curl snippets.

Default Oviond mapping:
- business manager: `287659180931920`
- system user: `61584969418636`
- Facebook Page: `1700329636926546`
- Instagram account: `17841415739993320`
- ad account: `act_286631686227626`
- currency: `ZAR`
- domain: `oviond.com`

## Core workflow

### 1) Diagnose access first

Before trusting reporting or attempting changes, run:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_doctor.py
```

This verifies:
- ad account access
- campaign listing
- recent ads insights
- Page token retrieval
- Facebook Page reads
- Instagram reads
- ad pixel listing

Do not bluff around auth issues. If this fails, read `references/errors.md`.

### 2) Pull reporting with the bundled reporter

Use `meta_report.py` for reusable reporting instead of inventing raw Graph API calls.

Quick examples:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py overview --days 7
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py insights campaign --days 30 --sort spend
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py breakdown campaign publisher_platform --days 30
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py action-types campaign --days 30
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py page-overview --limit 5
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py instagram-overview --limit 5
```

When the KPI is specific, pass the exact action type:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py overview --days 14 --primary-action-type landing_page_view
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py insights ad --days 14 --sort cost_per_primary_action --primary-action-type offsite_conversion.custom.936973485167575
```

If you do not know the conversion key yet, run `action-types` first.

### 3) Prepare changes with preview → validate → apply

All writes should go through `meta_mutate.py` with a JSON spec.

Preview only:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_mutate.py preview ./spec.json
```

Validate when supported:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_mutate.py validate ./spec.json
```

Apply for real:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_mutate.py apply ./spec.json --yes-apply
```

Supported operation families:
- campaign create/update
- ad set create/update
- ad creative create
- ad create/update
- Facebook Page post/photo publish
- Instagram media container + publish

## Scripts

### `scripts/meta_common.py`

Shared helpers for:
- token loading
- Graph API requests
- page-token retrieval
- pagination
- action-array flattening
- date-window handling

### `scripts/meta_doctor.py`

Purpose:
- verify access before reporting or writes
- catch the Page-token issue automatically
- confirm the core Oviond Meta asset map still works

### `scripts/meta_report.py`

Purpose:
- run reusable ad/account/social reporting
- flatten action arrays into analysis-friendly JSON
- compare current period vs previous period
- support platform, audience, geo, and placement breakdowns
- surface custom-conversion action types

### `scripts/meta_mutate.py`

Purpose:
- preview mutation payloads safely
- use server-side `validate_only` where supported
- require explicit opt-in for live writes
- force ads objects to `PAUSED` unless `--allow-active` is passed

## Guardrails

- Diagnose access before trusting data.
- Prefer `meta_report.py` over raw curl for repeatable analysis.
- Treat Page endpoints differently from ad-account endpoints; Page reads/publishes use a page token.
- Do not apply risky writes without preview and explicit approval.
- Keep new ads objects paused until copy, creative, targeting, budget, and tracking are reviewed.
- Be explicit about the denominator when discussing CPA.

## References

- `references/metrics.md` — metric definitions and action-type discipline
- `references/reporting-playbook.md` — repeatable audit/reporting command set
- `references/mutation-patterns.md` — JSON spec shapes and write workflows
- `references/operating-rhythm.md` — daily/weekly/monthly operating cadence
- `references/errors.md` — common failures and how to recover
