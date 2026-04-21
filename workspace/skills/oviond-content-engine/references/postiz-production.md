# Postiz Production Notes

## Purpose

Use this file when Postiz is part of live Oviond content operations.
It is the practical ops layer for auth, verification, safety, and publishing discipline.

## Canonical environment variables

Use these names:

```env
POSTIZ_API_KEY=
POSTIZ_API_URL=https://api.postiz.com
POSTIZ_MCP_URL=https://mcp.postiz.com/mcp
POSTIZ_MCP_AUTH_TYPE=bearer
POSTIZ_MCP_BEARER_TOKEN=
```

### Important typo trap

The MCP URL variable should be `POSTIZ_MCP_URL`, not `POSTIZ_MCP_UR`.
If the typo exists, fix it in AlphaClaw even if a local fallback script can still recover.

## Current Oviond validation workflow

Before trusting live automation, run:

```bash
python3 /data/.openclaw/workspace/skills/oviond-content-engine/scripts/postiz_healthcheck.py
```

This checks:
- API key presence
- API connectivity via `/public/v1/is-connected`
- live integrations via `/public/v1/integrations`
- MCP endpoint reachability with bearer auth

## What "healthy" looks like

- `connected: true` from the Postiz API
- expected social accounts visible in integrations
- MCP endpoint reachable and responding, even if a raw GET returns a session-handshake error

A raw MCP `400` complaining about a missing or invalid session is usually fine for a low-level probe. That means the endpoint is alive and expects proper MCP session flow.

## Current default operating mode

- use Postiz Cloud
- create drafts first
- batch schedules after review
- use immediate publish only when explicitly approved or clearly delegated

## Current known Oviond channels

At the time of live validation, these channels were visible through the Postiz API:
- LinkedIn Page
- Facebook Page
- X
- YouTube

Do not assume any new channel exists until the healthcheck or integrations list confirms it.

## Rate-limit discipline

Postiz public API limit is documented as 30 requests per hour.

Work accordingly:
- batch related writes
- avoid one-post-at-a-time loops when a larger grouped write is possible
- avoid noisy polling
- fetch integrations once, cache mentally for the current task, and move on

## Publishing safety rules

- do not publish live by default just because auth works
- prefer `draft` and `schedule`
- double-check the destination integration before writing
- make sure the content is channel-native, not copy-pasted sludge
- verify claims, screenshots, and links before queueing

## Recommended channel order for Oviond

1. LinkedIn
2. X
3. Facebook
4. YouTube only when there is an actual video asset or announcement worth posting

## Practical workflow

1. run the Postiz healthcheck
2. inspect integrations
3. confirm which channels are in scope for the batch
4. prepare the primary asset and channel adaptations
5. prepare visuals if needed through `oviond-design-director`
6. queue drafts or scheduled posts in Postiz
7. pull analytics later and feed the learning loop

## If the check fails

### API fails
- verify `POSTIZ_API_KEY`
- verify `POSTIZ_API_URL`
- make sure AlphaClaw envars were saved and applied
- restart the gateway if the new env values were added moments ago

### MCP fails
- verify `POSTIZ_MCP_URL`
- verify `POSTIZ_MCP_BEARER_TOKEN`
- confirm the URL is the exact one from Postiz's developer settings
- remember that MCP requires a proper client session, so a raw probe is only a partial check
