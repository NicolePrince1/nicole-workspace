# Oviond Sanity + Astro Strategy Read — 2026-05-12

## Scope

Read-only inspection of Oviond's Sanity project and dataset using the configured `SANITY_CMS` credential. No Sanity writes were made.

## Sanity docs / architecture learnings

- Sanity Content Lake is a JSON document store organized by project and dataset.
- GROQ is the core query language. It should be used to shape frontend/API responses, dereference relationships with `->`, and safely pass parameters rather than string-interpolating user input.
- API versions should be date-pinned. `2025-02-19` is an important modern baseline because the default perspective behavior changed to published and release/version support is available.
- Production public reads should explicitly use the `published` perspective.
- Draft/preview reads require token-backed access, `useCdn: false`, and should be kept separate from public reads.
- Static Astro is a strong fit for Oviond's marketing site, blog, docs-lite pages, integration pages, templates, and SEO pages.
- Static Astro content changes need rebuilds; Sanity webhooks should trigger deployment rebuilds or cache invalidation.
- Presentation/Visual Editing in Astro requires Astro 5+, Node 20+, `@sanity/astro`, React integration, an adapter/SSR preview surface, viewer token, CORS with credentials, and stega/content-source-map configuration.
- Sanity should be treated as Oviond's marketing operating system, not just a blog CMS: reusable CTAs, proof, reviews, integration metadata, reporting templates, feature modules, comparison pages, and campaign pages should live there.

## Current Sanity project/dataset observed

- Project ID: `pd9luxir`
- Project name: `Oviond`
- Dataset inspected: `production`
- Workspace schema inspected: `oviond-website`
- Current schema document updated: `2026-04-29T11:18:29Z`
- Legacy starter schema still exists: `sanity-template-astro-clean`

## Content inventory

Document counts observed:

- `blogPost`: 217
- `dataSource`: 62
- `customerReview`: 54
- `reportingTemplate`: 35
- `blogCategory`: 16
- `docPage`: 16
- `dataSourceCategory`: 15
- `legalPolicy`: 9
- `marketingPage`: 9
- `navigation`: 7
- `productFeature`: 5
- `solutionPage`: 3
- `reviewSource`: 2
- `siteSettings`: 1
- `pricingPage`: 1
- `logoCloud`: 1
- `reusableCta`: 1
- `sanity.imageAsset`: 1105

## Current content model

The model is already more than a starter blog. It contains:

- Global site settings
- Navigation groups
- Marketing pages
- Pricing page
- Blog posts and categories
- Data source / integration pages and categories
- Reporting template pages
- Solution pages
- Reviews and review sources
- Customer logos
- Product features
- Documentation-style pages
- Legal policies
- Reusable CTAs
- Redirect schema
- Shared section/module types including feature grids, CTAs, FAQ sections, content/media sections, template collections, data source collections, reviews sliders/grids, workflow sections, logo clouds, comparison sections, and related content

This is a decent foundation for a marketing operating system, not just a migrated WordPress archive.

## Strong parts

- The schema is meaningfully customized for Oviond.
- Core commercial page types exist: marketing pages, solution pages, pricing, data sources, templates, reviews, features.
- SEO fields exist on route-bearing documents: meta title, meta description, no-index, OG image.
- Migration metadata exists, including source WordPress ID, legacy URL, migration status, last imported date, review-before-launch flag, and notes.
- Strong reusable primitives exist: CTAs, image-with-alt, sections, FAQ, stats, features, reviews, logo clouds.
- Data-source and template entities can become a serious SEO moat if cleaned and expanded.
- Review/testimonial data is structured rather than pasted into pages.

## Strategic concerns / risks

1. Navigation is currently label-only in several places. Many navigation items have no URL or internal reference, which is dangerous for launch UX and crawlability.
2. The blog was clearly imported from WordPress and is not launch-clean. 217 posts exist, but much of the category structure is legacy/noisy.
3. `Uncategorized` still has 26 posts. That is a clear taxonomy hygiene problem.
4. Blog category descriptions are empty across the inspected categories.
5. 173 of 217 blog posts have meta descriptions over 180 characters. That is not fatal, but it is sloppy and suggests migrated metadata should be rewritten.
6. 11 of 62 data source pages have missing SEO descriptions; one has an overlong description.
7. 8 of 16 doc pages have missing SEO descriptions.
8. The pricing page meta description appears to contain scraped page text / HTML entity remnants, not a deliberate SERP description.
9. The Small Business solution page has an empty SEO description.
10. Some fields contain obvious placeholder/low-quality copy, e.g. `Digital Marketing Dashboard` template short description is `ggg`.
11. Several marketing pages have zero sections: `brand`, `getting-started-guide`, `oviond-brand-guide-2025`. These should not accidentally ship as thin/indexable pages.
12. The route strategy needs explicit frontend mapping. Example: `home` probably maps to `/`, pricing has no slug, and navigation labels do not currently prove URL resolution.
13. The old starter `post` document type still exists with one document. This could cause confusion unless intentionally preserved or excluded.
14. No visible author/person content type was observed in the schema inventory. That weakens blog E-E-A-T and editorial governance.
15. No obvious comparison-page content type was observed, despite competitor/comparison SEO being strategically important for Oviond.
16. No obvious case-study/customer-story type was observed. Reviews exist, but that is not the same as narrative proof.
17. No obvious campaign/landing-page variant type was observed beyond generic marketing pages. That may be fine initially, but it matters for post-launch acquisition.

## SEO interpretation

The Sanity build contains enough structure to support a strong SEO system, but the content is currently in a migrated/raw state. The highest SEO value areas are:

1. Agency reporting intent: marketing reporting software, client reporting software, agency dashboards, automated reports, white-label reports.
2. Template intent: Google Ads reporting template, GA4 reporting template, PPC dashboard template, social media report template, etc.
3. Integration/data-source intent: Google Analytics 4, Google Ads, Facebook Ads, LinkedIn Ads, Search Console, Stripe, Mailchimp, etc.
4. Competitor/comparison intent: AgencyAnalytics alternative, Looker Studio alternative, DashThis alternative, Swydo alternative, Whatagraph alternative, etc. The model is not yet obviously built for this.
5. Pain/problem intent: client reporting, report automation, agency workflow, reporting time drain, client-ready reporting, white-label delivery.

The CMS should support pillar → cluster → product page → template/data-source interlinking. Right now, the raw material exists, but the editorial architecture is not yet tight enough.

## Recommended operating model

1. Use Sanity as the single source of truth for public website content.
2. Keep production frontend reads explicitly `published`.
3. Add draft preview separately using token-backed `drafts`, CDN off, and restricted preview routes.
4. Use static Astro for public pages with Sanity webhooks triggering rebuilds.
5. Add SSR only where preview/Presentation/Visual Editing requires it.
6. Keep reusable modules constrained around Oviond's actual page patterns; avoid a chaotic drag-and-drop page builder.
7. Build a launch QA checklist into the content workflow: SEO title, meta description, slug, route path, canonical intent, CTA, internal links, image alt, no-index status, migration review flag.
8. Treat data-source and reporting-template records as structured SEO entities, not just content pages.
9. Add or model comparison pages and customer stories before serious SEO launch expansion.
10. Create editorial ownership rules: every blog/SEO page needs a status, owner, target keyword, refresh cadence, funnel stage, and internal-link targets.

## Immediate cleanup priorities before launch

1. Fix navigation URLs/references.
2. Decide what zero-section marketing pages should do: complete, redirect, no-index, or remove from nav/indexing.
3. Rewrite pricing SEO description.
4. Add SEO description for Small Business solution page.
5. Clean `Uncategorized` and empty category descriptions.
6. Rewrite overlong blog meta descriptions where pages are worth keeping.
7. Fix obvious placeholder copy such as template short descriptions.
8. Define the frontend route map for every route-bearing type.
9. Confirm redirect handling from old WordPress URLs to new Astro routes.
10. Add comparison/customer-story schema coverage or a deliberate workaround before launch.

## Strategic conclusion

The Sanity build is promising. It is not just a starter template anymore. The team has already modeled the core commercial inventory Oviond needs: pages, integrations, templates, reviews, solution pages, reusable CTAs, and modular sections.

But it is not launch-polished yet. The current state looks like a successful migration plus early modeling pass, not a final content operating system. The risk is not Sanity or Astro. The risk is shipping migrated WordPress residue, thin pages, broken navigation, messy metadata, and unfocused taxonomy into a website that is supposed to reset Oviond's market perception.

Nicole's standing role should be to own the marketing/content model, SEO architecture, editorial QA, and launch readiness rules on top of Sanity/Astro.
