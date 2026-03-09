# Stripe metrics notes

Use the bundled snapshot for fast orientation.

## Definitions

- Estimated MRR: sum monthly-normalized recurring subscription item amounts from the sampled subscriptions returned by Stripe.
- This is directional, not finance-grade revenue recognition.
- Past-due and unpaid subscriptions may still be included when estimating at-risk MRR.

## Good follow-up questions

- How many subscriptions are active vs trialing vs past_due?
- Which plans drive most MRR?
- Which customers expanded or churned in the last 30/90 days?
- Are failed invoices creating avoidable churn?
