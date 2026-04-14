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
- Treat Cape Town, South Africa as the shared local context with Chris.
- Default to SAST for everyday time references unless a task explicitly requires another timezone.

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
- Google Ads production API access is operational for Oviond through the current service-account-first setup. Keep durable status here; keep blocker/debug history in the Google Ads skill references and dated daily notes.
- Durable Google Ads acquisition read: USA PMAX was the only clearly proven Google Ads acquisition engine in the early April 2026 audits, while Display looked like a waste-risk due to low-quality placements and polluted low-value conversion activity. Optimize around real free-trial signup truth, not inflated platform fluff.
- Durable Google Ads South Africa rule: Chris explicitly overrode the earlier no-South-Africa stance on 2026-04-04 and authorized South Africa Google Ads work. The standing rule now is: South Africa campaigns are allowed when Chris has directed that work, but they should still be treated cautiously because South African customer stickiness / LTV appears weaker. Use South Africa as a supervised test market or tactical acquisition lane when explicitly in play, not as an automatic market to scale by default, and do not treat cheap trial volume there as sufficient proof of good growth economics.
- On 2026-04-04 Chris decided to fully retire MailerLite and Loops from active operational workflows.
- Lifecycle email / marketing automation will be rebuilt from a fresh start in Sequenzy, with Nicole expected to learn the new setup and take over operation once the initial build is in place.
- Durable Sequenzy platform status after the 2026-04-14 live audit: Oviond's `SEQUENZY_API_KEY` is operational for read access, and the live account exposes not only the documented subscriber / transactional / metrics surface but also broader account, company, website, list, template, campaign, and sequence reads. Important caveats: direct API calls from this runtime should send an explicit `User-Agent`; `/health/deliverability` and standalone `/subscribers/{email}/activity` did not validate cleanly; and live response envelopes often use resource-specific keys instead of a universal `data` wrapper.
- Old MailerLite / Loops materials should be preserved only as archived historical reference, not treated as active runbooks.
- Gleap is a critical operational platform for Oviond across customer service, ticketing, feature/roadmap handling, internal planning, and the public help center. The local `use-gleap` skill was first drafted on 2026-04-04 and live API validation succeeded on 2026-04-08.
- Durable Gleap live-read facts after the 2026-04-08 validation: admin-level API access works; users, teams, tickets, help center, unified inbox, and statistics endpoints are readable; recent ticket routing appears mostly through `processingUser` rather than `processingTeam`; help-center content uses localized field objects plus rich `content` and `plainContent`; and `/tickets/tracker-tickets` currently returns empty, so Nicole should not assume active roadmap data lives there until proven.
- Durable Gleap strategic interpretation after the 2026-04-08 deep read: Oviond’s Gleap queue behaves more like a customer-success / implementation / trust-repair system than a pure bug queue. The dominant recurring friction themes are connectors and data trust, white-label/custom-domain/report-delivery operations, permissions/setup, automation/email issues, and account/billing exceptions. Gleap should be treated as an activation, trust, and retention signal, not just a support inbox.
- Durable Gleap operating implication after the 2026-04-08 strategy pack: use Gleap as a customer-truth operating system that feeds weekly product prioritization, retention diagnosis, help-center improvements, and customer-language capture for messaging. Do not assume roadmap structure lives in tracker tickets until that is proven in live use.
- Durable Gleap operating risk: support remains meaningfully person-dependent, with Michelle carrying a disproportionate share of ticket work in the April 2026 analysis.
- Durable help-center/process read: the help center has real substance but is still rough, and recent product/feature signal appears to live mostly inside normal support tickets rather than a mature tracker-ticket roadmap flow.
- Chris wants Gleap treated as part of Nicole’s core operating context, not as an isolated support tool. It should feed retention/churn diagnosis, product-friction discovery, customer-language capture for messaging/positioning, roadmap prioritization, and help-center quality alongside the rest of the Oviond operating stack.
- Meta access is configured for Oviond’s Facebook, Instagram, and Ads assets.
- Durable Meta remarketing lesson: tighter Facebook-only previous-visitor remarketing with the stronger image creative was materially cleaner than the broader mixed-placement setup; avoid trusting weaker carousel variants or noisy expansion-heavy delivery by default.
- Oviond design capability should be built as a skill-led operating system: Nicole as art director/QA, a dedicated Oviond design skill as the reusable brain, and Gemini/Nano Banana as the rendering layer.
- The November 2024 Oviond brand refresh guide is now the primary source of truth for the internal design system, especially its direction toward abstract feeling-led imagery, Inter Semibold logotype treatment, and restrained use of white/black/main blue.
- Early Oviond design demos established a durable workflow lesson: use Gemini/Nano Banana mainly for concept, composition, and brand-feel generation, then prefer text-free or overlay-safe outputs over trusting the model with important final marketing copy.
- Oviond blog covers should currently bias toward product-preview aesthetics rather than pure abstract covers, especially layered report architecture, emerging UI from white space, and elegant detail-window treatments.

## Pointers

- Local operator details, helper paths, wrapper commands, and implementation notes live in `TOOLS.md`.
- Secret material must never be stored in tracked workspace files; keep only references to approved secret storage locations.

