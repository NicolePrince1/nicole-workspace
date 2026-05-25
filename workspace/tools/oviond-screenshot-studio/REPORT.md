# Oviond Screenshot Studio — initial build

## What works now

- Playwright Chromium is installed and working.
- `capture-url.js` captures real rendered web pages at fixed viewports.
- `annotate.js` creates demo product and marketing visuals and supports freeform overlay annotations.
- `panel-annotate.js` creates the preferred help-center style: screenshot left, numbered markers, explanation panel right.
- Sample outputs were generated under `outputs/annotated/`.

## Samples

- `outputs/annotated/mock-clients-panel.png` — help-center style product walkthrough sample.
- `outputs/annotated/marketing-card-panel.png` — static marketing creative annotation sample.
- `outputs/annotated/docs-introduction-panel-v2.png` — real Playwright browser capture from `docs.oviond.com/introduction` with generated annotations.

## Current limitation

Real `app.oviond.com` captures still need a stable QA login/session and demo data. The tooling is ready; the next step is capturing real product screens from a test account and replacing mock/demo samples with real app flows.

## Recommended next pass

1. Create/confirm a clean Oviond QA account with seeded demo clients.
2. Capture the first real flows:
   - Clients list
   - Add client
   - Connect data source
   - Create report
   - Add widget
   - Share report
   - Schedule automation
3. Upload approved screenshot assets to the chosen public asset host.
4. Attach images to the corresponding Gleap articles.
