# Oviond App QA — Retest Pass 2

Date: 2026-05-21  
Tester: Nicole Prince  
Account: `nicole@oviond.com`  
Environment: `https://app.oviond.com`  
Run type: clean-account retest + deeper functional sweep

## Executive verdict

The app is meaningfully better than the first pass, but I still would not call it launch-polished.

The two scariest first-pass blockers have improved:

- Account deletion worked.
- Fresh onboarding completed without the previous `Template not found` failure.
- The default Digital Marketing Dashboard now renders demo content instead of opening blank.

Remaining launch blockers are mostly polish/UX/routing rather than total flow failure:

- Billing still shows `null - 5 Clients`.
- Mobile still uses the desktop sidebar/navigation pattern and is not launch-ready.
- Top-level/direct routes still get misread as client IDs and show `Client not found`.
- Template preview still throws a missing theme 404.
- Template library still has duplicate-looking templates.

## Retest summary

| ID | Area | Retest status | Severity | Evidence |
|---|---|---:|---:|---|
| QA-001 | Onboarding | Fixed in this pass | Pass | `onboarding-06-after-finish.png` |
| QA-002 | Default dashboard | Fixed in this pass | Pass | `interaction-project-opened.png` |
| QA-003 | Mobile responsive UI | Still open | P1 | `mobile-home.png`, `mobile-settings.png`, `mobile-templates.png` |
| QA-004 | Billing plan/trial copy | Still open | P1 | `billing-page.png` |
| QA-005 | Direct-route handling | Still open | P2 | `route-bad-clients-route.png`, route logs |
| QA-006 | Missing template theme 404 | Still open | P2 | `template-preview-first.png`, network logs |
| QA-007 | Duplicate-looking templates | Still open | P2 | `templates-list.png` |
| QA-008 | Chart container warnings | New technical warning | P2/P3 | `logs.json`, `functional-logs.json` |
| QA-009 | Dialog accessibility warnings | New technical warning | P3 | `functional-logs.json` |

## What I tested

### Account reset and authentication

- Logged into existing Nicole QA account by magic link.
- Opened Settings → My Account.
- Used Danger Zone → Delete Account.
- Confirmed deletion by typing the email address.
- Verified the app returned to sign-in with `Account deleted` toast.
- Started again from a fresh sign-in/magic-link session.

Result: **Pass**.

Evidence:

- `delete-account-settings-page.png`
- `delete-account-modal.png`
- `delete-account-after-confirm.png`
- `fresh-account-after-login.png`

### Fresh onboarding

Completed all onboarding steps from a clean account:

1. Name: Nicole Prince
2. Company: Nicole QA Agency Retest 2
3. Website: oviond.com
4. Client count: 6–20
5. First client: Retest 2 Client
6. Finish

Result: **Pass**.

The old failure did not reproduce. Onboarding finished and landed on the created client’s Projects page with a default Digital Marketing Dashboard.

Evidence:

- `onboarding-01-name.png`
- `onboarding-02-company.png`
- `onboarding-03-website.png`
- `onboarding-04-client-count.png`
- `onboarding-05-first-client.png`
- `onboarding-06-after-finish.png`

### Default dashboard

Opened the default dashboard created by onboarding.

Result: **Pass**.

The dashboard is no longer blank. It renders demo widgets, sections, charts, and table content.

Evidence:

- `interaction-client-opened-project-list.png`
- `interaction-project-opened.png`

Note: the console still emitted repeated chart warnings: `The width(-1) and height(-1) of chart should be greater than 0`. The visible dashboard rendered, but this should still be cleaned up because it can become a real layout issue on slower devices or hidden containers.

### Main app routes and settings pages

Opened:

- `/`
- `/templates`
- `/automations`
- `/notifications`
- `/settings/my-account`
- `/settings/company`
- `/settings/users`
- `/settings/billing`
- `/settings/api-keys`
- `/settings/activity-log`
- `/settings/custom-domains`
- `/settings/email-settings`
- `/settings/data-sources`
- `/settings/archive`

Result: **Mostly pass**.

All expected settings pages loaded with sensible empty states or page content.

Evidence:

- `route-home.png`
- `route-templates.png`
- `route-automations.png`
- `route-notifications.png`
- `route-settings-my-account.png`
- `route-settings-company.png`
- `route-settings-users.png`
- `route-settings-billing.png`
- `route-settings-api-keys.png`
- `route-settings-activity.png`
- `route-settings-domains.png`
- `route-settings-emails.png`
- `route-settings-data-sources.png`
- `route-settings-archive.png`

### Direct-route bug

Opened direct/top-level paths:

- `/clients`
- `/projects`
- `/billing`
- `/api-keys`

Result: **Fail / still open**.

These still redirect into client-scoped paths like `/clients/projects` and trigger `Client not found`. The API calls confirm the bug, e.g. `https://api.oviond.com/v1/clients/clients` and similar 404s.

Expected behavior: either redirect intentionally to the correct global route, show a clean 404, or keep these as valid top-level aliases. They should not be interpreted as client IDs.

Evidence:

- `route-bad-clients-route.png`
- `route-bad-projects-route.png`
- `route-bad-billing-route.png`
- `route-bad-api-keys-route.png`
- `raw/route-results.json`
- `raw/logs.json`

### Billing

Opened Settings → Billing on the fresh trial account.

Result: **Fail / still open**.

Still visible:

- `null - 5 Clients`
- `Renews Jun 5, 2026` while the card says the account is on a free trial.
- Status label: `Trialing`.
- `Select Plan` CTA on what appears to be the current trial plan.

Expected:

- Real plan label, e.g. `Agency Plan — 5 Clients`.
- Trial-safe date copy, e.g. `Trial ends Jun 5, 2026`.
- Friendlier state label: `Trial` or `Free Trial`.
- CTA should reflect current state: `Current plan`, `Add payment method`, `Confirm plan`, or `Upgrade`, depending on billing logic.

Evidence:

- `billing-page.png`
- `route-settings-billing.png`

### Templates

Opened template library and previewed E-commerce Dashboard.

Result: **Partial pass, still has issues**.

Template preview rendered, but the network log still shows:

- `404 https://api.oviond.com/v1/themes/jaY2LSDDiC97JzWak`

Duplicate-looking templates also remain:

- `Google Analytics 4 Dashboard` appears twice.
- `Social Media Marketing Dashboard (Organic Insights)` appears twice, one marked `(new)`.

Expected:

- Template preview should not throw missing theme errors.
- Legacy/new templates should either be deduplicated or intentionally labeled in a way that makes the difference obvious.

Evidence:

- `templates-list.png`
- `template-preview-first.png`
- `raw/logs.json`

### API keys

Opened Settings → API Keys.

- Created a temporary key named `Retest 2 QA Key`.
- Verified the key appeared as active.
- Revoked it immediately.
- Verified it now shows as revoked.
- Redacted/remediated local evidence so the full key is not stored or uploaded.

Result: **Pass**.

Evidence:

- `api-keys-before.png`
- `api-key-create-modal.png`
- `api-key-after-revoke-redacted.png`
- `raw/api-key-after-revoke.json`

Security note: the key was revoked successfully. Do not use the original `api-key-created` screenshot as shareable evidence because that screen intentionally displayed the full one-time key.

### Automations

Opened Automations and New Automation.

Result: **Pass**.

The empty form blocks progress, which is correct validation behavior.

Evidence:

- `automations-page.png`
- `automation-new-modal.png`

### AI connectors

Opened AI Connectors panel.

Result: **Pass smoke test**.

Panel renders with connector options.

Evidence:

- `ai-connectors-panel.png`

### Client and project management

Created a second test client: `Functional QA Client`.

Result: **Pass**.

After create, app correctly routed into the new client’s Projects page and showed the empty project state.

Opened Add Project flow.

Result: **Pass smoke test**.

The project creation modal opens with choices:

- Start from scratch
- Start from a template

Evidence:

- `functional-add-client-modal.png`
- `functional-after-add-client.png`
- `functional-project-list.png`
- `functional-add-project-modal.png`

### Project sharing and editor

Opened default dashboard, clicked Share, then opened Edit mode.

Result: **Pass smoke test**.

Share panel rendered with:

- Link
- Email
- Download
- Embed
- Default share link
- Sharing options
- Link preview

Editor rendered with Add Content controls:

- Data Query
- Heading
- Textbox
- Image
- Button
- Embed

Evidence:

- `functional-share-modal.png`
- `functional-project-edit.png`

### Users, domains, and email settings

Opened form workflows without submitting external actions:

- Users → Invite User
- Domains → Add Domain
- Emails → Create Template

Result: **Pass smoke test**.

All expected forms opened.

Evidence:

- `functional-users-invite.png`
- `functional-domains-add.png`
- `functional-emails-template-create.png`

### Mobile/responsive

Opened at 390 × 844 mobile viewport:

- Home
- Settings → My Account
- Templates

Result: **Fail / still open**.

The desktop navigation/sidebar still appears in the mobile layout. Content is readable in places, but the IA still feels desktop-first and cramped. This is not launch-polished for mobile.

Expected:

- Collapsed hamburger/drawer navigation.
- No full persistent desktop sidebar.
- Better viewport use and less cramped content.

Evidence:

- `mobile-home.png`
- `mobile-settings.png`
- `mobile-templates.png`

## New technical warnings

### QA-008 — Chart container warnings

Repeated console warnings on project dashboards:

```text
The width(-1) and height(-1) of chart should be greater than 0
```

Severity: P2/P3 depending on whether it affects actual mobile/hidden-tab rendering.

Recommendation: inspect chart containers, especially Recharts/ResponsiveContainer wrappers, hidden panels, and edit/share overlay states.

### QA-009 — Dialog accessibility warnings

Repeated Radix-style dialog warnings:

```text
Warning: Missing `Description` or `aria-describedby={undefined}` for {DialogContent}.
```

Severity: P3.

Recommendation: add accessible descriptions to dialogs/modals, especially Add Client, Add Project, Invite User, Add Domain, Email Template.

## Launch recommendation

Do not launch yet if mobile and billing are part of the public first impression.

If launch pressure is extreme, the app is closer than before because onboarding and the default dashboard now work. But I would still fix these before inviting real trial users:

1. Billing plan header/copy (`null - 5 Clients`) — P1.
2. Mobile navigation/layout — P1.
3. Direct-route misclassification — P2 but embarrassing.
4. Template missing theme 404 — P2.
5. Duplicate template labels — P2 polish.

## Retest notes for next pass

Next retest should focus on:

- Confirm billing copy fixed.
- Confirm mobile layout has proper collapsed nav.
- Confirm `/clients`, `/projects`, `/billing`, `/api-keys` no longer resolve as client IDs.
- Confirm template preview no longer calls missing theme IDs.
- Confirm duplicate template naming is intentional or removed.
- Re-run clean-account onboarding one more time to ensure the fix is stable, not lucky.
