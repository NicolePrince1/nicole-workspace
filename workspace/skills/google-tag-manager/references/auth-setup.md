# GTM Auth Setup

## Recommended model

Use a two-path setup:

1. **Primary:** Google Workspace service-account impersonation of `nicole@oviond.com`
2. **Fallback:** OAuth refresh token for `nicole@oviond.com`

This mirrors the durable pattern used in other Google skills here: automation-first, human-token fallback second.

## Why both paths matter

### Service-account impersonation

Best for:
- repeatable automation
- scheduled audits
- fewer manual reauth events
- sharing one stable auth path across skills

Required pieces:
- the existing Workspace service account remains valid
- Google Tag Manager API is enabled in the backing Google Cloud project
- the service account's domain-wide delegation client is authorized for GTM scopes
- `nicole@oviond.com` has active GTM access at the right account/container level

Recommended scopes:
- `https://www.googleapis.com/auth/tagmanager.readonly`
- `https://www.googleapis.com/auth/tagmanager.edit.containers`
- `https://www.googleapis.com/auth/tagmanager.edit.containerversions`
- `https://www.googleapis.com/auth/tagmanager.publish`
- `https://www.googleapis.com/auth/tagmanager.manage.accounts`
- `https://www.googleapis.com/auth/tagmanager.manage.users` (only if user/permission management is part of the workflow)

Optional but dangerous:
- `https://www.googleapis.com/auth/tagmanager.delete.containers`

Recommendation: skip delete scope by default unless Chris explicitly wants destructive GTM powers enabled.

### OAuth refresh-token fallback

Best for:
- cases where GTM rejects service-account impersonation
- recovery when Workspace DWD scopes drift
- verifying that the actual invited human user can reach the GTM account

Required env vars:
- `GTM_OAUTH_CLIENT_ID`
- `GTM_OAUTH_CLIENT_SECRET`
- `GTM_OAUTH_REFRESH_TOKEN`

## Practical checklist

### 1) Confirm GTM user access

`nicole@oviond.com` must appear in GTM with the right level of access.

Minimum for most work:
- account-level or container-level admin/edit/publish access

Important:
- a pending invite is not enough
- the invite must be accepted and visible as active access

### 2) Enable the Tag Manager API

In the Google Cloud project backing the current Google Workspace service account:
- enable **Tag Manager API**

### 3) Expand domain-wide delegation scopes

In Google Workspace Admin:
- find the OAuth client ID tied to the current service account
- add the GTM scopes listed above

### 4) Add fallback OAuth credentials

Create a Google OAuth client for Nicole's GTM access and store the refresh-token config in OpenClaw env vars.

This fallback is worth it even if service-account auth works.

## Env conventions for this skill

Optional defaults:
- `GTM_AUTH_MODE=auto|service-account|oauth-refresh-token`
- `GTM_ACCOUNT_PATH=accounts/...`
- `GTM_CONTAINER_PATH=accounts/.../containers/...`
- `GTM_WORKSPACE_PATH=accounts/.../containers/.../workspaces/...`

## Operator rule

When auth breaks, run:

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_auth_doctor.js --json
```

Do not guess.
