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
- Google Ads production API access is operational for Oviond through the current service-account-first setup. Keep durable status here; keep blocker/debug history in the Google Ads skill references and dated daily notes.
- Durable Google Ads operating rule: do not re-enable or expand South African Google Ads campaigns just because they produce cheap trials. Chris explicitly said South African customers have weak stickiness / LTV, so South Africa should be used only as a creative/performance reference benchmark, not as a target market to scale, unless Chris explicitly overrides that decision.
- On 2026-04-04 Chris decided to fully retire MailerLite and Loops from active operational workflows.
- Lifecycle email / marketing automation will be rebuilt from a fresh start in Sequenzy, with Nicole expected to learn the new setup and take over operation once the initial build is in place.
- Old MailerLite / Loops materials should be preserved only as archived historical reference, not treated as active runbooks.
- Gleap is a critical operational platform for Oviond across customer service, ticketing, feature/roadmap handling, internal planning, and the public help center. The local `use-gleap` skill was first drafted on 2026-04-04 and live API validation succeeded on 2026-04-08.
- Durable Gleap live-read facts after the 2026-04-08 validation: admin-level API access works; users, teams, tickets, help center, unified inbox, and statistics endpoints are readable; recent ticket routing appears mostly through `processingUser` rather than `processingTeam`; help-center content uses localized field objects plus rich `content` and `plainContent`; and `/tickets/tracker-tickets` currently returns empty, so Nicole should not assume active roadmap data lives there until proven.
- Durable Gleap strategic interpretation after the 2026-04-08 deep read: Oviond’s Gleap queue behaves more like a customer-success / implementation / trust-repair system than a pure bug queue. The dominant recurring friction themes are connectors and data trust, white-label/custom-domain/report-delivery operations, permissions/setup, automation/email issues, and account/billing exceptions. Gleap should be treated as an activation, trust, and retention signal, not just a support inbox.
- Durable Gleap operating implication after the 2026-04-08 strategy pack: use Gleap as a customer-truth operating system that feeds weekly product prioritization, retention diagnosis, help-center improvements, and customer-language capture for messaging. Do not assume roadmap structure lives in tracker tickets until that is proven in live use.
- Chris wants Gleap treated as part of Nicole’s core operating context, not as an isolated support tool. It should feed retention/churn diagnosis, product-friction discovery, customer-language capture for messaging/positioning, roadmap prioritization, and help-center quality alongside the rest of the Oviond operating stack.
- Meta access is configured for Oviond’s Facebook, Instagram, and Ads assets.
- Oviond design capability should be built as a skill-led operating system: Nicole as art director/QA, a dedicated Oviond design skill as the reusable brain, and Gemini/Nano Banana as the rendering layer.
- The November 2024 Oviond brand refresh guide is now the primary source of truth for the internal design system, especially its direction toward abstract feeling-led imagery, Inter Semibold logotype treatment, and restrained use of white/black/main blue.
- Early Oviond design demos established a durable workflow lesson: use Gemini/Nano Banana mainly for concept, composition, and brand-feel generation, then prefer text-free or overlay-safe outputs over trusting the model with important final marketing copy.
- Oviond blog covers should currently bias toward product-preview aesthetics rather than pure abstract covers, especially layered report architecture, emerging UI from white space, and elegant detail-window treatments.

## Pointers

- Local operator details, helper paths, wrapper commands, and implementation notes live in `TOOLS.md`.
- Secret material must never be stored in tracked workspace files; keep only references to approved secret storage locations.

## Promoted From Short-Term Memory (2026-04-10)

<!-- openclaw-memory-promotion:memory:memory/2026-04-03.md:25:48 -->
- - PMAX campaign `PMAX- Start Trial USA` (`21330916203`) was the only currently proven acquisition engine. - Display campaign `Display Remarketing USA Feb 2026` (`23607074353`) was identified as a waste-risk: - heavy low-quality placement mix - meaningful spend with no recent true trial-signup conversions - polluted reporting due to low-value conversion activity like `page_view` - Chris wants Google Ads optimized around real free-trial signups with a practical ceiling around `R1000/day` total and low tolerance for waste. - Immediate operating stance: - keep PMAX live - pause or near-zero bad Display activity - do not force major bidding changes before asset quality is cleaned up [score=0.802 recalls=5 avg=0.401 source=memory/2026-04-03.md:25-35]

## Promoted From Short-Term Memory (2026-04-10)

<!-- openclaw-memory-promotion:memory:memory/2026-04-08.md:44:62 -->
- - 30-day team performance strongly reinforced person-dependence: Michelle had 191 assigned tickets, 262 replies, and 130 tickets worked on, far above the rest of the team. - Gleap appears to mix several jobs into one system: - product bug reporting - customer-success handholding - white-label / domain / automation operations - subscription/account exception handling - inbox noise from external email traffic and some bot-created low-context tickets - Support data lines up with the existing retention thesis that Oviond’s main pain is not just price or billing failure. The dominant pattern is complexity, confidence, setup friction, data-trust issues, and product-operability gaps. - Gleap also suggests Oviond’s strongest value and biggest risk both sit around connectors, trusted data, white-label delivery, permissions, and automation. That reinforces the strategy of evolving toward an AI-assisted agency reporting operating system rather than a static dashboard builder. - The help center is more substantial than expected but still rough in places: - 34 collections were visible - sampled core collections included drafts - collection summary counts did not always match article-list counts - search queries clustered around migration, connectors, widget language, permissions, custom domains, API/MCP, and reporting tasks - One important process gap: tracker tickets are currently empty and recent feature-signal seems to be living inside normal support tickets instead of a structured roadmap intake flow. # 2026-04-08 ## Gleap live validation and skill refinement [score=0.810 recalls=5 avg=0.406 source=memory/2026-04-08.md:44-62]

## Promoted From Short-Term Memory (2026-04-13)

<!-- openclaw-memory-promotion:memory:memory/2026-03-27.md:31:53 -->
- - Paused campaign `Remarketing USA` (`120234146733660563`). - Increased campaign `Remarketing USA - Free Trial Test` (`120242845828470563`) daily budget from `35000` to `70000` (R700/day). - Paused the weak test ad `Carousels - Product` (`120242846212370563`). - Kept the stronger test ad `Images - Product` (`120242846210870563`) active. - Tightened ad set `United States` (`120242846203880563`) so it now targets only the existing custom audience `All Website Visitors 120 Days`, keeps targeting expansion off, and restricts placements to Facebook only (`feed`, `right_hand_column`) on mobile and desktop. - Verified post-change state: - control campaign now `PAUSED` - test campaign now `ACTIVE` at `70000` daily budget - test ad set still optimized to `OFFSITE_CONVERSIONS` on custom event `Customer Signs Up` - test carousel ad now `PAUSED` ## Operator read after tighten-up - The account is now much cleaner: one active campaign, one active ad set, one active image ad, previous-visitors-only audience, and no Audience Network leakage. - This is a better B2B SaaS remarketing structure than the earlier mixed-placement setup. - Important caution: the audience is now much tighter while budget is higher, so watch for rising frequency / saturation over the next 24-48 hours. - Next monitoring focus should be: - whether Facebook-only traffic still generates enough volume - whether `Customer Signs Up` attribution starts showing cleanly - whether frequency climbs too fast inside the 120-day site-visitor pool ## Voice-note response requirement [score=0.804 recalls=4 avg=0.412 source=memory/2026-03-27.md:31-53]

## Promoted From Short-Term Memory (2026-04-14)

<!-- openclaw-memory-promotion:memory:memory/2026-04-08.md:1:26 -->
- # 2026-04-08 ## Gleap live validation and skill refinement - Chris confirmed the required Gleap env vars were added and asked Nicole to test and refine the local `use-gleap` skill. - Live validation succeeded against Oviond's Gleap project using the public v3 API. - Verified readable surfaces: - permissions / roles - project users - teams - tickets - unified inbox - help center collections and articles - support statistics - Current live-read takeaways: - access is admin-level - 5 readable users were returned - 4 manual-assignment teams were returned: Engineering, Support, Marketing, Sales - recent ticket statuses included `OPEN`, `INPROGRESS`, and `DONE`, with the count endpoint also exposing older/custom statuses including `SNOOZED` and `PLANNED` - recent ticket types included `BOT`, `BUG`, `CUSTOMERSUCCESS`, `FEATURE_REQUEST`, and `INQUIRY` - recent priorities included `LOW`, `MEDIUM`, and `HIGH` - recent routing appears mostly via `processingUser`; `processingTeam` was not populated in the sampled recent tickets - ticket content in practice is mostly `formData` plus `plainContent`; `customData` and `attributes` were not observed in the 25-ticket sample - `/tickets/tracker-tickets` returned an empty list, so tracker tickets are API-backed but not yet proven to be Oviond's active roadmap store - help-center collections/articles use localized fields like `{en: ...}` and article records include both rich `content` and `plainContent` - sampled help-center articles included drafts [score=0.845 recalls=6 avg=0.388 source=memory/2026-04-08.md:1-26]
