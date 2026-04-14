# Oviond Growth Operating System

_Last updated: 2026-04-14_

This is the durable working to-do list for getting Oviond onto a clean path toward **$100k MRR by Dec 2026**.

## How we use this

- This file is the **single working source of truth** for the current growth push.
- We keep it simple and alive, not pretty and forgotten.
- New work gets added here.
- Completed work gets marked done here.
- If priorities change, we reorder this file instead of pretending the old plan still matters.

## Current situation

- Revenue is still roughly **$28.5k to $28.7k MRR**.
- Paid media is **paused on purpose** until measurement is trustworthy.
- Measurement has been dirty, especially because GA4 has mixed website, app, and white-label traffic.
- GTM cleanup is now live, but the full analytics stack still needs verification.
- Retention is a bigger problem than pure top-of-funnel volume.
- Main churn drivers appear to be **unused**, **switched service**, **complexity**, and **client-trust / client-readiness issues**.
- Sequenzy is the rebuild path for lifecycle, but the operating system is not fully live yet.
- Gleap is now a critical source of truth for friction, support pain, and retention risk.
- We now have an extra **$70,000** available for paid media, but it should only be deployed once the system is tight enough to trust.

## Primary objective

**Build a clean, measurable, activatable funnel, then relaunch paid media with discipline.**

## Rules

1. No paid scaling before tracking truth.
2. No optimisation against polluted goals.
3. Retention and activation matter as much as acquisition.
4. Every item must have a next concrete action.
5. If something is important, it goes on this list.

## Status key

- `NOW` = active priority
- `NEXT` = ready immediately after current priority
- `LATER` = important, but not yet the next move
- `BLOCKED` = waiting on something external
- `DONE` = completed

## Top 10 priorities

### 1. Lock the measurement truth map
**Status:** NOW  
**Why it matters:** If we cannot define the real business events cleanly, every dashboard and ad platform will keep lying to us.  
**Definition of done:** We have one agreed definition each for trial started, verified signup, activation, paid, churn, past_due, and attribution source of truth.  
**Next action:** Write the event dictionary and truth hierarchy across app, GA4, Google Ads, Meta, and Stripe.

### 2. Finish separating website and app analytics
**Status:** NEXT  
**Why it matters:** Mixed host data makes acquisition reporting and landing-page analysis unreliable.  
**Definition of done:** `www.oviond.com` and `v2.oviond.com` are cleanly separated in tracking, with remaining non-GTM senders identified or removed.  
**Next action:** Recheck GA4 after propagation time, then trace any remaining `v2` analytics senders outside GTM.

### 3. Rebuild conversion tracking around real business outcomes
**Status:** NEXT  
**Why it matters:** We cannot spend against junk conversions and expect sane CAC.  
**Definition of done:** Google Ads, Meta, and GA4 optimise against real signup / activation outcomes, not noisy placeholder events.  
**Next action:** Audit all active conversion actions and mark each one keep, demote, fix, or remove.

### 4. Baseline the real funnel end to end
**Status:** NEXT  
**Why it matters:** We need to know exactly where growth is leaking before we throw fuel on it.  
**Definition of done:** We have a baseline for visit -> trial -> verified -> activated -> paid, segmented by source and geography where possible.  
**Next action:** Pull the latest clean funnel numbers and build the first baseline snapshot.

### 5. Run a trial activation rescue push
**Status:** NEXT  
**Why it matters:** Near-expiry trials are the fastest path to immediate revenue lift.  
**Definition of done:** High-risk active trials have been identified, prioritised, and contacted with a clear rescue sequence.  
**Next action:** Build the at-risk trial list and define the rescue message path.

### 6. Put the first core Sequenzy lifecycle flows live
**Status:** NEXT  
**Why it matters:** Activation and recovery cannot stay manual if we want scalable growth.  
**Definition of done:** Core flows are live for trial start, verify email, onboarding nudges, activation rescue, and past-due recovery.  
**Next action:** Turn the existing draft work into a production-ready minimum viable lifecycle setup.

### 7. Build the retention attack plan
**Status:** LATER  
**Why it matters:** The business likely misses the goal if churn stays where it is, even with better acquisition.  
**Definition of done:** We have a practical retention plan covering delinquency rescue, win-backs, annual conversion, and high-risk monthly cohorts.  
**Next action:** Segment churn and churn-risk accounts into action buckets.

### 8. Turn Gleap friction into the top 5 product fixes
**Status:** LATER  
**Why it matters:** Product friction is poisoning activation, trust, and retention.  
**Definition of done:** We have a ranked list of the top 5 growth-blocking product/setup issues with clear owners and rationale.  
**Next action:** Pull repeated Gleap pain themes and match them to churn / activation evidence.

### 9. Design the paid media relaunch architecture
**Status:** LATER  
**Why it matters:** The $70k only matters if deployed into a system that can measure and compound.  
**Definition of done:** We have a relaunch plan covering budget split, geo priority, campaign structure, landing paths, creative needs, and stop-loss rules.  
**Next action:** Draft the controlled relaunch framework, assuming US-first unless data says otherwise.

### 10. Make the controlled relaunch decision
**Status:** LATER  
**Why it matters:** Spending should be a decision earned by evidence, not by impatience.  
**Definition of done:** We have a yes/no go-live decision based on clean tracking and credible funnel truth.  
**Next action:** Define the exact criteria that must be true before paid media turns back on.

## Parking lot

Use this section for important items that are real, but not top-10-right-now work.

- Investigate all white-label host pollution in the mixed GA4 property.
- Review annual-plan conversion opportunities in the mature monthly base.
- Build the long-term AI-assisted reporting-system positioning roadmap.
- Revisit Google Ads USA Search once measurement and landing-path confidence are restored.

## Daily operating rhythm

When we review this list, we should ask only five things:

1. What is the single most important thing today?
2. What moved forward since yesterday?
3. What is blocked?
4. What changed in the evidence?
5. Should the order change?
