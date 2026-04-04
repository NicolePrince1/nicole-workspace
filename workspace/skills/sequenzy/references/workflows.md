# Oviond Sequenzy workflows

## 1. Subscriber management

### Use for
- add or update a person in Sequenzy
- inspect a subscriber record
- tag a subscriber into a lifecycle bucket
- remove/unsubscribe a person

### Preferred path
- REST for direct API work
- MCP if richer search/activity context is available

### Recommended pattern
1. Check whether the subscriber already exists.
2. Update attributes for durable facts.
3. Add tags for operational grouping.
4. Trigger an event if the change reflects behavior or a milestone.
5. Verify final state before reporting completion.

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

## 2. Stripe lifecycle integration

### Use for
- onboarding trial users
- payment-failed recovery
- cancellation win-back
- churn reactivation
- upgrade/downgrade lifecycle messaging

### Preferred path
1. Connect native Stripe integration in Sequenzy first.
2. Let Sequenzy own billing-derived tags/events where possible.
3. Add only product-specific custom events from Oviond.

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

## 3. Sequence drafting

### Use for
- onboarding
- trial conversion
- payment recovery
- cancellation recovery
- churn win-back
- product adoption nudges

### Preferred path
- dashboard or MCP, not public REST

### Drafting rules
1. Keep the first version small and testable.
2. Tie the trigger to an event or tag that genuinely exists.
3. Define stop conditions before activation.
4. Review every email for claims, links, and CTA clarity.
5. Never enable automatically after generation.

### Good first Oviond sequences
- New signup onboarding
- Trial conversion
- Payment failed recovery
- Cancellation save / offboarding
- Feature adoption for unactivated accounts

## 4. Campaign drafting

### Use for
- newsletters
- product launches
- webinar invites
- content promotion
- customer education sends

### Preferred path
- dashboard or MCP

### Recommended pattern
1. Define audience first: tag/list/segment.
2. Draft copy and subject lines.
3. Send test email.
4. Check links, preview text, and unsubscribe expectations.
5. Only then schedule or launch.

## 5. Transactional email

### Use for
- welcome email
- password reset-like operational flows if Sequenzy is in the stack
- receipts / one-off customer notices
- single-recipient operational sends

### Preferred path
- public REST is credible here

### Guardrails
- transactional is not a substitute for a broad campaign send
- validate template slug, variables, recipient, and attachments before send
- use test or low-risk recipients first when access is new

## 6. Metrics and diagnostics

### Use for
- account-level engagement summary
- campaign performance review
- sequence performance review
- individual subscriber debugging

### Preferred path
- REST for documented metrics
- MCP for richer subscriber activity if live-tested

### Recommended pattern
1. Pull the right grain: account vs campaign vs sequence vs recipient.
2. Compare sends, delivered, opens, clicks, unsubscribes.
3. Flag unusual drops in delivery or open rate.
4. Tie findings back to audience, copy, timing, and trigger quality.

## 7. Human-review checkpoints

Always require review before:
- enabling a sequence
- launching a campaign
- applying broad audience mutations
- trusting inferred/private endpoints for production use
- changing sender/domain/integration configuration
