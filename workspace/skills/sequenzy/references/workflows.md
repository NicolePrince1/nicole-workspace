# Oviond Sequenzy workflows

## 1. Read-only audit

### Use for
- proving live access works
- checking workspace shape before any mutation
- confirming what route families are actually available
- debugging whether a task belongs to documented REST, live private routes, or dashboard

### Preferred path
- run `scripts/live_audit.py` with `SEQUENZY_API_KEY` set
- fall back to focused manual GET checks only when you need a narrower answer

### Recommended pattern
1. confirm the key exists
2. run the audit script
3. classify each needed route as documented, live-private, repo-inferred, or dashboard-first
4. only then decide whether the requested task is safe to automate

### Important note
- send an explicit `User-Agent` on direct API calls from this workspace

## 2. Subscriber management

### Use for
- add or update a person in Sequenzy
- inspect a subscriber record
- tag a subscriber into a lifecycle bucket
- remove or unsubscribe a person

### Preferred path
- documented REST for direct API work
- subscriber detail route before trying any separate activity route

### Recommended pattern
1. check whether the subscriber already exists
2. update attributes for durable facts
3. add tags for operational grouping
4. trigger an event if the change reflects behavior or a milestone
5. verify final state before reporting completion

### Oviond field ideas

Use attributes for facts like:
- plan
- billing_interval
- workspace_count
- report_count
- connected_integrations_count
- signup_source
- trial_end_at
- customer_since
- mrr

Use tags for buckets like:
- lead
- trial
- customer
- cancelled
- churned
- past-due
- high-intent
- partner

## 3. Stripe lifecycle integration

### Use for
- onboarding trial users
- payment-failed recovery
- cancellation win-back
- churn reactivation
- upgrade or downgrade lifecycle messaging

### Preferred path
1. connect native Stripe integration in Sequenzy first
2. let Sequenzy own billing-derived tags and events where possible
3. add only product-specific custom events from Oviond

### What to avoid
- do not duplicate Stripe lifecycle logic manually if native integration already provides it
- do not mix conflicting tag semantics between Stripe sync and custom scripts

### Oviond custom events worth tracking
- `signup.completed`
- `workspace.created`
- `data-source.connected`
- `first-dashboard-published`
- `scheduled-report-enabled`
- `team-member-invited`
- `onboarding.completed`

## 4. Sequence drafting

### Use for
- onboarding
- trial conversion
- payment recovery
- cancellation recovery
- churn win-back
- product adoption nudges

### Preferred path
- dashboard or live-private surface, not public REST

### Drafting rules
1. keep the first version small and testable
2. tie the trigger to an event or tag that genuinely exists
3. define stop conditions before activation
4. review every email for claims, links, and CTA clarity
5. never enable automatically after generation

### Good first Oviond sequences
- new signup onboarding
- trial conversion
- payment failed recovery
- cancellation save or offboarding
- feature adoption for unactivated accounts

## 5. Campaign drafting

### Use for
- newsletters
- product launches
- webinar invites
- content promotion
- customer education sends

### Preferred path
- dashboard or live-private surface

### Recommended pattern
1. define audience first, tag, list, or segment
2. draft copy and subject lines
3. send a test email if the route is proven or use dashboard preview
4. check links, preview text, and unsubscribe expectations
5. only then schedule or launch

## 6. Transactional email

### Use for
- welcome email
- password-reset-like operational flows if Sequenzy is in the stack
- receipts or one-off customer notices
- single-recipient operational sends

### Preferred path
- documented REST

### Guardrails
- transactional is not a substitute for a broad campaign send
- validate template slug, variables, recipient, and attachments before send
- use internal or low-risk recipients first when access is new

## 7. Metrics and diagnostics

### Use for
- account-level engagement summary
- campaign performance review
- sequence performance review
- individual subscriber debugging

### Preferred path
- documented REST metrics first
- private stats aliases when they are more convenient and already validated
- subscriber detail route for individual activity debugging

### Recommended pattern
1. pull the right grain, account vs campaign vs sequence vs recipient
2. compare sends, delivered, opens, clicks, and unsubscribes
3. flag unusual drops in delivery or open rate
4. tie findings back to audience, copy, timing, and trigger quality

## 8. Human-review checkpoints

Always require review before:
- enabling a sequence
- launching a campaign
- applying broad audience mutations
- trusting repo-inferred private endpoints for production use
- changing sender, domain, or integration configuration
