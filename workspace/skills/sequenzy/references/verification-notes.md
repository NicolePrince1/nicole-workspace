# Sequenzy verification notes and guardrails

## What has been directly verified

### Public docs and OpenAPI

Verified public docs list public API coverage for:
- subscribers
- subscriber tags
- subscriber events
- transactional emails
- metrics and analytics
- preferences widget token

The downloaded OpenAPI also shows that narrow surface and sets the public server base to:
- `https://api.sequenzy.com/api/v1`

### Official public skill

Verified the official skill intentionally narrows CLI expectations. It explicitly says many advertised CLI areas should be treated as unsupported or partial until implementation is confirmed.

### Public MCP implementation

Verified by code inspection that the MCP server calls a much broader set of routes than the public OpenAPI exposes.

## Known mismatches / caution points

### 1. REST surface vs MCP surface

The biggest mismatch is scope:
- public OpenAPI = narrower, cleaner, mostly subscriber/transactional/metrics
- public MCP = much broader operational surface

Interpretation: Sequenzy likely has more internal/private endpoints than the public REST docs currently describe.

### 2. Base URL / path-style ambiguity

OpenAPI declares a server base ending in `/api/v1`.
MCP defaults to `https://api.sequenzy.com` and then appends `/api/v1/...` paths itself.

These are compatible in practice, but be careful not to duplicate `/api/v1` when constructing requests manually.

### 3. Stats route naming inconsistency

Public OpenAPI documents metrics under routes like:
- `/metrics`
- `/metrics/campaigns/{campaignId}`
- `/metrics/sequences/{sequenceId}`
- `/metrics/recipients`

The MCP code uses routes like:
- `/api/v1/stats`
- `/api/v1/campaigns/{id}/stats`
- `/api/v1/sequences/{id}/stats`
- `/api/v1/subscribers/{email}/activity`

Do not assume these are interchangeable without live validation.

### 4. Company-scoped operations

The MCP sends `x-company-id` headers for many operations and supports multi-company selection.
This concept does not appear in the public OpenAPI inspected so far.

Implication: multi-brand/company handling likely exists, but should be treated as MCP/private-surface behavior until confirmed live.

### 5. Resource endpoints may be optimistic

MCP resources include things like deliverability health and recent engaged subscribers. Some of those endpoints may exist only on private/internal APIs or may drift faster than public docs.

## Practical guardrails for future work

- Mark route confidence when planning work: public REST, MCP-only, or dashboard-only.
- For production changes, prefer documented REST or dashboard unless the MCP path has been live-tested successfully.
- Never present AI-generated copy as ready to go without human review.
- Keep campaign/sequence activation manual.
- Prefer native Stripe integration over reimplementing billing lifecycle tags/events.

## Live-validation checklist once credentials exist

### Connectivity and auth
- confirm bearer auth format
- confirm whether one API key is account-wide or company-scoped
- confirm whether `x-company-id` is required for Oviond's workspace

### Public REST checks
- create or update a test subscriber
- add/remove a test tag
- trigger a harmless custom event
- list transactional templates
- send a test transactional email to an internal address
- fetch account/sequence/campaign metrics if available to the key

### MCP/private-surface checks
- get account and inspect company list
- select company if multiple exist
- verify list/segment/template/campaign/sequence endpoints actually respond
- verify stats route family used by MCP
- verify subscriber activity endpoint
- verify deliverability-health endpoint
- verify AI generation endpoints and output shape

### Dashboard checks
- connect Stripe integration
- inspect which tags/events Sequenzy auto-creates from Stripe
- verify domain/website status flow
- verify test-email flow for campaigns
- verify sequence status model: draft, paused, active, processing

### Operational sign-off for Oviond
- define canonical lifecycle tags and attributes
- define which custom events Oviond will emit
- choose initial sequence set
- document review/approval path before activation
