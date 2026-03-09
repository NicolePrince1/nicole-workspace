# Trial Onboarding Email Audit — 9 March 2026

## Executive Summary

The trial onboarding automation (1.1 Trialling Simplified) has a **32.8% open rate and 0.91% click rate** across 10,766 sends. The click rate is critically low — people are reading but not acting. The sequence has structural problems that are likely contributing to the low ~8-9% trial-to-paid conversion rate.

**Verdict: Needs significant rework. The foundation is there, the execution needs tightening.**

---

## Current Sequence Map

| Day | Email | Subject | From |
|-----|-------|---------|------|
| 0 | Welcome | "Welcome to Oviond, {name}! Let's start your reporting trial" | Chris from Oviond |
| 1 | Build First Report | "Tips for Creating Your First Oviond Report" | Oviond Customer Success |
| 2 | Connect Data | "Connect Your Clients Data to Oviond!" | Oviond Team |
| 3 | Automate | "Automate your marketing reports—save valuable agency hours" | Oviond Team |
| 4 | Templates | "Client Reporting with 1 Click Templates" | Oviond Team |
| 5 | Branding | "Give your reports the professional touch, {name}" | Oviond Team |
| 6 | Share Reports | "Share Your Agency Reports and Impress Clients" | Oviond Team |
| — | *4-day silence* | | |
| 12 | Pricing | "Your Oviond trial ends soon—plans from only $15/month!" | Oviond Team |
| — | *3-day silence* | | |
| 15 | Final Reminder | "Final reminder: Your Oviond trial ends today" | Oviond Team |

**End of sequence:** Routes to Paying Customer Onboarding (if converted) or Trial Expired Re-Engagement (if not).

---

## Problems Identified

### 🔴 CRITICAL: Wrong order of operations
Email 1 (Day 1) says "Tips for Creating Your First Report" but email 2 (Day 2) says "Connect Your Clients Data." **You can't build a report without data.** The logical order should be: connect data → build report → customize → share.

### 🔴 CRITICAL: 7 emails in 6 days is too aggressive
Users get hammered with a daily email for an entire week. This explains the **586 unsubscribes from the trial group** — people are opting out of onboarding. For a 15-day trial, this is way too front-loaded.

### 🔴 CRITICAL: 0.91% click rate = emails lack clear CTAs
A 33% open rate means people are reading. But fewer than 1 in 100 clicks through. The emails are likely too long, too feature-dumpy, or the CTAs are buried/unclear. Every email should have ONE obvious action button.

### 🟡 MAJOR: No behavior-based branching
Everyone gets the same 9 emails regardless of whether they've:
- Connected their data sources
- Created a report
- Shared a report with a client
- Invited team members

Someone who set up everything on Day 1 still gets "Connect Your Data" on Day 2. This feels out of touch and trains users to ignore the emails.

### 🟡 MAJOR: The "dead zone" (Day 7-11)
After 7 straight emails, there's complete silence for 5 days during the most critical decision-making window. Day 7-11 is when trial users are deciding whether this tool is worth paying for. We go dark.

### 🟡 MAJOR: Only 1 pricing email before the deadline
The pricing email arrives on Day 12. That's the FIRST time we talk about cost. By Day 12, many users have already mentally checked out. Pricing/value should be woven in earlier.

### 🟡 MAJOR: Inconsistent sender identity
The welcome comes from "Chris from Oviond" (personal, warm) and then immediately switches to "Oviond Customer Success" and "Oviond Team" (corporate, impersonal). Pick one voice and stick with it.

### 🟡 MODERATE: No social proof
None of the subject lines reference other agencies, case studies, or success stories. Trial users need confidence that other agencies like them are succeeding with Oviond.

### 🟡 MODERATE: Subject lines are feature-focused, not outcome-focused
"Connect Your Clients Data to Oviond!" tells users what to do. "Your clients will love this week's report" tells them WHY. Outcome-focused subjects get higher opens and clicks.

---

## What's Working

✅ **Welcome email from Chris** — personal touch from the founder is good
✅ **Subscription status check** — automatically routes paying customers out of the trial sequence
✅ **End-of-sequence routing** — properly segments into Trial Expired or Lapsed groups
✅ **Content topics are right** — the WHAT is correct (setup, templates, branding, sharing, automation)
✅ **The paying customer onboarding (3.1)** has a 52% open rate and 2.88% click rate — 3x better engagement, proving the product delivers value once people convert

---

## Recommended New Sequence

### Principles:
1. **One email, one action** — every email has exactly one CTA
2. **Behavior-aware** — skip steps the user has already completed (requires Stripe/product data sync)
3. **Spaced properly** — match the 15-day trial rhythm
4. **Outcome-focused** — sell the result, not the feature
5. **Consistent voice** — all from Chris (or Nicole), personal and warm
6. **Social proof throughout** — real agency examples

### Proposed Sequence:

| Day | Email | Subject (Draft) | Goal |
|-----|-------|-----------------|------|
| 0 | Welcome | "Welcome {name} — here's your 3-step quick start" | Set expectations, give a clear path |
| 1 | Connect Data | "Step 1: Connect {company}'s data (takes 2 mins)" | Activation — get data flowing |
| 3 | First Report | "Step 2: Your first client report is one click away" | Value moment — see the product work |
| 5 | Social Proof | "How [Agency X] cut reporting time from 4 hours to 15 minutes" | Build confidence |
| 7 | Share/Customize | "Step 3: Brand it, share it, impress your client" | Show the full loop |
| 9 | Value Reminder | "You've got 6 days left — here's what you'd lose" | Loss aversion, mid-trial nudge |
| 11 | Pricing + ROI | "For less than one billable hour, never build a report manually again" | Frame the cost vs. their time |
| 13 | Urgency | "48 hours left on your trial, {name}" | Deadline pressure |
| 14 | Final | "Last day — your reports and data will be deleted tomorrow" | Maximum urgency |

**Key differences:**
- 9 emails over 15 days (vs 9 emails in 15 days, but front-loaded to 7 in 6 days)
- Logical order: connect → build → share (not build → connect)
- Social proof email on Day 5 (the decision wavering point)
- Pricing introduced on Day 11 (not Day 12)
- Two urgency emails at the end (Day 13 + 14) instead of one
- Every subject is outcome-focused and personal

---

## Downstream Sequences

### 1.2 Trial Expired Re-Engagement (currently 32 steps, 22% open, 0.21% click)
- Open rate dropped from 33% (trial) to 22% — expected but the 0.21% click rate is abysmal
- Offers escalate: 15% off → personalized demo → 50% off first year → 50% last chance
- The discount ladder is good in concept but the emails aren't compelling enough
- **Recommendation:** Fewer emails, stronger copy, lead with what's changed since they left

### 3.1 Paying Customer Onboarding (18 steps, 52% open, 2.88% click)
- Much better engagement — these people are invested
- Smart mix of Chris (personal) and Customer Success (helpful)
- Topics: welcome → collaborate → customize → secure → brand → check-in
- **This is good.** Minor improvements but not broken.

---

## Immediate Action Items

1. [ ] **Reorder existing emails** — swap Day 1 and Day 2 at minimum (connect data before building reports)
2. [ ] **Reduce frequency** — space out to every 2 days instead of daily for the first week
3. [ ] **Rewrite subject lines** — outcome-focused, not feature-focused
4. [ ] **Add a social proof email** — case study or testimonial from a real agency
5. [ ] **Unify sender** — all from "Chris from Oviond" or a consistent persona
6. [ ] **Add urgency earlier** — pricing/value email on Day 9-10, not Day 12
7. [ ] **Write the new sequence** — implement the 9-email proposed sequence above

## Next Step
Get Chris's input on this audit, then I'll write the actual email copy for the new sequence and we can A/B test against the current one.
