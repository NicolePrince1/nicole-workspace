# Gleap workflows

## Contents
- [Bootstrap after credentials exist](#bootstrap-after-credentials-exist)
- [Triage and respond to a ticket](#triage-and-respond-to-a-ticket)
- [Convert support noise into feature / roadmap structure](#convert-support-noise-into-feature--roadmap-structure)
- [Maintain the help center safely](#maintain-the-help-center-safely)
- [Run support analytics and health checks](#run-support-analytics-and-health-checks)
- [Escalate to UI/manual fallback](#escalate-to-uimanual-fallback)

## Bootstrap after credentials exist
Run this first once `GLEAP_API_KEY` and `GLEAP_PROJECT_ID` are available.

1. Run the safe probe:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py probe
   ```
2. Inspect and save the live facts that matter:
   - roles and permission count
   - real users and teams
   - real ticket statuses, types, priorities, tags
   - whether unified inbox and help center are accessible
3. Pull a few recent tickets to inspect actual shape:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request GET /tickets \
     --query limit=10 \
     --query sort=-updatedAt \
     --query ignoreArchived=true
   ```
4. Pull tracker tickets to learn how Oviond uses feature planning in practice:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request GET /tickets/tracker-tickets \
     --query page=1
   ```
   If this returns an empty list, do not force a tracker-ticket-centric workflow. Confirm whether roadmap work is actually living in tracker tickets, a public roadmap UI, tags, or a manual process before you create anything.
5. Pull help center collections to learn the current taxonomy:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request GET /helpcenter/collections/all
   ```
6. If in the main Chris session, write durable findings into workspace memory after discovery.

## Triage and respond to a ticket
Use this workflow for normal support handling.

1. Read the ticket:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request GET /tickets/TICKET_ID
   ```
2. Read the conversation history:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request GET /messages \
     --query ticket=TICKET_ID \
     --query sort=createdAt \
     --query limit=200
   ```
3. If needed, inspect customer context:
   - session record
   - session activities
   - session events
   - console logs / network logs / replay-related fields on the ticket
4. If a draft is useful, generate one first instead of freehand replying:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request POST /tickets/TICKET_ID/draft-reply
   ```
5. Prefer **internal notes** for early analysis or uncertain guidance:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request POST /messages \
     --data '{
       "ticket": "TICKET_ID",
       "comment": "Initial analysis: likely auth/session issue. Need to verify login flow and recent deploys.",
       "isNote": true,
       "sendToChannel": false
     }'
   ```
6. For a real support reply, be explicit about whether it should remain internal or reach the customer. Do not assume `sendToChannel` behavior until Oviond validates it.
7. Update routing/state only after reading current values. In Oviond's live sample, user-level assignment was much more evident than team-level assignment, so do not default to `processingTeam` unless the ticket already shows team routing:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request PUT /tickets/TICKET_ID \
     --data '{
       "status": "OPEN",
       "processingTeam": "TEAM_ID",
       "priority": "HIGH",
       "tags": ["billing", "vip"]
     }'
   ```
8. Use snooze only when there is a clear follow-up date or dependency:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request PUT /tickets/TICKET_ID/snooze \
     --data '{"duration": 48}'
   ```

## Convert support noise into feature / roadmap structure
Use this when multiple tickets point to the same product gap.

1. Search similar tickets with list filters first, then search endpoints if needed.
2. Pull existing tracker tickets before creating a new one:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request GET /tickets/tracker-tickets \
     --query searchTerm=utm \
     --query page=1
   ```
3. If the clustering work is messy, use duplicate detection:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request POST /tickets/deduplicate
   ```
4. If tracker tickets are confirmed to be the right live object and no matching one exists, create one:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request POST /tickets/tracker-tickets \
     --data '{
       "title": "Improve attribution / UTM visibility",
       "description": "Aggregate multiple customer tickets around missing campaign attribution context.",
       "type": "FEATURE_REQUEST",
       "linkedTicketIds": ["TICKET_1", "TICKET_2"]
     }'
   ```
5. If you want help shaping the summary, use the AI tracker-data endpoint:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request POST /tickets/generate-data \
     --data '{
       "sourceTicketId": "TICKET_ID",
       "type": "FEATURE_REQUEST"
     }'
   ```
6. Treat tracker tickets as one possible public API stand-in for roadmap items, not an assumption. In Oviond, verify they are actually in use before building process around them.
7. Do not claim there is a separate public roadmap API unless you have just validated it.

## Maintain the help center safely
Use this workflow for collections, articles, and publishing.

1. Inspect the collection tree first:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request GET /helpcenter/collections/all
   ```
2. Pull articles inside the relevant collection:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request GET /helpcenter/collections/COLLECTION_ID/articles
   ```
3. Prefer draft edits first. Update an article only after confirming the content shape in a live example. For Oviond, preserve localized `title` / `description` objects and both rich `content` plus `plainContent` when you edit:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request PUT /helpcenter/collections/COLLECTION_ID/articles/ARTICLE_ID \
     --data @article-update.json
   ```
4. Move articles when taxonomy changes:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request PUT /helpcenter/collections/COLLECTION_ID/articles/ARTICLE_ID/move \
     --data '{"newCollectionId": "NEW_COLLECTION_ID"}'
   ```
5. Treat publish toggles as risky, because they affect live help content:
   ```bash
   python3 skills/use-gleap/scripts/gleap_api.py request PUT /helpcenter/collections/COLLECTION_ID/toggle-publish \
     --data '{"unpublished": false}'
   ```
6. Use the shared endpoints for help-center search and answer behavior when you need to inspect retrieval/AI behavior rather than admin content.

## Run support analytics and health checks
Use the statistics endpoints for diagnostic reads and weekly summaries.

### Fact examples
```bash
python3 skills/use-gleap/scripts/gleap_api.py request GET /statistics/facts \
  --query chartType=NEW_TICKETS_COUNT \
  --query timezone=Africa/Johannesburg \
  --query startDate=2026-04-01T00:00:00.000Z \
  --query endDate=2026-04-07T23:59:59.999Z
```

```bash
python3 skills/use-gleap/scripts/gleap_api.py request GET /statistics/facts \
  --query chartType=MEDIAN_FIRST_RESPONSE_TIME \
  --query timezone=Africa/Johannesburg \
  --query startDate=2026-04-01T00:00:00.000Z \
  --query endDate=2026-04-07T23:59:59.999Z
```

### List examples
```bash
python3 skills/use-gleap/scripts/gleap_api.py request GET /statistics/lists \
  --query chartType=TEAM_PERFORMANCE_LIST \
  --query timezone=Africa/Johannesburg \
  --query startDate=2026-04-01T00:00:00.000Z \
  --query endDate=2026-04-07T23:59:59.999Z
```

```bash
python3 skills/use-gleap/scripts/gleap_api.py request GET /statistics/lists \
  --query chartType=ARTICLE_SEARCH_RESULT_LIST \
  --query timezone=Africa/Johannesburg \
  --query startDate=2026-04-01T00:00:00.000Z \
  --query endDate=2026-04-07T23:59:59.999Z
```

Guidelines:
- Use explicit date windows.
- Prefer read-only stats first before building narratives.
- Treat chart type enums as fixed; do not invent them.

## Escalate to UI/manual fallback
Use the dashboard or a manual fallback when:
- the public docs expose an endpoint but only `{}` schemas and no safe payload example
- the action is clearly customer-visible and live behavior is not validated
- the task involves engagement surfaces that are underdocumented
- the request appears to depend on a non-public board/workflow model
- the user asks for a destructive bulk action and has not confirmed it
