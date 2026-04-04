---
name: loops
description: "Manage Oviond's Loops account for SaaS lifecycle marketing: contact properties, mailing lists, contact sync, event design, transactional email setup, and migration planning from MailerLite."
metadata:
  {
    "openclaw":
      {
        "emoji": "🔁"
      }
  }
---

# Loops Skill — Oviond

Operate Oviond's Loops account as the SaaS lifecycle email system.

## Auth

- API key in env var: `LOOPS`
- Auth test endpoint: `GET https://app.loops.so/api/v1/api-key`
- Team name currently resolves successfully via API auth

## What the Loops API supports well

- Create / update / find / delete contacts
- Create and list contact properties
- List mailing lists
- Add/remove contacts to mailing lists via contact create/update
- Send events
- Send transactional emails
- List transactional emails

## What the Loops API does *not* appear to support fully

- Programmatic creation of marketing loops / visual workflow automations
- Full visual email builder automation creation like MailerLite

This means Loops should be treated as:
1. **Data model + sync engine** via API
2. **Lifecycle orchestration UI** on top of a clean event/property foundation

## Core Oviond contact properties to create

### Identity
- `firstName` (built-in)
- `lastName` (built-in)
- `companyName` (string)
- `userId` (built-in or external id)
- `source` (built-in/custom source)

### Lifecycle / billing
- `subscriptionStatus` (string)
- `trialing` (boolean)
- `trialEndsAt` (date)
- `currentPeriodEnd` (date)
- `planName` (string)
- `billingInterval` (string)
- `mrr` (number)
- `isLifetimeUser` (boolean)
- `pastDue` (boolean)
- `paused` (boolean)

### Product / usage
- `projectsCount` (number)
- `dashboardsCount` (number)
- `clientsCount` (number)
- `connectedSourcesCount` (number)
- `firstReportCreatedAt` (date)
- `lastActiveAt` (date)
- `hasCreatedReport` (boolean)
- `hasSharedReport` (boolean)
- `hasConnectedDataSource` (boolean)
- `hasInvitedTeamMember` (boolean)

### Marketing / classification
- `customerType` (string)
- `agencySize` (string)
- `country` (string)
- `leadSource` (string)
- `needsUpgrade` (boolean)
- `atRisk` (boolean)

## Suggested Loops mailing lists

Keep mailing lists small and intentional. Use properties for logic; lists for subscription buckets and manual sends.

- `trial-users`
- `paying-customers`
- `lapsed-customers`
- `lifetime-users`
- `newsletter`
- `product-updates`
- `reactivation`

## Core event vocabulary

These are the events Oviond should send into Loops:

### Acquisition
- `trial_started`
- `demo_requested`
- `lead_captured`

### Activation
- `data_source_connected`
- `first_report_created`
- `report_shared`
- `branding_completed`
- `team_member_invited`

### Revenue
- `subscription_started`
- `subscription_upgraded`
- `subscription_downgraded`
- `subscription_paused`
- `subscription_resumed`
- `payment_failed`
- `subscription_canceled`
- `trial_expired`

### Retention / risk
- `user_became_inactive`
- `user_reactivated`
- `usage_threshold_reached`

## Strategic principle

**Use properties for state, events for behavior, lists for broad audience buckets.**

Bad setup = recreating MailerLite's rigid group sprawl.
Good setup = behavior-driven lifecycle marketing for SaaS.

## Migration approach from MailerLite

1. Export all subscribers + group memberships + important custom fields
2. Normalize into Loops property schema
3. Import contacts into Loops
4. Rebuild key lists (not every legacy group)
5. Recreate lifecycle logic in Loops UI using events/properties
6. Run MailerLite + Loops in parallel briefly
7. Cut over when stable

## Immediate priorities

1. Define final property schema
2. Create required contact properties in Loops
3. Decide final mailing lists
4. Export MailerLite contacts and map fields
5. Prepare sync scripts from Stripe / app / GA sources into Loops
