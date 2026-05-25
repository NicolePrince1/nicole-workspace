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

Default to **marker-only screenshots for Gleap/help-center articles**:

- Real screenshot with numbered markers only
- Put the numbered explanations in the article body, not inside the image
- Do not add “Open screenshot” links below images; Gleap expands images on click
- Avoid covering UI labels, buttons, form values, or important text with badges
- Crop tightly when a modal/drawer is the focus
- Oviond blue `#5676FF`, cyan `#75D2DA`, ink `#0B1020`
- Desktop viewport first: `1440x980`

Use side-panel annotations only for marketing explainers, social posts, internal QA summaries, or standalone images that must make sense outside an article.

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
- Does the article body explain every marker in text?
- Is the asset regenerated from JSON, not hand-edited?

Read `references/style-guide.md` when designing a new asset family or changing annotation style.
