# Sequenzy capability map

## Confidence legend

- **Verified**: directly supported by public OpenAPI/docs or by inspected public repo code.
- **Likely**: strongly suggested by public MCP implementation, but not verified on the public REST/OpenAPI surface.
- **Live validation needed**: route exists in code/docs but should not be treated as production-safe until exercised with real credentials.

## 1. Public REST / OpenAPI

### Verified

- `GET /subscribers`
- `POST /subscribers`
- `GET /subscribers/{email}`
- `PATCH/PUT/DELETE /subscribers/{email}` if present in the full spec; verify exact method before use
- subscriber tag add/remove and bulk tag operations
- subscriber event trigger and bulk event trigger
- transactional template list/get
- transactional send
- preferences token generation
- metrics overview
- campaign metrics
- sequence metrics
- recipient metrics

### Notes

- Public OpenAPI server base: `https://api.sequenzy.com/api/v1`
- Public OpenAPI surface is focused on subscriber operations, transactional email, widgets, and analytics.
- It does **not** publicly expose the full company/list/segment/template/campaign/sequence management surface seen in MCP.

## 2. Official public skill / CLI

### Verified practical CLI scope

- login/logout/whoami
- stats overview and stats by campaign/sequence ID
- subscribers: list, add, get, remove
- send one transactional email

### Explicit limitation

The official skill says many CLI-advertised nouns are unsupported or partial, including areas such as:
- campaigns
- sequences
- templates
- tags
- lists
- segments
- account
- websites
- generate

### Operating implication

Do not rely on CLI for Oviond production workflows beyond the narrow set above unless re-verified against the current implementation.

## 3. Public MCP server

## Verified in inspected MCP code

### Account / setup
- get account
- select company
- create company
- get company
- create API key
- list/add/check websites
- get integration guide

### Subscribers
- add/update/remove/get/search subscribers

### Audience structure
- list tags
- list lists
- create list
- list segments
- create segment
- get segment count

### Templates
- list/get/create/update/delete template

### Campaigns
- list/get/create/update campaign
- send test email

### Sequences
- list/get/create/update/enable/disable/delete sequence

### Transactional
- send one-off email

### Analytics
- get overview stats
- get campaign stats
- get sequence stats
- get subscriber activity

### AI generation
- generate email
- generate sequence
- generate subject lines

### MCP resources
- dashboard overview
- recent campaigns
- recent subscribers
- engaged subscribers
- sequences
- templates
- segments
- tags
- deliverability health

## Important caution

The MCP code calls many routes such as:
- `/api/v1/account`
- `/api/v1/companies`
- `/api/v1/websites`
- `/api/v1/lists`
- `/api/v1/segments`
- `/api/v1/templates`
- `/api/v1/campaigns`
- `/api/v1/sequences`
- `/api/v1/generate/*`
- `/api/v1/health/deliverability`

These routes are **verified as referenced by the MCP implementation**, not verified as stable public REST endpoints.

## 4. Dashboard-only or dashboard-first work

Treat these as dashboard-first until live-tested otherwise:
- domain/sender verification
- deliverability configuration
- billing-provider integration setup
- human review of AI-generated copy
- campaign/sequence activation
- workspace/company provisioning

## 5. Oviond task routing summary

### Good REST-first candidates
- subscriber CRUD
- tag application/removal
- event triggering
- transactional send
- reporting pulls

### Good MCP-or-dashboard candidates
- create/edit segments
- create/edit templates
- draft campaigns
- create AI-assisted sequences
- company selection and setup
- integration-guide/code-snippet generation

### Dashboard strongly preferred
- connect Stripe and other billing providers
- verify domains/websites
- approve copy and activate sequences/campaigns
- inspect deliverability health if MCP output disagrees with UI
