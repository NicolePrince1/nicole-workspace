# Service-account setup for Oviond Google Ads

Use this reference when the task is to make Google Ads API access actually work, not just to write reporting queries.

## Default Oviond account mapping

- Manager account (MCC): `638-795-6297`
- Target Ads account: `290-615-4258`
- Default service account principal: `nicole-workspace@oviond-workspace-cli.iam.gserviceaccount.com`
- Expected Cloud project: `oviond-workspace-cli`
- Current failing project number seen in live tests: `480335022137`

## Best-practice auth path

Prefer a **service account that is added as a real Google Ads user**.

Why:
- keeps automation off a human refresh token
- survives staff changes
- makes daily reporting and maintenance durable
- matches Google's documented service-account workflow for Google Ads

## Current observed state (2026-04-03)

Live checks from this workspace currently show:

- service-account token mint succeeds for `nicole-workspace@oviond-workspace-cli.iam.gserviceaccount.com`
- the backing Cloud project is `oviond-workspace-cli` / `480335022137`
- Google Ads API calls still fail with `PROJECT_DISABLED`
- an attempted domain-wide-delegation-style token mint for `nicole@oviond.com` with the Ads scope returned `unauthorized_client`
- the current runtime does **not** have enough project IAM to inspect or enable `googleads.googleapis.com` directly via Service Usage

Interpretation:
- the present blocker is **not** basic JWT minting
- the current blocker is now on the **Cloud project / Google Ads API permission** side
- the old domain-wide-delegation assumption should not be treated as the live default

## Required setup checklist

### 1) Cloud project

Make sure the Cloud project behind the service-account JSON is the project you want to use for Google Ads API access.

Check:
- `googleads.googleapis.com` is enabled on that project
- the project is active
- the credentials being used by the scripts actually belong to that project
- if Google Ads API Center or Google support requires project/token approval, use the same project consistently
- if the project is definitely correct and still returns `PROJECT_DISABLED`, treat a **fresh Cloud project + fresh credentials** as a serious recovery option, not a last-resort fantasy

### 2) Service account access inside Google Ads

In Google Ads UI:
- sign into the manager account as an admin
- go to **Admin → Access and security**
- add `nicole-workspace@oviond-workspace-cli.iam.gserviceaccount.com`
- grant at least **Standard** access
- if the planned workflow truly needs admin-only actions, upgrade later only if necessary

### 3) Manager/client linkage

Confirm the manager account `6387956297` is linked to client `2906154258`.

For client-account queries, keep the request shape consistent:
- request path customer = client account
- `login-customer-id` = manager account

### 4) Smoke test before any reporting work

Run:

```bash
node /data/.openclaw/workspace/skills/google-ads/scripts/ads_auth_doctor.js --json
```

Healthy state should show:
- developer token present
- access token mint succeeds
- accessible customers call succeeds
- target account query succeeds
- manager → client linkage query succeeds

## Interpreting common failures

### `PROJECT_DISABLED`

Meaning:
- the Cloud project behind the token is not currently allowed to call Google Ads API

Most likely actions:
- enable Google Ads API on the service-account project
- confirm you are using the intended project credentials
- if already enabled, verify the project/token setup in Ads API Center or with Google Ads API support
- if that still fails, create a fresh Cloud project, enable Google Ads API there, mint fresh credentials, add that principal as a Google Ads user, and retry

### `USER_PERMISSION_DENIED`

Meaning:
- the authenticated principal does not have usable access to the target customer in the way the request is being made

Most likely actions:
- add the service account as a user in the manager account
- confirm the manager is actually linked to the client account
- keep `login-customer-id` set to the manager account when querying the client account

## Fallback path

If the service-account route remains blocked after proper setup, fall back to a real OAuth user with offline refresh token. That is a fallback, not the preferred operating model for Oviond.

Force the fallback path with:

```bash
GOOGLE_ADS_AUTH_MODE=oauth-refresh-token
```

Expected fallback env/config:

- `GOOGLE_ADS_OAUTH_CLIENT_ID` or `GOOGLE_ADS_CLIENT_ID`
- `GOOGLE_ADS_OAUTH_CLIENT_SECRET` or `GOOGLE_ADS_CLIENT_SECRET`
- `GOOGLE_ADS_REFRESH_TOKEN`
