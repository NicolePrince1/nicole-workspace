---
name: browser-use
description: Browser-oriented guidance for workspaces that may or may not have a first-class browser tool. Use when the user wants website inspection, browsing, extraction, screenshots, or form interaction. In this workspace, do not assume a `browser` tool exists; prefer the actually available web/UI tools, or only use first-class browser instructions if that tool is explicitly enabled.
---

# Browser / web work

This workspace does **not** guarantee a first-class `browser` tool.

## Default rule for this workspace

For browser-like work, prefer the tools that actually exist here:
- `web_search` for discovery and result finding
- `web_fetch` for reading and extracting page content
- `canvas` for OpenClaw Canvas/UI rendering, navigation, evaluation, and snapshots when a page or UI needs to be visually inspected through Canvas

## Do not assume a `browser` tool

Do **not** write instructions that depend on a `browser` tool unless that tool is explicitly available in the current workspace/runtime.

If a request truly requires first-class browser automation and this workspace does not expose that tool, say so plainly instead of pretending it exists.

## Practical guidance

- Use `web_search` first when the task is research or finding the right page.
- Use `web_fetch` when the goal is to read or extract the contents of a page quickly.
- Use `canvas` when visual inspection, rendered-state checks, page snapshots, or lightweight page interaction is needed through the Canvas flow.
- Do not default to any legacy `browser-use` CLI workflow.
- Do not invent browser actions (`act`, `snapshot`, `screenshot`, tabs, profiles) unless the actual toolset for the current workspace supports them.

## Outcome

This skill exists to keep browser-related work grounded in the real tool availability of the workspace instead of assuming a nonexistent first-class browser tool.