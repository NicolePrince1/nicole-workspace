# Gleap live validation

## Contents
- [Required environment variables](#required-environment-variables)
- [First-pass probe](#first-pass-probe)
- [Validation checklist](#validation-checklist)
- [Known doc quirks](#known-doc-quirks)
- [Post-validation writeback](#post-validation-writeback)

## Required environment variables
Use env vars, not tracked workspace files:
- `GLEAP_API_KEY`
- `GLEAP_PROJECT_ID`
- `GLEAP_BASE_URL` (optional; default `https://api.gleap.io/v3`)

If only the API key exists and the project id is missing, stop and ask for the project id or retrieve it from the authenticated Gleap project settings if a safe surface exists.

## First-pass probe
Run the safe probe first:

```bash
python3 skills/use-gleap/scripts/gleap_api.py probe
```

This should confirm whether the following are readable in Oviond's live workspace:
- current user permissions
- project users
- teams
- ticket count + sample ticket shapes
- help center collections
- unified inbox

## Validation checklist

### 1. Auth and permissions
- Confirm `/users/me/permissions` works.
- Capture the current roles.
- Note whether permissions look broad enough for help-center edits, tracker work, and message writes.

### 2. User and team routing model
- Read `/projects/users`.
- Read `/teams`.
- Map real user ids, team ids, and assignment methods.
- Check whether specific teams appear to own support vs product/engineering queues.

### 3. Ticket object model
Pull recent tickets and record:
- actual `status` values
- actual `type` values
- actual `priority` values
- common `tags`
- whether `processingUser` and `processingTeam` are commonly populated
- whether form fields live in `formData`, `customData`, `attributes`, or somewhere else
- whether replay/screenshot fields are populated in real tickets

Suggested command:
```bash
python3 skills/use-gleap/scripts/gleap_api.py request GET /tickets \
  --query limit=25 \
  --query sort=-updatedAt \
  --query ignoreArchived=true
```

### 4. Roadmap / tracker model
Validate how Oviond actually uses feature planning.
- Read `/tickets/tracker-tickets`
- inspect fields and types
- confirm whether tracker tickets are the real roadmap objects
- check whether support tickets are linked directly to tracker tickets
- validate whether ticket voting is used in practice

### 5. Help center model
Validate how Oviond stores knowledge content.
- Read `/helpcenter/collections/all`
- read articles inside 1-2 collections
- identify whether `content` vs `plainContent` is the field to preserve/edit
- confirm whether content is kept as rich JSON, HTML-ish data, or plain text derivatives
- identify draft vs published patterns

Suggested commands:
```bash
python3 skills/use-gleap/scripts/gleap_api.py request GET /helpcenter/collections/all
python3 skills/use-gleap/scripts/gleap_api.py request GET /helpcenter/collections/COLLECTION_ID/articles
```

### 6. Messaging / outbound safety
Before sending anything customer-visible, validate:
- whether `isNote: true` behaves as expected
- whether `sendToChannel: false` safely keeps a message internal
- whether customer replies require `session`
- whether attachment URLs are accepted as-is
- whether outbound channel metadata is required in Oviond's setup

Start with internal-note tests only.

### 7. Workflow and automation model
If Chris asks to run workflows or engagement content:
- discover actual workflow ids before using `/tickets/{ticketId}/workflow`
- do not invent workflow ids
- inspect engagement surfaces read-only first because payloads are underdocumented

### 8. Analytics model
Test a few known-good statistics enums:
- `NEW_TICKETS_COUNT`
- `MEDIAN_FIRST_RESPONSE_TIME`
- `TEAM_PERFORMANCE_LIST`
- `ARTICLE_SEARCH_RESULT_LIST`

If these fail, inspect the live error response rather than guessing enum names.

## Known doc quirks
- Public docs are generated from OpenAPI and are useful, but many response schemas are empty `{}`.
- Some pages omit obvious route params or do not show enough payload detail.
- Treat live readbacks from Oviond's project as the source of truth when docs and reality diverge.
- Prefer list endpoints with explicit query filters over vague search endpoints when possible.
- Do not assume attachment upload flows beyond URL-based attachment metadata without testing.

## Post-validation writeback
After the first real validation pass:
1. Update this skill if Oviond's live object model differs from assumptions.
2. Record durable Gleap operating facts in workspace memory when appropriate.
3. Promote only validated write flows into the default workflows.
