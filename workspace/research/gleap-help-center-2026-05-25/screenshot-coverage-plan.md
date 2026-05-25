# Gleap Help Center Screenshot Coverage Plan

Source: `/data/.openclaw/workspace/research/gleap-help-center-2026-05-25/gleap-help-center-live-export.json`

Standard: marker-only screenshots; ordered/numbered explanation list in the article body; no bullet+manual numbers; no “Open screenshot” links. Screenshot only when it supports the article.

Totals: 46 articles; 36 screenshots recommended; 10 no screenshot.

## Getting Started

| Article | Screenshot needed | Recommended app surface | Why |
|---|---:|---|---|
| What is Oviond? | No | None | Conceptual overview; a screenshot would add decoration rather than clarify a task. |
| Quick start checklist | No | None | Checklist spans multiple workflows; better as text until split into task-specific articles. |
| Key terms in Oviond | No | None | Glossary content; no single UI surface explains the terms better than concise definitions. |
| Create your first client report | Yes | Client workspace → Projects → new report/template flow | A marker-only screenshot can orient new users to the exact path from client to project creation. |
| Where to get help | No | None | Support-prep checklist; screenshots should come from the user’s issue, not the article. |

## Clients

| Article | Screenshot needed | Recommended app surface | Why |
|---|---:|---|---|
| Add a client | Yes | Clients list → Add Client modal/form | Shows where Add Client lives and which fields matter without over-explaining. |
| Edit client details | Yes | Client settings/details page | Helps users locate editable fields like website, timezone, currency, manager, folder, and theme. |
| Organize clients with folders | Yes | Clients list → folder/sidebar controls | Useful for showing the folder control and where client organization happens. |
| Refresh a client screenshot | Yes | Client settings or client card screenshot/thumbnail action | The action is visual and easy to miss; a marker can identify the refresh/update control. |
| Archive or delete a client | Yes | Client settings → archive/delete danger area | Supports a high-risk action by showing the exact location while article text carries the warnings. |

## Data Sources

| Article | Screenshot needed | Recommended app surface | Why |
|---|---:|---|---|
| What are data sources? | No | None | Conceptual definition; avoid unnecessary integration screenshots. |
| Connect a data source | Yes | Client integrations or global Integrations → platform connect flow | Shows the connect entry point and where account/profile selection begins. |
| Choose the right account or profile | Yes | Integration account/profile selection screen | A screenshot can mark account name/ID/profile selectors, which directly supports avoiding wrong connections. |
| Reconnect an expired data source | Yes | Integrations list → connected account status/reconnect action | Users need to find the affected connection and Reconnect control. |
| Troubleshoot missing data | Yes | Widget settings/data source selector plus integration status area | Supports the diagnostic path: confirm selected source/date range, then test the connection. |

## Reports & Dashboards

| Article | Screenshot needed | Recommended app surface | Why |
|---|---:|---|---|
| Reports vs dashboards | No | None | Decision guidance; UI screenshot would be redundant unless article expands into project creation. |
| Create a report or dashboard | Yes | Client workspace → Projects → New Project modal | Shows project type choice, naming, and template/blank entry points. |
| Add and organize pages | Yes | Report editor → pages/sidebar/page controls | Page controls are spatial; markers can show add, rename, and reorder areas. |
| Add widgets | Yes | Report/dashboard editor → Add Widget panel | Directly supports finding widget types, data source, metric, and settings controls. |
| Share a report | Yes | Report editor/preview → Share dialog | Shows share link, public/private state, and preview/test controls. |
| Export a report as PDF | Yes | Report editor/preview → Export/PDF control | Helps users find the PDF export action and preview/download step. |

## Templates, Themes & Media

| Article | Screenshot needed | Recommended app surface | Why |
|---|---:|---|---|
| Use a template | Yes | New project/template gallery or template picker | Shows where templates are selected and reinforces review-after-apply. |
| Create or update a template | Yes | Report editor/template save or Templates area | Useful because saving/updating templates is app-specific and easy to confuse with normal report edits. |
| Apply a theme | Yes | Report/client theme selector or branding panel | Shows where theme selection happens and what to preview afterward. |
| Upload and manage media | Yes | Media library/uploader inside report or account settings | Visual task; screenshot can mark upload, file list, and insert/manage controls. |
| Troubleshoot branding not showing | Yes | Branding/theme settings with logo and domain status visible | A focused screenshot helps users check theme, logo, report refresh, and domain status locations. |

## Automations & Email Delivery

| Article | Screenshot needed | Recommended app surface | Why |
|---|---:|---|---|
| Schedule report delivery | Yes | Automation creation screen for a report | Shows schedule, recipients, sender/subject, PDF attachment, and test controls. |
| Test an automation | Yes | Automation detail screen → Test/send now action | The core action is a specific button/status area; screenshot prevents hunting. |
| Pause or resume an automation | Yes | Automation list/detail screen → active toggle/status | Shows the automation status and pause/resume control clearly. |
| Troubleshoot failed scheduled reports | Yes | Automation history/detail screen plus email setup status | Supports checking active state, schedule, recipients, history, and sender setup. |
| Set up branded email sending | Yes | Email sending/domain verification settings | Verification states and sender configuration benefit from markers. |

## White Label & Sharing

| Article | Screenshot needed | Recommended app surface | Why |
|---|---:|---|---|
| What white label means in Oviond | No | None | Conceptual positioning; screenshots belong in theme/domain/email setup articles. |
| Set up a custom domain | Yes | White label/domain settings → add domain/DNS instructions | DNS setup is procedural; screenshot can mark domain field, required records, and status. |
| Check custom domain status | Yes | White label/domain settings → domain status table/card | Article is about interpreting the status; screenshot should show where status appears. |
| Remove a custom domain | Yes | White label/domain settings → domain menu/remove action | High-risk action; screenshot supports finding the correct domain and remove area while warnings stay in text. |
| Share links safely | Yes | Report Share dialog/link settings | Shows where to copy/test the link and verify the correct client/report before sending. |

## Team, Account & Billing

| Article | Screenshot needed | Recommended app surface | Why |
|---|---:|---|---|
| Invite a team member | Yes | Team/users settings → Invite user modal | Shows invite email, role, and access controls. |
| User roles and permissions | Yes | Team/users settings → role/permission selector | Permissions are UI-specific; screenshot can mark role and client-access controls. |
| Update company settings | Yes | Company/account settings page | Shows company profile, logo, timezone, and default branding locations. |
| View usage and plan limits | Yes | Billing/account usage page | Usage meters/limits are visual and worth showing if no sensitive account data is exposed. |
| Billing, invoices, and subscription help | No | None | Billing pages may expose sensitive payment/customer data; text checklist is safer unless a sanitized mock exists. |

## Troubleshooting

| Article | Screenshot needed | Recommended app surface | Why |
|---|---:|---|---|
| I cannot log in | No | None | Logged-out troubleshooting is generic; article should stay text-first and avoid stale login-screen captures. |
| My integration account is not appearing | No | None | OAuth/account lists can expose sensitive external accounts; text checklist is safer than screenshots. |
| Widgets are empty or showing zero | Yes | Report editor → widget settings/date range/data source selector | Shows the exact places to verify date range, selected source, and widget configuration. |
| A report link is not working | Yes | Report Share dialog/settings and preview/open-link controls | Supports checking sharing enabled, link copied, and private-window testing path. |
| PDF export or email delivery failed | Yes | Report export controls and/or automation delivery history | A screenshot can orient users to export status, delivery history, and manual test controls. |

