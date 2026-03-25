# Operating rhythm for Oviond Google Ads

Use this reference when the user wants actual account management, optimization cadence, or strategy operating rules.

## Ground rules

- reporting can run freely once auth is healthy
- mutations should default to `validate-only`
- real account changes should be explicit, reversible, and documented
- do not pause or materially reallocate budget based on a single noisy day unless there is obvious breakage
- conversion tracking integrity comes before optimization bravado

## Daily maintenance

### 1) Spend pacing

Check:
- today's spend by campaign
- campaigns limited by budget
- sudden drops to zero spend
- sudden spikes without conversion support

Actions:
- flag underdelivery
- flag runaway spend
- propose budget shifts toward proven campaigns
- only apply budget changes after validate-only passes and the user approves

### 2) Search-term hygiene

Check:
- expensive irrelevant search terms
- low-intent variants
- competitor or research traffic with no conversion path

Actions:
- prepare negative keyword additions
- group negatives by theme, not random one-offs
- protect exact/high-intent winners while excluding junk variants

### 3) Broken delivery / policy issues

Check:
- disapproved or limited ads
- asset shortages
- status mismatches
- conversion actions that stopped firing

Actions:
- surface the issue immediately
- treat tracking and approval issues as urgent blockers

### 4) Efficiency anomalies

Check:
- CPA spikes
- conversion-rate drops
- click spikes from weak geos/devices
- campaigns with spend but no qualified outcomes

Actions:
- isolate by search term, geo, device, and campaign before touching bids or budgets

## Twice-weekly optimization

### Search structure

Check:
- winning queries with no dedicated keyword/ad coverage
- broad match waste
- ad groups mixing intent badly
- landing page mismatch

Actions:
- propose new exact/phrase keywords for proven queries
- tighten sloppy ad groups
- improve message match between query, ad, and landing page

### Bid / budget allocation

Check:
- impression share lost to budget on winners
- impression share lost to rank where economics justify more aggression
- campaigns carrying weak returns but taking budget from strong ones

Actions:
- move budget toward efficient campaigns
- reduce waste before increasing total spend

## Weekly strategic review

Produce a decision memo covering:
- top spenders
- top converters
- wasted spend pockets
- new negatives to add
- new keyword opportunities
- geo/device insights
- recommended budget moves
- landing-page or offer issues revealed by search behaviour

## Monthly review

Do a deeper review of:
- campaign architecture
- branded vs non-branded mix
- high-intent vs research traffic mix
- conversion lag and attribution assumptions
- whether the account is learning in the right direction or just getting busier

## Mutation workflow

### Safe pattern

1. inspect the account with queries
2. decide the change set
3. prepare the mutation JSON
4. run `ads_mutate.js ... --validate-only`
5. review the response
6. only then run `--apply` if approved

### Good candidates for validate-only first

- pause bad keywords
- add negatives
- update campaign budgets
- pause obviously broken campaigns
- adjust assets or statuses

## Objective framing

Do not optimize for vanity metrics. Default objectives should be tied to:
- qualified conversions
- cost per qualified conversion
- spend concentration into real demand
- cleaner search intent
- fewer reporting surprises
