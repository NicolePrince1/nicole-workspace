# Postiz Cloud

## Recommendation

Default to **Postiz Cloud**, not self-hosted.

Reason:
- faster to get live
- less infra drag
- less failure surface
- no need to own Docker, storage, Redis, Postgres, Temporal, and update overhead for a problem that is not our differentiator

Hosted does **not** remove the real setup work around platform apps, OAuth, permissions, and business verification. It simply removes the unnecessary infrastructure tax.

## Plan recommendation

### Start here
- **Team ($39/mo)** is the best default if this is mainly Oviond's own channels and one small operating team.

### Upgrade trigger
Move to **Pro ($49/mo)** or higher if one of these becomes true:
- more than 10 connected channels are needed
- multiple brands or environments are being managed
- higher AI-image or AI-video usage becomes useful
- more channel sprawl makes the Team cap annoying

### Do not overbuy early
Ultimate is great for agency-scale multi-client use, but it is overkill if this is just Oviond plus a handful of owned channels.

## Initial setup order

1. create the Postiz Cloud workspace
2. generate an API key in `Settings > Developers > Public API`
3. store the API key in approved secret storage or OpenClaw envars, never in tracked workspace files
4. connect channels in this order:
   - LinkedIn Page and optionally LinkedIn profile
   - Facebook Page
   - Instagram if needed
   - X
   - Threads later if useful
5. verify account names carefully so the agent does not post to the wrong property
6. create a simple naming convention for channels and posting groups

## Platform caveats

### Meta
- Facebook and Instagram can share the same Meta app
- business verification or advanced permissions may still be required for production-grade use

### LinkedIn
- Page posting can require app verification and the right products/scopes
- token refresh capability depends on proper app setup

### X
- still awkward relative to other networks
- media posting has historical API weirdness, so treat setup and testing carefully

## Agent operating rule

Use Postiz as the execution rail.
Do not let Postiz decide the strategy.

## Preferred workflow inside Postiz

### For normal use
- create drafts first
- batch schedule approved posts
- use customer groups or channel groupings if helpful
- use calendar view to sanity-check spacing and overlap

### For API-driven use
Prefer the public API over brittle UI automation.

Core sequence:
1. list integrations
2. confirm the right integration IDs
3. check platform schema/settings before posting
4. upload media if needed
5. create draft or scheduled post payloads
6. retrieve analytics later

## API discipline

### Rate limit
The public API is documented at **30 requests per hour**.

Work accordingly:
- batch post creation when possible
- do not spray one request per tiny action
- upload media once, reuse where sensible
- prefer fewer larger write operations

### Content formatting
The API expects platform content in HTML-like blocks for some flows. Wrap lines properly and validate the payload shape before posting.

### Default post mode
Prefer:
- `draft` for review-heavy work
- `schedule` for approved queues
- `now` only for explicitly approved immediate publishing

## Suggested first operating pattern

Start with a boring reliable loop:
- 1 blog-derived LinkedIn post
- 1 native X post or thread
- 1 selective Facebook version
- all queued in Postiz
- analytics reviewed after publication

Then expand once the system proves stable.

## Self-hosting note

Self-host only if one of these becomes materially important:
- data/control requirements justify the operational cost
- there is a need for heavy customization not available in Cloud
- channel volume or multi-client complexity makes self-host ROI obvious

Until then, hosted is the adult decision.