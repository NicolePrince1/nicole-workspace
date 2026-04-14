# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

## Current Local Setup Notes

### TTS

- Default provider: OpenAI TTS via `messages.tts` in `openclaw.json`.
- Keep this section to provider/setup mechanics only; user voice preferences belong in `MEMORY.md`.

### Google Workspace

- Token helper: `/data/.openclaw/secrets/gws-token.js`
- Credentials and helper material live in gitignored secret storage under `/data/.openclaw/secrets/`.
- Handle Google Workspace tasks through the live `gog` skill/operator path rather than a missing local wrapper.
- Durable platform/access status belongs in `MEMORY.md`; keep this section for local operator mechanics only.

### Stripe

- Preferred secret location: OpenClaw Envars as `STRIPE_SECRET_KEY`.
- Stripe is not one of the workspace-local skills.
- The managed Stripe analysis skill lives under the managed root at `/data/.openclaw/skills/stripe-reader/`.
- Current helper script: `/data/.openclaw/skills/stripe-reader/scripts/stripe_analytics.py`.
- Capability/access posture belongs in `MEMORY.md`; keep this section for local secret/path notes only.

### Sequenzy

- Local skill lives at `skills/sequenzy/`.
- Preferred credential source: OpenClaw Envars via `SEQUENZY_API_KEY`.
- Use `skills/sequenzy/scripts/live_audit.py` for repeatable read-only validation.
- Live credential connection is now working; keep this section to local operator mechanics only.

### Meta

- Meta token material lives in gitignored secret storage under `/data/.openclaw/secrets/`.
- Local skill lives at `skills/meta/`.

### Google Analytics

- Local skill lives at `skills/google-analytics/`.
- Token helper material lives in gitignored secret storage under `/data/.openclaw/secrets/`.
- Keep this section to local helper/path mechanics only; project history and auth state belong in `MEMORY.md` or the relevant skill docs.

### Google Ads

- Local skill lives at `skills/google-ads/`.
- Preferred credential source: OpenClaw Envars via `GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT`.
- Keep this section to local helper/path mechanics only; project history, auth state, and incident-specific blockers belong in `MEMORY.md` or `skills/google-ads/SKILL.md`.

---

Add whatever helps you do your job. This is your cheat sheet.
