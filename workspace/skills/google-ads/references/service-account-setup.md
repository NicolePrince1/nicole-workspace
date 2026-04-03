# Service-account setup for Oviond Google Ads

Use this reference when the task is to make Google Ads API access actually work, not just to write reporting queries.

## Current production mapping

- Manager account (MCC): `638-795-6297`
- Target Ads account: `290-615-4258`
- Preferred credential source: OpenClaw Envar `GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT`
- Current production GCP project: `northern-card-492208-q6`
- Current production service-account principal: `nicole-google-ads@northern-card-492208-q6.iam.gserviceaccount.com`

## Live production state (2026-04-03)

The recovered production path is working.

Live checks succeeded for:
- access-token mint
- `customers:listAccessibleCustomers`
- target-account query against client `2906154258`
- manager → client linkage query

Practical interpretation:
- Google Ads production API access is operational again
- the service-account-first architecture remains the preferred default
- the earlier `PROJECT_DISABLED` issue belonged to the retired old project path, not to the overall operating model
- limited Cloud-project introspection permissions may still affect some diagnostics, but they are non-blocking for actual Google Ads API usage

## Best-practice auth path

Prefer a **service account that is added as a real Google Ads user**.

Why:
- keeps automation off a human refresh token
- survives staff changes
- makes daily reporting and maintenance durable
- matches Google Ads' intended service-account workflow

## Active setup checklist

### 1) Credential source

Make sure the scripts are using the current production service-account JSON via:
- `GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT`

Do not treat old local project references as the live default unless a specific historical debug task requires them.

### 2) Cloud project

For the active production project:
- confirm `googleads.googleapis.com` is enabled
- confirm the service-account JSON actually belongs to the intended production project
- keep the project/token pairing consistent if Google Ads API Center or support review is ever needed

### 3) Service account access inside Google Ads

In Google Ads UI:
- sign into the manager account as an admin
- go to **Admin → Access and security**
- confirm `nicole-google-ads@northern-card-492208-q6.iam.gserviceaccount.com` is present
- keep at least **Standard** access unless a task truly requires more

### 4) Manager/client linkage

Confirm the manager account `6387956297` is linked to client `2906154258`.

For client-account queries, keep the request shape consistent:
- request path customer = client account
- `login-customer-id` = manager account

### 5) Smoke test before any reporting work

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

## Interpreting common failures now

### `USER_PERMISSION_DENIED`

Meaning:
- the authenticated principal does not have usable access to the target customer in the way the request is being made

Most likely actions:
- confirm the current production service account is still a user in the manager account
- confirm the manager is still linked to the client account
- keep `login-customer-id` set to the manager account when querying the client account

### Auth-doctor passes token mint but customer queries fail

Meaning:
- the credential itself is valid, but Ads-side access, manager/client linkage, or request shape is wrong

Most likely actions:
- confirm the active service account matches the production principal
- re-check manager/client linkage
- verify request customer vs `login-customer-id`

### Historical `PROJECT_DISABLED` context

This is now a **historical** troubleshooting path tied to the retired project `oviond-workspace-cli` / `480335022137`.

Only revisit that line of investigation if a task explicitly asks for historical root-cause analysis.

## Fallback path

If the service-account route becomes unusable again after proper setup, fall back to a real OAuth user with offline refresh token. That is a fallback, not the preferred operating model for Oviond.

Force the fallback path with:

```bash
GOOGLE_ADS_AUTH_MODE=oauth-refresh-token
```

Expected fallback env/config:

- `GOOGLE_ADS_OAUTH_CLIENT_ID` or `GOOGLE_ADS_CLIENT_ID`
- `GOOGLE_ADS_OAUTH_CLIENT_SECRET` or `GOOGLE_ADS_CLIENT_SECRET`
- `GOOGLE_ADS_REFRESH_TOKEN`
