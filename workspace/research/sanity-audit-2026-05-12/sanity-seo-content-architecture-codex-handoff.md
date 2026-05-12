# Oviond Sanity + Astro SEO Content Architecture Handoff

Date: 2026-05-12  
Prepared by: Nicole Prince  
Audience: Codex / website implementation agent  
Scope: strategy and implementation plan only. Do **not** write to Sanity as part of this handoff.

## 1. Objective

Build Oviond into the best SEO property in the agency reporting niche while protecting existing WordPress-era URL equity now stored in Sanity.

The winning strategy is **not** to rebuild the site as a generic SaaS brochure. It is to turn the current Sanity content model into a structured SEO operating system:

- preserve every useful existing URL first;
- make current content better without breaking routes;
- use existing Sanity entities like data sources, reporting templates, reviews, CTAs, feature sections, and logo clouds as reusable proof modules;
- add only the lean schema and frontend routing needed to cover high-intent SEO gaps;
- avoid live editing / Presentation / Visual Editing complexity for now;
- keep Astro static, fast, simple, and reliable.

## 2. Source evidence to use

Use these local artifacts as source-of-truth inputs:

- `research/sanity-audit-2026-05-12/oviond-sanity-astro-strategy-read.md`
- `research/sanity-audit-2026-05-12/sanity-current-route-inventory.json`
- `research/seo/full-audit-2026-05-12/deliverables/SEO_Strategy_Brief.md`
- `research/seo/full-audit-2026-05-12/deliverables/01_Cluster_Map.csv`
- `research/seo/full-audit-2026-05-12/deliverables/02_Priority_Roadmap.csv`
- `research/seo/full-audit-2026-05-12/deliverables/04_Content_Briefs.csv`
- `research/seo/full-audit-2026-05-12/deliverables/08_Oviond_Current_Pages.csv`
- `research/seo/competitor-keyword-cluster-audit-2026-05-12.md`

## 3. Non-negotiable route principle

**Do not casually move existing WordPress URLs.**

Most imported Sanity content already mirrors current WordPress routes via `migration.legacyUrl`, `slug.current`, or `routePath`. That is valuable. Preserve it unless there is a deliberate 301 plan backed by traffic/indexing checks.

### Route preservation rules

| Content type | Current / legacy URL pattern | Recommended action |
|---|---|---|
| Homepage / marketing pages | `routePath`, e.g. `/`, `/blog/`, `/marketing-reporting/`, `/marketing-dashboards/` | `routePath` wins. Keep exact paths. |
| Blog posts | root slug, e.g. `/client-reporting-software/`, `/automated-marketing-reports/` | Keep root URLs. Do **not** move all posts under `/blog/`. |
| Data sources | `/data-sources/{slug}/` | Keep exact routes. Enhance templates and internal links. |
| Docs | `/doc/{slug}/` | Keep exact routes. No-index selectively only if these are not marketing assets. |
| Legal | `/legal/{slug}/` | Keep exact routes and no-index. |
| Existing solution pages | `/solution/{slug}/` where imported from WordPress | Keep or 301 only with deliberate route map. Do not accidentally switch singular/plural. |
| Pricing | `/pricing/` | Implement explicit route despite no slug. |
| New SEO solution pages | `/solutions/{slug}/` | Use only for genuinely new pages that do not already have a strong legacy equivalent. |
| New comparison pages | `/alternatives/{competitor}-alternative/` | New route family. Do not overwrite old comparison posts until reviewed. |
| New glossary pages | `/glossary/{slug}/` or `/metrics/{platform}-{metric}/` | Phase 3+ only. |

### Legacy-first canonical rule

If a roadmap keyword already has a close existing WordPress-era URL, upgrade the existing URL first instead of creating a duplicate clean URL.

Examples:

| Target intent | Existing URL to preserve / upgrade | Avoid initially |
|---|---|---|
| client reporting software | `/client-reporting-software/` | `/solutions/client-reporting-software/` |
| automated marketing reports | `/automated-marketing-reports/` | `/solutions/automated-marketing-reports/` |
| marketing reporting software | `/marketing-reporting/` and homepage support | `/solutions/marketing-reporting-software/` unless SERP data proves need |
| marketing dashboard software | `/marketing-dashboards/` | `/solutions/marketing-dashboard-software/` unless SERP data proves need |
| PPC report template | `/building-the-perfect-ppc-report/` as immediate refresh candidate | `/templates/ppc-report-template/` until cannibalization is resolved |
| AgencyAnalytics alternative | `/agencyanalytics-and-oviond-stacking-up-the-software/` as legacy support; new modern page can be `/alternatives/agencyanalytics-alternative/` | leaving old page orphaned |
| DashThis alternative | `/dashthis-and-oviond-stacking-up-the-software/` as legacy support; new modern page can be `/alternatives/dashthis-alternative/` | leaving old page orphaned |
| Looker Studio alternative | `/google-data-studio-and-oviond-stacking-up-the-software/` as legacy support; new modern page can be `/alternatives/looker-studio-alternative/` | unreviewed duplicate content |

The rule: **preserve first, expand second, redirect only with evidence.**

## 4. What exists in Sanity now

The current Sanity model is already strong enough to build on:

- `marketingPage`: 9
- `solutionPage`: 3
- `blogPost`: 217
- `dataSource`: 62
- `reportingTemplate`: 35
- `customerReview`: 54
- `reviewSource`: 2
- `productFeature`: 5
- `logoCloud`: 1
- `reusableCta`: 1
- `pricingPage`: 1
- `docPage`: 16
- `legalPolicy`: 9
- `navigation`: 7
- `sanity.imageAsset`: 1105

Reusable section/module primitives already available:

- page hero
- solution hero
- content/media section
- feature grid
- feature showcase
- feature spotlight
- comparison section
- workflow showcase
- template collection
- data source collection
- reviews slider/grid
- logo cloud section
- FAQ section
- CTA band
- related content
- stats
- CTAs
- image-with-alt
- SEO object

This is enough to build a serious SEO system without making Sanity heavy.

## 5. What not to build now

Keep the CMS lean. Do **not** add:

- Sanity Presentation Tool
- Visual Editing
- live preview routes
- stega overlays
- SSR-only editing flows
- complex release workflows
- page-builder soup with unlimited arbitrary modules
- client-side token usage
- AI-generated public content automation

For now: static Astro + Sanity Content Lake + explicit route map + webhook rebuilds is the right architecture.

## 6. Core SEO architecture

Oviond should own seven linked SEO layers.

### Layer 1 — Category money pages

Purpose: capture highest-intent agency reporting software searches.

Use existing URLs where possible:

- `/` — brand/category homepage: “simple marketing reporting software for agencies”
- `/marketing-reporting/` — marketing reporting software hub
- `/client-reporting-software/` — upgrade existing post into client reporting software money page
- `/automated-marketing-reports/` — upgrade existing post into automation money page
- `/marketing-dashboards/` — dashboard hub
- `/how-to-white-label-your-digital-marketing-reports-and-dashboards/` and related white-label posts — refresh and decide whether to consolidate into a white-label hub

New pages only where no strong existing URL exists:

- `/solutions/agency-reporting-software/`
- `/solutions/marketing-agency-reporting-software/`
- `/solutions/automated-client-reporting/`
- `/solutions/white-label-reporting-software/`
- `/solutions/white-label-dashboard-software/`
- `/solutions/client-dashboard-software/`

Page recipe:

1. Hero with clear pain + outcome.
2. “Who this is for” section for agencies.
3. Problem section: reporting chaos, manual work, client confidence.
4. Product proof: dashboards, reports, white label, automation, templates.
5. Related data sources pulled from `dataSource`.
6. Related templates pulled from `reportingTemplate`.
7. Reviews/proof from `customerReview`.
8. FAQ section.
9. CTA band.
10. Internal links to templates, integrations, alternatives, pricing.

### Layer 2 — Channel clusters

Purpose: win “SEO reporting”, “PPC reporting”, and “social reporting” intent.

Priority clusters from keyword research:

- SEO reporting: strongest aggregate opportunity.
- Paid ads / PPC reporting.
- Social media reporting.
- Dashboard / KPI reporting.

Recommended approach:

- Use existing blog URLs as support where they already match intent.
- Create new `/solutions/` pages only when there is no current equivalent.
- Use `dataSource` and `reportingTemplate` as embedded proof modules on every page.

Priority builds:

- `/solutions/seo-reporting-software/`
- `/solutions/seo-reporting-tool/`
- `/solutions/seo-reporting-for-clients/`
- `/solutions/google-search-console-dashboard/`
- `/solutions/ppc-reporting-tool/`
- `/solutions/ppc-reporting-software/`
- `/solutions/google-ads-reporting-tool/`
- `/solutions/facebook-ads-reporting-tool/`
- `/solutions/meta-ads-reporting/`
- `/solutions/social-media-reporting-tool/`
- `/solutions/social-media-reporting-software/`
- `/solutions/instagram-analytics-report/`
- `/solutions/linkedin-ads-reporting/`
- `/solutions/youtube-analytics-report/`

### Layer 3 — Data-source / integration pages

Purpose: use the existing 62 `dataSource` docs as structured SEO landing pages.

Current route pattern should remain:

- `/data-sources/google-ads/`
- `/data-sources/google-analytics-4/`
- `/data-sources/google-search-console/`
- `/data-sources/facebook-ads/`
- `/data-sources/instagram-ads/`
- `/data-sources/linkedin-ads/`
- `/data-sources/shopify/`
- etc.

Enhance the data-source page template. Each data-source page should include:

1. “Connect {source} to Oviond” hero.
2. What data/metrics can be reported.
3. Common agency reporting use cases.
4. Related report templates.
5. Related solution pages.
6. Setup / workflow explanation.
7. FAQ.
8. CTA.

Do not create thin duplicate pages like `/data-sources/google-ads-reporting-tool/` if `/data-sources/google-ads/` can credibly rank. Instead, first expand the existing data-source page to target the reporting-tool intent.

Create separate pages only when SERP intent is meaningfully different, e.g. “Google Ads to Google Sheets” or “Google Ads report template”.

### Layer 4 — Reporting-template library

Purpose: turn the existing 35 `reportingTemplate` docs into a proper acquisition library.

Existing template docs include:

- Google Ads
- Google Analytics 4
- Google Search Console
- Facebook Ads
- Facebook Pages
- Instagram
- Instagram Ads
- LinkedIn
- LinkedIn Ads
- TikTok Ads
- PPC Dashboard
- Social Media Marketing
- Social Media Ads
- Digital Marketing Dashboard
- Stripe
- Shopify-adjacent/ecommerce templates
- Mailchimp, Brevo, MailerLite, etc.

Build a template hub and detail routes. Recommended route family:

- `/reporting-templates/`
- `/reporting-templates/{slug}/`

But for keyword-specific templates that already have a legacy URL with equity, preserve/upgrade the legacy URL first.

Priority template intents:

- SEO report template
- PPC report template
- Google Ads report template
- Facebook Ads report template
- GA4 report template
- Google Search Console report template
- social media reporting template
- client report template
- monthly marketing report template
- digital marketing report template
- white-label report template
- dashboard report template

Page recipe:

1. Template hero.
2. Preview/screenshot section.
3. KPIs included.
4. Data sources used.
5. How to automate it in Oviond.
6. When agencies should use it.
7. Related templates.
8. Related data sources.
9. FAQ.
10. CTA.

### Layer 5 — Competitor alternative pages

Purpose: capture bottom-funnel comparison traffic.

Create a lean `comparisonPage` document type or use a constrained `seoLandingPage` subtype. I recommend a dedicated `comparisonPage` type because these pages need repeatable structured fields.

Priority pages:

- `/alternatives/agencyanalytics-alternative/`
- `/alternatives/dashthis-alternative/`
- `/alternatives/whatagraph-alternative/`
- `/alternatives/swydo-alternative/`
- `/alternatives/looker-studio-alternative/`
- `/alternatives/supermetrics-alternative/`
- `/alternatives/two-minute-reports-alternative/`
- `/alternatives/databox-alternative/`
- `/alternatives/tapclicks-alternative/`
- `/alternatives/reportgarden-alternative/`
- `/alternatives/reporting-ninja-alternative/`
- `/alternatives/coupler-io-alternative/`
- `/alternatives/porter-metrics-alternative/`
- `/alternatives/power-my-analytics-alternative/`

Important: keep old “stacking up the software” posts alive initially. Link them into the new alternative pages or later 301 only after performance checks.

Comparison page fields:

- competitor name
- competitor logo/image
- competitor website URL
- primary keyword
- meta title/description
- summary verdict
- best-for comparison
- feature comparison rows
- pricing notes
- migration notes
- Oviond strengths
- honest Oviond limitations
- related alternatives
- CTA
- FAQ

Tone rule: honest and useful, not attack pages. These should convert because they are credible.

### Layer 6 — AI-assisted reporting pages

Purpose: capture emerging AI + reporting searches without overclaiming.

Build after core pages and alternatives. Do not claim product capabilities that are not live.

Potential URLs:

- `/solutions/ai-marketing-reporting/`
- `/solutions/ai-client-reporting/`
- `/solutions/ai-report-generator/`
- `/solutions/ai-marketing-report-generator/`
- `/solutions/ai-reporting-software/`
- `/solutions/chatgpt-marketing-reporting/`
- `/solutions/claude-marketing-reporting/`
- `/solutions/mcp-marketing-reporting/`
- `/solutions/connect-marketing-data-to-chatgpt/`
- `/solutions/connect-marketing-data-to-claude/`

Positioning:

> AI is only useful when it is grounded in reliable connector data, scheduled reporting workflows, permissions, white-label delivery, and client-ready context.

Avoid: “magic AI dashboard” fluff.

### Layer 7 — Metrics / dimensions glossary

Purpose: long-tail topical authority and internal-link fuel.

Phase 3+ only. Do not block launch on this.

Possible structure:

- `metricGlossaryEntry`
- `/glossary/{platform}-{metric}/`
- `/data-sources/{source}/metrics-and-dimensions/` if we want platform-level summaries

Start with platform-level pages before individual metric pages:

- GA4 metrics and dimensions
- Google Ads metrics and dimensions
- Facebook Ads metrics and dimensions
- Google Search Console metrics and dimensions
- LinkedIn Ads metrics and dimensions
- TikTok Ads metrics and dimensions

## 7. Minimal Sanity schema changes

Do not overbuild. Keep the current schema and add only what supports SEO operations.

### 7.1 Add shared SEO strategy fields

Add a reusable object, e.g. `seoStrategy`, to route-bearing docs:

- `primaryKeyword` string
- `secondaryKeywords` array of strings
- `searchCluster` string / enum
- `searchIntent` enum: commercial, transactional, informational, comparison, navigational
- `funnelStage` enum: TOFU, MOFU, BOFU, retention/support
- `canonicalUrlOverride` url/string
- `legacyUrl` already exists inside `migration`; keep using it
- `reviewStatus` enum: imported, needs_review, refreshed, launch_ready, noindex, redirect_candidate
- `lastSeoReviewAt` datetime
- `owner` string or reference later
- `notes` text

Do not require these fields for all existing docs immediately, but use validation warnings for launch-critical page types.

### 7.2 Add `comparisonPage`

Dedicated document type for `/alternatives/` pages.

Fields:

- title
- slug
- competitorName
- competitorUrl
- competitorLogo/imageWithAlt
- hero
- summaryVerdict
- bestForRows
- comparisonRows
- pricingNotes
- migrationNotes
- oviondStrengths
- oviondLimitations
- relatedCompetitors
- sections
- FAQ
- CTA
- SEO
- seoStrategy

### 7.3 Add optional `customerStory`

Not urgent for first SEO launch, but important for conversion and proof.

Fields:

- customer/company name
- industry
- agency size
- problem
- solution
- result
- quote
- related features
- related templates
- related data sources
- SEO

### 7.4 Add `redirect` discipline

A `redirect` document type already exists. Codex should ensure the frontend/build layer can export these redirects to the hosting platform.

Redirect fields should include:

- fromPath
- toPath
- statusCode: 301 or 302
- source
- notes

Redirect governance:

- 301 only when a page is intentionally consolidated.
- Never redirect high-value legacy pages without checking GSC/GA/Search Console data.
- Keep a generated redirect manifest in the repo.

### 7.5 Do not add heavy preview fields

No Presentation Tool, no live editing, no draft-mode complexity for now.

## 8. Astro implementation plan

### 8.1 Static routing

Use Astro static generation with explicit route builders:

- `src/pages/index.astro` for homepage from `marketingPage` routePath `/`.
- `src/pages/[...slug].astro` or explicit generated routes for `marketingPage.routePath` and root `blogPost` legacy slugs.
- `src/pages/data-sources/[slug].astro` for `dataSource`.
- `src/pages/reporting-templates/[slug].astro` for `reportingTemplate`.
- `src/pages/alternatives/[slug].astro` for `comparisonPage`.
- `src/pages/doc/[slug].astro` for `docPage`.
- `src/pages/legal/[slug].astro` for `legalPolicy`.
- `src/pages/pricing.astro` or `/pricing/index.astro` for `pricingPage`.

Route resolver priority:

1. Explicit `routePath`.
2. Existing `migration.legacyUrl` path.
3. Type default pattern.
4. New clean SEO route pattern.

### 8.2 GROQ rules

- Use date-pinned API version.
- Use explicit `published` perspective for production.
- Use CDN where appropriate for public runtime reads; static builds can use non-CDN for freshness.
- Never expose Sanity tokens client-side.
- Query only fields needed for each page.
- Dereference reusable entities server-side in GROQ.

### 8.3 SEO components

Every route-bearing page should render:

- title tag
- meta description
- canonical URL
- no-index when set
- Open Graph image/title/description
- Twitter card
- JSON-LD where appropriate
- breadcrumbs
- trailing slash consistency

Structured data candidates:

- `BreadcrumbList`
- `Article` / `BlogPosting` for blog posts
- `FAQPage` when FAQ exists
- `ItemList` for template/data-source collections
- `SoftwareApplication` or `Product` only where claims are accurate
- `Review` aggregate only if review source data is valid and legally safe

### 8.4 Internal linking components

Create reusable Astro/Sanity-driven sections:

- related data sources
- related templates
- related solution pages
- related alternatives
- related blog posts
- CTA band
- FAQ
- review proof
- logo proof

Internal linking is the moat. Every page should push users and crawlers toward the next commercial step.

### 8.5 Sitemaps and no-index

Generate separate sitemap groups:

- core pages
- blog posts
- data sources
- reporting templates
- alternatives
- docs
- legal, if included, but no-index pages should be excluded

No-index:

- legal pages already no-index
- thin zero-section pages until completed
- internal docs if not intended for search
- tag/category pages unless deliberately built

## 9. Frontend page templates to build first

Build reusable Astro templates, not one-off pages.

### 9.1 Marketing / solution page template

Used by: homepage, marketing pages, solution pages, SEO landing pages.

Must support:

- hero
- flexible but constrained sections
- data-source collections
- template collections
- reviews
- FAQ
- CTA band
- related links

### 9.2 Blog post template

Blog already works well. Preserve it, but add:

- better table of contents if content is long
- related templates/data sources/manual internal links
- default blog CTA
- author fallback if author schema is not ready
- breadcrumb to `/blog/`
- canonical route at root slug

### 9.3 Data-source template

This is a major SEO asset.

Must support:

- related reporting templates
- metrics/use cases section
- compatible channel/category
- screenshots or image asset
- FAQ
- related solution pages
- CTA

### 9.4 Reporting-template template

Must support:

- template preview image
- data sources referenced
- KPIs included
- who should use it
- setup/automation explanation
- related templates
- CTA

### 9.5 Comparison template

Must support:

- competitor summary
- comparison table
- “choose Oviond if...” section
- “choose competitor if...” honest section
- migration angle
- pricing/packaging notes
- related alternatives
- CTA

## 10. Content build phases

### Phase 0 — SEO safety foundation

Goal: do not lose existing traffic.

Codex tasks:

1. Generate a current Sanity URL inventory from all route-bearing docs.
2. Generate a planned Astro URL inventory.
3. Diff the two before launch.
4. Fail build if any current indexable legacy URL disappears without a redirect.
5. Implement redirect export from Sanity `redirect` docs.
6. Add canonical URL handling.
7. Add trailing slash consistency.
8. Add sitemap generation.
9. Add no-index handling.
10. Add basic SEO validation warnings in Sanity Studio.

Acceptance criteria:

- All imported blog URLs remain live at root.
- All `/data-sources/` URLs remain live.
- All `/doc/` URLs remain live or intentionally redirected.
- All `/legal/` URLs remain live and no-index.
- `/marketing-reporting/` and `/marketing-dashboards/` remain live.
- No high-value URL is silently moved to `/blog/`, `/solutions/`, or another new family.

### Phase 1 — Upgrade what already exists

Goal: use current URL equity as the first SEO lever.

Priority existing pages to refresh/upgrade:

1. `/marketing-reporting/` — core marketing reporting software hub.
2. `/client-reporting-software/` — client reporting software hub.
3. `/automated-marketing-reports/` — automated reporting hub.
4. `/marketing-dashboards/` — marketing dashboard software hub.
5. `/building-the-perfect-ppc-report/` — PPC report template page or support asset.
6. `/white-label-seo-dashboards/` — white-label SEO dashboard support asset.
7. `/how-to-white-label-your-digital-marketing-reports-and-dashboards/` — white-label reporting support asset.
8. `/agencyanalytics-and-oviond-stacking-up-the-software/` — legacy support for AgencyAnalytics alternative.
9. `/dashthis-and-oviond-stacking-up-the-software/` — legacy support for DashThis alternative.
10. `/google-data-studio-and-oviond-stacking-up-the-software/` — legacy support for Looker Studio alternative.

Sanity work needed:

- mark as `launch_ready` / `needs_refresh` via strategy fields;
- add related templates/data sources;
- add FAQs;
- add CTAs;
- shorten weak/overlong meta descriptions;
- clean category assignment.

### Phase 2 — Build new high-intent gaps

Goal: cover page-level intents where no existing URL should own the query.

Build in this order:

1. SEO reporting cluster
   - `/solutions/seo-reporting-software/`
   - `/solutions/seo-reporting-tool/`
   - `/solutions/seo-reporting-for-clients/`
   - `/solutions/google-search-console-dashboard/`
   - `/templates/seo-report-template/` only after deciding whether to preserve a legacy URL instead
2. Paid ads reporting cluster
   - `/solutions/ppc-reporting-tool/`
   - `/solutions/ppc-reporting-software/`
   - `/solutions/google-ads-reporting-tool/`
   - `/solutions/facebook-ads-reporting-tool/`
   - `/solutions/meta-ads-reporting/`
3. Social reporting cluster
   - `/solutions/social-media-reporting-tool/`
   - `/solutions/social-media-reporting-software/`
   - `/solutions/instagram-analytics-report/`
   - `/solutions/linkedin-ads-reporting/`
   - `/solutions/youtube-analytics-report/`
4. White-label / dashboard cluster
   - `/solutions/white-label-reporting-software/`
   - `/solutions/white-label-dashboard-software/`
   - `/solutions/client-dashboard-software/`
5. Template cluster
   - generic template pages after duplication review

### Phase 3 — Competitor alternatives

Goal: capture bottom-funnel switchers.

Build after comparison schema/template exists.

Start with:

1. AgencyAnalytics alternative
2. DashThis alternative
3. Whatagraph alternative
4. Swydo alternative
5. Looker Studio alternative
6. Supermetrics alternative
7. 2-Minute Reports alternative

Internal linking:

- Old comparison blog post -> new alternative page.
- New alternative page -> pricing, templates, integrations, relevant old blog post, and comparison hub.
- Comparison hub -> all alternatives.

### Phase 4 — AI / agent-native reporting

Goal: stake the future direction without overclaiming.

Build after product messaging is locked.

Priority:

- AI report generator
- AI marketing reporting
- AI client reporting
- MCP marketing reporting
- connect marketing data to ChatGPT / Claude

Keep copy grounded in product truth:

- reliable connectors
- structured reporting data
- agency-ready workflows
- permissions
- scheduled delivery
- white label
- API/MCP direction

### Phase 5 — Metrics and dimensions moat

Goal: long-tail authority.

Start with platform-level pages, not thousands of thin metric pages.

Priority:

- GA4 metrics and dimensions
- Google Ads metrics and dimensions
- Google Search Console metrics and dimensions
- Facebook Ads metrics and dimensions
- LinkedIn Ads metrics and dimensions
- TikTok Ads metrics and dimensions

## 11. Navigation plan

Current navigation is too label-only. Fix this before launch.

Header should be simple:

- Platform → `/marketing-reporting/`
- Data Sources → `/data-sources/`
- Templates → `/reporting-templates/`
- Pricing → `/pricing/`
- Resources → `/blog/` or dropdown later

Footer groups:

- Platform: Reporting, Dashboards, Data Sources, Templates, Pricing
- Solutions: Marketing Agencies, Marketing Teams, Small Business, White Label Reporting
- Resources: Blog, Help/Docs, Reviews, Updates
- Comparisons: AgencyAnalytics Alternative, DashThis Alternative, Whatagraph Alternative, Looker Studio Alternative
- Legal: current legal URLs

Codex should convert nav items to internal references or explicit URLs. No label-only nav items should ship.

## 12. Content QA rules

Every indexable route-bearing page must have:

- valid route
- canonical URL
- SEO title
- SEO description
- no-index explicitly false or unset
- H1
- primary CTA
- at least one internal link to a commercial page
- at least one relevant related page/module where appropriate
- image alt text where images are used
- FAQ for money pages
- schema where relevant
- review status not `needs_review`

Known cleanup items from audit:

- 173 blog posts have overlong meta descriptions.
- 11 data-source pages have missing SEO descriptions.
- 8 doc pages have missing SEO descriptions.
- Small Business solution page has missing SEO description.
- Pricing page meta description needs rewrite.
- `Uncategorized` has 26 posts.
- Blog category descriptions are empty.
- Some placeholder copy exists, e.g. `Digital Marketing Dashboard` template short description is `ggg`.
- Zero-section marketing pages must be completed, no-indexed, or removed from navigation.

## 13. Codex build checklist

### Step A — Read and inventory

- Read Sanity schema.
- Read current route inventory.
- Generate all planned static paths.
- Generate URL diff against current legacy inventory.

### Step B — Implement lean route system

- Preserve legacy paths.
- Use `routePath` when present.
- Use type defaults only when no legacy path exists.
- Add tests for route collisions.
- Add tests for missing redirects.

### Step C — Implement page templates

- Marketing/solution template.
- Blog post template.
- Data-source template.
- Reporting-template template.
- Comparison template.
- Pricing template.
- Legal/doc templates.

### Step D — Implement SEO plumbing

- canonical
- meta
- OG/Twitter
- no-index
- sitemap
- breadcrumbs
- JSON-LD
- trailing slash
- image URLs via Sanity image URL builder

### Step E — Implement internal-link modules

- related data sources
- related templates
- related posts
- related alternatives
- CTA band
- FAQ
- reviews/proof

### Step F — Add minimal schema extensions

- `seoStrategy` object.
- `comparisonPage` document.
- optional `customerStory` document.
- validation warnings.

### Step G — Generate launch QA report

Output a markdown/CSV report showing:

- total generated URLs by type;
- legacy URLs preserved;
- legacy URLs redirected;
- legacy URLs missing;
- no-index pages;
- missing meta titles/descriptions;
- duplicate slugs;
- duplicate canonicals;
- thin/zero-section pages;
- nav items without href/reference.

## 14. Measurement plan after launch

Track weekly:

- GSC clicks/impressions by route family;
- rankings for Phase 1 and Phase 2 target keywords;
- indexed pages by route family;
- crawl errors / 404s;
- organic trial starts;
- template page conversion to signup;
- data-source page conversion to signup;
- comparison page conversion to signup;
- internal-link path from blog → money page → signup.

Do not restart paid ads until the website and tracking are properly live and Chris explicitly reauthorizes.

## 15. Strategic conclusion

The path is clear:

1. **Do not break the WordPress URLs.** Existing root blog slugs and data-source URLs are equity.
2. **Upgrade existing high-intent pages first.** Especially `/marketing-reporting/`, `/client-reporting-software/`, `/automated-marketing-reports/`, and `/marketing-dashboards/`.
3. **Use Sanity’s reusable entities as proof.** Data sources, templates, reviews, CTAs, features, and logo clouds should appear across money pages.
4. **Add comparison pages and new solution pages only where they fill real gaps.** Do not create duplicates for the sake of clean URL aesthetics.
5. **Keep the stack lean.** Static Astro, published Sanity reads, webhook rebuilds, no live editing.
6. **Build an internal-link machine.** Every page should feed the SEO system.

If we execute this properly, Oviond can become the clearest, most useful, most commercially focused SEO property in agency reporting: simple reporting, client-ready proof, templates, integrations, alternatives, and eventually AI-agent-native reporting — all tied together in a disciplined Sanity/Astro architecture.
