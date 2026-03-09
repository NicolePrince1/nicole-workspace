# Oviond Growth Strategy: $28.5k → $100k MRR by December 2026

**Author:** Nicole Prince, VP Marketing
**Date:** 9 March 2026
**Timeline:** 9 months (March → December 2026)

---

## The Numbers

**Where we are:**
- ~$28.5k MRR
- ~350 active paying customers
- ~$81 average MRR per customer
- ~46 active trials right now
- ~1,916 lapsed customers (cancelled or stale trials in last 180 days)
- ~1,027 lifetime deal users
- ~2,644 dormant contacts

**Where we need to be:**
- $100k MRR by December 2026
- That's +$71.5k net new MRR in 9 months
- ~$8k net new MRR per month (accelerating)

**The math (three levers):**
1. **New customers:** At $81 ARPU, we need ~880 net new paying customers (or ~98/month)
2. **Reduce churn:** Every customer we keep is one we don't need to replace
3. **Increase ARPU:** Move $81 → $100+ through upsells, annual plans, and higher tiers

Realistically, it's a blend of all three. Here's how.

---

## Current Funnel (Last 30 Days)

| Stage | Volume | Conversion |
|-------|--------|------------|
| Website visitors | 15,454 users | — |
| Trial signups | ~265 unique | 1.7% of visitors |
| Active trials | 46 | — |
| New paying customers | ~23 (onboarding group) | ~8-9% of signups |
| Paying customers (total) | ~350 | — |

**Biggest leaks:**
1. **Visitor → Trial (1.7%)** — Industry benchmark is 3-7% for SaaS free trials. Doubling this alone doubles everything downstream.
2. **Trial → Paid (~8-9%)** — Industry benchmark is 15-25%. This is where the onboarding experience matters most.
3. **Churn** — 1,916 lapsed in the last 180 days against 350 active = churn is eating us alive.

---

## The Five Plays

### PLAY 1: Fix Trial-to-Paid Conversion (Month 1-3)
**Impact: HIGH | Effort: MEDIUM**
**Target: 8% → 20% conversion**

This is the single highest-leverage move. We're generating trials but losing them before they pay.

**Actions:**
- [ ] Audit the 15-day trial onboarding automation (1.1 Trialling Simplified) — what emails, when, what content?
- [ ] Map the actual user journey: signup → first login → first report → first share → payment
- [ ] Identify where trials drop off (need product data — will ask Chris)
- [ ] Rewrite onboarding emails with clear "next step" CTAs, not feature dumps
- [ ] Add a "day 3" personal check-in email from me (nicole@oviond.com)
- [ ] Create a "quick win" guide: "Set up your first client report in 5 minutes"
- [ ] Implement trial expiry urgency: countdown emails at day 10, 13, 14, 15
- [ ] Test trial extension as a conversion tool (day 15: "Need more time? Here's 7 more days")

**Metrics to track weekly:**
- Trial starts
- Day 1/3/7 activation rates
- Trial-to-paid conversion rate
- Time to first report created

### PLAY 2: Reactivate Lapsed Customers (Month 1-2)
**Impact: HIGH | Effort: LOW**
**Target: Reactivate 100-150 customers ($8-12k MRR)**

We have 1,916 lapsed customers who already know the product. This is the cheapest MRR we can get.

**Actions:**
- [ ] Segment lapsed customers by: recency, previous plan value, reason for leaving
- [ ] Build a 5-email reactivation sequence: "Here's what's new since you left"
- [ ] Offer a comeback incentive: 30% off first 3 months, or free trial extension
- [ ] Personal outreach to high-value churned customers (was on $100+/mo plans)
- [ ] Run a Meta remarketing campaign to churned customer emails (custom audience)

**Note:** There's already a "101 - Reactivate or Scrub" automation (31K sends) and recent Feb/Nov reactivation series. Need to audit what worked and what didn't before launching another round.

### PLAY 3: Double Organic Traffic (Month 1-6)
**Impact: HIGH | Effort: MEDIUM | Compounds over time**
**Target: 5,253 → 10,000+ organic sessions/month**

Organic search is our most efficient channel (123 signups last 30 days, zero cost). The data shows massive untapped potential.

**Quick wins (position 10-20, high impressions — move to page 1):**
- [ ] `/client-onboarding-checklist/` — 40K impressions, pos 18 → optimize, internal link, refresh content
- [ ] `/content-in-social-media-marketing/` — 30K impressions, pos 12 → close to page 1
- [ ] `/digital-marketing-reporting-explained/` — 13.5K impressions, pos 14.5 → this is a CORE topic for us
- [ ] `/free-ai-tools-for-digital-marketing/` — 14.4K impressions, pos 20 → trending topic, refresh
- [ ] `/importance-of-paid-advertising/` — 13.7K impressions, pos 24 → longer play

**New content strategy:**
- [ ] Identify top 20 keywords agencies search when looking for reporting tools
- [ ] Create comparison pages: "Oviond vs AgencyAnalytics", "Oviond vs Looker Studio", "Oviond vs Swydo"
- [ ] Build a "reporting templates" hub (the /reporting-templates/ pages already rank — expand)
- [ ] Publish 2 high-quality blog posts per month targeting high-intent keywords
- [ ] Optimize existing pages for featured snippets and People Also Ask

### PLAY 4: Fix Paid Advertising (Month 2-4)
**Impact: MEDIUM | Effort: MEDIUM**
**Target: Profitable paid acquisition at <$100 CAC**

Current Meta ads are inefficient:
- "Remarketing USA" — R3,578 spent, 17 landing page views, ~R210 per landing page view
- Only 43 link clicks from 128K impressions (0.06% CTR) — the creative isn't working
- Google Ads basically off (22 sessions last 30 days from paid search)

**Actions:**
- [ ] Pause current Meta campaign — it's burning budget with bad targeting/creative
- [ ] Build new creative: focus on the "simple reporting" message, show the actual product
- [ ] Test Google Ads for high-intent keywords: "agency reporting tool", "white label reporting", "automated client reports"
- [ ] Set up proper conversion tracking (trial signup as the conversion event)
- [ ] Start with $500/month test budget, scale what works
- [ ] Build lookalike audiences from our 350 paying customers

### PLAY 5: Increase ARPU (Month 3-6)
**Impact: MEDIUM | Effort: LOW**
**Target: $81 → $100+ average MRR**

**Actions:**
- [ ] Analyze plan distribution (need Stripe data — currently not in env vars)
- [ ] Identify customers near their client limit (upsell trigger)
- [ ] Build annual plan promotion: "Save 20% — lock in your rate"
- [ ] Segment paying customers by usage and send targeted upgrade nudges
- [ ] Add premium features or higher tiers that justify increased pricing

The MailerLite groups 3.6 (Ready to Upgrade - Annual), 3.7 (Ready to Upgrade - Client Limit) exist but have 0 members — need to populate these segments.

---

## Tech Stack & Migration Strategy (March 2026)

### Pivot to Loops.so
- **Decision:** Moving from MailerLite to Loops.so for email automation.
- **Why:** Loops is API-first and SaaS-native; removes manual UI drag-and-drop bottlenecks. Allows full programmatic control of onboarding, activation, and churn sequences.
- **End-to-End Migration Strategy:**
    1. **Infrastructure (Days 1-2):** Set up Loops.so account, configure DNS (SPF/DKIM/DMARC), map Stripe data to custom fields.
    2. **Logic Migration (Days 3-5):** Re-engineer 15-day trial sequence (behavior-driven triggers, not just time-based).
    3. **Content Sync (Days 6-7):** Insert new copy from audit into Loops templates.
    4. **Cutover (Day 8):** Shadow run, then activate.

---

## Operational Cadence

### Daily (Automated / Heartbeat)
- [ ] Check for urgent support signals or churning customers
- [ ] Monitor trial signups (Stripe webhook or MailerLite new subscriber alerts)
- [ ] Check email deliverability / automation errors

### Weekly (Every Monday — Report to Chris)
- [ ] **Weekly metrics dashboard:**
  - New trials started
  - Trial → paid conversions
  - MRR change (new + expansion - churn)
  - Website traffic + signups by channel
  - Email automation performance
  - Ad spend + results
- [ ] Review top Search Console movers (keyword position changes)
- [ ] Check MailerLite automation health (delivery rates, open rates)

### Monthly (First Monday of Month)
- [ ] **Monthly growth report** — full MRR analysis, funnel metrics, channel performance
- [ ] Content calendar for next month (blog posts, social posts)
- [ ] Review and optimize ad campaigns
- [ ] Competitor check (pricing, features, positioning changes)
- [ ] Update this strategy doc with learnings

### Quarterly (End of Quarter)
- [ ] Full strategy review — what worked, what didn't, what to change
- [ ] Adjust MRR targets based on trajectory
- [ ] Plan next quarter's big bets

---

## Cron Jobs & Reminders

| Schedule | Task |
|----------|------|
| Mon 09:00 SAST | Weekly metrics pull + report to Chris |
| 1st of month, 09:00 | Monthly growth report |
| Wed 12 Mar | Check Google Ads API Basic Access approval |
| Daily 08:00 | Check for new trial signups (MailerLite) |
| Fri 14:00 | Weekly SEO check (GSC position changes) |

---

## Immediate Next Steps (This Week)

1. **Get Stripe key into env vars** — I'm blind to revenue data right now
2. **Audit the trial onboarding automation** — read every email in the 1.1 sequence
3. **Audit the lapsed customer reactivation** — what's been tried, what worked?
4. **Optimize the top 3 GSC quick-win pages** — content refresh for page 2 → page 1
5. **Pause the Meta remarketing campaign** — it's burning R350/day for almost nothing
6. **Set up the weekly reporting cron** — automated Monday morning dashboard

---

## MRR Growth Trajectory (Target)

| Month | Target MRR | Net New | Cumulative New Customers |
|-------|-----------|---------|-------------------------|
| Mar 2026 | $30k | +$1.5k | Baseline + reactivations |
| Apr 2026 | $34k | +$4k | Reactivation campaign peaks |
| May 2026 | $39k | +$5k | Onboarding fixes live |
| Jun 2026 | $45k | +$6k | SEO content starting to rank |
| Jul 2026 | $52k | +$7k | Paid ads optimized |
| Aug 2026 | $60k | +$8k | All channels firing |
| Sep 2026 | $69k | +$9k | Compounding organic |
| Oct 2026 | $79k | +$10k | Annual plan push |
| Nov 2026 | $89k | +$10k | Black Friday + expansion |
| Dec 2026 | $100k | +$11k | 🎯 Target |

This assumes decreasing churn as we improve onboarding and increasing acquisition as organic and paid scale. The first 2-3 months are foundation work; months 4-9 are where compounding kicks in.

---

*This is a living document. Updated as we learn, test, and iterate.*
