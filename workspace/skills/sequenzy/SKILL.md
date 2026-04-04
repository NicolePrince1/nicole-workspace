---
name: sequenzy
description: Operate Sequenzy for Oviond email marketing, lifecycle automation, subscriber management, transactional email, analytics, and SaaS billing-trigger workflows. Use when work involves Sequenzy subscribers, tags, attributes, events, sequences, campaigns, templates, transactional sends, Stripe-driven lifecycle email, deliverability/engagement metrics, or choosing the safest path across dashboard, REST API, CLI, and MCP surfaces.
---

# Sequenzy

Use this skill to operate Sequenzy itself, not Sequenzy source code.

## Core operating stance

1. Start by deciding which surface is credible for the requested task:
   - **REST/OpenAPI** for verified public API work.
   - **MCP** for richer operations that appear implemented in the public MCP server.
   - **Dashboard** for setup, review, approval, and anything the public API surface does not clearly expose.
   - **CLI** only for flows explicitly confirmed in the official public skill.
2. Treat **verified**, **inferred**, and **needs live validation** as separate categories. Do not blur them.
3. Prefer inspection before mutation.
4. For email content that could reach real users, require human review before enabling/sending at scale.
5. For SaaS lifecycle work, prefer native billing integrations over hand-rolled event plumbing when Sequenzy supports the provider.

## What is solidly verified

### Verified via public OpenAPI / docs

The public REST API clearly covers:
- subscribers
- tags on subscribers
- subscriber events
- transactional email templates lookup + send
- preferences-widget token generation
- aggregate metrics, campaign metrics, sequence metrics, recipient metrics

This makes REST a strong path for:
- add/update/get/delete subscribers
- tag subscribers
- trigger product or lifecycle events
- send transactional emails
- read performance metrics

### Verified via official public skill

The official Sequenzy skill is deliberately conservative. It confirms the current practical CLI path is centered on:
- auth / identity
- subscriber list/add/get/remove
- stats
- single transactional send

Treat other CLI-advertised areas as unsupported or partial unless re-verified.

### Verified via public MCP repo

The public MCP server exposes a broader operating surface, including:
- account/company selection and API-key creation
- websites/domains
- lists, tags, segments
- templates
- campaigns
- sequences
- analytics
- AI generation
- integration-guide helpers

This is strong evidence those areas exist in Sequenzy's internal or private API surface, but it is **not** the same thing as public REST stability.

## Workflow selection

### If the task is subscriber, tag, event, transactional, or metrics work

Use REST first if direct API work is needed.

### If the task is sequence, campaign, template, list, segment, company, website, or AI-generation work

Assume dashboard or MCP is the better fit. Do not claim the public REST API supports it unless live-tested.

### If the task is setup or brand/account provisioning

Prefer dashboard. Use MCP guidance as evidence of likely capability, but mark it as needing live validation.

## Oviond operating rules

### Subscriber and lifecycle data

1. Keep subscriber identity stable around email as the primary key unless the live API proves otherwise.
2. Use attributes for durable facts such as plan, source, role, MRR-related metadata, or lifecycle state.
3. Use tags for operational grouping and trigger entry points, not as the only store of truth.
4. Trigger events for behavior and milestones.

### Stripe and SaaS lifecycle

When Stripe or another supported billing provider is available, prefer the native Sequenzy integration over manually recreating billing events.

Use manual/custom events for product actions Sequenzy will not infer itself, such as:
- onboarding completed
- report created
- integration connected
- dashboard viewed
- trial value milestone reached

### Sequences and campaigns

1. Keep first drafts simple: usually 3-5 emails.
2. Match sequences to the actual Oviond funnel and available triggers.
3. Do not enable sequences automatically after creation.
4. Have a human review AI-generated copy, audience, trigger logic, stop conditions, and links.

### Transactional email

Use transactional sends for operational one-to-one messages, not broadcast marketing.

### Metrics

Prefer account/campaign/sequence/recipient metrics for trend diagnosis.
Use subscriber activity views for individual debugging once live access exists.

## Guardrails

- Do not invent endpoint names, payload shapes, or stats routes.
- Do not assume MCP routes are publicly documented REST routes.
- Do not promise CLI support for nouns that the official skill says are placeholder or partial.
- Do not send or enable production email flows without review.
- Do not require real credentials while drafting plans or artifacts.

## Read these references as needed

- `references/capability-map.md` — surface-by-surface capability map with confidence levels.
- `references/workflows.md` — Oviond-relevant workflows for subscribers, Stripe lifecycle, sequences, campaigns, transactional email, and reporting.
- `references/verification-notes.md` — known mismatches, route inconsistencies, and live-validation checklist.