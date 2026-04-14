---
name: sequenzy
description: Operate Sequenzy for Oviond email marketing, lifecycle automation, subscriber management, transactional email, analytics, and SaaS billing-trigger workflows. Use when work involves Sequenzy subscribers, tags, attributes, events, sequences, campaigns, templates, transactional sends, Stripe-driven lifecycle email, deliverability and engagement metrics, or choosing the safest path across dashboard, documented REST, live private routes, CLI, and MCP surfaces.
---

# Sequenzy

Use this skill to operate Sequenzy itself, not Sequenzy source code.

## Core operating stance

1. Start by deciding which surface is credible for the task:
   - **Documented REST** for subscriber CRUD, tags, events, transactional email, and metrics.
   - **Live-validated private surface** for account, companies, websites, lists, templates, campaigns, and sequences when the Oviond key proves those routes work.
   - **Dashboard** for setup, review, sender/domain work, Stripe wiring, and approval-sensitive actions.
   - **CLI** only for the narrow flows the official public skill clearly confirms.
2. Treat **documented**, **live-validated**, **repo-inferred**, and **unknown** as separate buckets. Do not blur them.
3. Prefer inspection before mutation.
4. Require human review before enabling or sending real email at scale.
5. Prefer native billing integrations over hand-rolled lifecycle plumbing when Sequenzy supports the provider.
6. Send an explicit `User-Agent` on direct API calls from this workspace. Oviond's runtime hit edge blocking without one during live validation.
7. Expect response-shape drift. The docs describe a generic `data` envelope, but live responses often return resource-specific top-level keys like `subscribers`, `transactional`, `campaigns`, `sequences`, and `stats`.

## What is verified enough to trust

### Verified via public docs and OpenAPI

The documented REST API clearly covers:
- subscribers
- subscriber tags
- subscriber events
- transactional template lookup and send
- preferences-widget token generation
- metrics, including campaign, sequence, and recipient views

### Verified live on Oviond on 2026-04-14

The current Oviond `SEQUENZY_API_KEY` successfully reached these read-only routes:
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

This means Oviond already has more than just the narrow public REST surface available.

### Verified limitation from live validation

These routes did not validate cleanly on the Oviond account:
- `/health/deliverability` returned `404`
- `/subscribers/{email}/activity` returned `404`, even though subscriber detail already included an `activity` array

### Verified via official public skill

The official Sequenzy skill is deliberately conservative. Its practical CLI scope is centered on:
- auth and identity
- subscriber list, add, get, remove
- stats
- single transactional send

Treat broader CLI nouns as unsupported or partial unless re-verified.

## Default workflow selection

### Subscriber, tag, event, transactional, or metrics work

Use documented REST first.

### Account, company, website, list, template, campaign, or sequence work

Use the live-validated private surface if the task is read-only or low-risk drafting.
Prefer dashboard for setup changes, activation, or anything with unclear side effects.

### Setup, sender/domain, Stripe integration, deliverability, or activation work

Use dashboard first.

## Operational workflow

1. Start with a read-only audit.
2. If the task may touch a private route family, confirm the route class against `references/capability-map.md` and `references/verification-notes.md`.
3. If you need a fresh read-only account sweep, run `scripts/live_audit.py` with `SEQUENZY_API_KEY` in the environment.
4. Only move from audit to mutation after the exact route family and risk level are clear.
5. Keep campaign and sequence activation behind human review.

## Oviond operating rules

### Subscriber and lifecycle data

1. Keep subscriber identity stable around email as the primary key unless the live API proves otherwise.
2. Use attributes for durable facts such as plan, source, role, MRR-related metadata, or lifecycle state.
3. Use tags for operational grouping and trigger entry points, not as the only store of truth.
4. Trigger events for behavior and milestones.

### Stripe and SaaS lifecycle

When Stripe or another supported billing provider is available, prefer the native Sequenzy integration over manually recreating billing events.

Use manual custom events for product actions Sequenzy will not infer itself, such as:
- onboarding completed
- report created
- integration connected
- dashboard viewed
- trial value milestone reached

### Sequences and campaigns

1. Keep first drafts simple, usually 3 to 5 emails.
2. Match sequences to the actual Oviond funnel and available triggers.
3. Do not enable sequences automatically after creation.
4. Have a human review AI-generated copy, audience logic, stop conditions, and links.

### Transactional email

Use transactional sends for operational one-to-one messages, not broadcast marketing.

### Metrics

Prefer account, campaign, sequence, and recipient metrics for trend diagnosis.
For individual debugging, first check subscriber detail because the embedded `activity` array validated live even when the standalone `/subscribers/{email}/activity` route did not.

## Guardrails

- Do not invent endpoint names or payload shapes.
- Do not assume documented response envelopes are universal.
- Do not assume every MCP-exposed route is stable just because one adjacent route worked.
- Do not send or enable production email flows without review.
- Do not trust AI-generated copy without human approval.
- Do not require real credentials while drafting plans or artifacts.

## Read these resources as needed

- `references/capability-map.md` for route-by-route confidence and the current Oviond live-validation map.
- `references/workflows.md` for subscriber, Stripe lifecycle, sequence, campaign, transactional, and audit workflows.
- `references/verification-notes.md` for known mismatches, edge-block quirks, and the live-validation checklist.
- `scripts/live_audit.py` for a repeatable read-only account audit.
