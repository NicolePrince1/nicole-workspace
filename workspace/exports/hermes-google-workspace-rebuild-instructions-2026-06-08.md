# Hermes / New Nicole — Google Workspace Rebuild Instructions

**Prepared for:** Chris Irwin, Hermes, and the new Nicole agent  
**Prepared by:** Nicole Prince  
**Date:** 2026-06-08  
**Purpose:** Recreate the exact Google Workspace connection pattern that worked for Nicole, using the current setup as the template.  
**Security note:** This document intentionally excludes private keys, access tokens, and raw credential JSON. It includes architecture, identifiers, scopes, file paths, validation commands, and implementation patterns.

---

## 1. Executive summary

Nicole’s working Google Workspace access was built the **proper server-side way**:

> **Google Cloud service account + Google Workspace domain-wide delegation + impersonation of `nicole@oviond.com`.**

This is the model Hermes/new Nicole should recreate or adapt.

It is not a normal user OAuth refresh-token setup. It is not a “robot Drive” setup where the service account owns isolated files. The service account mints OAuth access tokens **as Nicole** using the JWT bearer flow and the `sub` claim:

```text
sub: nicole@oviond.com
```

That is what lets the agent work in Nicole’s real Workspace context:

- Gmail for `nicole@oviond.com`
- Calendar for `nicole@oviond.com`
- Drive as Nicole
- Docs / Sheets as Nicole
- Contacts / Tasks where scoped
- Related Google APIs where Nicole has access and scopes are granted

Hermes should use this exact architecture as the template, then implement it cleanly in the new environment.

---

## 2. Working model at a glance

### Google Cloud service account

From the current working credential metadata:

```text
Service account email: nicole-workspace@oviond-workspace-cli.iam.gserviceaccount.com
Service account client ID: 100236162289445083006
Google Cloud project ID: oviond-workspace-cli
Token endpoint: https://oauth2.googleapis.com/token
Impersonated Workspace user: nicole@oviond.com
```

Do **not** copy the private key into docs or chat. The private key lives only in the secure credential file / secret store.

### Current credential/helper paths

Current environment stores Google Workspace helper material under:

```text
/data/.openclaw/secrets/
```

Known files:

```text
/data/.openclaw/secrets/gws-service-account.json
/data/.openclaw/secrets/gws-token.js
/data/.openclaw/secrets/gws-analytics-token.js
/data/.openclaw/secrets/gws-gsc-token.js
/data/.openclaw/secrets/gws-ads-token.js
```

Important:

- `gws-service-account.json` is secret and must never be committed.
- Token helper scripts are implementation examples, but if copied, check that they do not expose private key material.
- In a rebuilt environment, prefer secret storage / Envars / vault-style config over tracked files.

### Current successful live verification

On 2026-06-08, the current setup successfully minted tokens and verified:

Gmail profile:

```json
{
  "emailAddress": "nicole@oviond.com",
  "messagesTotal": 121,
  "threadsTotal": 108
}
```

Calendar list:

```json
{
  "items": [
    {
      "id": "nicole@oviond.com",
      "summary": "nicole@oviond.com",
      "accessRole": "owner"
    }
  ]
}
```

Drive about:

```json
{
  "user": {
    "displayName": "Nicole Prince",
    "emailAddress": "nicole@oviond.com"
  }
}
```

This proves the working setup impersonates Nicole correctly for Gmail, Calendar, and Drive.

---

## 3. Why this architecture matters

A plain service account can access only resources explicitly shared with the service account or owned by the service account. That is not enough for Nicole.

Nicole needs real Workspace access as a user:

- read/send/manage Gmail as `nicole@oviond.com`
- create/read calendar events in Nicole’s calendar
- create/upload/read Drive files in Nicole’s Drive context
- operate Docs, Sheets, Contacts, Tasks
- use Google APIs where Nicole has user-level access, e.g. GSC, GA4, GTM if configured

Domain-wide delegation solves this by allowing a trusted service account to impersonate a Workspace user for approved scopes.

Key distinction:

```text
Bad / limited model:
service account acts as itself → robot-owned Drive, not Nicole’s Workspace

Correct model:
service account uses DWD + sub=nicole@oviond.com → acts as Nicole for approved scopes
```

Hermes should preserve this distinction. If the new setup “works” but Drive files are owned by the service-account robot, it is not the same working setup.

---

## 4. Required Google-side setup

### Step 1 — Google Cloud project

Use the existing project if still valid, or recreate equivalent:

```text
Project ID: oviond-workspace-cli
```

Required APIs depend on desired tools. At minimum enable:

- Gmail API
- Google Calendar API
- Google Drive API
- Google Docs API
- Google Sheets API
- People API / Contacts-related API as needed
- Google Tasks API if Tasks are needed

Additional APIs used by other Nicole skills:

- Google Analytics Data API
- Google Analytics Admin API, where applicable
- Google Search Console API / Webmasters API
- Google Tag Manager API
- Google Ads API, if using the Ads service account path

### Step 2 — Service account

Existing service account metadata:

```text
Name/email: nicole-workspace@oviond-workspace-cli.iam.gserviceaccount.com
Client ID: 100236162289445083006
```

Required property:

- **Domain-wide delegation must be enabled** on the service account.

If rebuilding from scratch:

1. Create a service account in Google Cloud.
2. Enable **Domain-wide delegation** for that service account.
3. Create a fresh JSON key.
4. Store the JSON key only in secure storage.
5. Record the service account’s **OAuth client ID**. This is not the email; it is the numeric client ID used in Google Workspace Admin DWD.

### Step 3 — Google Workspace Admin domain-wide delegation

In Google Workspace Admin:

```text
Security → Access and data control → API controls → Domain-wide delegation
```

Add or edit the OAuth client ID:

```text
Client ID: 100236162289445083006
```

Authorize scopes. The exact final scope set can be tightened, but this is the known useful starter set for Nicole’s Workspace work:

```text
https://www.googleapis.com/auth/gmail.readonly,
https://www.googleapis.com/auth/gmail.modify,
https://www.googleapis.com/auth/gmail.send,
https://www.googleapis.com/auth/calendar,
https://www.googleapis.com/auth/drive,
https://www.googleapis.com/auth/documents,
https://www.googleapis.com/auth/spreadsheets,
https://www.googleapis.com/auth/contacts,
https://www.googleapis.com/auth/contacts.readonly,
https://www.googleapis.com/auth/tasks
```

The current `gws-token.js` default scopes are:

```text
https://www.googleapis.com/auth/gmail.modify
https://www.googleapis.com/auth/gmail.send
https://www.googleapis.com/auth/calendar
https://www.googleapis.com/auth/drive
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/documents
https://www.googleapis.com/auth/contacts.readonly
https://www.googleapis.com/auth/tasks
```

If Gmail read operations fail, make sure Gmail read/modify scopes are authorized.

### Step 4 — User being impersonated

The impersonated user is:

```text
nicole@oviond.com
```

The user must exist and be active in Google Workspace.

---

## 5. Token helper pattern

The working helper uses the OAuth 2.0 JWT bearer flow manually in Node.js.

### Core JWT claims

The important payload fields are:

```json
{
  "iss": "SERVICE_ACCOUNT_EMAIL",
  "sub": "nicole@oviond.com",
  "scope": "SPACE_SEPARATED_SCOPES",
  "aud": "https://oauth2.googleapis.com/token",
  "iat": CURRENT_UNIX_SECONDS,
  "exp": CURRENT_UNIX_SECONDS_PLUS_3600
}
```

The JWT is signed with the service account private key using RS256.

Then POST to:

```text
https://oauth2.googleapis.com/token
```

With body:

```text
grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=<SIGNED_JWT>
```

The response contains an `access_token`.

### Current helper behavior

Current helper:

```bash
node /data/.openclaw/secrets/gws-token.js
```

Prints an access token for default Workspace scopes.

It also accepts scope overrides:

```bash
node /data/.openclaw/secrets/gws-token.js gmail.modify
node /data/.openclaw/secrets/gws-token.js drive
node /data/.openclaw/secrets/gws-token.js calendar
node /data/.openclaw/secrets/gws-token.js 'https://www.googleapis.com/auth/drive'
```

The helper expands non-URL scope names like `drive` to:

```text
https://www.googleapis.com/auth/drive
```

### Minimal pseudocode

```js
const creds = readJsonFromSecretStore();
const scopes = [
  'https://www.googleapis.com/auth/gmail.modify',
  'https://www.googleapis.com/auth/gmail.send',
  'https://www.googleapis.com/auth/calendar',
  'https://www.googleapis.com/auth/drive',
  'https://www.googleapis.com/auth/spreadsheets',
  'https://www.googleapis.com/auth/documents',
  'https://www.googleapis.com/auth/contacts.readonly',
  'https://www.googleapis.com/auth/tasks'
];

const payload = {
  iss: creds.client_email,
  sub: 'nicole@oviond.com',
  scope: scopes.join(' '),
  aud: 'https://oauth2.googleapis.com/token',
  iat: now,
  exp: now + 3600
};

const jwt = signRs256(header, payload, creds.private_key);
const accessToken = postJwtBearer(jwt);
```

Hermes can implement this with Google auth libraries instead of hand-rolled JWT signing, but the behavior must be equivalent: service account + domain-wide delegation + subject impersonation.

---

## 6. Exact validation commands

Use these read-only checks after rebuilding.

### 6.1 Mint a generic token

```bash
node /data/.openclaw/secrets/gws-token.js | head -c 20
```

Expected:

- non-empty output
- no JSON error

If using a new helper path, adjust the path.

### 6.2 Gmail profile check

```bash
TOKEN=$(node /data/.openclaw/secrets/gws-token.js gmail.modify)
curl -sS \
  -H "Authorization: Bearer $TOKEN" \
  'https://gmail.googleapis.com/gmail/v1/users/me/profile'
```

Expected user:

```json
{
  "emailAddress": "nicole@oviond.com"
}
```

If it returns service-account identity, the impersonation is wrong.

### 6.3 Calendar check

```bash
TOKEN=$(node /data/.openclaw/secrets/gws-token.js calendar)
curl -sS \
  -H "Authorization: Bearer $TOKEN" \
  'https://www.googleapis.com/calendar/v3/users/me/calendarList?maxResults=3&fields=items(id,summary,accessRole)'
```

Expected:

```json
{
  "items": [
    {
      "id": "nicole@oviond.com",
      "summary": "nicole@oviond.com",
      "accessRole": "owner"
    }
  ]
}
```

### 6.4 Drive identity check

```bash
TOKEN=$(node /data/.openclaw/secrets/gws-token.js drive)
curl -sS \
  -H "Authorization: Bearer $TOKEN" \
  'https://www.googleapis.com/drive/v3/about?fields=user(emailAddress,displayName),storageQuota'
```

Expected:

```json
{
  "user": {
    "displayName": "Nicole Prince",
    "emailAddress": "nicole@oviond.com"
  }
}
```

### 6.5 Drive upload smoke test

Use a harmless Markdown file:

```bash
cat > /data/.openclaw/workspace/exports/gws-smoke-test.md <<'EOF'
# Google Workspace smoke test

If this file exists, Nicole can upload to Drive as nicole@oviond.com.
EOF

TOKEN=$(node /data/.openclaw/secrets/gws-token.js drive)
cat > /data/.openclaw/workspace/exports/gws-smoke-metadata.json <<'EOF'
{"name":"gws-smoke-test.md","mimeType":"text/markdown"}
EOF

curl -sS -X POST \
  'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,name,webViewLink,webContentLink,owners(emailAddress,displayName)' \
  -H "Authorization: Bearer $TOKEN" \
  -F 'metadata=@/data/.openclaw/workspace/exports/gws-smoke-metadata.json;type=application/json;charset=UTF-8' \
  -F 'file=@/data/.openclaw/workspace/exports/gws-smoke-test.md;type=text/markdown'
```

Expected owner/user should reflect Nicole/Workspace context, not a robot-only account.

### 6.6 Share file with Chris

```bash
FILE_ID="<uploaded file id>"
TOKEN=$(node /data/.openclaw/secrets/gws-token.js drive)
curl -sS -X POST \
  "https://www.googleapis.com/drive/v3/files/${FILE_ID}/permissions?sendNotificationEmail=false&fields=id,type,role,emailAddress" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"type":"user","role":"reader","emailAddress":"chris@oviond.com"}'
```

Expected:

```json
{
  "type": "user",
  "emailAddress": "chris@oviond.com",
  "role": "reader"
}
```

---

## 7. Additional Google API helpers

Nicole had separate token helpers for specialized Google APIs.

### 7.1 Google Analytics token helper

Path:

```text
/data/.openclaw/secrets/gws-analytics-token.js
```

Purpose:

- Generates token for Analytics scopes while impersonating `nicole@oviond.com`.

Scopes:

```text
https://www.googleapis.com/auth/analytics.readonly
https://www.googleapis.com/auth/analytics
```

Use for GA4 Data/Admin API work where service-account impersonation is needed.

### 7.2 Google Search Console token helper

Path:

```text
/data/.openclaw/secrets/gws-gsc-token.js
```

Purpose:

- Generates token for Search Console / Webmasters API while impersonating `nicole@oviond.com`.

Scope:

```text
https://www.googleapis.com/auth/webmasters.readonly
```

Known GSC property:

```text
sc-domain:oviond.com
```

### 7.3 Google Tag Manager

GTM uses the same Workspace impersonation model.

Important GTM setup requirements:

- Google Tag Manager API enabled in the backing Google Cloud project.
- Domain-wide delegation includes needed GTM scopes.
- `nicole@oviond.com` has active GTM access. A pending invite is not enough.

Recommended GTM scopes:

```text
https://www.googleapis.com/auth/tagmanager.readonly
https://www.googleapis.com/auth/tagmanager.edit.containers
https://www.googleapis.com/auth/tagmanager.edit.containerversions
https://www.googleapis.com/auth/tagmanager.publish
https://www.googleapis.com/auth/tagmanager.manage.accounts
```

Only add this when explicitly needed:

```text
https://www.googleapis.com/auth/tagmanager.manage.users
```

Avoid by default:

```text
https://www.googleapis.com/auth/tagmanager.delete.containers
```

Existing GTM facts:

```text
GTM account: Oviond / accounts/6002040978
Main web container: www.oviond.com and v2.oviond.com
Main container ID: GTM-WXRJGTK / containers/32460546
Server container: www.oviond.com - Server
Server container ID: GTM-WGXKZQH / containers/65118591
```

### 7.4 Google Ads caution

There is a helper:

```text
/data/.openclaw/secrets/gws-ads-token.js
```

But Google Ads is special. The current Google Ads skill says:

- prefer service-account-first setup for Google Ads,
- canonical credential source is `GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT`,
- do **not** assume Google Workspace-style domain-wide delegation is the right model for Google Ads,
- OAuth refresh-token fallback exists if needed.

Known Ads mapping:

```text
MCC: 638-795-6297
Target account: 290-615-4258
Developer token env: GOOGLE_ADS_DEVELOPER_TOKEN
```

Also: ads-off hold remains active. Do not relaunch or unpause ads without Chris’s explicit approval.

---

## 8. `gog` CLI note

The managed `gog` CLI skill exists for Google Workspace tasks:

- Gmail
- Calendar
- Drive
- Contacts
- Sheets
- Docs

But in the current environment:

```bash
gog auth list
```

returned:

```text
No tokens stored
```

Despite that, Google Workspace still worked through the service-account helper path.

So Hermes should not assume `gog auth list` is the source of truth. There are two possible rebuild choices:

### Option A — integrate `gog` properly with OAuth/user tokens

Pros:

- Uses standard CLI flows.
- Easier day-to-day commands.

Cons:

- May need human OAuth setup.
- Less ideal for always-on server automation unless refresh-token handling is robust.

### Option B — preserve service-account DWD helper as primary path

Pros:

- This is the exact working model.
- Server-side and durable.
- No browser OAuth needed after admin setup.
- Correctly acts as `nicole@oviond.com`.

Cons:

- Requires Hermes/new Nicole to maintain API wrappers or helper scripts.
- Needs careful scope/admin setup.

Recommendation:

> Use Option B as the foundation. Add `gog` convenience only if it can be made to use the same durable impersonation model or if a separate OAuth flow is explicitly desired.

---

## 9. Where to store this in the new environment

Current layout:

```text
/data/.openclaw/secrets/gws-service-account.json
/data/.openclaw/secrets/gws-token.js
/data/.openclaw/secrets/gws-analytics-token.js
/data/.openclaw/secrets/gws-gsc-token.js
/data/.openclaw/secrets/gws-ads-token.js
```

Recommended new layout:

```text
/data/.openclaw/secrets/google-workspace/service-account.json
/data/.openclaw/secrets/google-workspace/token.js
/data/.openclaw/secrets/google-workspace/analytics-token.js
/data/.openclaw/secrets/google-workspace/gsc-token.js
```

Or equivalent secret manager / Envars.

Rules:

- Do not store private keys in tracked workspace files.
- Do not print tokens in logs unless deliberately debugging and immediately redacting.
- Keep helper scripts durable under `/data/.openclaw`, not `/tmp`.
- If using environment variables, use AlphaClaw Envars or the new equivalent, not manual edits to `/data/.env`.

---

## 10. Common failure modes and fixes

### Failure: `unauthorized_client`

Likely causes:

- Domain-wide delegation not enabled on service account.
- Wrong numeric client ID in Workspace Admin.
- Scope requested by helper is not authorized in DWD.
- Trying to impersonate a user outside the domain or inactive user.

Fix:

- Confirm service account DWD is enabled.
- Confirm numeric client ID is `100236162289445083006` or the new service account’s client ID.
- Confirm scopes exactly match what helper requests.
- Confirm `sub` is `nicole@oviond.com`.

### Failure: `invalid_grant`

Likely causes:

- Clock skew.
- Bad/private key mismatch.
- JWT signed incorrectly.
- `exp` too far in future.

Fix:

- Ensure host clock is accurate.
- Recreate JSON key if needed.
- Use Google auth library or verify RS256 signing.
- Keep `exp` within 3600 seconds.

### Failure: Gmail/Drive/Calendar returns service-account context

Likely cause:

- Missing `sub` claim.
- Auth library not configured with subject impersonation.

Fix:

- Set subject/delegated user to `nicole@oviond.com`.

### Failure: Drive upload works but file is owned by robot/service account

Likely cause:

- Using service account as itself, not domain-wide delegation.

Fix:

- Use DWD impersonation with `sub=nicole@oviond.com`.
- Re-run Drive about check and confirm `user.emailAddress` is `nicole@oviond.com`.

### Failure: GTM access fails while Gmail works

Likely causes:

- GTM API not enabled.
- GTM scopes missing from DWD.
- `nicole@oviond.com` does not have active GTM account/container access.

Fix:

- Enable Tag Manager API.
- Add GTM scopes in Workspace Admin DWD.
- Accept/activate GTM invite for Nicole.

### Failure: GA4/GSC access fails while Gmail works

Likely causes:

- Missing Analytics/GSC scopes in DWD.
- API not enabled.
- `nicole@oviond.com` lacks property access.

Fix:

- Add API scopes.
- Enable APIs.
- Confirm Nicole has property access.

---

## 11. What Hermes should build

Hermes should find the cleanest way to get this working again, but use the exact working setup above as the reference implementation.

### Minimum deliverable

A Google Workspace connector that can:

1. Load service-account credential from secure storage.
2. Mint access tokens with JWT bearer flow.
3. Impersonate `nicole@oviond.com`.
4. Request scoped tokens per Google product.
5. Verify Gmail profile.
6. Verify Calendar list.
7. Verify Drive identity.
8. Upload a Markdown file to Drive.
9. Share a Drive file with `chris@oviond.com`.
10. Keep all secrets out of repo/logs.

### Better deliverable

A reusable `google-workspace` skill or module with commands/functions:

```text
gws token --scope drive
gws whoami drive
gws gmail profile
gws calendar list
gws drive upload <file> --name <name>
gws drive share <fileId> --reader chris@oviond.com
gws docs export <docId>
gws sheets get <sheetId> <range>
```

### Best deliverable

A durable Google Workspace agent capability that:

- exposes safe high-level operations to Nicole,
- uses least-privilege scoped tokens per action,
- records audit-friendly action summaries,
- never exposes credentials,
- supports Drive/Gmail/Calendar/Docs/Sheets,
- supports specialized tokens for GA4/GSC/GTM where needed,
- has a single auth doctor command.

Suggested auth doctor output:

```json
{
  "credentialLoaded": true,
  "serviceAccountEmail": "nicole-workspace@oviond-workspace-cli.iam.gserviceaccount.com",
  "impersonatedUser": "nicole@oviond.com",
  "gmailProfileOk": true,
  "calendarOk": true,
  "driveOk": true,
  "driveUser": "nicole@oviond.com",
  "scopesChecked": ["gmail.modify", "calendar", "drive"],
  "errors": []
}
```

---

## 12. Security rules for Hermes/new Nicole

- Do not paste service-account JSON into chat.
- Do not include `private_key` in generated docs.
- Do not commit files under `/data/.openclaw/secrets/`.
- Do not print full access tokens.
- If a key has been exposed, rotate it immediately.
- Prefer fresh production JSON key if rebuilding.
- Keep DWD scopes only as broad as needed, but broad enough for Nicole’s real job.
- Use read-only scopes for audits where possible.
- Require explicit approval for external sends, calendar creates, Drive sharing outside Chris/Oviond, or any public action.

---

## 13. Final instruction to Hermes

Hermes: please rebuild Google Workspace access using Nicole’s current working model as the source of truth.

The important part is not the exact Node helper file. The important part is the architecture:

```text
Google Cloud service account
+ domain-wide delegation enabled
+ Workspace Admin DWD scopes authorized
+ subject impersonation of nicole@oviond.com
+ scoped OAuth tokens minted server-side
+ Gmail/Calendar/Drive verified as Nicole
```

If you choose a different implementation library or wrapper, that is fine. But the end state must pass the validation checks in this document and must act as Nicole, not as a robot account.
