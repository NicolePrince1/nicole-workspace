# Session: 2026-04-09 03:48:06 UTC

- **Session Key**: agent:main:telegram:direct:5810523015
- **Session ID**: 7d832a8d-fc28-4fc9-a937-a9de99842ea5
- **Source**: telegram

## Conversation Summary

assistant: I’m going a layer deeper now, read-only. I want the answer to come from the actual shape of the queue, the help centre, and the support stats, not just one or two anecdotal tickets.
assistant: Quick note, I’m pulling a wider ticket/help-centre sample now. Gleap is a bit slow when you walk the whole tree, but this is the pass that should show the real shape of support, not just the obvious headlines.
assistant: [[reply_to_current]] I think the big picture is this:

**Oviond does not mainly have a “support team” problem.**  
It has a **confidence, activation, and operational-friction** problem, and Gleap is where all of that pain lands.

**My blunt diagnosis**
Gleap is currently doing five jobs at once:
- support desk
- onboarding coach
- implementation / white-label ops desk
- bug catcher
- half-formed roadmap inbox

That is why it feels messy. The queue is absorbing problems from across the whole business.

**What the data says**

**Volume and speed**
- Last **30 days**: **419 new tickets**
- Last **7 days**: **108 new tickets**
- Median first response time:
  - **30d:** about **7.8 hours**
  - **7d:** about **11.1 hours**

So the queue is active, and the last week was slower than the 30 day baseline.

**This is not mostly a bug queue**
From the recent **100-ticket sample**:
- `INQUIRY`: **37**
- `CUSTOMERSUCCESS`: **34**
- `BOT`: **19**
- `BUG`: **8**
- `FEATURE_REQUEST`: **1**
- `SALES`: **1**

That is the loudest signal in the whole analysis.

Most of the work is **not engineering defect resolution**.  
It is customer guidance, exception handling, data trust problems, setup friction, and general handholding.

**The recurring pain patterns**
In the recent sample, the strongest themes were:
- **connector / data issues**: Google Ads, Google Business Profile, Meta, Shopify, API keys, integrations, tokens, refresh issues
- **reporting / white-label / delivery friction**: custom domains, automation blocks, dashboard discrepancies, share-link/email issues
- **email / domain setup**: sender auth, company email, domain problems
- **billing / account exceptions**: refund requests, pause requests, paid accounts showing incorrectly
- **bot / email noise**: empty bot tickets, unrelated inbound emails/newsletters/security disclosures landing in the queue

Some of the most repeated title words were:
- `request`
- `data`
- `custom`
- `domain`
- `error`
- `api`
- `ads`
- `integration`
- `automation`
- `expired`

That is not random. It is a map of where the product feels fragile.

**The queue is heavily person-dependent**
Over the last 30 days:
- **Michelle:** **191 assigned**, **262 replies**, **130 tickets worked**
- **Brendan:** **34 assigned**
- **Lesedi:** **23 assigned**
- **Chris:** **4 assigned**
- **Neil:** **0**

In the recent 100-ticket sample:
- **51** sat with Michelle
- **6** with Brendan
- **1** with you
- **42** had no readable named assignee in the API sample

So despite teams existing in Gleap, the actual system behaves much more like a **person-led queue**, especially around Michelle.

That tells me support is working more through human tribal routing than through a clean operational model.

**This is not a giant backlog crisis**
Core readable states right now are roughly:
- **57 OPEN**
- **61 INPROGRESS**
- **16 SNOOZED**
- **15 PLANNED**

So the main issue is **not** “holy shit, thousands of active tickets are piled up.”

The issue is:
- recurring friction keeps creating work
- ownership is person-heavy
- taxonomy is messy
- support is doing too much non-support work

**Your ticket taxonomy is messy**
`ticketscount` exposed a bunch of odd legacy/custom status IDs beyond the normal states, covering about **230 tickets**.

That matters because it means:
- support reporting is dirtier than it should be
- operational visibility is weaker than it should be
- old process scar tissue is still sitting in the system

**The product feedback loop is weak**
This one is important.

- `/tickets/tracker-tickets` is currently **empty**
- recent queue only had **1 FEATURE_REQUEST** ticket in the 100-ticket sample

That does **not** mean customers have no feature pain. It means the feature signal is getting trapped inside normal support/customer-success tickets instead of being turned into structured roadmap input.

So right now Gleap contains product truth, but it is **not being converted into product system**.

**What this says about the business**

**1. It strongly confirms the churn thesis**
We already thought churn was being driven more by:
- unused product
- switched service
- complexity
- trust / confidence issues

Gleap backs that up hard.

The queue is full of:
- “why is this data wrong?”
- “why is this setup failing?”
- “why is this domain/email/automation weird?”
- “why does this not match?”
- “can you fix this account state?”

That is not a pricing story.  
That is a **confidence and operability** story.

**2. Your strongest value prop and biggest pain surface are the same thing**
Oviond wins on:
- simplicity
- white-label reporting
- lower cost
- easy agency delivery

But the support data says the painful edges are exactly around:
- connectors
- trusted data
- white-label setup
- permissions
- automation
- delivery mechanics

So the thing you sell is also the thing that keeps needing human rescue.

That is the clearest product priority signal in Gleap.

**3. Support is functioning as a trust-repair layer for the product**
A lot of these tickets are not “the app exploded.”
They are “the customer hit uncertainty.”

Once that happens, support has to restore confidence.

That is why this matters for growth. If confidence drops after signup, support becomes the patch, and churn follows later.

**4. White-label is a growth lever, but also a manual-ops tax**
“Custom Domain Request” shows up repeatedly.
Email/domain setup questions are common.
Automation exceptions show up.
Branding/delivery mechanics keep surfacing.

That tells me white-label is not just a feature, it is an operational workflow.

If that workflow is clunky, it costs you twice:
- support time
- customer confidence

**5. Gleap is quietly one of your best growth datasets**
You have over **10,500 DONE tickets** in there.

That is a huge voice-of-customer archive covering:
- onboarding friction
- integration pain
- trust breakdowns
- customer language
- high-friction accounts
- repeat implementation asks

Honestly, Gleap is probably more strategically useful than most marketing dashboards right now.

**Help centre read**
This was interesting too.

- **34 collections** visible
- core areas like **Home Page**, **Getting Started**, and **Email Setup** have real content
- but sampled core collections still had **draft articles**
- collection summary counts do not always match live article counts
- many searches are about:
  - migration
  - Shopify / Google Sheets / Instagram connection issues
  - widget language
  - permissions / minimal access / billing access
  - API / MCP
  - custom domains
  - report summaries

So the help centre is **not empty**, but it is not yet absorbing enough support load.

My take:
- some docs exist
- discoverability / specificity / retrieval quality are still weak
- users are searching in plain human language, often with typos
- the content system needs to serve real operator intent better

Also, the search endpoint kept returning 10 results for basically everything, which makes me suspicious that retrieval precision may be mediocre.

**One strategic signal I did not expect**
I saw both:
- a ticket about **MCP server not working**
- help-centre searches around **Oviond API and MCP**

That is small-volume, but strategically juicy.

It suggests a slice of your market wants **programmable / automatable Oviond**, not just static reporting.

That fits your bigger strategic direction really well:
not just dashboards, but a more operational reporting system with automation and AI around it.

**One operational weakness**
Conversation rating data exists, but it is thin.
In the 30 day ratings list I only saw a tiny handful of rated tickets.

So right now you do **not** have a strong CSAT-style feedback loop in Gleap.
You have support activity data, but weak satisfaction instrumentation.

## So what is really going on here?

**Oviond’s support system is compensating for product and process gaps more than it is handling classic support.**

The core pattern is:

1. Agencies come in wanting easy reporting, white-label delivery, and reliable integrations.  
2. They hit edge cases around setup, domains, data sync, permissions, automation, or trust.  
3. Support steps in to manually bridge the gap.  
4. That saves the account in the short term, but it also hides the real product friction unless someone structures the signal.  
5. Because tracker tickets are empty and taxonomy is messy, a lot of that learning is not becoming clean roadmap input.

That is the loop.

**My strongest opinion**
The biggest leak is not “we need more support people.”

It is:
- productizing repeat support work
- improving routing / ownership
- cleaning queue contamination
- turning support pain into structured roadmap and lifecycle action

If you fix those, support gets easier, activation gets better, trust improves, and churn should come down with it.

## What I’d do next

**Immediate operating fixes**
- clean up queue contamination from irrelevant email / bot junk
- normalize statuses and kill legacy nonsense
- create a proper support-to-roadmap flow, because tracker usage is basically nonexistent
- separate true bugs, customer-success help, white-label ops, and billing/lifecycle exceptions into clean buckets

**Product priorities from this read**
- connector reliability and re-auth flows
- custom domain / email / branding setup
- automation and shared-report reliability
- permissions / role clarity
- trust surfaces around “why does this data not match?”

**Help-centre priorities**
- migration
- connector troubleshooting
- custom domains
- permissions / minimal access
- API / MCP
- reporting summaries / exports / email delivery

**Strategic use of Gleap**
- use it as a retention radar
- use it as a roadmap intake source
- use the language in tickets for positioning and messaging
- use recurring ticket clusters to choose what gets productized next

If you want, I’ll turn this into a **proper Gleap strategy pack** next:
- top support themes
- top churn-risk themes
- top product fixes
- top help-centre gaps
- top messaging insights
- a ranked 30/60/90 day action plan

Changes committed ([67d6fe4](https://github.com/NicolePrince1/nicole-workspace/commit/67d6fe4)):
• `workspace/memory/2026-04-08.md` (edit) — logged the Gleap big-picture support analysis and business implications
user: System (untrusted): [2026-04-08 14:37:53 UTC] Exec failed (sharp-tr, signal SIGTERM)

Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.
When reading HEARTBEAT.md, use workspace file /data/.openclaw/workspace/HEARTBEAT.md (exact case). Do not read docs/heartbeat.md.
Current time: Wednesday, April 8th, 2026 - 2:44 PM (UTC) / 2026-04-08 14:44 UTC
assistant: Stripe heartbeat check: trial pressure is up.

- Current trialing subscriptions: 58, up from 48 on the last check.
- 7 active trials expire within the next 3 days.
- Rolling 7-day paid invoice revenue is slightly down, $6,648.34 vs $6,803.45 in the prior 7-day window, but invoice count is up 133 vs 108.
- Past_due subscriptions are 7, still below the >20 alert threshold.

Changes committed ([276c48f](https://github.com/NicolePrince1/nicole-workspace/commit/276c48f)):
• `workspace/memory/heartbeat-state.json` (edit) — updated the Stripe trial-health and revenue-pulse heartbeat state with fresh live values
user: System (untrusted): [2026-04-08 14:46:33 UTC] Exec completed (dawn-riv, code 0) :: windows use paid invoices only and are restricted to the needed date range for speed.", "Restricted keys may block some account-level endpoints; this script does not depend on /ac…
System (untrusted): [2026-04-08 14:47:50 UTC] Exec completed (grand-cl, code 0) :: e paid invoices only and are restricted to the needed date range for speed.", "Restricted keys may block some account-level endpoints; this script does not depend on /account." ],…
System (untrusted): [2026-04-08 14:48:53 UTC] Exec failed (amber-cl, signal SIGTERM)
System (untrusted): [2026-04-08 14:48:53 UTC] Exec completed (amber-ne, code 0) :: orkdir\":\"/data/.openclaw/workspace\",\"yieldMs\":1000,\"timeout\":180}"}],"api":"openai-codex-responses","provider":"openai-codex","model":"gpt-5.4","usage":{"input":991,"output…
System (untrusted): [2026-04-08 14:50:05 UTC] Exec completed (fast-lag, code 0) :: 6-04-08T14:49:47.221637+00:00", "prior_7_start": "2026-03-25T14:49:47.221637+00:00", "prior_7_end": "2026-04-01T14:49:47.221637+00:00" }, "last_7_days_paid_revenue": 6648.34, "las…

Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.
When reading HEARTBEAT.md, use workspace file /data/.openclaw/workspace/HEARTBEAT.md (exact case). Do not read docs/heartbeat.md.
Current time: Wednesday, April 8th, 2026 - 2:51 PM (UTC) / 2026-04-08 14:51 UTC
assistant: Meta ads needs attention: 7-day landing-page-view CPA is **R222.02**, above the **R200** threshold, with **R4,440.48** spent for **20 LPVs**. That is materially worse than the previous 7-day window, which sat at **R94.05** per LPV.

Changes committed ([c6512d6](https://github.com/NicolePrince1/nicole-workspace/commit/c6512d6)):
• `workspace/memory/heartbeat-state.json` (edit) — updated the Meta ad-spend heartbeat check with the fresh 7-day LPV CPA alert
user: Pre-compaction memory flush. Store durable memories only in memory/2026-04-08.md (create memory/ if needed). Treat workspace bootstrap/reference files such as MEMORY.md, DREAMS.md, SOUL.md, TOOLS.md, and AGENTS.md as read-only during this flush; never overwrite, replace, or edit them. If memory/2026-04-08.md already exists, APPEND new content only and do not overwrite existing entries. Do NOT create timestamped variant files (e.g., 2026-04-08-HHMM.md); always use the canonical 2026-04-08.md filename. If nothing to store, reply with NO_REPLY.
Current time: Wednesday, April 8th, 2026 - 3:23 PM (UTC) / 2026-04-08 15:23 UTC
assistant: NO_REPLY
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1847",
  "sender_id": "5810523015",
  "sender": "Chris Irwin",
  "timestamp": "Wed 2026-04-08 15:23 UTC"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Chris Irwin (5810523015)",
  "id": "5810523015",
  "name": "Chris Irwin"
}
```

Yes turn j to Gleap strategy pack
assistant: [[reply_to_current]] **Gleap Strategy Pack**

Here’s the blunt version:

**Gleap says Oviond’s main growth problem is not awareness. It is post-signup confidence.**  
Customers are hitting friction around connectors, data trust, white-label delivery, permissions, automation, and account exceptions. Support is absorbing that pain manually instead of the product handling it cleanly.

## 1. Executive diagnosis

Gleap is currently doing **five jobs at once**:

- support desk
- onboarding coach
- implementation / white-label ops desk
- bug catcher
- messy roadmap inbox

That is the core story.

It means support is not just “support.” It is the place where product friction, retention risk, and customer truth all pile up.

## 2. What the live data is telling us

### Support is not mostly bug-fixing
In the recent 100-ticket sample:

- `INQUIRY`: 37
- `CUSTOMERSUCCESS`: 34
- `BOT`: 19
- `BUG`: 8
- `FEATURE_REQUEST`: 1

So this is **not a classic engineering ticket queue**.  
It is mostly customer-success intervention, implementation help, and confidence repair.

### The queue is person-dependent
30-day team performance showed:

- **Michelle**: 191 assigned, 262 replies, 130 tickets worked
- Brendan: 34 assigned
- Lesedi: 23 assigned
- Chris: 4 assigned
- Neil: 0

That means the system currently runs more through **key humans** than through a strong operating model.

### The bottleneck is earlier than actual resolution
- 30-day median first response time: **7.8 hours**
- 7-day median first response time: **11.1 hours**

But once a ticket seems to have a real owner, things move better.  
So the drag looks more like **triage, routing, prioritisation, and queue shape**, not pure inability to solve issues.

### The active queue is not catastrophic, but it is messy
Readable states included roughly:

- `OPEN`: 57
- `INPROGRESS`: 61
- `SNOOZED`: 16
- `PLANNED`: 15

That tells me this is **not a giant backlog apocalypse**.

The real problem is:
- repeated friction
- poor signal capture
- person dependence
- mixed queue types
- too much manual rescue work

## 3. The real issue clusters

These are the strongest live patterns I see.

### A. Connectors and data trust
Big recurring themes:
- Google Ads
- Google Business Profile
- Meta
- Shopify
- API keys
- integration setup
- data not pulling through
- discrepancies between dashboard/project/shared report

This matters most because **trusted, cross-source reporting is the product**.  
If customers doubt the data, they doubt Oviond.

### B. White-label delivery and operational setup
Repeated signals:
- custom domains
- automation blocks
- email/share-link issues
- branding / delivery mechanics
- report export / PDF / dashboard delivery issues

This is huge.

White-label is one of Oviond’s reasons to win, but Gleap says it is also one of the biggest support taxes.

### C. Permissions, setup, and customer-success handholding
Searches and tickets showed demand around:
- permissions / minimal access
- account setup
- migration
- how-to guidance
- widget language
- API / MCP
- onboarding basics

That means users do not only need bug fixes.  
They need **clear operational pathways**.

### D. Billing and account exceptions
Not the biggest volume, but strategically important:
- refund requests
- pause requests
- paid account showing as expired trial
- account email changes
- subscription exceptions

That is the revenue-risk end of Gleap.

### E. Noise in the queue
You have real queue contamination:
- bot-created low-context tickets
- weird email junk
- newsletters / external noise
- security disclosure style spam

That wastes attention and slows real customers down.

## 4. What this means for the rest of the business

## Retention
This strongly supports the existing churn thesis.

The problem is not mainly price.  
It is:
- complexity
- low confidence
- setup friction
- trust issues
- “this doesn’t feel reliable enough to stay mission-critical”

Gleap is basically the receipts for that.

## Product
Your roadmap should be more driven by:
- connector reliability
- re-auth / token refresh clarity
- white-label setup flow
- delivery consistency
- permissions clarity
- data trust diagnostics

Right now, too much product truth is stuck inside support tickets.

## Marketing
This is gold for messaging.

Customers are effectively telling you what matters:
- reliable data
- easy setup
- client-ready delivery
- fewer weird edge cases
- confidence, not just features

That means marketing should lean less on generic “all-in-one reporting” language and more on:
- trusted reporting
- clean client delivery
- easy agency operations
- fewer manual headaches

## Lifecycle / onboarding
Gleap says you need support-led lifecycle intervention, especially for:
- trial users stuck on setup
- connector failures
- domain/email friction
- first-report delivery issues
- account confusion

If support sees these problems before Stripe sees cancellation, you can rescue earlier.

## Paid acquisition
This matters even more because your paid efficiency is under pressure.

When LPV CPA worsens, every acquired trial matters more.  
So poor activation and support friction get more expensive fast.

In plain English:
**you cannot buy your way around weak activation.**

## 5. The biggest structural gaps

### 1. Support-to-roadmap is broken
Tracker tickets are empty.  
That means feature pain is not being converted into structured product input.

So Gleap is acting like a truth source, but not yet like a decision system.

### 2. Help centre exists, but is not pulling enough load
You have 34 collections and decent breadth, but:
- some core collections still have drafts
- article counts are inconsistent
- searches cluster around exactly the same things support is handling manually

That means the help centre is present, but not yet doing enough deflection or confidence-building.

### 3. Support work is not cleanly separated
Right now the queue mixes:
- bugs
- customer success
- implementation ops
- billing exceptions
- noise
- internal-ish requests

That makes prioritisation muddy and reporting weaker.

### 4. Michelle is a system
That is not sustainable.

If one person is carrying the operational brain of support, then:
- response quality becomes fragile
- throughput becomes fragile
- insight capture becomes fragile
- scale becomes fragile

## 6. Strategic priorities, ranked

### Priority 1: Productize repeated support pain
Focus first on:
- connectors
- data discrepancy diagnosis
- custom domains
- email/delivery
- permissions

That is the highest leverage move.

### Priority 2: Redesign support operations
Create distinct lanes:
- bugs
- customer success / how-to
- implementation / white-label ops
- billing / account risk
- spam / noise

### Priority 3: Turn Gleap into a roadmap intake system
If tracker tickets are not the real live object, fine.  
But you still need a structured weekly flow from:
**ticket cluster → product insight → owner → decision**

### Priority 4: Rebuild help-centre content around real search intent
Top content priorities should be:
- connector troubleshooting
- migration
- custom domains
- permissions / minimal access
- API / MCP
- reporting exports / email delivery

### Priority 5: Use Gleap as a retention radar
Specifically for:
- pause / refund / cancel requests
- repeated setup friction
- high-touch customers with trust issues
- accounts that need support just to stay functional

## 7. My recommended 30 / 60 / 90 day plan

### Next 30 days
- clean status taxonomy
- define queue categories
- cut spam/noise where possible
- create weekly top-issue review
- publish top 10 help-centre articles for real search demand
- identify top recurring manual support actions to productize

### Days 31-60
- formalise support-to-roadmap workflow
- create a “retention risk” ticket segment
- add support themes into lifecycle rescue flows
- rebalance assignment away from one-person dependency
- define ownership between support, CS, and product

### Days 61-90
- instrument a real support dashboard by theme
- measure ticket volume by friction type
- measure deflection from docs
- measure issue clusters tied to churn / pause / refund risk
- use support language in positioning and onboarding copy

## 8. KPIs I would track weekly

- median first response time
- time to first assignment
- active queue by category
- tickets by theme
- top 10 recurring ticket clusters
- share of tickets converted into roadmap items
- help-centre search queries with poor deflection
- refund / pause / cancel related tickets
- concentration of assigned tickets by person
- connector-related tickets as a % of total

## 9. The single biggest takeaway

**Oviond’s support queue is really an activation-and-trust dashboard in disguise.**

If you treat Gleap like “support software,” you underuse it.  
If you treat it like a **customer-truth operating system**, it becomes one of the most strategically important datasets in the company.

My recommendation is simple:

**Do not optimise Gleap as a support inbox.  
Optimise it as the system that tells Oviond where trust breaks, where retention leaks, and what the product must absorb next.**

If you want, next I’ll turn this into one of these three:
1. a **CEO one-pager**,  
2. a **30/60/90 execution plan**, or  
3. a **board-style deck outline** with slides and talking points.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1853",
  "sender_id": "5810523015",
  "sender": "Chris Irwin",
  "timestamp": "Wed 2026-04-08 15:27 UTC"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Chris Irwin (5810523015)",
  "id": "5810523015",
  "name": "Chris Irwin"
}
```

Yes do it
assistant: [[reply_to_current]] **1. CEO one-pager**

**Headline**  
Gleap says Oviond’s main growth constraint is not lead volume. It is post-signup confidence.

**What’s going on**
- Support is handling far more than bugs.
- In the recent 100-ticket sample, the queue was dominated by `INQUIRY` (37) and `CUSTOMERSUCCESS` (34), with only `BUG` (8).
- Last 30 days showed **419 new tickets** and a **7.8 hour median first response time**.
- The queue is heavily person-dependent, especially on Michelle, who carried **191 assigned tickets, 262 replies, and 130 tickets worked** over 30 days.
- The most repeated themes are:
  - connector / data issues
  - white-label / custom domain / delivery friction
  - email / account setup
  - billing exceptions
  - generic noise and bot junk
- Tracker tickets are empty, so support pain is not being converted into structured roadmap input.
- The help center has substance, but it is not absorbing enough load yet.

**What it means**
- Oviond’s support queue is really an **activation, trust, and retention dashboard**.
- Customers are not mainly saying “your price is wrong.”
- They are saying:
  - “I’m not sure this data is right”
  - “this setup is annoying”
  - “this white-label / delivery flow is clunky”
  - “I need a human to get value”
- That lines up with the churn thesis: complexity, confidence, and product-operability are the real drag.

**Core conclusion**
Oviond is winning on the same surfaces where it is leaking:
- connectors
- trusted data
- white-label delivery
- permissions
- automation

Those are both the value prop and the pain surface.

**What to do next**
- Productize repeat support work.
- Separate queue types cleanly.
- Turn support themes into roadmap inputs weekly.
- Upgrade help-center coverage around real search intent.
- Reduce one-person dependency in support ops.

**The bet**
If Oviond reduces support-causing friction in setup, trust, and delivery, you should get:
- better activation
- lower churn
- higher paid acquisition efficiency
- cleaner customer messaging
- less manual support load

---

**2. 30/60/90 execution plan**

**Next 30 days**
**Goal:** make the queue readable and reduce obvious waste.

- Clean up status taxonomy
  - retire or map legacy status codes
  - define one clean operating set: Open, In Progress, Snoozed, Done, Planned
- Split the queue into clear lanes
  - bug
  - customer success / how-to
  - implementation / white-label ops
  - billing / account risk
  - spam / noise
- Run a weekly Gleap review
  - top 10 ticket themes
  - top 5 retention-risk tickets
  - top 5 repeated manual tasks
- Build a “support insight” capture habit
  - each week convert repeated friction into one product issue, doc issue, or lifecycle issue
- Patch top help-center gaps
  - connectors
  - custom domains
  - permissions
  - migrations
  - email delivery
  - API / MCP
- Cut queue contamination
  - filter junk email where possible
  - identify low-value bot-created ticket patterns

**Success markers**
- cleaner weekly reporting
- fewer uncategorized tickets
- obvious noise reduced
- first version of support-theme tracking running

**Days 31-60**
**Goal:** turn support into a decision system.

- Formalize support-to-roadmap flow
  - support cluster
  - evidence
  - impact
  - owner
  - decision
- If tracker tickets stay empty, create a manual roadmap intake process instead of pretending they work
- Create a retention-risk view inside Gleap ops
  - refund
  - pause
  - cancel intent
  - setup frustration
  - repeated trust/data issues
- Rebalance support ownership
  - reduce dependency on Michelle
  - define who owns bug triage vs CS vs ops
- Add lifecycle hooks
  - use recurring support pain to trigger onboarding and rescue messaging
- Build a top-friction backlog
  - connectors
  - white-label ops
  - permissions
  - account-state anomalies
  - delivery failures

**Success markers**
- weekly support themes feeding roadmap
- visible owner for top recurring friction
- retention-risk tickets identifiable fast
- reduced one-person concentration

**Days 61-90**
**Goal:** make Gleap a core operating system.

- Stand up a proper support intelligence dashboard
  - volume by theme
  - response time by category
  - queue by owner
  - help-center deflection gaps
  - churn-risk ticket trends
- Link support themes to product planning
  - what got fixed
  - what got documented
  - what got automated
- Use support language in marketing and onboarding
  - trusted data
  - easier client delivery
  - fewer manual headaches
- Tighten help-center retrieval quality
  - real search intent
  - typos / natural language queries
  - article freshness
- Review whether Gleap should remain one mixed queue or evolve into more explicit operating streams

**Success markers**
- repeated support pain converted into roadmap and docs
- better trust messaging
- lower avoidable manual work
- support data used in product and growth decisions, not just support meetings

---

**3. Board-style deck outline with talking points**

**Slide 1: Title**
**Gleap strategy pack: what support is telling us about growth**
- Support is not just support.
- It is the clearest live view of product friction, retention risk, and customer truth.

**Slide 2: Executive summary**
- Oviond’s main drag is post-signup confidence, not just acquisition.
- Gleap shows repeated friction around connectors, trust, white-label delivery, permissions, and automation.
- Support is absorbing product and process gaps manually.

**Slide 3: What the queue actually is**
- Recent sample dominated by inquiry and customer-success work, not bugs.
- 419 tickets in 30 days.
- Median first response time 7.8h.
- Gleap currently functions as:
  - support desk
  - onboarding desk
  - implementation desk
  - exception-handling desk
  - loose roadmap inbox

**Slide 4: The main pain themes**
- connector / data reliability
- white-label / custom domain / delivery
- permissions / setup / how-to
- billing and account edge cases
- bot and email noise
Talking point: the strongest customer pain maps directly to Oviond’s product promise.

**Slide 5: Org and ops signal**
- queue is person-dependent
- Michelle is carrying disproportionate operational weight
- routing is more human-led than system-led
Talking point: this is workable short term, dangerous long term.

**Slide 6: Retention implication**
- support patterns match existing churn thesis
- risk is driven more by complexity, trust, and “not mission-critical enough” than price
Talking point: support pain is an early warning system for churn.

**Slide 7: Product implication**
- strongest product priorities:
  - connector reliability
  - trust and discrepancy diagnosis
  - white-label setup flow
  - permissions clarity
  - automation stability
Talking point: the product should absorb repeat support work.

**Slide 8: Help-center implication**
- help center is broader than expected, but still underpowered
- searches show real demand for migration, connectors, custom domains, permissions, API / MCP
Talking point: docs should reduce support load and increase customer confidence.

**Slide 9: Structural gap**
- tracker tickets are empty
- support signal is not becoming structured roadmap input
Talking point: customer truth exists, but the conversion into product decisions is weak.

**Slide 10: 90-day response plan**
- 30 days: clean queue, taxonomy, and noise
- 60 days: formalize support-to-roadmap and retention-risk handling
- 90 days: build support intelligence into product, marketing, and lifecycle

**Slide 11: What success looks like**
- lower avoidable support load
- better activation
- better customer confidence
- cleaner roadmap prioritization
- stronger retention
- more efficient paid growth

**Slide 12: Final message**
- Gleap should not be treated as a support inbox.
- It should be treated as a customer-truth operating system.

**What I changed and why**
- I turned the raw Gleap analysis into three usable formats so you can use it for decision-making, execution, or presentation immediately.

If you want, next I’ll turn this into a **clean final doc in Chris-ready wording**, either:
1. a polished internal memo, or  
2. a slide-by-slide board draft with speaker notes.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1860",
  "sender_id": "5810523015",
  "sender": "Chris Irwin",
  "timestamp": "Thu 2026-04-09 00:41 UTC"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Chris Irwin (5810523015)",
  "id": "5810523015",
  "name": "Chris Irwin"
}
```

remember all thisvstuff
assistant: [[reply_to_current]] Yep. I’ve locked in the durable bits.

I stored the core Gleap conclusions as long-term memory, especially:
- Gleap = customer-truth operating system, not just support inbox
- support pain is mostly activation / trust / implementation friction, not just bugs
- biggest recurring pain areas are connectors, data trust, white-label delivery, permissions/setup, automation/email, and billing exceptions
- tracker tickets are empty, so roadmap signal is not yet structured there
- this should keep shaping product, retention, help-center, onboarding, and messaging decisions

Changes committed ([0f34914](https://github.com/NicolePrince1/nicole-workspace/commit/0f34914)):
• `workspace/MEMORY.md` (edit) — added durable Gleap strategic interpretation and operating implication  
• `workspace/memory/2026-04-09.md` (new) — logged Chris’s instruction to remember the Gleap work and the key takeaways
