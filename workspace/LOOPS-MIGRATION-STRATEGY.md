# Oviond → Loops Migration Strategy

**Date:** 9 March 2026
**Owner:** Nicole Prince
**Goal:** Replace MailerLite-centric lifecycle marketing with a cleaner SaaS lifecycle setup in Loops.

---

## Executive summary

Loops is a better fit than MailerLite for Oviond **if we use it correctly**.

The big shift is this:
- **MailerLite model:** list/group-heavy, campaign/automation builder centric
- **Loops model:** contact properties + events + mailing lists + lifecycle UI

That means we should **not** try to port MailerLite 1:1.
We should rebuild the system around SaaS lifecycle states and behaviors.

---

## Critical platform truth

From the Loops API docs:

### Strong API support
- Contact create / update / find / delete
- Contact property creation
- Mailing list subscriptions on contact create/update
- Events
- Transactional email

### Weak / missing API support
- Full programmatic creation of marketing loops / automation workflows
- Full programmatic visual email builder automation creation

## Implication

I can fully automate:
- data modeling
- imports
- property creation
- contact syncing
- lifecycle state syncing
- behavioral event ingestion
- transactional email setup

I likely **cannot** fully automate:
- the creation of each marketing loop in the Loops UI itself

So the migration strategy should optimize for:
1. **Perfect backend architecture first**
2. **Minimal manual loop-building on top**

---

## What we have today (source system: MailerLite)

### Audience shape
- ~9,000+ subscribers
- many lifecycle groups
- heavy group sprawl from legacy logic
- rich custom fields already synced from Stripe

### Important current lifecycle groups
- Trial Users
- Trial Expired
- Active Paying Customers
- Lapsed Customers
- Lifetime Users
- Dormant Contacts

### Important current automations
- trial onboarding
- trial expired re-engagement
- paying customer onboarding
- past due recovery
- LTD upgrade / reactivation sequences

### Problems in current setup
- too many groups
- logic too tied to email-builder platform constraints
- hard to operate programmatically
- manual intervention required for automation content/building

---

## Target architecture in Loops

## 1. Contacts = source of truth for lifecycle state

Each contact should carry the key business truth as properties.

### Required contact properties

#### Identity
- `companyName` (string)
- `leadSource` (string)
- `customerType` (string)
- `agencySize` (string)
- `country` (string)

#### Billing / lifecycle
- `subscriptionStatus` (string)
- `trialing` (boolean)
- `trialEndsAt` (date)
- `currentPeriodEnd` (date)
- `planName` (string)
- `billingInterval` (string)
- `mrr` (number)
- `isLifetimeUser` (boolean)
- `pastDue` (boolean)
- `paused` (boolean)

#### Product activation
- `hasConnectedDataSource` (boolean)
- `hasCreatedReport` (boolean)
- `hasSharedReport` (boolean)
- `hasInvitedTeamMember` (boolean)
- `connectedSourcesCount` (number)
- `projectsCount` (number)
- `dashboardsCount` (number)
- `clientsCount` (number)
- `firstReportCreatedAt` (date)
- `lastActiveAt` (date)

#### Strategic segmentation
- `needsUpgrade` (boolean)
- `atRisk` (boolean)
- `daysUntilTrialEnd` (number)
- `daysSinceLastActive` (number)

---

## 2. Events = behavior signals

These will drive lifecycle automation far better than static lists.

### Acquisition events
- `trial_started`
- `lead_captured`
- `demo_requested`

### Activation events
- `data_source_connected`
- `first_report_created`
- `report_shared`
- `branding_completed`
- `team_member_invited`

### Revenue events
- `subscription_started`
- `subscription_upgraded`
- `subscription_downgraded`
- `subscription_paused`
- `subscription_resumed`
- `payment_failed`
- `trial_expired`
- `subscription_canceled`

### Retention events
- `user_became_inactive`
- `user_reactivated`
- `usage_threshold_reached`

---

## 3. Mailing lists = broad communication buckets only

Do **not** recreate every MailerLite group.

Recommended lists:
- `trial-users`
- `paying-customers`
- `lapsed-customers`
- `lifetime-users`
- `newsletter`
- `product-updates`
- `reactivation`

Rule: use **properties/events for logic**, use **lists for audience buckets**.

---

## Core Loops to build first

### Loop 1 — Trial Onboarding
**Trigger:** `trial_started`
**Exit:** `subscription_started`
**Inputs:** trial status + activation behavior
**Goal:** increase trial-to-paid conversion

### Loop 2 — Trial Rescue / Expiry
**Trigger:** `trial_expired`
**Goal:** recover near-miss trials

### Loop 3 — Paying Customer Onboarding
**Trigger:** `subscription_started`
**Goal:** faster activation, lower churn

### Loop 4 — Past Due Recovery
**Trigger:** `payment_failed`
**Goal:** recover failed revenue quickly

### Loop 5 — Reactivation
**Trigger:** `subscription_canceled` or long inactivity
**Goal:** win back old users

### Loop 6 — Upgrade Trigger
**Trigger:** `usage_threshold_reached`
**Goal:** move customers to higher plans

---

## Migration phases

## Phase 1 — Foundation

### What I do
- read Loops API and document operating model
- create Loops skill locally
- define final property schema
- define mailing list model
- define event taxonomy

### What Chris does
- provide Loops account + API key
- confirm sending domain approach

**Status:** in progress

---

## Phase 2 — Account setup

### What I can do via API
- verify auth
- create contact properties
- test contact create/update/delete flows

### What Chris likely needs to do in UI
- sending domain / DNS verification
- brand settings
- any loop UI configuration not exposed by API

### Deliverables
- Loops account architecture doc
- property schema live in Loops
- clean empty environment ready for import

---

## Phase 3 — Data migration design

### Source systems
- MailerLite audience + groups
- Stripe billing states
- product/app usage data (when available)

### Mapping rules

#### MailerLite → Loops
- Trial group → list `trial-users` + `trialing=true`
- Paying group → list `paying-customers` + `subscriptionStatus=active`
- Lapsed group → list `lapsed-customers` + `subscriptionStatus=canceled`
- LTD group → list `lifetime-users` + `isLifetimeUser=true`

#### Important principle
Do not import junk legacy segmentation blindly.
Only move what is strategically useful.

---

## Phase 4 — First import

### Recommended approach
1. export MailerLite contacts
2. normalize fields to Loops schema
3. import a small QA batch first
4. validate properties and list membership
5. run full import

### Import strategy
- first import: trials + active paying only
- second import: lapsed + LTD
- third import: dormant and newsletter-only contacts if still strategically useful

### Risk controls
- keep MailerLite untouched during initial import
- do not trigger all loops on all contacts immediately
- use controlled batches

---

## Phase 5 — Loop rebuild

### Build order
1. Trial onboarding
2. Paying onboarding
3. Past due recovery
4. Reactivation
5. Upgrade nudges

### Important rule
Rebuild for SaaS behavior, not for old MailerLite structure.

For example:
- instead of “wait 1 day, send email” only
- use “trial started but no data source connected after 24h”
- use “report created but not shared after 72h”
- use “3 days before trial end and no subscription started”

That is the whole reason to migrate.

---

## Phase 6 — Parallel run and cutover

### Parallel run
- keep MailerLite as fallback while Loops is being validated
- route a limited subset first if practical
- verify contact syncing, loop triggering, unsubscribe handling, and deliverability

### Cutover criteria
- contact sync stable
- trial loop built and reviewed
- paying onboarding built and reviewed
- sending domain healthy
- unsubscribe and preference behavior confirmed

Then:
- pause MailerLite automations
- stop new operational dependence on MailerLite
- treat MailerLite as archive/export source only

---

## What I can do now

### Immediately
- create local Loops skill ✅
- document architecture ✅
- define property schema ✅
- define event taxonomy ✅
- test API auth ✅

### Next with the API key/account
- create Loops contact properties
- test contact CRUD
- test mailing list flows
- prepare import mapping scripts
- create migration checklist and runbook

### What may still require Loops UI
- building the actual marketing loops
- editing visual marketing email content
- configuring sending domain / branding

---

## What you need to do

### Right now
- confirm the sending domain we should use in Loops (`hi@getoviond.com` vs other)
- be ready to add DNS records when needed
- confirm we are comfortable not migrating every old MailerLite group exactly

### Soon
- review the final property schema
- review the first rebuilt loops before activation

---

## Recommended next execution order

1. create the Loops property schema
2. create the core mailing lists
3. export MailerLite contacts and map fields
4. import QA batch
5. build Trial Onboarding v2 in Loops
6. build Paying Onboarding
7. wire Stripe/app events into Loops
8. cut over

---

## Success criteria

A successful migration means:
- all strategically valuable contacts preserved
- lifecycle state preserved cleanly
- onboarding logic improved, not just copied
- no dependency on MailerLite builder for core growth work
- Loops becomes the operating system for SaaS lifecycle email

## Loops.so Mailing List IDs (Confirmed via UI)

- `trial-users`: `cmmjb3d6a01c00iwn55sld83u`
- `paying-customers`: `cmmjb3z3b2uj20iwgar195n78`
- `lapsed-customers`: `cmmjb4inp01h90isyddn5hhzv`
- `lifetime-users`: `cmmjb4jt82vao0iy58hy8bnot`
- `newsletter`: `cmmjb4kuz01xk0ix4hguv0cgz`

## Strategy Status

- **Properties:** All 26 properties created.
- **Lists:** Mapped and ready.
- **Next:** Full migration script.
