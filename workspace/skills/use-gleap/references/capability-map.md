# Gleap capability map

## Contents
- [Primary sources](#primary-sources)
- [Confidence labels](#confidence-labels)
- [Verified public API surface](#verified-public-api-surface)
  - [Auth and API shape](#auth-and-api-shape)
  - [Tickets and tracker tickets](#tickets-and-tracker-tickets)
  - [Messages and conversations](#messages-and-conversations)
  - [Sessions and customer context](#sessions-and-customer-context)
  - [Help center](#help-center)
  - [Users, teams, inbox, and routing](#users-teams-inbox-and-routing)
  - [Support analytics](#support-analytics)
  - [Engagement / lifecycle surfaces](#engagement--lifecycle-surfaces)
- [Mixed or needs-live-validation areas](#mixed-or-needs-live-validation-areas)
- [Not publicly verified](#not-publicly-verified)
- [Legacy server-side admin endpoints](#legacy-server-side-admin-endpoints)
- [Operating implications for this skill](#operating-implications-for-this-skill)

## Primary sources
- Docs index: `https://docs.gleap.io/llms.txt`
- Marketing/product index: `https://www.gleap.io/llms.txt`
- Public OpenAPI: `https://api.gleap.io/api-docs.json`
- API overview: `https://docs.gleap.io/documentation/server/api-overview`
- Official public agent skills: `https://github.com/GleapSDK/agent-skills`

## Confidence labels
- **Verified**: explicitly documented in the public OpenAPI/docs.
- **Mixed**: documented, but the docs omit important payload/response detail or live-send semantics are unclear.
- **Not verified**: not found in the public API/docs during research.

## Verified public API surface

### Auth and API shape
- Base URL: `https://api.gleap.io/v3`
- Normal auth: `Authorization: Bearer <api-key>` plus `Project: <project-id>` header.
- API overview explicitly says list-style GET endpoints support querying on document properties.
- Public rate limit: **1000 requests / 60 seconds / project**.

### Tickets and tracker tickets
**Verified read/write surface:**
- `/tickets` — create + list
- `/tickets/{ticketId}` — get + update + delete
- `/tickets/search` and `/tickets/extendedsearch`
- `/tickets/ticketscount`
- `/tickets/by-session-query`
- `/tickets/{ticketId}/activity-logs`
- `/tickets/{ticketId}/console-logs`
- `/tickets/{ticketId}/network-logs`
- `/tickets/{ticketId}/draft-reply`
- `/tickets/{ticketId}/workflow`
- `/tickets/{ticketId}/snooze`
- `/tickets/{ticketId}/archive` and `/tickets/{ticketId}/unarchive`
- `/tickets/{ticketId}/link` and `/tickets/{ticketId}/unlink`
- `/tickets/merge` and `/tickets/deduplicate/merge`
- `/tickets/deduplicate`
- `/tickets/{ticketId}/send-transcript`
- `/tickets/{ticketId}/send-to-integration`
- `/tickets/{ticketId}/vote`
- `/tickets/tracker-tickets` — list + create tracker tickets
- `/tickets/generate-data` — AI-generated tracker data

**Important observed fields in create/update ticket DTOs:**
- `title`, `description`, `type`, `status`, `priority`
- `processingUser`, `processingTeam`
- `tags`, `dueDate`, `linkedTickets`, `duplicateOf`
- `session`, `sessions`, `customData`, `formData`
- `archived`, `isSpam`, `snoozed`, `snoozedUntil`

**Implication:** ticket workflows are first-class and strong enough for a real operator skill. Tracker tickets are publicly API-backed, but Oviond's 2026-04-08 live validation returned an empty tracker-ticket list, so roadmap usage must be confirmed before building process around them.

### Messages and conversations
**Verified:**
- `/messages` — list + create messages
- Message create DTO supports:
  - `ticket`
  - `comment`
  - `isNote`
  - `session` (customer-side message)
  - `attachments` with URL-based metadata
  - `sendToChannel`
  - `channel`
  - `replyTo`

**Practical takeaway:** internal notes and conversation entries are clearly supported. Oviond live readbacks showed `NOTE`-type history entries, but customer-visible send semantics should still be treated carefully until a safe write test validates `isNote` / `sendToChannel` behavior in the real workspace.

### Sessions and customer context
**Verified:**
- `/sessions` — create + list
- `/sessions/{sessionId}` — get/update/delete
- `/sessions/search`
- `/sessions/by-user-id/{userId}`
- `/sessions/{sessionId}/activities`
- `/sessions/{sessionId}/events`
- `/sessions/{sessionId}/checklists`
- `/sessions/{sessionId}/stripe`
- `/sessions/{sessionId}/chargebee`
- `/sessions/{sessionId}/lemonsqueezy`
- `/sessions/{sessionId}/shopify`
- `/sessions/unsubscribe` and `/sessions/{sessionId}/resubscribe`
- `/sessions/export`, `/sessions/importer`, `/sessions/importer/intercom`

**Implication:** session-level customer debugging and enrichment are strong API-backed surfaces.

### Help center
**Verified:**
- Collections:
  - `/helpcenter/collections` — create + list
  - `/helpcenter/collections/{helpcenterCollectionId}` — get/update/delete
  - `/helpcenter/collections/all`
  - `/helpcenter/collections/{helpcenterCollectionId}/toggle-publish`
- Articles:
  - `/helpcenter/collections/{helpcenterCollectionId}/articles` — create + list
  - `/helpcenter/collections/{helpcenterCollectionId}/articles/{helpcenterArticleId}` — get/update/delete
  - `/helpcenter/collections/{helpcenterCollectionId}/articles/{helpcenterArticleId}/move`
- Redirects:
  - `/helpcenter-redirect` + item endpoints
- Shared help center endpoints:
  - `/shared/helpcenter/search`
  - `/shared/helpcenter/answer`
  - `/shared/helpcenter/sources`

**Important observed fields in article/collection DTOs:**
- Collection: `title`, `description`, `iconUrl`, `parent`, `externalId`, `targetAudience`
- Article: `title`, `description`, `content`, `plainContent`, `helpcenterCollection`, `author`, `isDraft`, `tags`, `targetAudience`, `newCollectionId`

**Implication:** the help center is solidly API-operable, especially for draft/edit/move/publish workflows. In Oviond's live data, collection/article fields are localized objects like `{ "en": "..." }`, articles carry both rich `content` and `plainContent`, and collection summary counts may not perfectly match article-list results.

### Users, teams, inbox, and routing
**Verified:**
- `/projects/users`
- `/teams`
- `/users/me`
- `/users/me/permissions`
- `/users/unified-inbox`
- `/users/unified-inbox/{ticketId}`
- `/users/me/reassign-tickets`

**Implication:** role discovery, team discovery, and some inbox/routing operations are available. In Oviond's recent live sample, routing appeared much more user-assigned (`processingUser`) than team-assigned (`processingTeam`).

### Support analytics
**Verified:**
- `/statistics/facts`
- `/statistics/lists`
- `/statistics/lists/export`
- `/statistics/raw-data`
- `/statistics/bar-chart`
- `/statistics/heatmap`
- `/statistics/email-overview`
- `/statistics/email-client-usage`
- `/statistics/email-client-bounces`

**Verified enumerations seen in docs:**
- Facts include examples like `NEW_TICKETS_COUNT`, `MEDIAN_FIRST_RESPONSE_TIME`, `MEDIAN_TIME_TO_CLOSE`, `SNAPSHOT_OPEN_TICKETS`, `KAI_DEFLECTION_RATE`
- Lists include examples like `TEAM_PERFORMANCE_LIST`, `ARTICLE_SEARCH_RESULT_LIST`, `TICKETS_WITH_RATING_LIST`, `SLA_REPORTS_LIST`

### Engagement / lifecycle surfaces
**Verified endpoints exist for:**
- checklists
- product tours
- cobrowse tours
- emails
- surveys and survey response exports/summaries
- banners
- modals
- news
- push notifications
- tooltips
- WhatsApp messages
- message templates
- engagement statistics

**Caution:** many of these endpoints expose `{}` request/response schemas in docs. Treat read access as likely fine, but treat mutations as mixed until live-tested.

## Mixed or needs-live-validation areas
- **Roadmap model**: no separate first-class public roadmap object was found. Tracker tickets are the nearest public API-backed feature object, but Oviond's 2026-04-08 live validation returned an empty tracker-ticket list, so do not assume active roadmap work currently lives there.
- **Internal team to-do lists / work boards**: no distinct public API object was found.
- **Customer-visible outbound messaging**: messages support `sendToChannel`, but actual behavior should be validated in Oviond's channel setup before using it in production.
- **Attachments**: message/ticket schemas clearly support URL-based attachments, but a public direct binary upload flow was not verified.
- **Search endpoints**: present, but less informative than the generic list endpoints. Prefer list endpoints with explicit query filters where possible.
- **Engagement mutations**: endpoints exist, but payload schemas are often underdocumented.
- **Workflow IDs**: ticket workflow execution exists, but workflow enumeration was not clearly found in public docs.

## Not publicly verified
- A public **MCP server** for Gleap.
- A public **operator/admin AgentSkill** for day-to-day support work.
- A separate public API for **roadmap boards** or **internal task boards** beyond tracker tickets and voting.

## Legacy server-side admin endpoints
Gleap also documents older server-side endpoints under `/admin` using `Api-Token` auth:
- `/admin/identify`
- `/admin/track`

Use these only for server-side identify/event syncing. Do **not** route normal support operations through them.

## Operating implications for this skill
1. Prefer the public v3 API for support, help center, and analytics work.
2. Treat **tickets** as the strongest public foundation today, and treat **tracker tickets** as an optional extension only after confirming they are actually in use for Oviond's roadmap workflow.
3. Use **read-first** behavior whenever the requested action could affect customers or published help content.
4. Keep risky writes behind explicit confirmation:
   - merges
   - deletes
   - archive/unarchive at scale
   - workflow runs with unknown side effects
   - publish toggles
   - customer-visible outbound sends
5. When docs are thin, let live readbacks become the source of truth for Oviond's actual object model.
