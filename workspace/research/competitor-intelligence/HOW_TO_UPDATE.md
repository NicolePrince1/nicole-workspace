# How to Update Competitor Intelligence

Last updated: 2026-05-07

## Quick workflow

1. Open `competitor-universe.csv` and find the competitor.
2. Open its profile in `competitors/`.
3. Re-check primary sources: pricing page, docs, help center, API/MCP docs, product pages.
4. Update the profile with a new `Last verified` date and source URLs.
5. If the change affects a broader pattern, update the relevant category doc in `categories/`.
6. If pricing/packaging changed, update `pricing/pricing-and-gate-map.md`.
7. If the launch implication changed, update `positioning/launch-positioning-implications.md` and/or `positioning/battlecards.md`.
8. Add any new source URL to `sources/source-log.md`.
9. Commit the changes.

## What to re-check first

For launch-critical competitors, verify these weekly until launch:

- AgencyAnalytics pricing and feature gates.
- Whatagraph source-credit pricing and AI/API gates.
- DashThis dashboard/source pricing and AI add-ons.
- Swydo data-source pricing and “all features included” claims.
- Databox pricing, white-label add-ons, AI/MCP/API positioning.
- Supermetrics API/MCP/AI-ready data positioning.
- Porter/Dataslayer/Coupler/Windsor/TMR MCP and AI destination changes.
- Semrush MCP and API-unit packaging.
- SE Ranking Agency Pack/API/MCP packaging.

## Update standard

Every meaningful update should answer:

- What changed?
- Is it a pricing change, feature gate change, positioning change, AI/API/MCP change, or source correction?
- Does this make Oviond’s simple client-count/all-features-included position stronger or weaker?
- Does public launch copy need to change?

## Do not do this

- Do not rely on AI summaries without checking primary pages.
- Do not use competitor claims as facts unless they are clearly sourced.
- Do not add secrets, customer data, screenshots from logged-in accounts, or private material.
- Do not write public attack copy here; this is intelligence, not a smear file.
