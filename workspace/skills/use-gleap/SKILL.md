---
name: use-gleap
description: Operate Gleap for Oviond customer support, ticketing, tracker-ticket roadmap work, help center content, inbox routing, sessions, and support analytics. Use when work involves Gleap tickets, tracker tickets, conversations/messages, help-center articles or collections, customer sessions, unified inbox, support metrics, or deciding whether a Gleap task is API-backed, risky-write, or UI-only.
---

# Use Gleap

Operate **Gleap itself**, not Gleap source code or SDK installation. For SDK integration work, use a dedicated SDK/setup skill instead.

## Core operating stance

1. Separate **verified public API**, **mixed / needs live validation**, and **UI-only / not verified** work.
2. Prefer **read before write**.
3. Treat customer-visible changes as risky until Oviond's live setup is validated.
4. Treat **tracker tickets** as a possible public API-backed roadmap object, but inspect first. Oviond's 2026-04-08 live validation returned zero tracker tickets, so do not assume roadmap work currently lives there.
5. Do not store secrets in workspace files.

## Credentials and config

Use environment variables:
- `GLEAP_API_KEY`
- `GLEAP_PROJECT_ID`
- `GLEAP_BASE_URL` (optional; defaults to `https://api.gleap.io/v3`)

After credentials exist, start with:

```bash
python3 skills/use-gleap/scripts/gleap_api.py probe
```

Use the helper for arbitrary requests:

```bash
python3 skills/use-gleap/scripts/gleap_api.py request GET /tickets --query limit=5 --query sort=-updatedAt
```

## Routing

Read only the reference that matches the task.

| Intent | Reference | Use for |
|---|---|---|
| Decide what Gleap can or cannot do publicly | `references/capability-map.md` | API coverage, confidence levels, risky gaps |
| Execute common operator flows | `references/workflows.md` | triage, routing, tracker work, help center, analytics |
| Validate Oviond's live Gleap setup | `references/live-validation.md` | first-pass discovery after envs are wired |
| Reuse known-safe request bodies | `references/payload-patterns.md` | ticket, message, tracker, help center, stats payload starters |

## Default rules

- Prefer the public **v3** API for support, help center, session, and stats work.
- Prefer list endpoints with explicit query filters over vague search endpoints when possible.
- Use internal notes as the safest first write.
- In Oviond's live project, recent tickets are usually assigned via `processingUser`, not `processingTeam`, so inspect current routing before assuming team assignment is active.
- In Oviond's live help center, collection/article titles and descriptions are localized objects like `{ "en": "..." }`, and articles carry both rich `content` and derived `plainContent`. Preserve both when editing.
- Confirm before merges, deletes, archive/unarchive at scale, workflow runs with unclear side effects, publish toggles, or customer-visible outbound sends.
- Use the old `/admin/identify` and `/admin/track` endpoints only for server-side identity/event sync, not day-to-day support ops.
- When docs are thin, let live readbacks from Oviond's project become the source of truth.

## Guardrails

Do **not** assume the following without live proof:
- a separate public roadmap board API
- a public internal team to-do/task-board API
- direct binary attachment upload support
- outbound send semantics for messages
- workflow IDs or engagement payloads not already observed live

If a requested task lands in one of those areas, inspect first or fall back to UI/manual guidance instead of bluffing.
