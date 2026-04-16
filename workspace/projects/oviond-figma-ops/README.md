# Oviond Figma Ops

Local operator project for connecting Nicole's workflow to Figma through the live `FIGMA_ACCESS_TOKEN`.

## What this is for

This project gives us a clean, reusable way to:
- validate the Figma token
- inspect Figma team projects
- inspect files inside a project
- pull file metadata and node JSON
- export node renders for review or production handoff

## Current status

- `FIGMA_ACCESS_TOKEN` is live and valid for `chris@oviond.com`
- Figma REST is available from this workspace
- Important limitation: Figma's REST API does **not** let us programmatically discover team IDs, and it is not a good path for creating new projects/files in the workspace. We need one real Figma URL from the Oviond team workspace to anchor the automation.

## Scripts

### Validate token

```bash
node projects/oviond-figma-ops/scripts/validate-token.mjs
```

### List projects in a team

```bash
node projects/oviond-figma-ops/scripts/team-projects.mjs <team_id>
```

### List files in a project

```bash
node projects/oviond-figma-ops/scripts/project-files.mjs <project_id>
```

### Get file metadata

```bash
node projects/oviond-figma-ops/scripts/file-meta.mjs <file_key>
```

### Parse IDs from a Figma URL

```bash
node projects/oviond-figma-ops/scripts/parse-url.mjs <figma_url>
```

### Get a shallow document tree

```bash
node projects/oviond-figma-ops/scripts/file-tree.mjs <file_key> [depth]
```

### Export rendered images for one or more nodes

```bash
node projects/oviond-figma-ops/scripts/export-images.mjs <file_key> <node_ids_csv> [format] [scale]
```

Example:

```bash
node projects/oviond-figma-ops/scripts/export-images.mjs abc123 1:2,1:8 png 2
```

Exports are written to `projects/oviond-figma-ops/exports/`.

## Recommended next step in Figma

Create or share one Figma team/project URL for the Oviond design system, for example:
- team URL, so we can capture the `team_id`
- project URL, so we can capture the `project_id`
- or a starter file URL, so we can begin reading and exporting immediately

## Recommended Figma operating model

Use Figma as the production system, not the creative brain.

- **Nicole**: briefs, art direction, QA, asset family logic
- **AI generation**: concept and source visual creation
- **Figma**: components, templates, overlays, resizing, exports, library management

## Out-of-the-box skill stance

Do **not** install a pile of Figma Community skills on day one.

Start with:
1. core Figma structure
2. a clean brand library
3. template families
4. only then add a few skills/plugins that clearly save time without fragmenting the workflow

The right first-wave add-ons are likely to be in these categories:
- batch rename / layer cleanup
- mockup or frame export helpers
- image compression / asset export helpers
- icon management
- content population helpers
- accessibility or contrast checking

What I do **not** recommend as the foundation:
- relying on community skills to define the brand system
- using AI-in-Figma tools as the main creative director
- installing 10 overlapping generation tools and hoping consistency emerges
