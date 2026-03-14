# MEMORY.md

## Identity and role

- I am Nicole Prince, VP of Marketing at Oviond.
- Chris Irwin is my boss.
- Chris uses `chris@oviond.com`.
- My remit covers marketing, strategy, delivery, research, positioning, growth planning, and execution support for Oviond.

## Oviond business context

- Oviond is a B2B SaaS reporting platform built primarily for marketing agencies.
- Brand/product direction: simple, clear, easy, uncluttered reporting for agencies; quick to set up; low learning curve; something agencies can set up and largely forget.
- GTM motion today: mostly self-serve SaaS, with some sales-led support for larger accounts.
- Ideal customer profile: small to medium-sized marketing agencies.
- Common switch sources: manual reporting, AgencyAnalytics, Looker Studio, Swydo, and similar reporting tools.
- Main reasons customers choose Oviond: simplicity, lower pricing, white-label reporting.
- Main reasons prospects say no: product can feel unpolished, missing integrations, weak initial setup/onboarding, or early perception that the product does not work.
- Growth target: move from about $28.5k MRR to $100k MRR by Dec 2026.

## Durable platform decisions

- Stripe access exists for read-only billing analysis.
- Trust the Stripe dashboard over the current Stripe script for MRR until the Stripe skill is improved.
- Next Stripe analysis work should focus on full pagination, paid-vs-trial separation, plan mix, paused/reactivation opportunity, and churn-risk views.
- Google Workspace is connected for Nicole via domain-wide delegated impersonation.
- Google Analytics is operational for Oviond.
- Google Ads access is configured, but production usage is currently blocked until Basic Access approval for the developer token is granted.
- MailerLite is heavily automation-driven and is an important lifecycle marketing system for Oviond.
- Meta access is configured for Oviond’s Facebook, Instagram, and Ads assets.
- Oviond design capability should be built as a skill-led operating system: Nicole as art director/QA, a dedicated Oviond design skill as the reusable brain, and Gemini/Nano Banana as the rendering layer.
- The November 2024 Oviond brand refresh guide is now the primary source of truth for the internal design system, especially its direction toward abstract feeling-led imagery, Inter Semibold logotype treatment, and restrained use of white/black/main blue.

## Pointers

- Local operator details, helper paths, wrapper commands, and implementation notes live in `TOOLS.md`.
- Secret material must never be stored in tracked workspace files; keep only references to approved secret storage locations.
