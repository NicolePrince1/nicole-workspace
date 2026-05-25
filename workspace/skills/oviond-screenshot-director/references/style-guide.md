# Oviond screenshot and annotation style guide

## Purpose

Create beautiful, consistent screenshots that help users understand the product quickly. These images support Gleap help articles, Mintlify docs, launch assets, social posts, ads, and internal QA.

## Standard formats

- Help-center desktop: base capture `1440x980`; side-panel output about `1940x980`.
- Marketing/social landscape: `1600x1000` or `1920x1080`.
- Keep source JSON beside every output PNG.

## Annotation rules

- For Gleap/help-center articles, prefer marker-only screenshots plus numbered explanations in the article body.
- Do not place instruction text or right-side explanation panels inside help-center screenshots.
- Do not add separate “Open screenshot” links below Gleap images; Gleap expands images on click.
- Side-panel explanation images are for marketing, social, internal QA, and standalone explainers only.
- One screenshot should explain 3–5 things, not 12.
- Do not cover customer data, totals, email addresses, tokens, billing details, or private account names.
- Use fake/demo data or blur sensitive areas.

## Visual system

- Primary: `#5676FF`
- Accent: `#75D2DA`
- Text: `#0B1020`
- Background: `#F8FAFC`
- Marker stroke: 5px for screenshots, 4px for marketing visuals.
- Marker radius: 14–18px.
- Right panel should be calm, high-contrast, and readable.

## Product capture rules

- Capture in a stable test/demo account.
- Use seeded demo clients and fake-safe names.
- Prefer deterministic routes and selectors.
- Do not depend on hover-only states unless the article is specifically about hover behavior.
- Capture the smallest useful area: full page only when context matters.

## Marketing image rules

- Product-preview visuals can be real screenshots or mock UI.
- Avoid tiny unreadable UI text.
- Use generous whitespace.
- Keep one clear message per asset.
- QA for mobile crop safety if the image will be used on social.
