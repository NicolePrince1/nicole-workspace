# Sequenzy capability map

## Confidence legend

- **Documented**: supported by public OpenAPI or public docs.
- **Live-validated**: confirmed against Oviond's live workspace on 2026-04-14.
- **Repo-inferred**: supported by inspected public MCP code, but not yet proven on the live Oviond account.
- **Dashboard-first**: possible, but safer or clearer in the Sequenzy UI.

## 1. Documented REST surface

### Documented and live-validated

- `GET /subscribers`
- `POST /subscribers`
- `GET /subscribers/{email}`
- documented update and delete variants for `/subscribers/{email}`, though write paths remain untested on Oviond
- subscriber tag add and bulk tag operations
- subscriber event trigger and bulk trigger operations
- `GET /transactional`
- `GET /transactional/{slug}`
- `POST /transactional/send`
- `GET /metrics`
- `GET /metrics/campaigns/{campaignId}`
- `GET /metrics/sequences/{sequenceId}`
- `GET /metrics/recipients`
- preferences token generation remains documented but untested on Oviond

### Notes

- Public OpenAPI server base: `https://api.sequenzy.com/api/v1`
- The public OpenAPI surface is still mainly subscriber, transactional, widget, and analytics focused.
- Live responses do not always use a universal `data` field.

## 2. Official public skill and CLI

### Verified practical CLI scope

- login, logout, whoami
- stats overview and stats by campaign or sequence ID
- subscribers list, add, get, remove
- send one transactional email

### Treat as unsupported or partial until re-verified

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

## 3. Live private surface on Oviond

### Live-validated route families

#### Account and workspace
- `GET /account`
- `GET /companies`
- `GET /websites`

#### Audience structure
- `GET /lists`
- `GET /segments`

#### Templates and transactional
- `GET /templates`
- `GET /templates/{id}`
- `GET /transactional`
- `GET /transactional/{slug}`

#### Campaigns and sequences
- `GET /campaigns`
- `GET /campaigns/{id}`
- `GET /campaigns/{id}/stats`
- `GET /sequences`
- `GET /sequences/{id}`
- `GET /sequences/{id}/stats`

#### Analytics aliases
- `GET /stats`

### Live-validated account-shape facts

- `/account` and `/companies` returned one company
- `/websites` returned one website
- `/lists` returned two lists
- `/segments` returned zero segments at validation time
- `/templates` returned seventeen templates
- `/campaigns` returned one campaign
- `/sequences` returned two sequences

### Live-validated caveats

- `GET /health/deliverability` returned `404`
- `GET /subscribers/{email}/activity` returned `404`
- subscriber detail already included embedded `activity`, `lists`, `sequenceEnrollments`, and `emailStats`

## 4. Repo-inferred MCP surface not yet live-tested on Oviond

### Setup and account
- create company
- select company
- create API key
- add or check websites
- get integration guide

### Audience structure
- create list
- create segment
- get segment count
- list tags

### Templates
- create, update, delete template

### Campaigns
- create or update campaign
- send test email

### Sequences
- create, update, enable, disable, delete sequence

### AI generation
- generate email
- generate sequence
- generate subject lines

Treat these as plausible, not proven.

## 5. Dashboard-first work

Treat these as dashboard-first until live-tested otherwise:
- sender and domain verification
- deliverability configuration
- billing-provider integration setup
- human review of AI-generated copy
- campaign or sequence activation
- workspace or company provisioning

## 6. Oviond task routing summary

### Good documented-REST candidates
- subscriber CRUD
- tag application or removal
- event triggering
- transactional send
- metrics pulls

### Good live-private read candidates
- inspect account and company state
- inspect websites, lists, templates, campaigns, and sequences
- inspect campaign and sequence stats through private aliases

### Good dashboard candidates
- connect Stripe and other billing providers
- verify domains and websites
- review copy and activate campaigns or sequences
- inspect deliverability if private health routes disagree or fail
