# Figma integration notes

## Confirmed on 2026-04-16

- `FIGMA_ACCESS_TOKEN` is configured in the runtime environment.
- Token validation succeeded against `GET /v1/me`.
- Authenticated identity: `chris@oviond.com` / handle `chris`.

## Important API limitations

- Team IDs are not discoverable through the standard projects endpoint flow.
- The REST surface is strong for reading files, file trees, node JSON, image exports, components, styles, variables, comments, webhooks, and analytics.
- It is **not** the right tool for fully managing the entire workspace structure from scratch.

## Practical implication

For production use, we should:
1. create or identify the main Oviond design-system project in Figma UI
2. capture one team/project/file URL
3. use this local ops project to inspect, export, and automate around that source of truth

## Recommendation on Figma Community skills

Promising later, but not the starting point.

Use them only after we lock:
- brand system
- component library
- template families
- naming conventions
- export workflow

Otherwise we risk building the design stack on third-party cleverness instead of our own system.
