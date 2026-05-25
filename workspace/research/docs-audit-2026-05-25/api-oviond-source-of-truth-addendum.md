# Addendum — `api.oviond.com/docs` changes the Mintlify plan

Date: 2026-05-25

Chris pointed out that the live app API docs exist at `https://api.oviond.com/docs` and that the app works from this API. I inspected that surface and the OpenAPI file behind it.

## What I found

`https://api.oviond.com/docs` is a Swagger UI page. Its HTML loads the spec from:

`https://api.oviond.com/openapi.json`

That endpoint works and returns the current live API spec:

- Title: `Oviond Backend API`
- OpenAPI: `3.1.0`
- Server: `https://api.oviond.com`
- Paths: `135`
- Schemas: `210`

I also tested live public behavior:

- `GET /v1/health` returns 200 and a healthy response.
- Authenticated endpoints like `/v1/users/me` and `/v1/clients` return 401 without a Bearer token.
- The spec marks `POST /v1/public/verify-email` as public; a GET request returns 404, which is expected if the route is POST-only.

## How this changes the docs plan

This changes the source-of-truth decision.

The canonical API spec should not be the copied/stale file on `docs.oviond.com`. It should be the live backend spec at:

`https://api.oviond.com/openapi.json`

Mintlify should either import this spec directly or sync from the exact same generated source used by the backend. Right now `docs.oviond.com/api/openapi.json` appears stale compared to the live backend spec.

## Critical diff: Mintlify spec is stale

Compared the live backend spec against the current docs spec:

- `api.oviond.com/openapi.json`: 135 paths, 210 schemas
- `docs.oviond.com/api/openapi.json`: 102 paths, 151 schemas
- Paths only in live API: 56
- Paths only in docs spec: 23

Examples only in the live API spec:

- Admin routes: `/v1/admin/users`, `/v1/admin/impersonate`, `/v1/admin/accounts/:account_id`
- New datasource naming: `/v1/datasources/...`
- Custom domains: `/v1/custom-domains/...`
- Email templates/senders/provider routes
- Goals routes
- Exports routes
- Project versions routes
- Onboarding route
- Widget refresh/duplicate/bulk-each routes

Examples still in the docs spec but not the live API spec:

- Old integration naming: `/v1/integrations/...`
- Old white-label naming: `/v1/white-label/domains...`
- Old email domain/setup/queue routes
- `/v1/projects/{id}/pdf`
- `/v1/widgets/ids`

This means Mintlify is not only messy; it is probably documenting an older API shape in places.

## New highest-priority recommendation

Before rewriting hundreds of pages, fix the API source pipeline:

1. Make `https://api.oviond.com/openapi.json` the canonical source of truth, or export Mintlify from the exact same backend OpenAPI generator.
2. Update `docs.oviond.com` to consume that canonical spec.
3. Remove/redirect the Plant Store sample at `/api-reference/openapi.json`.
4. Remove the stale copied docs spec at `/api/openapi.json`, or make it a proxy/redirect to the live canonical spec.
5. Regenerate API reference pages from the live spec.
6. Only then do the human editorial pass.

If the team edits Mintlify pages before this, they risk polishing stale/generated pages that will need to be regenerated anyway.

## Still broken in the live API spec

The live backend spec is useful, but not launch-clean yet. It still has issues that should be fixed at source:

1. **Colon-style path params**

There are 33 paths using `:id` style instead of OpenAPI `{id}` style, e.g.

- `/v1/users/:id`
- `/v1/admin/users/:id/email`
- `/v1/clients/:id`
- `/v1/datasources/:client_id/link`
- `/v1/datasources/:datasource_id/profiles/:profile_name`
- `/v1/automations/:id`

These should be fixed in the OpenAPI generator/source annotations.

2. **Internal/vendor language still leaks**

The live spec still mentions terms like Supabase, S3, Resend, Vercel, cron scheduler, accounts row, users table, upstream API, raw_data, resource_type, Stripe, and impersonate.

Some admin/internal routes may be legitimate, but public docs should decide whether to expose them. If they are only for Oviond staff, hide them from public Mintlify docs or move them to private/internal docs.

3. **Auth language still needs a product decision**

The live spec says `bearerFormat: JWT`. If customer-facing credentials are API keys rather than JWTs, this should change in the spec source.

4. **Swagger UI is not enough for launch docs**

`api.oviond.com/docs` is useful for truth/testing, but it is not a replacement for Mintlify. Swagger tells developers what exists. Mintlify should explain how to use it safely and successfully.

## Revised docs workflow

Use Swagger/OpenAPI as the source layer, Mintlify as the explanation layer.

### Layer 1 — Backend OpenAPI source

Owner: dev team

Must contain:

- Correct routes
- Correct schemas
- Correct examples
- Correct auth scheme
- No stale route names
- No invalid path templates
- No public internal implementation leaks

### Layer 2 — Mintlify generated API reference

Owner: docs/dev

Must be generated from canonical OpenAPI, not manually copied stale spec.

### Layer 3 — Human-authored Mintlify guides

Owner: product/docs/marketing/dev together

Must explain:

- Auth setup
- First API call
- Clients/projects/data sources workflow
- Report/dashboard creation flow
- Automations/PDF/email delivery flow
- Custom domains/white label flow
- MCP usage and safety
- Destructive actions and recovery behavior

## Practical next step for dev team

Do this before page rewriting:

- Compare the backend OpenAPI generator/source to Mintlify config.
- Wire Mintlify to `https://api.oviond.com/openapi.json` or to the same generated OpenAPI artifact.
- Decide whether admin/internal routes should be public.
- Fix OpenAPI path params at source.
- Regenerate docs.
- Then run the editorial launch pass from the existing action plan.

Bottom line: this helps a lot. It gives us the real source of truth. It also proves the docs problem is not just writing quality — it is a broken/stale documentation pipeline.
