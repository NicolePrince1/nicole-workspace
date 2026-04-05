# Session: 2026-04-04 04:07:27 UTC

- **Session Key**: agent:main:telegram:direct:5810523015
- **Session ID**: d305f5ce-61a1-419d-a09e-789c957aeb20
- **Source**: telegram

## Conversation Summary

assistant: [[reply_to_current]] Quick note: one temp Stripe audit script got blocked by the shell safety filter because it looked obfuscated. I finished the analysis with cleaner Stripe search passes instead, so we still got the signal we need; the only piece I still treat as directional is the exact churn-rate denominator.

Here’s the real read.

**This is mostly voluntary churn, not card-failure churn**
- In the paid / revenue-bearing cohort, the last year shows **high-30s real cancellations**.
- Almost all are `cancellation_requested`.
- Only a small minority are `payment_failed`.
- So the main problem is **customers choosing to leave**, not Stripe failing to collect.

**The strongest churn reasons are value decay and switching**
Most common feedback themes:
- `unused`
- `switched_service`
- then `too_expensive`
- then `too_complex`

That translates to:
- some customers stop getting enough value
- some move to another tool
- price complaints are often downstream of weak perceived value, not the root cause

**The written comments are pretty damning**
A few examples:
- reports were **“never ready to send to clients”**
- the product felt **too difficult / irritating**
- users mentioned **resetting and re-integrating**
- one customer said the platform got **worse with updates over time**

That points straight at product trust, setup friction, and client-ready output quality.

**Monthly plans are where the real churn pain lives**
In the clean cohort I could classify reliably:
- live base is roughly **95 monthly vs 31 yearly**
- churn over the year is overwhelmingly **monthly**, not annual

So annuals look materially stickier. The retention problem is concentrated in **monthly SMB-style accounts**.

**The worst cohorts are small / legacy plan families**
Biggest recurring churn buckets:
- **Small Agency Monthly**
- legacy **2409_ST_M**
- **4011 / Trial_4011**

That suggests:
- smaller agencies are easier to lose
- older legacy cohorts may carry weaker-fit customers or old positioning baggage

**This is not just an onboarding problem**
The uncomfortable bit:
- most paid churners had been around **1+ years**

So this is not only “new users fail setup and disappear.”
It’s also a **long-term essentialness problem**:
customers can stay for a while, then still decide Oviond is not mission-critical enough to keep.

**Billing leakage exists, but it’s secondary**
- Live Stripe delinquency still shows a meaningful queue of delinquent subscriptions.
- Worth fixing immediately.
- But historically, that is **not** the main engine of churn. Voluntary churn dominates.

**One important audit caveat**
I also tested a raw “all subscriptions in Stripe” denominator.
It produced obvious nonsense spikes, which means Stripe contains a bunch of **legacy / trial / non-revenue subscription objects** that would badly distort headline churn.
So I do **not** trust naive all-subscription churn counts.
I trust the **reason mix, cohort patterns, and monthly-vs-yearly split** much more.

**My ranked hypotheses**
1. **Customers are not reaching durable recurring value**
   - They set up Oviond, but it doesn’t become a locked-in reporting habit.
2. **Product trust is hurting retention**
   - Integrations, report readiness, reset/reconnect pain, update regressions.
3. **Some SMB / legacy cohorts are weak-fit**
   - Easy to acquire on simplicity/price, easy to lose later.
4. **Competitor displacement is real**
   - `switched_service` shows this is not just passive churn.
5. **Price pain is mostly a symptom**
   - If usage/value is weak, any price feels too high.
6. **Our save motion is weak**
   - Once accounts drift, they leave; there’s little sign of strong reactivation.

This lines up with what we already knew about Oviond’s weak points: missing integrations, onboarding/setup friction, and the first impression that the product may not work properly. Source: MEMORY.md#L23-L33

**My blunt conclusion**
This does **not** look like a simple pricing problem.
It looks like:
- **insufficient durable value**
- **product trust / integration friction**
- **monthly SMB customers with weak stickiness**
- plus some avoidable billing leakage on the side

**What I’d do next**
Split today’s churn work into 2 tracks:

**1) Immediate save / damage control**
- audit every current delinquent subscription
- pull the cancel-at-period-end queue
- create reason-based save offers:
  - `unused` → rescue / lighter plan / pause
  - `switched_service` → competitor rescue / migration help / win-back
  - `too_expensive` → annual / downgrade / right-size
  - `too_complex` → setup concierge / done-with-you rescue

**2) Structural retention fixes**
- define activation as:
  - integrations connected
  - first client-ready report built
  - first report actually sent/shared
- reduce integration/reset pain
- improve report trust / readiness
- push healthy monthly customers to annual faster
- clean up or migrate weak legacy plan families
- capture much better churn reasons so “none” stops dominating

If you want, I’ll do the next layer now:
- a **customer-by-customer churn dossier**
- a **ranked retention action plan**
- and a **save-playbook draft** for cancel flow + win-back.
user: [Queued messages while agent was busy]

---
Queued #1
System: [2026-04-04 02:35:57 UTC] Exec completed (swift-wh, code 0) :: e paid invoices only and are restricted to the needed date range for speed.", "Restricted keys may block some account-level endpoints; this script does not depend on /account." ],…
System: [2026-04-04 02:36:05 UTC] Exec failed (sharp-gl, signal SIGTERM)
System: [2026-04-04 02:36:05 UTC] Exec failed (tide-atl, signal SIGTERM)
System: [2026-04-04 02:41:38 UTC] Exec failed (mellow-s, signal SIGTERM)
System: [2026-04-04 02:41:38 UTC] Exec failed (neat-sho, signal SIGTERM)
System: [2026-04-04 02:46:47 UTC] Exec failed (tender-b, signal SIGTERM)
System: [2026-04-04 02:50:47 UTC] Exec failed (glow-gul, signal SIGTERM)
System: [2026-04-04 02:54:46 UTC] Exec failed (young-sh, signal SIGTERM)
System: [2026-04-04 02:56:35 UTC] Exec completed (crisp-pi, code 0) :: "voluntary_count": 4, "involuntary_count": 1, "unknown_count": 0 }, { "month": "2025-04", "start_count": 157, "start_mrr_proxy": 19989.58, "churn_count": 4, "churn_mrr_proxy": 507…
System: [2026-04-04 02:57:58 UTC] Exec completed (delta-ri, code 0) :: ther": 1, "missing_features": 2, "low_quality": 2, "too_complex": 1 } }, { "month": "2026-04", "start_count": 415, "churn_count": 3, "logo_churn_rate": 0.72, "reasons": { "cancell…
System: [2026-04-04 02:58:54 UTC] Exec completed (calm-orb, code 0) :: { "current": { "monthly": { "count": 95, "mrr_proxy": 13973.99 }, "yearly": { "count": 31, "mrr_proxy": 2754.59 } }, "churned_365": { "monthly": { "count": 34, "mrr_proxy": 3229.0…
System: [2026-04-04 02:59:23 UTC] Exec completed (swift-cl, code 0) :: { "monthly": { "switched_service": 10, "too_expensive": 5, "none": 6, "low_quality": 1, "too_complex": 3, "unused": 9 }, "yearly": { "none": 4 } }
System: [2026-04-04 02:59:51 UTC] Exec completed (swift-bl, code 0) :: tched_service": 8, "too_expensive": 5, "none": 6, "low_quality": 1, "too_complex": 3, "unused": 9 } }, "yearly": { "count": 4, "feedback": { "none": 4 } } }, "90d": { "monthly": {…
System: [2026-04-04 03:00:31 UTC] Exec completed (grand-co, code 0) :: { "current_bucket_counts": { "<$20": 9, "$20-$49": 27, "$50-$99": 51, "$200+": 15, "$100-$199": 24 }, "churn_bucket_counts_365": { "<$20": 3, "$100-$199": 8, "$20-$49": 13, "$50-$…
System: [2026-04-04 03:01:37 UTC] Exec completed (warm-wil, code 0) :: t_mrr_proxy": 299.0, "churn_mrr_proxy": 0.0 }, { "tag": "250 Keywords Monthly", "current": 1, "churn_365": 0, "rough_churn_share_pct": 0.0, "current_mrr_proxy": 158.0, "churn_mrr_…

Conversation info (untrusted metadata):
```json
{
  "message_id": "1420",
  "sender_id": "5810523015",
  "sender": "Chris Irwin",
  "timestamp": "Sat 2026-04-04 03:00 UTC"
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

Any news
assistant: [[reply_to_current]] Yes — and the signal is getting pretty clear.

**What Stripe is saying so far**
- This is **mostly voluntary churn**, not failed-card churn.
- In the paid/revenue-bearing cohort over the last 12 months, I can see roughly **38 real cancellations**:
  - **34** were `cancellation_requested`
  - **4** were `payment_failed`
- So the main issue is **customers choosing to leave**, not billing failure.

**Main churn reasons**
- Strongest feedback themes are:
  - **unused**
  - **switched_service**
  - then **too_expensive**
  - then **too_complex**
- Last 90 days specifically: **4 unused**, **3 switched_service**, **2 no feedback**

**Big structural clue**
- Churn is concentrated in **monthly plans**, not annuals:
  - about **34 monthly churns**
  - vs **4 yearly churns**
- That’s a big sign that our monthly customers are not becoming sticky enough.

**Worst cohorts**
- Biggest churn concentration is in:
  - **Small Agency Monthly**
  - legacy **2409_ST_M**
  - **4011 / Trial_4011** families
- So it looks like smaller / older / legacy cohorts are especially fragile.

**Most important insight**
- This is **not just onboarding churn**.
- A lot of churners had been with Oviond **1+ years**.
- So the deeper problem is: **people can stay for a while, but Oviond still isn’t becoming essential enough to keep forever.**

**The ugliest product signal**
The few written comments are blunt:
- reports were **not ready to send to clients**
- setup felt **too difficult / irritating**
- users mentioned **resetting and re-integrating**
- one said the platform got **worse with updates over time**

That points to:
1. **product trust**
2. **integration/setup friction**
3. **client-ready report quality**
4. **long-term value decay**

**My current working hypothesis**
Our churn problem is mainly:
- weak durable value / habit formation
- some competitor switching
- monthly SMB customers with weak stickiness
- price complaints that are often a **symptom** of low perceived value, not the root cause

There’s also a **saveable delinquency queue** in Stripe, but that looks like a secondary leak compared with the voluntary churn issue.

I’m now building the next layer: **customer-by-customer churn dossier + ranked retention actions** so we can decide exactly what to fix first.
assistant: Yes — and the signal is getting pretty clear.

**What Stripe is saying so far**
- This is **mostly voluntary churn**, not failed-card churn.
- In the paid/revenue-bearing cohort over the last 12 months, I can see roughly **38 real cancellations**:
  - **34** were `cancellation_requested`
  - **4** were `payment_failed`
- So the main issue is **customers choosing to leave**, not billing failure.

**Main churn reasons**
- Strongest feedback themes are:
  - **unused**
  - **switched_service**
  - then **too_expensive**
  - then **too_complex**
- Last 90 days specifically: **4 unused**, **3 switched_service**, **2 no feedback**

**Big structural clue**
- Churn is concentrated in **monthly plans**, not annuals:
  - about **34 monthly churns**
  - vs **4 yearly churns**
- That’s a big sign that our monthly customers are not becoming sticky enough.

**Worst cohorts**
- Biggest churn concentration is in:
  - **Small Agency Monthly**
  - legacy **2409_ST_M**
  - **4011 / Trial_4011** families
- So it looks like smaller / older / legacy cohorts are especially fragile.

**Most important insight**
- This is **not just onboarding churn**.
- A lot of churners had been with Oviond **1+ years**.
- So the deeper problem is: **people can stay for a while, but Oviond still isn’t becoming essential enough to keep forever.**

**The ugliest product signal**
The few written comments are blunt:
- reports were **not ready to send to clients**
- setup felt **too difficult / irritating**
- users mentioned **resetting and re-integrating**
- one said the platform got **worse with updates over time**

That points to:
1. **product trust**
2. **integration/setup friction**
3. **client-ready report quality**
4. **long-term value decay**

**My current working hypothesis**
Our churn problem is mainly:
- weak durable value / habit formation
- some competitor switching
- monthly SMB customers with weak stickiness
- price complaints that are often a **symptom** of low perceived value, not the root cause

There’s also a **saveable delinquency queue** in Stripe, but that looks like a secondary leak compared with the voluntary churn issue.

I’m now building the next layer: **customer-by-customer churn dossier + ranked retention actions** so we can decide exactly what to fix first.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1425",
  "sender_id": "5810523015",
  "sender": "Chris Irwin",
  "timestamp": "Sat 2026-04-04 03:22 UTC"
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

Okay keep going
assistant: I’m splitting the churners into actual cohorts now — tenure, price band, legacy plan family, and current saveable risk — so we can move from “interesting” to “what do we fix first?”
assistant: I’ve got a clean customer-level pull now. One more pass: I want to see which active monthly cohorts are the best annual-conversion targets, because that’s probably the fastest retention lever outside product fixes.
assistant: [[reply_to_current]] I kept going. The next layer is more useful now.

I’m managing against the **clean paid cohort**, not every Stripe subscription object, because the raw Stripe set has legacy/trial oddities that distort churn.

**What’s newly clear**
- The highest-value churners are **not** mostly instant bad-fit trials.
- We have multiple **$199/mo accounts** that stayed for **7–16 months** and then churned with reasons like:
  - `switched_service`
  - `unused`
  - `too_complex`
- We also have **$99–$139/mo Small Agency Monthly** customers churning after **1–5 years**.
- That means the problem is not just acquisition quality or first-week onboarding. It’s **long-term stickiness and product trust**.

**Customer-level pattern**
A few strong examples from the churn list:
- Several **Trial_4011 / $199** accounts churned after roughly **224, 297, 306, and 481 days**
- **Regular Agency Monthly / $199** churned after roughly **640–898 days**
- **Small Agency Monthly** churners often lasted **400–2,000+ days**
- One explicit comment: the platform got **worse over time**
- Another explicit comment: reports were **never ready to send to clients**, and integrations kept needing resets

That’s ugly, but useful. It says:
1. customers can get far enough in to pay for quite a while
2. then still decide Oviond is not dependable / essential enough to keep

**Current save / retention levers**
From the clean revenue-bearing base:
- **126** active paid subscriptions
- **95 monthly**
- **31 yearly**

**Immediate save queue**
- **13 delinquent paid accounts**
- about **$874.60 MRR proxy** at risk
- many are very old accounts, so this is probably recoverable leakage rather than true product churn

**Pending cancels**
- only **2** clean paid accounts currently set to cancel at period end
- about **$39 MRR proxy**
- so the live cancel-now queue is not the main fire

**Best structural lever: annual conversion**
This is the big one:
- **82** active monthly customers have already been around **180+ days**
- worth about **$13.1k MRR proxy**
- these are your best annual-conversion targets

Top annual-conversion candidate cohorts:
- **Large Agency Monthly** — 8 accounts / **$3.19k MRR proxy**
- **Regular Agency Monthly** — 14 accounts / **$2.79k**
- **Small Agency Monthly** — 26 accounts / **$2.61k**
- plus a long tail of legacy monthly plans

That matters because your churn pain is overwhelmingly on **monthly** plans.

**My current diagnosis, sharpened**
The churn problem is really four problems:

1. **Oviond is not becoming operationally indispensable enough**
   - shows up as `unused`

2. **Some customers are actively finding a better home elsewhere**
   - shows up as `switched_service`

3. **Product friction / trust issues are poisoning retention**
   - “not ready to send to clients”
   - “resetting and re-integrating”
   - “got worse over time”

4. **Monthly plan exposure is too high**
   - even healthy customers remain easy to lose because they stay on monthly

**What I think we should do first**
In order:

**1. Billing rescue sprint**
- Work the **13 delinquent paid accounts** first
- This is fastest recoverable MRR

**2. Win-back sprint on the highest-value churners**
Start with:
- `$199/mo` churners
- `switched_service`
- `too_complex`
- recent `unused`
These are the clearest signal accounts for why we lose valuable customers.

**3. Annual conversion campaign**
This is probably the fastest structural retention lever you have.
If we move even a chunk of the **82 mature monthly accounts** onto annual, churn pressure drops materially.

**4. Product retention fixes**
The data keeps pointing back to the same things:
- report readiness
- integration stability
- setup / reset pain
- regression control after product changes

**5. Better churn instrumentation**
Too many exits still say `none`.
We need a better exit survey and better pre-churn usage signals.

**My hard read now**
Your churn problem is **not mainly payments**.
It is **not mainly “too expensive.”**
It is mostly:
- **weak durable value**
- **switching**
- **complexity / trust**
- and too much exposure sitting on **monthly plans**

Next I’d turn this into a proper **retention war plan**:
- exact rescue list
- exact annual-conversion target list
- exact win-back segments
- and the product fixes ranked by likely churn impact.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1432",
  "sender_id": "5810523015",
  "sender": "Chris Irwin",
  "timestamp": "Sat 2026-04-04 03:34 UTC"
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

Yes do full next steps
assistant: I want the top annual-conversion targets and the most actionable recent win-back list, so the next step is concrete rather than “strategy deck” territory.
assistant: [[reply_to_current]] Good. Here’s the full next-step plan — not just diagnosis, but what I’d actually do.

**Core read**
Your churn problem is mainly:
- **voluntary**
- **monthly-plan concentrated**
- driven by **unused / switched_service / complexity / trust**
- with **price** usually acting as a symptom of weak perceived value, not the primary cause

That also lines up with the durable issues we already knew about Oviond: setup friction, missing integrations, and the feeling that the product doesn’t quite work reliably enough. Source: MEMORY.md#L23-L33

**Important caveat**
- I’m using the **clean paid / revenue-bearing cohort**
- counts, cohorts, and reasons are the strongest signal
- dollar churn values are still best treated as **MRR proxies**, not finance-grade numbers

---

## 1) Immediate action plan: four workstreams

### Workstream A — Recover revenue now
This is the fastest money.

**Live save queue**
- **13 delinquent paid accounts**
- about **$874.60 MRR proxy** at risk
- only **2 cancel-at-period-end** accounts in the clean cohort, worth about **$39 MRR proxy**

So:
- **delinquency rescue matters**
- **cancel-at-period-end monitoring is not the main lever right now**

**What to do**
1. **Clean the delinquent list first**
   - There are clear internal / stale / odd accounts in it
   - examples: `templates@oviond.com`, `giuliagallioviond@gmail.com`
   - so don’t mistake all 13 as equal revenue risk

2. **Prioritize real customer recovery by value**
Top real-looking at-risk accounts from the queue:
- `chris@inbound.co.za` — **$158/mo** — Small Agency Monthly + 250 Keywords
- `maxine@famousmedia.co.za` — **$99/mo** — Small Agency Monthly
- `hello@vbrand.asia` — **$99/mo** — Small Agency Monthly
- `alejandro@estudioa.cl` — **$49/mo** — custom monthly
- `baderagourram@hotmail.com` — **$49/mo** — One Code

**Rescue motion**
- Day 0: plain-text “payment issue” email + update card CTA
- Day 2: manual follow-up for accounts >$99/mo
- Day 5: “need help / pause / downgrade?” option
- Remove internal/test/stale noise from the list before reporting recovered MRR

**Success metric**
- recovered MRR from delinquency within 7 days
- cleaned delinquency dashboard with internal/test accounts excluded

---

### Workstream B — Win back recent churners
This is the second-fastest lever.

**What the data says**
Recent churn is mostly:
- `unused`
- `switched_service`
- some `too_complex`
- high-value churn is **not mostly price-led**

That last bit matters:
- among **$199+ churners**, the feedback skews **unused / too_complex / switched_service / none**
- almost nobody at the top end is saying “too expensive” first

So discounting alone will not fix this.

**Tier 1 recent win-back targets**
Start with these:

**High-value / high-signal**
- `mark@surmarketing.io` — **$199/mo** — Regular Agency Monthly — canceled Jan 2026 — no reason
- `pete@ddswebsolutions.com` — **$199/mo** — Regular Agency Monthly — `unused`
- `ian@masscapital.ca` — **$199/mo** — Trial_4011 — `unused`
- `richard@glazedigital.com` — **$139/mo** — Small Agency Monthly — `switched_service`
  - comment: *platform got worse with updates over time*
- `hello@promotoon.com.au` — **$99/mo** — Small Agency Monthly — `switched_service`
- `dean@hawkerdigital.com` — **$99/mo** — Small Agency Monthly — `too_complex`
- `massimo@sosidee.com` — **$99/mo** — Small Agency Monthly — `too_expensive`

**Reason-based win-back playbooks**
- **unused**
  - offer: “we’ll rebuild your reporting setup and get one client-ready report out in 7 days”
  - fallback: pause / downgrade / lighter plan
- **switched_service**
  - ask what they switched to
  - offer migration help or side-by-side rebuild
  - position around simplicity + white-label + lower admin load
- **too_complex**
  - offer a done-with-you reset
  - 30-minute setup rescue + integration fix + first report proof
- **too_expensive**
  - only after value rescue
  - annual discount / right-size plan / client-count downgrade

**Priority order**
1. $199+ churners in last 180 days
2. switched_service churners with clear history
3. too_complex churners with long tenure
4. unused churners with >12 months tenure

---

### Workstream C — Reduce future churn with annual conversion
This is probably the biggest structural retention lever.

**Current base**
- **126** active paid subscriptions
- **95 monthly**
- **31 yearly**

**Best annual-conversion pool**
- **82** active monthly accounts with **180+ days tenure**
- worth about **$13.1k MRR proxy**

That is a very healthy pool.

**Top annual-conversion cohorts**
- **Large Agency Monthly** — 8 accounts — **$3.19k MRR proxy**
- **Regular Agency Monthly** — 14 accounts — **$2.79k**
- **Small Agency Monthly** — 26 accounts — **$2.61k**

**Top account targets**
- `data@reporting.biz` — **$1,562.50/mo**
- `philip@titandigital.ie` — **$449/mo**
- multiple **Large Agency Monthly** accounts at **$399/mo**
- multiple **Regular Agency Monthly** accounts at **$199/mo**

**What to do**
Launch a focused annual conversion offer to mature monthlies:
- target accounts with **6+ months tenure**
- especially those with bigger plans and older tenure
- do **not** blast everyone the same way

**Suggested offer**
- annual plan at **15–20% effective savings**
- plus a “report optimization / setup review” bonus
- message the benefit as:
  - lower admin burden
  - less reporting hassle
  - locked-in savings
  - priority support / review session

**Why this matters**
If you convert even **25%** of that mature monthly pool, you materially reduce future churn exposure.

---

### Workstream D — Fix the actual retention engine
This is the hard but necessary part.

Stripe says the real issue is not just acquisition quality. Customers often stay **months or years**, then still leave.

That means Oviond is failing on **durable essentialness**.

## 2) Product hypotheses ranked by likely impact

### Hypothesis 1 — “Client-ready report” is the missing activation milestone
Customers aren’t truly activated when they connect accounts.
They’re activated when they:
- connect integrations
- build the report
- trust the report
- actually send it to a client

**Fix**
Define activation as:
- first client-ready report created
- first report shared/sent
- first repeat report cycle completed

### Hypothesis 2 — Integration/reset pain is destroying trust
The written comments point straight at this:
- resetting
- re-integrating
- reports not ready
- friction over time

**Fix**
Instrument and reduce:
- reconnect events
- broken integrations
- stale data sources
- report errors before export/share

### Hypothesis 3 — Product quality regressions are causing long-tenure churn
“The platform got worse with updates over time” is the most dangerous comment in the set.

**Fix**
Add a retention-focused QA layer:
- regression checklist for key reporting workflows
- monitor high-value customer accounts after major changes
- create a “reporting confidence” score internally

### Hypothesis 4 — Small monthly agencies are too easy to lose
They’re cheap to keep paying monthly until they aren’t.
Then they either drift into `unused` or switch.

**Fix**
- move healthy monthlies to annual faster
- give small agencies a clearer “you’re winning with Oviond” loop
- monthly health checks for accounts at 60/90/180 days

---

## 3) Cancellation flow and save playbook

Right now Stripe feedback is useful, but too shallow.

**Improve the cancel flow**
When a customer goes to cancel, make them choose:
- Not using enough
- Switched to another tool
- Too expensive
- Too hard / too much work
- Missing features / integrations
- Support / service issue
- Other

Then branch the rescue offer:

**If “unused”**
- offer: pause for 60 days
- offer: lighter plan
- offer: done-with-you report rebuild

**If “switched_service”**
- ask which tool
- offer migration / comparison call
- show one or two real differentiators

**If “too_expensive”**
- downgrade suggestion first
- annual savings second
- don’t jump straight to discounting everyone

**If “too hard / too complex”**
- offer 30-minute setup rescue
- fix integrations live
- help produce first client-ready report

**Key rule**
Do not let cancellation just become a blind Stripe form.
It needs to be a structured save workflow.

---

## 4) What not to do

### Don’t just cut prices
The data doesn’t support price as the primary root cause.

### Don’t obsess only over failed payments
Involuntary churn exists, but it’s not the main engine.

### Don’t focus only on new-user onboarding
This is also a **long-term product-value** problem.

### Don’t treat all monthly customers equally
Prioritize:
- high-ARPU monthlies
- long-tenure monthlies
- cohorts already showing stability but still exposed to monthly churn

---

## 5) 14-day execution plan

### Next 48 hours
- Clean delinquent queue into:
  - real customer recovery
  - internal/test/stale
- Finalize 3 outreach tracks:
  - delinquent rescue
  - win-back
  - annual conversion
- Tag the top 20 churners by reason and value

### Days 3–5
- Start manual outreach to:
  - top delinquent accounts
  - top 10 win-back targets
- Launch annual offer to mature monthly cohort starting with:
  - Large Agency Monthly
  - Regular Agency Monthly
  - top-value Small Agency Monthly

### Days 6–10
- Review replies and objections
- Cluster real customer language:
  - switched where?
  - what felt too hard?
  - what was not client-ready?
- Feed those objections into product + messaging

### Days 10–14
- Ship improved cancellation reason capture
- Define activation and retention health metrics
- Create a monthly retention dashboard:
  - mature monthlies
  - delinquent queue
  - cancel reasons
  - annual conversions
  - win-backs

---

## 6) Success metrics I’d use

**Revenue rescue**
- delinquent recovered MRR
- delinquent queue cleaned of non-real accounts

**Retention**
- monthly-to-annual conversion count
- win-back reactivation count
- monthly churn rate in Small / Regular / Large Agency Monthly

**Product**
- % of new payers who reach first client-ready report
- % who send/share first report
- integration reconnect rate
- support tickets related to broken/reset integrations

---

## 7) My blunt conclusion
If I strip this down:

**Oviond’s churn problem is not mainly billing and not mainly price.**
It is mainly:
- monthly customers not becoming sticky enough
- customers drifting into low usage
- customers switching when friction outweighs value
- product trust being damaged by complexity, report-readiness issues, and integration pain

So the winning sequence is:
1. **rescue live revenue**
2. **win back recent high-value churn**
3. **convert stable monthlys to annual**
4. **fix trust / activation / integration issues**

If you want, I can do the next practical layer now:
- draft the **actual email / in-app copy** for all 3 outreach tracks
- turn the churners into a **contact list grouped by reason**
- and build a **retention dashboard spec** Chris can use every week.

**Update:** I moved us from generic churn analysis to an actual operating plan with 3 revenue motions and 1 product-retention motion, because the Stripe data is now clear enough to act on.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1440",
  "sender_id": "5810523015",
  "sender": "Chris Irwin",
  "timestamp": "Sat 2026-04-04 03:49 UTC"
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

Remember all this properly progress we will work on this this week as part of our overall strategy to reach our goals
assistant: [[reply_to_current]] Locked in. I wrote today’s churn work into memory properly so we can keep building on it this week as part of the broader growth strategy, not start from scratch again.

I captured:
- churn/retention as a top strategic focus right now
- the working thesis that this is mainly **voluntary monthly-plan churn**
- the main drivers: **unused, switching, complexity/trust, integration/report-readiness pain**
- the four workstreams for the week: **delinquency rescue, win-backs, annual conversion, and product retention fixes**

I also committed the memory update locally, but the push to GitHub failed here because this runtime doesn’t currently have GitHub auth available.

Changes committed (d757faa, local only — push blocked by GitHub auth):
• workspace/MEMORY.md (edit) — recorded churn/retention as a strategic priority with the current working thesis and priorities
• workspace/memory/2026-04-04.md (new) — saved today’s churn audit findings and this week’s retention workstreams
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1442",
  "sender_id": "5810523015",
  "sender": "Chris Irwin",
  "timestamp": "Sat 2026-04-04 04:01 UTC"
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

How does this fit into our overall goal for this year ?
assistant: [[reply_to_current]] It fits **right at the center** of the goal, not off to the side.

The headline goal is to move Oviond from roughly **$28.5k MRR to $100k MRR by Dec 2026**. Source: MEMORY.md#L23-L32  
So the real equation this year is:

**Net growth = new MRR + expansion MRR - churned MRR**

That means churn work is not a “retention side project.” It’s one of the main things that decides whether the rest of the strategy actually compounds.

## How churn fits the 2026 goal

### 1. It protects the base we already have
If we keep leaking good customers, especially monthly agency customers, then every new customer we add is partly just replacing lost revenue.

Blunt version:
- if churn stays high, growth feels busy but not cumulative
- if churn comes down, the same acquisition effort produces much more net MRR

So retention is the **foundation layer** under the whole plan.

### 2. It makes paid acquisition actually work
One of our core priorities is improving paid efficiency. But paid only works if customers stick.

If customers churn because they:
- don’t get enough value
- find Oviond too hard
- lose trust in reporting quality
- switch later anyway

…then we can’t just spend our way to the goal. We’d be pouring traffic into a leaky bucket.

So churn work directly supports:
- better **LTV**
- healthier **CAC payback**
- less wasted ad spend
- more confidence scaling USA acquisition

### 3. It sharpens trial-to-paid conversion too
The churn comments are pointing at the same underlying weaknesses that probably hurt trial conversion:
- reports not feeling client-ready
- integration/reset pain
- product feeling difficult or unreliable

So the retention work is also conversion work.

If we fix:
- activation
- report confidence
- integration stability
- setup friction

…we should improve both:
- **trial-to-paid**
- **paid-to-retained**

That’s high leverage.

### 4. It supports the ARPU goal
Another core priority is increasing ARPU.

This churn work already showed a clean lever:
- monthly customers are much more fragile than annual customers
- we have a strong pool of mature monthlies who should be pushed to annual

So retention doesn’t just stop loss — it also helps:
- lock revenue in longer
- increase effective customer value
- make MRR more durable

That’s ARPU and retention working together.

### 5. It improves the quality of our acquisition strategy
The churn patterns tell us who we should acquire more of, and who we should stop overvaluing.

If the fragile cohorts are:
- small/legacy monthly plans
- customers who don’t become operationally dependent
- customers who buy on price but not durable value

…then we need acquisition to bias toward:
- better-fit agencies
- higher-intent buyers
- customers likely to use Oviond regularly
- customers who care about simplicity and white-label reporting enough to stick

So churn analysis feeds back into ICP quality, messaging, onboarding, and paid targeting.

## How I’d frame it strategically

This year’s plan is not:

- get more trials
- get more traffic
- spend more on ads
- separately “also reduce churn”

It’s more like:

1. **Acquire better-fit agencies**
2. **Get them to value faster**
3. **Make the product trustworthy enough to keep**
4. **Convert healthy monthlies to annual**
5. **Scale acquisition harder once the bucket leaks less**

That’s the real growth system.

## My strategic read
If we do not improve retention, the path to $100k gets much harder and more expensive.

If we do improve retention:
- every paid channel performs better
- SEO traffic monetizes better
- trial conversion work compounds better
- ARPU work gets stickier
- net MRR growth becomes much more believable

So for this year, churn work fits as a **force multiplier across the whole growth plan**.

## The practical implication for this week
This week’s churn work is giving us the order of operations:

1. **rescue live revenue**  
   delinquency + saveable accounts

2. **win back recent valuable churners**  
   especially switched / unused / complexity-led accounts

3. **convert mature monthly customers to annual**  
   fastest structural retention lever

4. **fix the product issues behind churn**  
   activation, client-ready report trust, integration/reset pain

That is how churn work plugs directly into the overall goal.

If you want, next I can turn this into a **2026 growth map** showing how retention, conversion, paid, SEO, reactivation, and ARPU all fit together in one plan.
