# Nicole Launch Checklist — Oviond June 9 Launch

Owner: Nicole Prince  
Primary goal: launch clean, restore trust, drive qualified trials, and start the path from ~$28–29k MRR toward $100k MRR by Dec 2026.  
Standing rule: no Google Ads, Meta Ads, Sequenzy blast, or public launch push goes live until Chris gives explicit go-ahead and tracking is verified.

## Launch principles

1. **Trust first, traffic second.** Paid traffic only matters if the product, signup path, and tracking are clean.
2. **No vanity metrics.** Judge the launch on real trial starts, activation, Stripe/app truth, retention signal, and support friction.
3. **Move fast, but not messy.** Every external action gets a pre-flight check, owner, rollback path, and post-launch read.
4. **One clear message.** Oviond is simple agency reporting: invisible, dependable, and done.
5. **Do not overload the team.** Product stability is the launch asset. Marketing must support it, not create chaos.

---

## 1. Pre-launch command center

### By Friday before launch

- [ ] Confirm final launch date, launch window, and go/no-go owner with Chris.
- [ ] Confirm who is on standby:
  - [ ] Chris — final approval / business decisions
  - [ ] Lesedi — product/migration status
  - [ ] Brendan — verification/data source status
  - [ ] Support/Gleap owner — inbound customer issues
  - [ ] Nicole — comms, paid acquisition, lifecycle, reporting
- [ ] Create launch-day Slack thread/channel for live updates.
- [ ] Create simple launch status format:
  - Status: Green / Amber / Red
  - Current blocker
  - Next check time
  - Owner
- [ ] Prepare internal launch-day message for team.
- [ ] Prepare customer-facing release wording.
- [ ] Prepare rollback/hold language in case launch is delayed.

### Go/no-go checklist before any public push

- [ ] App is live and stable.
- [ ] Migration completed cleanly.
- [ ] Core signup path tested.
- [ ] Trial creation tested.
- [ ] Stripe/billing state tested.
- [ ] Key integrations/data sources verified.
- [ ] Known launch-critical bugs are closed or accepted by Chris.
- [ ] Tracking verified end to end.
- [ ] Support team knows what changed.
- [ ] Chris gives explicit go-ahead.

---

## 2. Tracking and measurement verification

### GA4 / GTM / website tracking

- [ ] Confirm new website/app routes are firing clean GA4 events.
- [ ] Confirm host segmentation is clean enough to separate marketing site from app/customer-report domains.
- [ ] Confirm no old polluted conversion events are being used as optimization goals.
- [ ] Confirm signup-related event names and definitions.
- [ ] Confirm pricing page, signup page, trial start, and key activation events.
- [ ] Confirm UTMs persist through signup where technically possible.
- [ ] Confirm Google Ads conversion mapping uses real signup/trial events, not soft pageviews.
- [ ] Confirm Meta pixel/custom conversion mapping uses real signup/trial events, not generic visitors.
- [ ] Capture screenshots/logs of successful event firing before launch push.

### Source-of-truth dashboard

- [ ] Build launch dashboard view using the cleanest available truth:
  - [ ] trials started
  - [ ] source / campaign
  - [ ] signup country
  - [ ] activation step completed
  - [ ] trial-to-paid later
  - [ ] support tickets by issue type
  - [ ] churn/cancellation movement
- [ ] Define first 72-hour reporting cadence:
  - [ ] day-of: every 2–3 hours
  - [ ] day 2–3: twice daily
  - [ ] week 1: daily readout

---

## 3. Sequenzy launch plan

### Broadcast vs sequence strategy for ~10,000 warm contacts

Nicole's recommendation: **do both, but not as one blunt blast.**

The ~10,000 warm contacts — mostly expired trials, churned users, old leads, and prior evaluators — are one of the highest-leverage launch assets. But treating them as one list would be risky: different people left for different reasons, at different times, with different levels of trust. The right move is a **controlled reactivation program**: one launch broadcast to create awareness, followed by segmented Sequenzy sequences to reel the right people back in.

Launch posture:

- [ ] Do **not** send one generic email to all 10,000 contacts on launch day.
- [ ] Clean and segment the list before any send.
- [ ] Use a controlled first broadcast wave only after launch/tracking is stable and Chris approves.
- [ ] Follow with short, segmented sequences based on who they are and how they respond.
- [ ] Watch deliverability, unsubscribes, spam complaints, replies, and trial starts before scaling to the full list.

Recommended segmentation:

- [ ] **Expired trials, never activated:** simple “Oviond is easier now — try again” sequence.
- [ ] **Expired trials, partially activated:** “You were close — here is what changed” sequence.
- [ ] **Churned customers:** more careful “we rebuilt what frustrated you” win-back sequence.
- [ ] **High-value churned customers:** manual/personal outreach before generic automation.
- [ ] **Old leads / newsletter contacts:** lighter launch announcement and education sequence.
- [ ] **Dormant/unengaged contacts:** slow re-permission/reactivation wave, not aggressive sales pressure.

Recommended flow:

1. **Launch announcement broadcast**  
   A controlled campaign announcing that the new Oviond is live, framed around simplicity, reliability, and rebuilt foundations — not hype.

2. **Behavior-based branching**  
   - Opened/clicked → enter relevant reactivation sequence.
   - Did not open → resend once with a different subject after a few days, then cool down.
   - Replied → route to support/sales/manual follow-up.
   - Started trial → suppress from win-back and enter trial activation sequence.
   - Unsubscribed/complained → suppress immediately.

3. **Segmented Sequenzy sequences**  
   3–5 emails max per segment. Keep the copy sharp, honest, and benefit-led. No long “we are excited” nonsense.

4. **Stop-loss rules**  
   Pause if bounce/spam complaints spike, if unsubscribes are ugly, if tracking is not clean, or if support starts seeing confusion from the email.

What success looks like:

- [ ] Reactivated trials from old expired trials.
- [ ] Win-back replies from churned customers.
- [ ] Real trial starts attributed to email.
- [ ] Activation quality, not just opens/clicks.
- [ ] Clear objections we can feed back into website/product/comms.

### Pre-launch audit

- [ ] Run/read-only audit of Sequenzy account state.
- [ ] Confirm active lists, tags, campaigns, templates, and sequences.
- [ ] Confirm sender domain/authentication and deliverability status.
- [ ] Confirm suppression/unsubscribe handling.
- [ ] Confirm customer segments available or importable:
  - [ ] active customers
  - [ ] trials
  - [ ] churned customers / cancelled accounts
  - [ ] old leads / newsletter list if usable
  - [ ] high-value historical accounts
  - [ ] agencies by plan/client count if available
- [ ] Confirm whether Stripe/billing lifecycle data is natively wired or must be handled through attributes/events.
- [ ] Confirm no dormant/broken sequence accidentally starts firing after launch.

### Launch email segments

- [ ] **Active customers:** “The new Oviond is live” — confidence, what changed, what to expect, support path.
- [ ] **Current trials:** “You can now test the new Oviond” — push activation and first report/dashboard creation.
- [ ] **Recently churned customers:** “We rebuilt the thing that frustrated you” — careful win-back, no overclaiming.
- [ ] **Old leads:** “A simpler Oviond is here” — fresh reason to try again.
- [ ] **High-value past customers:** more personal/manual outreach rather than a generic blast.

### Sequenzy campaign drafts

- [ ] Draft customer release email.
- [ ] Draft trial activation email.
- [ ] Draft churn win-back email.
- [ ] Draft old-lead relaunch email.
- [ ] Draft founder/Chris-style note if needed.
- [ ] Check all links, UTMs, reply-to, and unsubscribe behavior.
- [ ] Send test emails to internal addresses.
- [ ] Chris reviews and approves before sending.
- [ ] Send in controlled waves, not one reckless blast if list quality is uncertain.

### Sequenzy lifecycle sequences after launch

- [ ] New trial sequence, 5-email max:
  - Day 0: welcome + quickest path to value
  - Day 1: connect first data source
  - Day 3: create/send first client report
  - Day 6: white label/client-ready confidence
  - Day 10/12: conversion nudge + help offer
- [ ] Activation rescue sequence:
  - no data source connected within 24–48h
  - no report/dashboard created within 72h
  - trial inactive after signup
- [ ] Trial expiry rescue sequence.
- [ ] Win-back sequence for recent churners.
- [ ] Annual conversion sequence for stable monthly customers, later — not launch day.
- [ ] Keep all sequences disabled until reviewed and approved.

### Sequenzy metrics to monitor

- [ ] Deliverability / bounce rate.
- [ ] Opens and clicks by segment.
- [ ] Trial starts from email.
- [ ] Replies / objections.
- [ ] Unsubscribes and spam complaints.
- [ ] Activated trials, not just email clicks.

---

## 4. Google Ads relaunch plan

### Pre-flight

- [ ] Run Google Ads auth/access check.
- [ ] Pull historical campaign performance.
- [ ] Identify usable winners:
  - [ ] USA PMAX historical signal
  - [ ] high-intent search terms
  - [ ] prior negative keyword lessons
- [ ] Confirm conversion actions are clean and imported correctly.
- [ ] Remove/ignore polluted conversions.
- [ ] Confirm landing pages and final URLs.
- [ ] Prepare budgets and stop-loss rules.

### Launch campaign structure

- [ ] **USA Search — Core Intent**
  - agency reporting software
  - client reporting software
  - white label reporting software
  - marketing dashboard software
  - automated client reports
  - marketing agency reporting tool
- [ ] **Competitor/switching intent** only if landing page supports it and legal tone is clean.
- [ ] **Brand Search** if needed to protect launch demand.
- [ ] **PMAX** only if signup conversion tracking is verified and asset quality is strong.
- [ ] No Display campaign relaunch unless there is a specific remarketing reason.
- [ ] Search partners off initially unless performance proves otherwise.

### Launch-day actions after Chris approval

- [ ] Apply validated campaign changes.
- [ ] Start with controlled daily budgets.
- [ ] Monitor search terms same day.
- [ ] Add negatives quickly:
  - free templates
  - jobs
  - courses
  - unrelated dashboard/reporting terms
  - BI-only enterprise noise if irrelevant
- [ ] Track cost per real trial.
- [ ] Track signup quality and country.
- [ ] Reallocate budget only after clean signal.

---

## 5. Meta / Facebook Ads relaunch plan

### Pre-flight

- [ ] Audit pixel/custom conversions.
- [ ] Confirm Website Visitor is not being mistaken for signup.
- [ ] Confirm Free Trial Signup / Customer Signs Up conversion mapping if available.
- [ ] Audit existing paused campaigns and creatives.
- [ ] Confirm broken ads remain paused or rebuilt.
- [ ] Prepare warm audiences:
  - [ ] website visitors
  - [ ] pricing visitors
  - [ ] signup visitors who did not convert
  - [ ] customer/lookalike audiences only if quality is strong
- [ ] Prepare exclusions:
  - [ ] existing active customers where appropriate
  - [ ] recent converters

### Launch campaign structure

- [ ] **Warm remarketing — Free Trial**
  - objective based on clean signup/trial conversion if available
  - otherwise controlled landing-page-view interim only with caution
- [ ] **Product proof creative**
  - simple screenshots/product-led visuals
  - agency pain → clean report outcome
  - white-label/client-ready angle
- [ ] **Launch announcement retargeting**
  - “The new Oviond is live”
  - “Agency reporting, rebuilt to be simpler”
- [ ] Avoid broad cold Meta spend until tracking and creative signal are proven.

### Launch-day actions after Chris approval

- [ ] Turn on warm remarketing first.
- [ ] Keep budgets conservative.
- [ ] Watch frequency, CTR, LPV, signup quality.
- [ ] Kill weak creative fast.
- [ ] Do not scale based on cheap clicks alone.

---

## 6. Gleap launch plan

### Product news / announcement

- [ ] Draft Gleap product update:
  - headline: new Oviond is live
  - what changed
  - who it affects
  - what customers should do next
  - where to get help
- [ ] Keep tone confident but not overhyped.
- [ ] Link to help docs / migration notes if available.
- [ ] Chris/product review before publishing.

### Support readiness

- [ ] Create/confirm support macros for likely launch issues:
  - login/access issue
  - missing data source
  - report/dashboard discrepancy
  - migration question
  - billing/pricing question
  - integration reconnect issue
- [ ] Create internal issue labels/tags:
  - launch-bug
  - migration
  - data-source
  - billing
  - login
  - report-accuracy
  - urgent-customer-risk
- [ ] Monitor Gleap aggressively on launch day.
- [ ] Summarize recurring issues back to team twice daily in first 72 hours.

### Help center

- [ ] Update or prepare key articles:
  - getting started
  - connecting a data source
  - creating first dashboard/report
  - white label/client portal basics
  - billing/trial FAQs
  - migration/new version FAQs
- [ ] Identify gaps from support tickets and patch quickly.

---

## 7. Existing customer communication

### Before public announcement

- [ ] Confirm whether existing customers need operational migration instructions.
- [ ] Confirm grandfathering/pricing language: existing customers remain on current plans unless Chris says otherwise.
- [ ] Prepare customer FAQ.
- [ ] Prepare support escalation route.

### Customer email themes

- [ ] “The new Oviond is live.”
- [ ] “What changed and what did not change.”
- [ ] “Your plan/pricing remains safe.”
- [ ] “Here is how to get help.”
- [ ] “Here is the fastest way to get value from the new version.”

---

## 8. Public marketing and content

### Website

- [ ] Check homepage message.
- [ ] Check pricing page.
- [ ] Check signup CTA.
- [ ] Check comparison/value pages if live.
- [ ] Check meta titles/descriptions.
- [ ] Check OG/social images.
- [ ] Check canonical URLs and redirects.
- [ ] Check noindex/robots issues.

### Blog / launch article

- [ ] Draft launch post if useful.
- [ ] Keep it customer-benefit-led, not engineering-heavy.
- [ ] Include simple positioning:
  - less reporting chaos
  - faster setup
  - cleaner client-ready reports
  - white label included
  - simple pricing

### Social

- [ ] Prepare LinkedIn launch post.
- [ ] Prepare X/Twitter short version if channel is active.
- [ ] Prepare Facebook page update if useful.
- [ ] Prepare founder-style Chris post if he wants one.
- [ ] Do not post until launch is confirmed stable.

---

## 9. Sales / win-back / retention plays

### Recent churn win-back

- [ ] Pull recent churn/cancel list where available.
- [ ] Prioritize high-value and recent accounts.
- [ ] Group by likely reason:
  - unused
  - switched service
  - complexity
  - data trust
  - missing integration
  - price/value
- [ ] Draft personal outreach for top accounts.
- [ ] Do not spam sensitive churned customers with generic hype.

### Current trial rescue

- [ ] Pull active trials.
- [ ] Identify trials expiring within 7 days.
- [ ] Identify trials with no activation event.
- [ ] Send targeted activation nudges.
- [ ] Offer help/manual setup for high-fit agencies.

### Existing customer retention

- [ ] Watch support tickets from active customers.
- [ ] Identify high-MRR customers with launch friction.
- [ ] Escalate high-risk customers quickly.
- [ ] Prepare “we’ll help you through this” messaging.

---

## 10. Launch day operating rhythm

### T-0: before Chris says go

- [ ] Confirm product green.
- [ ] Confirm tracking green.
- [ ] Confirm support ready.
- [ ] Confirm customer comms ready.
- [ ] Confirm paid campaigns ready but paused.
- [ ] Confirm Sequenzy campaigns ready but unsent.
- [ ] Confirm Chris approval.

### Hour 0–1: launch starts

- [ ] Internal Slack announcement.
- [ ] Publish/enable customer-facing release note if approved.
- [ ] Send first controlled customer email wave if approved.
- [ ] Turn on Google Search first if tracking is verified.
- [ ] Turn on Meta warm remarketing if tracking is verified.
- [ ] Start live monitoring dashboard.

### Hour 1–4

- [ ] Check signup flow after real traffic begins.
- [ ] Check conversion events in GA4/GTM/Google/Meta.
- [ ] Check Gleap for new issues.
- [ ] Check email deliverability and link clicks.
- [ ] Check paid spend and search terms.
- [ ] Send first status update to Chris/team.

### End of launch day

- [ ] Report:
  - trials started
  - traffic by source
  - paid spend
  - cost per trial if enough data
  - support issues
  - tracking issues
  - blockers for day 2
- [ ] Decide whether to scale, hold, or pause spend.

---

## 11. First 72 hours after launch

### Daily checks

- [ ] Trial starts.
- [ ] Trial activation quality.
- [ ] Signup source quality.
- [ ] Paid spend and CPA.
- [ ] Search terms and negatives.
- [ ] Meta creative performance.
- [ ] Sequenzy deliverability and replies.
- [ ] Gleap ticket themes.
- [ ] Bugs/friction affecting conversion.
- [ ] Churn/cancellation signal.

### Actions

- [ ] Kill waste quickly.
- [ ] Shift spend toward clean trial sources.
- [ ] Patch lifecycle emails based on objections.
- [ ] Feed support friction into product priorities.
- [ ] Prepare next customer/prospect update if launch is stable.

---

## 12. Stop-loss rules

Pause or hold campaigns if:

- [ ] Signup/trial tracking is broken.
- [ ] Product has a launch-critical bug.
- [ ] Paid traffic is spending without real trial signal.
- [ ] Meta optimizes to visitor junk again.
- [ ] Google search terms drift into irrelevant traffic.
- [ ] Support queue shows a systemic launch issue.
- [ ] Email deliverability shows abnormal bounce/spam complaints.

---

## 13. Nicole's immediate next tasks

- [ ] Turn this checklist into working launch board/tasks.
- [ ] Audit Sequenzy state read-only.
- [ ] Draft Sequenzy launch emails.
- [ ] Draft Gleap product news copy.
- [ ] Draft internal Slack launch-day command message.
- [ ] Prepare Google Ads relaunch structure.
- [ ] Prepare Meta relaunch structure.
- [ ] Prepare launch reporting template.
- [ ] Prepare customer FAQ/release copy.
- [ ] Keep all external sends/activation behind Chris approval.
