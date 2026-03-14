---
name: browser-use
description: Use the built-in first-class browser tool for website navigation, interaction, screenshots, extraction, and form filling. Trigger when the user needs browser automation or page inspection. Do not default to the legacy browser-use CLI workflow.
---

# Browser Automation

Use the first-class `browser` tool by default.

## Default rule

For browser work, always prefer the built-in `browser` tool for:
- navigating websites
- clicking and typing
- taking screenshots
- extracting page information
- filling forms
- checking logged-in pages when appropriate

## Do not default to the legacy CLI

Do **not** reach for the `browser-use` CLI unless the user explicitly asks for that specific tool or there is a very unusual edge case the first-class `browser` tool cannot handle.

The normal path is:
1. open/focus a tab with the `browser` tool
2. inspect with `snapshot`
3. interact with `act`
4. capture with `screenshot` if needed

## Practical guidance

- Prefer `profile="user"` when existing host-browser logins matter and user interaction is available.
- Prefer the isolated default browser when login state does not matter.
- Keep automation simple and local to the current task.
- Avoid adding extra browser stacks, cloud sessions, tunnels, cookie-sync flows, or CLI-specific workflows unless explicitly required.

## Outcome

This skill exists only to point browser tasks toward the first-class `browser` tool and away from unnecessary extra complexity.
