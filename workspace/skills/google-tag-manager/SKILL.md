---
name: google-tag-manager
description: Audit, diagnose, and manage Oviond's Google Tag Manager account, containers, workspaces, tags, triggers, variables, versions, and publishing flow. Use when inspecting GTM setup, confirming which domains or tags are sending data, setting up auth, exporting container state, preparing safe GTM changes, or applying controlled Tag Manager API writes.
---

# Google Tag Manager Skill — Oviond

Operate Oviond's Google Tag Manager setup with a durable **service-account-impersonation primary path** and an explicit **OAuth refresh-token fallback**.

Default rule:
- prefer impersonating `nicole@oviond.com` through the existing Google Workspace service account once Tag Manager scopes are granted
- keep a human OAuth refresh-token fallback configured so GTM work does not die when domain-wide delegation or scope grants drift

## Core workflow

### 1) Diagnose auth first

Before trusting any GTM audit or planning writes, run:

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_auth_doctor.js --json
```

If auth is blocked, read:
- `references/auth-setup.md`
- `references/api-recipes.md`

Do not pretend GTM management works if the auth doctor fails.

Optional auth-mode override when testing fallback auth:

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_auth_doctor.js --auth-mode oauth-refresh-token --json
```

### 2) Discover the GTM structure

List visible accounts, containers, and workspaces:

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_discover.js
```

Use `--json` when another script or agent needs the structure programmatically.

### 3) Audit the current setup

Export a structured audit for a container or workspace:

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_audit.js --container-path accounts/123456/containers/654321
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_audit.js --workspace-path accounts/123456/containers/654321/workspaces/7 --json
```

For a repeatable audit lens, read `references/audit-checklist.md`.

### 4) Prepare and apply controlled changes

Use the generic request runner for API writes that are not yet wrapped in a narrower helper:

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js GET /accounts
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js POST /accounts/123456/containers/654321/workspaces ./workspace.json --apply
```

Default mutation flow:
1. inspect the current state with `gtm_discover.js` or `gtm_audit.js`
2. prepare the request body in a file
3. run the same request without `--apply` to verify the target and payload
4. review the output and intended blast radius
5. only then rerun with `--apply`

### 5) Publish safely

Prefer workspace-based changes over editing the default workspace blindly.

Before publishing:
1. confirm the exact workspace path
2. audit tags, triggers, variables, and affected host filters
3. create or review a container version
4. publish only after the intended diff is clear

Use `references/api-recipes.md` for common request patterns, including workspace creation and version publishing.

## Scripts

### `gtm_auth_doctor.js`

Purpose:
- verify which auth mode is usable
- test `accounts` visibility
- optionally test account, container, or workspace paths when env defaults are configured
- explain the likely fix when service-account or refresh-token auth is blocked

### `gtm_discover.js`

Purpose:
- list accessible GTM accounts
- list containers under each account
- list workspaces under each container
- produce stable paths for later scripts and env defaults

### `gtm_audit.js`

Purpose:
- export a container or workspace summary
- list tags, triggers, variables, folders, templates, and built-in variables when available
- surface quick counts and common Google-tag clues for analysis

### `gtm_request.js`

Purpose:
- run controlled raw Tag Manager API requests
- require explicit `--apply` for non-GET writes
- support request bodies from inline JSON or file path

## Guardrails

- prefer the service-account impersonation path once it is correctly scoped, because it is the cleanest durable automation path in this workspace
- keep an OAuth refresh-token fallback configured anyway, because GTM access is user-centric and fallback resilience matters
- do not assume a GTM invitation email alone is enough; the invited user must be active, not pending
- do not publish or mutate live containers without first auditing the affected workspace or container state
- do not take delete actions casually; GTM has enough rope to hang reporting and conversion measurement in one bad publish
- for high-impact GTM changes, summarize exactly what will fire less, fire more, or stop firing before applying
- if the goal is to stop a hostname from sending GA4 data, fix the GTM firing conditions or the site-level tag injection, not just GA4 reporting views

## References

- `references/auth-setup.md` — robust auth model and required setup
- `references/audit-checklist.md` — repeatable GTM audit lens
- `references/api-recipes.md` — common API request patterns
