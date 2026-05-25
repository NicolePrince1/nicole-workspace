---
name: oviond-screenshot-director
description: Capture, annotate, QA, and manage consistent Oviond product screenshots and static marketing visuals for help center articles, launch docs, social posts, ads, and product explainers. Use when work involves screen grabs, screenshot annotations, visual walkthroughs, screenshot style systems, product-image QA, or adding images to Gleap/Mintlify/help content.
---

# Oviond Screenshot Director

Use this skill for production screenshot and annotation work.

## Core rule

Use the deterministic local studio first:

`/data/.openclaw/workspace/tools/oviond-screenshot-studio/`

It provides:

- `capture-url.js` — Playwright browser capture from real URLs
- `annotate.js` — product mock/static marketing image generation and freeform overlays
- `panel-annotate.js` — preferred side-panel annotation layout for scalable help-center images

## Workflow

1. Capture or generate the base image.
2. Remove/avoid sensitive customer data.
3. Annotate with numbered markers and a side explanation panel.
4. QA the image with vision before publishing.
5. Store source JSON next to output image so the asset can be regenerated.
6. Upload to the approved public asset host before embedding in Gleap/Mintlify.

## Preferred output style

Default to side-panel annotations for help center images:

- Screenshot on the left
- Numbered markers on the screenshot
- Explanations in a clean right-side panel
- No label boxes over product text unless unavoidable
- Oviond blue `#5676FF`, cyan `#75D2DA`, ink `#0B1020`
- Desktop viewport first: `1440x980`

For marketing/static visuals, use the same system but allow wider canvases and product-preview compositions.

## Capture examples

```bash
cd /data/.openclaw/workspace/tools/oviond-screenshot-studio
node capture-url.js outputs/example-capture.json
node panel-annotate.js outputs/example-panel.json
```

## Login/product captures

For `app.oviond.com`, use a QA-safe account only. Avoid destructive actions unless Chris explicitly approves them.

When logging in by magic link, use Nicole's Google Workspace/Gmail access only if the task explicitly needs it and the account is authorized.

## QA gates

Before final use, check:

- Does every marker point to the correct UI element?
- Does the overlay avoid hiding important product text?
- Is any real customer/private data visible?
- Is the crop focused enough for the article?
- Are title, subtitle, and callouts short enough?
- Is the asset regenerated from JSON, not hand-edited?

Read `references/style-guide.md` when designing a new asset family or changing annotation style.
