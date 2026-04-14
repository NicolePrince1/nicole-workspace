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

The public server base is:
- `https://api.sequenzy.com/api/v1`

### Official public skill

Verified the official public skill intentionally narrows CLI expectations. Treat many advertised CLI nouns as unsupported or partial until implementation is confirmed.

### Public MCP implementation

Verified by code inspection that the MCP server calls a much broader set of routes than the public OpenAPI exposes.

## Oviond live validation on 2026-04-14

### Auth and runtime behavior

- `SEQUENZY_API_KEY` works against the live Oviond workspace.
- Direct calls from this workspace should send an explicit `User-Agent`.
- Without an explicit `User-Agent`, a basic urllib request hit Sequenzy's edge with `403` and `error code: 1010`.
- With an explicit `User-Agent`, the same requests succeeded.

### Live routes that responded successfully

These route families returned `200` during read-only validation:
- `/subscribers`
- `/subscribers/{email}`
- `/transactional`
- `/metrics`
- `/metrics/campaigns/{id}`
- `/metrics/sequences/{id}`
- `/metrics/recipients`
- `/stats`
- `/account`
- `/companies`
- `/websites`
- `/lists`
- `/segments`
- `/templates`
- `/templates/{id}`
- `/campaigns`
- `/campaigns/{id}`
- `/campaigns/{id}/stats`
- `/sequences`
- `/sequences/{id}`
- `/sequences/{id}/stats`

### Live route failures or mismatches

- `/health/deliverability` returned `404`
- `/subscribers/{email}/activity` returned `404`
- subscriber detail still included an embedded `activity` array, so the detail route is currently the safer individual-debug path

### Live account-shape facts observed

- one company was returned from `/account` and `/companies`
- one website was returned
- two lists were returned
- zero segments were returned at validation time
- seventeen templates were returned
- one campaign was returned
- two sequences were returned
- one transactional template was returned
- subscriber detail included `lists`, `sequenceEnrollments`, `emailStats`, and `activity`

### `x-company-id` behavior

- `x-company-id` support appears real
- for the current Oviond workspace, routes like `/templates`, `/campaigns`, and `/sequences` still worked without forcing the header
- keep `x-company-id` in mind for multi-company use, but do not assume it is required in the current single-company workspace

## Known mismatches and caution points

### 1. Documented surface vs live private surface

The biggest mismatch is still scope:
- public OpenAPI = narrower and cleaner
- live account = materially broader route family already accessible with the Oviond key

Interpretation: Sequenzy exposes more operational surface than the public API docs currently admit.

### 2. Response envelope mismatch

The API reference presents a generic success envelope like:
- `{ "success": true, "data": ... }`

Live responses often returned resource-specific top-level keys instead, including:
- `subscribers`
- `transactional`
- `stats`
- `companies`
- `templates`
- `campaigns`
- `sequences`

Do not hardcode everything around a universal `data` field.

### 3. Base URL and path-style ambiguity

OpenAPI declares a server base ending in `/api/v1`.
MCP defaults to `https://api.sequenzy.com` and appends `/api/v1/...` paths itself.

These are compatible in practice, but do not duplicate `/api/v1` when building requests manually.

### 4. Stats route naming inconsistency

Both of these styles worked live for campaign and sequence metrics:
- `/metrics/campaigns/{id}` and `/metrics/sequences/{id}`
- `/campaigns/{id}/stats` and `/sequences/{id}/stats`

Additionally, `/stats` worked as an overview alias next to `/metrics`.

Treat the stats family as real, but still prefer the documented metrics family when you want the safer public contract.

### 5. Resource endpoints can drift

The MCP code references things like deliverability health and subscriber activity routes that are not currently cleanly available in the Oviond account.

Treat MCP coverage as a map, not gospel.

## Practical guardrails for future work

- Mark route confidence when planning work: documented REST, live private, repo-inferred, or dashboard-only.
- Prefer documented REST or dashboard for production mutations unless a private route has been proven safe and necessary.
- Never present AI-generated copy as ready to go without human review.
- Keep campaign and sequence activation manual.
- Prefer native Stripe integration over reimplementing billing lifecycle tags and events.
- Use `scripts/live_audit.py` when you need a fresh read-only sweep without leaking subscriber content into chat.

## Live-validation checklist for future expansion

### Safe read-only checks
- confirm account and company count
- confirm website and sender-related status surfaces
- inspect list, segment, template, campaign, and sequence counts
- compare `/metrics` vs `/stats`
- inspect subscriber detail shape

### Deferred write checks
- create or update a test subscriber
- add and remove a test tag
- trigger a harmless custom event
- send a transactional email to an internal address
- draft but do not activate a sequence or campaign unless Chris explicitly wants that

### Dashboard checks
- connect Stripe integration
- inspect which tags and events Sequenzy auto-creates from Stripe
- verify domain and website status flow
- verify test-email flow for campaigns
- verify sequence status model such as draft, paused, active, processing

### Operational sign-off for Oviond
- define canonical lifecycle tags and attributes
- define which custom events Oviond will emit
- choose the first production sequence set
- document the review and approval path before activation
