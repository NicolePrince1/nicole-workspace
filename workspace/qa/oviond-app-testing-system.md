# Oviond App QA Testing System

_Last updated: 2026-05-21_

## Purpose

Create a repeatable launch QA loop for the new Oviond app until it is genuinely launch-ready.

The goal is not to “click around and hope.” The goal is to catch launch-blocking trust issues before real customers do.

## QA hub structure

Google Drive folder:

- `Oviond App QA Testing System/`
  - `00 — Testing System/`
  - `01 — Reports/`
  - `02 — Evidence Screenshots/`
  - `03 — Retest Runs/`
  - `Oviond App QA Bug Tracker` Google Sheet

Each test pass should include:

1. Full written report
2. Prioritized bug list
3. Evidence screenshots
4. Retest checklist
5. Launch recommendation: `Do not launch`, `Conditional launch`, or `Ready`

## Severity system

### P0 — Launch blocker
Must be fixed before launch.

Examples:
- New users cannot complete onboarding.
- Signup/login breaks.
- Data creation corrupts or partially fails.
- Billing/pricing materially wrong.
- Security/privacy issue.

### P1 — High priority
Should be fixed before launch unless explicitly accepted.

Examples:
- Major empty/broken state.
- Mobile layout broken.
- Core agency owner workflow confusing.
- Error appears in normal happy path.

### P2 — Medium priority
Can launch with known issue if documented, but should be fixed soon.

Examples:
- Route aliases missing.
- Non-critical 404s handled visually.
- Duplicate-looking templates.
- Confusing copy.

### P3 — Polish
Nice-to-fix. Does not block launch.

Examples:
- Small wording inconsistencies.
- Minor layout polish.
- UX improvements.

## Core retest loop

When Chris says fixes are ready:

1. Start a new dated pass in `03 — Retest Runs`.
2. Use `nicole@oviond.com` with magic-link login unless Chris provides a fresh QA account.
3. Test first as a new agency owner.
4. Retest every open P0/P1 from the previous report.
5. Update the Google Sheet bug tracker with status, notes, and new issues.
6. Run a fresh smoke pass across the app because fixes can create regressions.
7. Produce an updated launch recommendation.

## Standard test pass checklist

### Access and auth

- App resolves at `app.oviond.com`.
- Magic-link login works.
- Session persists across reload.
- Logout/login recovery works.
- Error states are understandable.

### New-user onboarding

- Name step validates correctly.
- Company step validates correctly.
- Website step validates correctly.
- Client volume step saves correctly.
- First client creation validates correctly.
- Finish completes without partial failure.
- Account, company, client, and starter project state are consistent after completion.
- Retry behavior does not create duplicate or dirty state.

### Agency owner core workflow

- Client list loads.
- Add client works.
- Open client works.
- Project list loads.
- Create project works.
- Open dashboard/report works.
- Edit mode works.
- Empty states are useful when no data source is connected.

### Templates

- Template list loads.
- Template preview loads.
- Template naming is clear.
- Duplicate templates are intentional or removed.
- Use-template flow works.

### Data sources / integrations

- Empty data-source state is clear.
- Connect-data-source entry point is findable.
- Failed connection states are clear.
- Disconnection/reconnect language is safe.

### Automations

- Empty automation state is clear.
- New automation validates required fields.
- Schedule fields behave correctly.
- Project/client selection works when available.
- No automation is sent accidentally during QA.

### Settings

- My Account loads.
- Company/branding loads.
- Users loads.
- Billing loads with correct plan/trial state.
- API Keys create/revoke works.
- Activity Log works.
- Domains page works.
- Emails page works.
- Data Sources page works.
- Archive works.

### Billing/pricing

- Plan name is not null.
- Trial dates are correct.
- Trial copy says trial, not renewal, where appropriate.
- Plan CTA state is accurate.
- Client slider/limits are clear.
- API/MCP inclusion copy matches commercial strategy.

### API/MCP

- API key creation works.
- API key is shown once.
- API key can be copied.
- API key can be revoked.
- AI connector snippets behave correctly.
- No key is exposed after panel close.

### Responsive smoke test

- Mobile width: 390px.
- Tablet width: 768px.
- Desktop width: 1440px.
- Sidebar/header layout does not crush content.
- Primary actions remain reachable.

### Technical capture

For every pass, capture:

- Screenshots for failures.
- Console errors.
- Failed network requests.
- Reproduction steps.
- Expected vs actual result.
- Suggested fix.

## Current retest baseline — Retest Pass 2

From the 2026-05-21 Retest Pass 2:

1. PASS — Account deletion worked and returned to sign-in with `Account deleted`.
2. PASS — Fresh onboarding completed without the previous `Template not found` failure.
3. PASS — Default Digital Marketing Dashboard rendered demo content instead of blank state.
4. P1 — Mobile layout is still not launch-ready; desktop navigation remains visible on mobile.
5. P1 — Billing still shows `null - 5 Clients` and confusing trial/renewal copy.
6. P2 — Direct top-level routes are still misread as client IDs.
7. P2 — Template preview still triggers a missing theme 404.
8. P2 — Template library still contains duplicate-looking templates.
9. P2/P3 — Dashboard/chart container warnings appear in console.
10. P3 — Several dialogs have missing accessibility descriptions.

## Launch gate

Oviond should not launch until:

- All P0s are fixed and retested.
- All P1s are fixed or explicitly accepted by Chris.
- Billing/pricing states are accurate.
- New-user onboarding completes cleanly.
- A fresh agency-owner smoke pass produces no new launch blockers.
