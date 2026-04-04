# MEMORY.md

## Identity and role

- I am Nicole Prince, VP of Marketing at Oviond.
- Chris Irwin is my boss.
- Chris uses `chris@oviond.com`.
- My remit covers marketing, strategy, delivery, research, positioning, growth planning, and execution support for Oviond.

## Chris working preferences

- After finishing work, always send Chris a concise update covering what changed and why.
- When Chris sends a voice note, always reply with both a text response and a voice note response. Treat this as a standing requirement, not an occasional preference.
- Voice-note replies should use a nice female voice by default, currently OpenAI `coral`, at slightly faster speed (`1.25`) unless Chris asks otherwise.

## Oviond business context

- Oviond is a B2B SaaS reporting platform built primarily for marketing agencies.
- Brand/product direction: simple, clear, easy, uncluttered reporting for agencies; quick to set up; low learning curve; something agencies can set up and largely forget.
- GTM motion today: mostly self-serve SaaS, with some sales-led support for larger accounts.
- Ideal customer profile: small to medium-sized marketing agencies.
- Common switch sources: manual reporting, AgencyAnalytics, Looker Studio, Swydo, and similar reporting tools.
- Main reasons customers choose Oviond: simplicity, lower pricing, white-label reporting.
- Main reasons prospects say no: product can feel unpolished, missing integrations, weak initial setup/onboarding, or early perception that the product does not work.
- Growth target: move from about $28.5k MRR to $100k MRR by Dec 2026.
- Durable US-market interpretation after the 2026-04-04 strategy review: the US agency market appears large enough for Oviond’s current scale ambitions, including the $100k MRR goal. The near-term constraint is execution quality, stickiness, and repeatable acquisition — not US TAM.
- Durable AI-risk interpretation after the 2026-04-04 strategy review: LLMs are a real substitution risk for low-end report writing, narrative summaries, and one-off analysis, especially for small agencies willing to stitch together Sheets / Looker Studio / ChatGPT-style workflows. The stronger defensible value is in reliable connectors, cross-source normalization, white-label delivery, scheduled reporting, client-ready trust, permissions, and workflow automation. Oviond should evolve toward an AI-assisted agency reporting system, not remain just a static dashboard/report builder.

## Durable platform decisions

- Stripe access exists for read-only billing analysis.
- Stripe skill update on 2026-04-03: the old price-math MRR path was materially wrong for Oviond because it undercounted archived/tiered prices and did not model billing reality well. The Stripe skill now uses invoice-backed normalized MRR as its primary method, with archived-price/tier-aware subscription-item fallback and local cached snapshots for speed. Dashboard numbers should still win as the final finance-grade tie-breaker, but the skill is now suitable for fast operational reads again.
- Next Stripe analysis work should focus on full pagination, paid-vs-trial separation, plan mix, paused/reactivation opportunity, and churn-risk views.
- Churn / retention became a top strategic focus on 2026-04-04. Current working thesis: Oviond’s churn problem is mainly voluntary monthly-plan churn rather than billing failure, driven most by `unused`, `switched_service`, and complexity / trust issues more than raw price. This week’s retention work should prioritize delinquency rescue, recent high-value win-backs, mature monthly-to-annual conversion, and product fixes around activation, client-ready report confidence, and integration/reset pain.
- Google Workspace is connected for Nicole via domain-wide delegated impersonation.
- Google Analytics is operational for Oviond.
- Durable GA4 interpretation after the 2026-04-04 audit: the `Oviond Website + App` property is a mixed property spanning `www.oviond.com`, `v2.oviond.com`, white-label customer report domains, and even some localhost/dev traffic. Top-level GA4 channel, geo, landing-page, and conversion views should therefore not be treated as pure acquisition truth without host segmentation.
- Durable GA4 measurement warning after the 2026-04-04 audit: the GA4 `conversions` metric appears materially polluted / overstated from early March 2026 onward, likely due to non-business key-event configuration changes. For acquisition reads, prefer segmented host analysis plus specific signup-style events such as `ads_conversion_signup`, with backend app truth, Google Ads, and Stripe as tie-breakers.
- Chris explicitly wants the 2026-04-04 GA4 audit findings folded into ongoing strategy and decision-making. Treat segmented GA4 interpretation, Display skepticism, and backend/ad-platform/Stripe triangulation as part of the standing strategic lens going forward.
- Google Ads production access is operational again through a fresh GCP project, not the old `oviond-workspace-cli` project. On 2026-04-03 a new service account in project `northern-card-492208-q6` was created, added to MCC `6387956297`, and wired into OpenClaw via `GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT`. Live checks then succeeded for `customers:listAccessibleCustomers`, a target-account query against client `2906154258`, and the manager→client linkage query. The earlier `PROJECT_DISABLED` issue appears to have been specific to the old project `480335022137`, not the overall architecture. Cloud-project introspection checks may still show read-only GCP permission gaps, but those are non-blocking for actual Google Ads API usage.
- Durable Google Ads operating rule: do not re-enable or expand South African Google Ads campaigns just because they produce cheap trials. Chris explicitly said South African customers have weak stickiness / LTV, so South Africa should be used only as a creative/performance reference benchmark, not as a target market to scale, unless Chris explicitly overrides that decision.
- MailerLite is heavily automation-driven and is an important lifecycle marketing system for Oviond.
- Meta access is configured for Oviond’s Facebook, Instagram, and Ads assets.
- Oviond design capability should be built as a skill-led operating system: Nicole as art director/QA, a dedicated Oviond design skill as the reusable brain, and Gemini/Nano Banana as the rendering layer.
- The November 2024 Oviond brand refresh guide is now the primary source of truth for the internal design system, especially its direction toward abstract feeling-led imagery, Inter Semibold logotype treatment, and restrained use of white/black/main blue.
- Early Oviond design demos established a durable workflow lesson: use Gemini/Nano Banana mainly for concept, composition, and brand-feel generation, then prefer text-free or overlay-safe outputs over trusting the model with important final marketing copy.
- Oviond blog covers should currently bias toward product-preview aesthetics rather than pure abstract covers, especially layered report architecture, emerging UI from white space, and elegant detail-window treatments.

## Pointers

- Local operator details, helper paths, wrapper commands, and implementation notes live in `TOOLS.md`.
- Secret material must never be stored in tracked workspace files; keep only references to approved secret storage locations.
