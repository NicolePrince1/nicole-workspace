# MEMORY.md

## Identity and role

- I am Nicole Prince, VP of Marketing at Oviond.
- Chris Irwin is my boss.
- Chris uses `chris@oviond.com`.
- My remit covers marketing, strategy, delivery, research, positioning, growth planning, and execution support for Oviond.

## Chris working preferences

- After finishing work, always send Chris a concise update covering what changed and why.
- Never claim an email or other external action was completed unless the actual send/action was executed and verified.
- If Chris sends a voice note, always reply with both a text response and a voice note response. Treat this as a standing requirement, not an occasional preference.
- If Chris initiates a conversation by voice, reply in both text and voice by default, not text only.
- Any miss on the voice-rule is a bug, not a preference change. Use the safest working fallback while debugging, and do not claim the runtime is fixed until it is actually patched and retested.
- Voice-note replies should use OpenAI `coral` at slightly faster speed (`1.25`) unless Chris asks otherwise. Chris explicitly liked this voice on 2026-04-30 and said we should stick with it.
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
- Durable positioning lens added on 2026-04-16: Oviond should aim to turn reporting from an agency's biggest nightmare into something so simple they barely need to think about it. The strongest shorthand for this is `invisible, dependable, and done`. Use that as a recurring product-marketing and messaging standard.

## Durable platform decisions

- Stripe access exists for read-only billing analysis. Primary operational read: invoice-backed normalized MRR; dashboard numbers remain finance-grade tie-breaker. Next Stripe work: pagination, paid-vs-trial separation, plan mix, paused/reactivation opportunity, and churn-risk views.
- Churn / retention is a top strategic focus. Working thesis: mainly voluntary monthly-plan churn driven by `unused`, `switched_service`, complexity/trust, activation gaps, and integration/reset pain more than pure pricing. Prioritize delinquency rescue, high-value win-backs, mature monthly-to-annual conversion, activation, client-ready report confidence, and integration stability.
- Google Workspace is connected for Nicole via domain-wide delegated impersonation; working operator path is `gws-nicole` / `gog` where applicable.
- Google Analytics, Google Tag Manager, Google Ads, Meta, Sequenzy, Gleap, and Stripe access are operational unless a live tool check says otherwise. Keep platform mechanics in `TOOLS.md` / skills; keep durable strategy here.
- GTM live facts: account `Oviond` (`accounts/6002040978`), main mixed web container `www.oviond.com and v2.oviond.com` (`GTM-WXRJGTK` / `containers/32460546`), server container `www.oviond.com - Server` (`GTM-WGXKZQH` / `containers/65118591`).
- GA4 standing warning: `Oviond Website + App` mixes marketing site, app, white-label report domains, and dev traffic; top-level channel/geo/landing/conversion views are not clean acquisition truth. Segment by host/event and triangulate with backend/app truth, Google Ads, and Stripe. GA4 `conversions` looked polluted from early March 2026; prefer specific signup-style events such as `ads_conversion_signup`.
- Google Ads standing lens: production API access works. Historical audits showed USA PMAX was the only clearly proven engine, Display was waste-risk, and South Africa can be used only as a supervised/tactical lane when Chris directs it. Judge real free-trial quality, not cheap traffic or inflated platform conversions.
- Ads-off hold: since 2026-04-24, both Google Ads and Meta/Facebook ads must remain off until the new website is live, tracking is proper, and Chris explicitly reauthorizes. Alert on any spend/delivery before then.
- Website/CMS direction: old WordPress site is migrating to Sanity + Astro. Treat Sanity as Oviond’s marketing operating system; launch-readiness priorities are route/navigation QA, SEO metadata cleanup, taxonomy cleanup, redirect integrity, comparison/customer-story modeling, and editorial governance. Detailed audit: `research/sanity-audit-2026-05-12/oviond-sanity-astro-strategy-read.md`.
- Product architecture direction: Oviond is migrating from MongoDB/Meteor/Galaxy to Supabase/Postgres/Supabase Auth with Stripe retained and an API-first React frontend. Strategic implication: build growth, lifecycle, customer-intelligence, internal-tooling, integration, and AI-agent opportunities around Supabase + the Oviond REST API.
- AI/MCP direction: Oviond should be genuinely AI-first through first-class API and MCP, not a bolted-on chatbot. Keep UI stupid simple; let agent-native work happen in ChatGPT, Codex, Claude Desktop, etc. Lead marketing with clarity, not generic AI hype.
- Pricing direction: one clear all-features-included plan priced mainly by client count. Public slider starts at 5 clients for `$49/mo` and scales to 1,000 clients at `$4,900/mo`; eliminate 1-client tier and old 100-client ceiling. Existing customers are grandfathered forever. “Client” means one profile/store/franchise branch. Do not publicly attack competitors; make Oviond’s positive clarity strong enough. API/MCP is a premium differentiator, not the whole homepage story.
- Competitor intelligence base lives at `research/competitor-intelligence/` and covers 43 profiles. Market pattern: competitors monetize complexity via source credits, connected accounts, users, white-label/custom-domain/API/AI/MCP gates, refresh/history limits, support tiers, or annual commitments. Oviond wedge: simple client-count pricing with core reporting features included.
- Supabase growth-machine thesis: build a read-only Nicole Growth Intelligence Layer exposing trials, activation milestones, billing status, usage, data-source health, automation/reporting activity, churn risk, and lifecycle triggers; then pipe clean events into Sequenzy and combine Gleap support signal.
- Lifecycle email: MailerLite and Loops are retired; Sequenzy is the rebuild path. `SEQUENZY_API_KEY` works for read access; live API has broader reads than docs but needs explicit `User-Agent`, and some endpoints/envelopes are inconsistent.
- Gleap is core operating context for support, tickets, roadmap signal, help center, retention diagnosis, product friction, customer language, and prioritization. Treat it as activation/trust/retention signal, not just a support inbox. Caveats: tracker-ticket endpoint was empty in April validation; support work looked Michelle-dependent.
- Meta access is configured. Meta Ads MCP/CLI should be remembered for later optimization, but use read/audit/least-permission first and never relaunch spend before the ads-off hold is lifted. Durable lesson: tighter Facebook-only previous-visitor remarketing with stronger image creative was cleaner than broader noisy mixed-placement setups.
- Oviond design operating system: Nicole as art director/QA, dedicated Oviond design skill as reusable brain, and Gemini/Nano Banana mainly for concept/composition/brand-feel generation. Use the November 2024 brand refresh as source of truth; prefer text-free or overlay-safe outputs; blog covers should bias toward product-preview aesthetics.
- Platform direction: OpenClaw runs in AlphaClaw-managed Railway. Stay inside OpenClaw and polish this setup; Chris parked Hermes migration and Figma/Codex implementation work for now.

## Additional durable operating context

- Google Workspace's working operator path is `gws-nicole`, using delegated impersonation of `nicole@oviond.com`; Gmail and Calendar access were verified live on 2026-03-14.
- OpenClaw dreaming was enabled with a cautious stance: treat dream output as a review/backfill aid, not automatic truth, and only promote grounded material deliberately.
- Historical Google Ads context: on 2026-04-03 Chris approved a controlled USA Search campaign (`USA | Search | Trial | Core Intent | 2026-04-03`, campaign `23720451302`) at `R250/day` with USA-only Search targeting, no Display/Search Partners, tight exact/phrase buyer-intent keywords, and junk-intent negatives. This remains historical context only; ads must stay off until Chris reauthorizes after the new website and tracking are live.
- The Oviond design system should be rebuilt carefully from the original November 2024 brand guide and the dedicated `oviond-design-director` skill, with Nicole acting as creative director/QA and Gemini/Nano Banana used mainly for concept, composition, and abstract brand-feel generation.
- The real Figma source-of-truth file for Oviond design work is `Oviond Design System 2026`, file key `bqExCU8AssikVUKVxXpEk3`, currently in folder `Oviond Brand CI Refrences 2026`; it was effectively blank when inspected, making it suitable for a clean system build.
- Chris chose Figma as the scalable production source of truth for Oviond creative work; direct Codex/Figma canvas work remains blocked until a Figma MCP server is wired into ACPX/Codex. The ACPX config hook identified for that future work is `/data/.acpx/config.json`.
- Chris decided on 2026-04-16 to park the active Figma/Codex implementation work for now.

## Pointers

- Local operator details, helper paths, wrapper commands, and implementation notes live in `TOOLS.md`.
- Secret material must never be stored in tracked workspace files; keep only references to approved secret storage locations.

## Curated promotions from short-term memory

- South Africa Google Ads reporting lesson: when reviewing SA campaign health, separate real free-trial signal from cheap traffic noise before calling the account healthy. Historical April 2026 SA checks showed account access worked but campaigns could be paused or noisy.
- Retention/product durability lesson: Small Agency Monthly and some legacy monthly cohorts appear fragile; treat Oviond's churn problem as a durable-value / stickiness issue, not only a pricing issue. Prioritize activation, client-ready report confidence, and integration stability.
- GA4 interpretation reminder: the `Oviond Website + App` property mixes marketing, app, white-label report domains, and dev traffic; do not treat top-level GA4 channel, geo, landing-page, or conversion views as clean acquisition truth without host/event segmentation.
- Meta remarketing status: the USA remarketing campaigns remained paused in late April/May 2026, with control/test history showing weak or noisy landing-page and custom-conversion signal. Do not restart Meta spend while the standing ads-off/tracking caution remains in force.
