# Oviond App QA Pass — 2026-05-21

## Scope

Tested `https://app.oviond.com` as `nicole@oviond.com`, acting as a new agency owner.

Coverage included:

- Magic-link login
- New-user onboarding
- Client creation path
- Client/project list
- Default dashboard project view and edit mode
- Templates and template preview
- Automations entry flow
- Notifications
- Settings: account, company, users, billing, API keys, activity log, domains, emails, data sources, archive
- AI connectors panel
- Basic validation states
- Mobile viewport smoke test

QA data created:

- Company: `Nicole QA Agency`
- Client: `QA Launch Test Client`
- API key test: created and then revoked immediately

## Launch recommendation

**Do not launch until the onboarding failure is fixed.**

The app is usable after the failed onboarding flow, but the user sees a hard error during first-run setup. That is launch-blocking because it makes the product look broken at the exact moment trust matters most.

---

## P0 / launch-blocking

### 1. Onboarding ends with `Template not found`

**Severity:** P0  
**Area:** New-user onboarding  
**Screenshot:** `14-after-onboarding.png`

**Steps to reproduce**

1. Log in as a new user via magic link.
2. Complete onboarding:
   - Name: Nicole Prince
   - Company: Nicole QA Agency
   - Website: oviond.com
   - Clients: 6–20
   - First client: QA Launch Test Client / qa-client.example.com
3. Click **Finish**.

**Actual result**

- UI shows: `Something went wrong` / `Template not found`.
- Final card says: `We couldn't finish setting things up`.
- Retry is offered.

**Observed network evidence**

- `GET https://api.oviond.com/v1/users/me` → `404` during early onboarding/new-user state.
- `POST/GET https://api.oviond.com/v1/onboarding` → `404` / failure surfaced as `Template not found`.

**Important nuance**

Despite the error, the account/client/default project were later created. So the backend appears to partially complete the setup while the frontend reports failure. That is dangerous because users may retry and create duplicate/dirty setup state.

**Expected result**

- Onboarding should complete cleanly.
- If template creation fails, either:
  - create the account/client and show a recoverable “default dashboard could not be created” message, or
  - rollback cleanly and prevent partial state.

---

## P1 / high priority

### 2. Default dashboard opens blank after onboarding

**Severity:** P1  
**Area:** Project/dashboard view  
**Screenshot:** `21-project-opened.png`

**Steps**

1. Open the created client.
2. Open the default `Digital Marketing Dashboard` project.

**Actual result**

- Header loads, but main dashboard body is blank.
- No widgets, no skeleton loader, no empty state, no explanation.

**Expected result**

If no data sources are connected, show a clear empty state: connect data sources, use demo mode, or edit dashboard.

---

### 3. Mobile layout is not launch-ready

**Severity:** P1  
**Area:** Responsive UI  
**Screenshot:** `mobile-home.png`

**Actual result**

- Desktop sidebar remains visible on mobile.
- Main content is squeezed into the remaining width.
- Large grey/empty column consumes valuable screen space.
- Client cards and controls become cramped.

**Expected result**

Mobile should use a collapsed nav, drawer, or bottom nav. If full mobile support is not intended for launch, tablet/mobile should still not look broken.

---

### 4. Billing plan label renders `null - 5 Clients`

**Severity:** P1  
**Area:** Billing / pricing  
**Screenshot:** `settings-billing.png`

**Actual result**

Billing page shows: `null - 5 Clients`.

**Expected result**

Should show the real plan name, e.g. `Agency Plan - 5 Clients` or `Free Trial - 5 Clients`.

**Related copy issues**

- `Renews Jun 5, 2026` conflicts with trial messaging. For a trial, use `Trial ends Jun 5, 2026`.
- `Trialing` feels awkward; use `Trial` or `Free Trial`.
- `$59/Month` should be `$59/month`.

---

## P2 / medium priority

### 5. Direct route handling creates misleading `Client not found` pages

**Severity:** P2  
**Area:** Routing / deep links

**Examples tested**

- `/clients`
- `/projects`
- `/dashboards`
- `/reports`
- `/billing`
- `/users`
- `/api-keys`
- `/media`
- `/exports`

**Actual result**

Several direct top-level routes are interpreted as client IDs and redirect/render under `/clients/projects`, causing API calls like:

- `/v1/clients/clients`
- `/v1/clients/projects`
- `/v1/clients/billing`
- `/v1/clients/users`

The user sees repeated `Client not found` messaging.

**Expected result**

Top-level routes should either:

- resolve to real pages,
- redirect intentionally to the correct settings/client route,
- or show a proper 404 page.

---

### 6. Template preview loads, but theme request 404s

**Severity:** P2  
**Area:** Templates  
**Screenshot:** `30-template-preview.png`

**Observed network issue**

- `GET https://api.oviond.com/v1/themes/jaY2LSDDiC97JzWak` → `404`

**Actual result**

The template preview still renders with demo data, but a missing theme request appears in the logs.

**Expected result**

Template preview should not request missing theme IDs, or should handle fallback theme silently without noisy 404s.

---

### 7. Template library contains duplicate-looking templates

**Severity:** P2  
**Area:** Template library

Examples visible in the template list:

- `Social Media Marketing Dashboard (Organic Insights)` appears twice, one with `(new)` in the description.
- `Google Analytics 4 Dashboard` appears twice.
- `Google Ads Dashboard` appears twice.

**Expected result**

Either deduplicate before launch, label clearly as legacy/new, or add filters/version labels so users are not confused.

---

## P3 / polish

### 8. Settings URL names are not obvious from visible tab labels

**Severity:** P3  
**Area:** Settings routing

Direct `/settings/domains` and `/settings/emails` did not resolve to those pages, while clicking the sidebar tabs uses:

- `/settings/custom-domains`
- `/settings/email-settings`

This is not critical, but aliases would reduce confusion and improve shareability/support instructions.

---

### 9. AI connectors panel opens but should guide users based on key state

**Severity:** P3  
**Area:** API/MCP onboarding  
**Screenshot:** `25-ai-connectors.png`

The connector picker opens cleanly. If no active API key exists, it should clearly prompt users to create a key before showing connector setup snippets.

---

## Things that worked

- App domain works at `app.oviond.com`.
- Magic-link login works.
- New account/session creation works.
- Basic onboarding form validation works for required fields.
- Client list loads after setup.
- Client open flow works.
- Project list loads.
- Project edit mode opens.
- Templates page loads.
- Template preview renders demo dashboard content.
- Automation modal required-field validation works.
- Add-client modal required-field validation works.
- Settings pages mostly load cleanly.
- API key creation works.
- API key revoke works.
- Email/domain settings pages are accessible via settings sidebar.

## Cleanup performed

- Test API key was revoked.
- Sensitive browser storage/session state was not retained in this report.

## Priority fix order

1. Fix onboarding `Template not found` and partial-state behavior.
2. Add proper dashboard empty state for projects with no data/widgets.
3. Fix mobile responsive layout or explicitly block/support desktop-only with a sane layout.
4. Fix billing `null - 5 Clients` and trial copy.
5. Clean up route handling for top-level paths.
6. Fix template theme 404.
7. Deduplicate/label templates before launch.
