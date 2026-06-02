# GTM Auth Setup

## Current working model

Use the existing Google Workspace service-account impersonation path:

- token helper: `/data/.openclaw/secrets/gws-token.js`
- impersonated user: `nicole@oviond.com`
- GTM read scope used by default: `https://www.googleapis.com/auth/tagmanager.readonly`
- write-capable helper scripts request broader GTM scopes only when a non-GET request is explicitly run with `--apply`

This mirrors the durable Google Workspace pattern used elsewhere in Nicole's workspace and avoids a separate OAuth refresh-token setup for GTM.

## Required pieces

- Google Tag Manager API enabled in the backing Google Cloud project
- the Google Workspace service account remains valid
- domain-wide delegation includes the needed GTM scopes
- `nicole@oviond.com` has active GTM access at the relevant account/container level

Recommended scopes:

- `https://www.googleapis.com/auth/tagmanager.readonly`
- `https://www.googleapis.com/auth/tagmanager.edit.containers`
- `https://www.googleapis.com/auth/tagmanager.edit.containerversions`
- `https://www.googleapis.com/auth/tagmanager.publish`
- `https://www.googleapis.com/auth/tagmanager.manage.accounts`
- `https://www.googleapis.com/auth/tagmanager.manage.users` only if user/permission management is explicitly needed

Avoid by default:

- `https://www.googleapis.com/auth/tagmanager.delete.containers`

## Practical checklist

### 1) Confirm GTM user access

`nicole@oviond.com` must appear in GTM with active access. A pending invite is not enough.

Minimum for most work:

- account-level or container-level read/edit access for audits
- publish access only when publishing is explicitly required

### 2) Enable the Tag Manager API

In the Google Cloud project backing the current Google Workspace service account, enable **Tag Manager API**.

### 3) Confirm domain-wide delegation scopes

In Google Workspace Admin, find the OAuth client ID tied to the current service account and confirm the GTM scopes above are granted.

## Operator rule

When auth breaks, run:

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_auth_doctor.js --json
```

Do not guess. If this fails, fix Google Workspace service-account impersonation, DWD scopes, API enablement, or Nicole's GTM user access before attempting GTM work.
