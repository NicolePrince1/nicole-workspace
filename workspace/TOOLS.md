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

### Google Workspace

- The bootstrap note saying no Google accounts are configured is stale.
- Live access is working via service-account impersonation of `nicole@oviond.com` through `gws-nicole`.
- Verified on 2026-03-10:
  - Gmail profile resolves for `nicole@oviond.com`
  - Primary Calendar is accessible
  - Google Drive file listing works, including the `Nicole Prince Control` doc
- Wrapper path: `/usr/local/bin/gws-nicole`
- Token helper: `/data/.openclaw/secrets/gws-token.js`
- This is a local clarification note only; the AlphaClaw-managed bootstrap text should be corrected through the product-owned regeneration path, not by editing managed bootstrap files directly.

---

Add whatever helps you do your job. This is your cheat sheet.
