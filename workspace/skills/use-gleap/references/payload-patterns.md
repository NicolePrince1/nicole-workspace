# Gleap payload patterns

Use these as starting points. Read the live object first, then patch only the fields you intend to change.

## 1. Update a ticket

```json
{
  "status": "OPEN",
  "priority": "HIGH",
  "processingTeam": "TEAM_ID",
  "processingUser": "USER_ID",
  "tags": ["billing", "vip"],
  "dueDate": "2026-04-10T12:00:00.000Z"
}
```

Notes:
- Do not overwrite many fields blindly.
- Preserve the existing tags if you are only adding one.
- Confirm the real status/type vocabulary from live tickets first.

## 2. Add an internal note

```json
{
  "ticket": "TICKET_ID",
  "comment": "Internal note: investigating Stripe webhook mismatch.",
  "isNote": true,
  "sendToChannel": false
}
```

Notes:
- Use this as the safest default write for early support work.
- Keep `sendToChannel` explicit until live behavior is validated.

## 3. Add an agent reply draft or customer-visible response

```json
{
  "ticket": "TICKET_ID",
  "comment": "Thanks — we found the cause and are fixing it now.",
  "isNote": false,
  "sendToChannel": true
}
```

Notes:
- Treat this as risky until Oviond validates outbound behavior.
- If a channel-specific send needs extra metadata, read a live example first.

## 4. Add a customer-side message via session

```json
{
  "ticket": "TICKET_ID",
  "session": "SESSION_ID",
  "comment": "I tried again and it still fails.",
  "sendToChannel": false
}
```

Notes:
- Use this only when the intent is truly to create a customer-side comment.

## 5. Create a tracker ticket

```json
{
  "title": "Improve attribution / UTM visibility",
  "description": "Aggregate related customer requests around missing campaign attribution context.",
  "type": "FEATURE_REQUEST",
  "linkedTicketIds": ["TICKET_1", "TICKET_2", "TICKET_3"]
}
```

Notes:
- Treat tracker tickets as the default public roadmap object.
- Read current tracker ticket examples first so `type` matches reality.

## 6. Generate tracker data with AI

```json
{
  "sourceTicketId": "TICKET_ID",
  "type": "FEATURE_REQUEST"
}
```

Use this for summarization help, not as a substitute for actual review.

## 7. Create or update a help center collection

```json
{
  "title": "Google Ads",
  "description": "Help articles for Google Ads reporting and troubleshooting.",
  "parent": "PARENT_COLLECTION_ID",
  "targetAudience": "all"
}
```

Notes:
- Validate whether `parent` should be omitted or null for top-level collections.
- Publish/unpublish is a separate operation.

## 8. Create or update a help center article

```json
{
  "title": "Why your Google Ads cost looks different in Oviond",
  "description": "Explain cost mismatches, attribution windows, and sync timing.",
  "plainContent": "Short plain-text fallback or summary.",
  "content": {
    "type": "doc",
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "type": "text",
            "text": "Write the actual article content in the live structure Gleap expects."
          }
        ]
      }
    ]
  },
  "isDraft": true,
  "tags": ["google-ads", "troubleshooting"],
  "targetAudience": "all"
}
```

Notes:
- Do not assume the rich `content` structure until you inspect a real article.
- Prefer draft mode until reviewed.

## 9. Snooze a ticket

```json
{
  "duration": 48
}
```

Assume duration is hours only if live validation confirms it.

## 10. Toggle help center publish status

```json
{
  "unpublished": false
}
```

Notes:
- This is customer-visible. Ask before using it.

## 11. Statistics requests

Facts example:
```text
GET /statistics/facts?chartType=NEW_TICKETS_COUNT&timezone=Africa/Johannesburg&startDate=2026-04-01T00:00:00.000Z&endDate=2026-04-07T23:59:59.999Z
```

Lists example:
```text
GET /statistics/lists?chartType=TEAM_PERFORMANCE_LIST&timezone=Africa/Johannesburg&startDate=2026-04-01T00:00:00.000Z&endDate=2026-04-07T23:59:59.999Z
```

Use only documented enum names.
