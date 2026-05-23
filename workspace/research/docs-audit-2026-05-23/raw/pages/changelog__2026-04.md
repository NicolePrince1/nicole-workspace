> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# April 2026

> Release notes for the Oviond REST API.

<Update label="2026-04-20" description="Initial release">
  ### Public API reference launched

  The Oviond REST API reference is now live on Mintlify. The full endpoint catalog — projects, widgets, integrations, automations, public share links — is auto-generated from the backend's OpenAPI spec and kept in sync on every release.

  * Interactive **Try it** console against `https://api.oviond.com`
  * Bearer-token authentication via API keys generated in **Settings → API Keys**
  * Grouped by domain: Account, Projects, Widgets, Integrations, Automations, Public, and more
</Update>

<Update label="2026-04-19" description="Automations">
  ### Scheduled report delivery

  Schedule reports to be emailed to clients on a recurring cadence. Automations support pause/unpause, run history, and on-demand test sends.

  * `POST /v1/automations` — create an automation
  * `POST /v1/automations/:id/pause` and `/unpause`
  * `POST /v1/automations/:id/test` — send a test email without logging a run
  * `GET /v1/automations/history` — inspect past deliveries
</Update>

<Update label="2026-04-18" description="PDF export">
  ### PDF generation

  Render any report to PDF with selectable format and orientation. Jobs run asynchronously — enqueue, then poll for status until the download URL is ready.

  * `POST /v1/pdf/generate` — enqueue a job
  * `GET /v1/pdf/status/:job_id` — poll until complete
</Update>

<Update label="2026-04-17" description="White label & custom domains">
  ### Fully branded client experiences

  Serve reports under your own domain with end-to-end white label — logo, favicon, colors, OG preview, password gating, and error messaging.

  * `PUT /v1/white-label` — update branding settings
  * `POST /v1/white-label/domains` — add a custom domain (auto-detects Cloudflare / GoDaddy)
  * `GET /v1/white-label/domains/:id/status` — check DNS verification via Vercel
</Update>

<Update label="2026-04-16" description="Templates & themes">
  ### Reusable report scaffolds

  Create templates from existing reports (pages + widgets + date settings carry over) and apply themes to control typography, color palette, and chart styling across any project.

  * `POST /v1/templates` — create a template, optionally copying from a project
  * `POST /v1/themes` — create a theme (chart colors auto-derive from `primary_color`)
  * Shared library templates available to every account
</Update>

<Update label="2026-04-15" description="Media library">
  ### Uploads, folders, and S3-backed storage

  Upload images and assets, organize them into folders, and reference them directly from widgets. Deletes are soft — files stay in S3 for recovery.

  * `POST /v1/media/upload-url` — request a pre-signed upload URL
  * `GET /v1/media` and `/v1/media/folders`
  * Bulk delete, rename, and folder management
</Update>

<Update label="2026-04-14" description="API keys">
  ### Programmatic access

  Issue API keys from **Settings → API Keys** to call the REST API outside the app. Keys can be revoked instantly and support role-based scopes.

  * `POST /v1/api-keys` — create a key (secret shown once)
  * `POST /v1/api-keys/:id/revoke`
</Update>

<Update label="2026-04-13" description="Alerts">
  ### Workspace-level notifications

  In-app alerts for automation failures, integration disconnects, and team events — with read/unread tracking and per-user delivery preferences.

  * `GET /v1/alerts` — list recent alerts
  * `GET /v1/alerts/unread-count`
  * `PUT /v1/alerts/preferences` — opt in/out of email delivery
</Update>

<Update label="2026-04-12" description="Calculated & saved metrics">
  ### Custom KPIs and reusable queries

  Define formulas that combine metrics across integrations (e.g. `Revenue / Sessions`), and save data-query configurations you use across multiple reports.

  * `POST /v1/calculated-metrics` — define a formula
  * `POST /v1/saved-metrics` — save a query config
  * Both support duplicate for quick variants
</Update>

<Update label="2026-04-11" description="Custom data">
  ### Bring your own CSVs

  Upload CSV datasets and query them alongside integration data. Useful for offline sales, forecasts, or any metric that doesn't live in a connected platform.

  * `POST /v1/custom-data` — upload and parse a dataset
  * `POST /v1/custom-data/:id/duplicate`
</Update>

<Update label="2026-04-10" description="Integrations">
  ### Connect marketing platforms via OAuth

  OAuth 2.1 connection flow for Google Analytics, Meta Ads, LinkedIn, and the rest of the Oviond integration catalog. Datasources link to clients; profiles are selected per integration.

  * `GET /v1/integrations/auth-url` — start an OAuth flow
  * `POST /v1/integrations/auth` — exchange the code
  * `POST /v1/data/query` — pull metrics from connected sources
</Update>

<Update label="2026-04-09" description="Reports, pages & widgets">
  ### The report canvas

  The core editor API — create reports, add pages, and drop widgets (charts, KPIs, text, images, embeds, goals, buttons). Atomic `/save` endpoint persists pages and bulk widget upserts in a single call.

  * `POST /v1/projects` — create a report or dashboard
  * `POST /v1/pages` — add a page to a project or template
  * `POST /v1/widgets` — batch upsert widgets
</Update>

<Update label="2026-04-08" description="Clients & folders">
  ### Client workspaces

  Every report ties to a client. Organize clients into folders, bulk-delete, and filter by folder across the dashboard.

  * `POST /v1/clients` — create a client
  * `POST /v1/folders` — organize clients into folders
  * `PUT /v1/clients/:id/move` — move between folders
</Update>

<Update label="2026-04-07" description="Team & account management">
  ### Multi-user accounts

  Invite team members, assign roles, and restrict users to a subset of projects. Account-level settings for company info, branding, and billing.

  * `POST /v1/users/invite` — invite a team member
  * `GET /v1/account` and `/v1/account/usage` — plan + usage snapshot
  * `PUT /v1/branding` — set logo, favicon, brand color
</Update>

<Update label="2026-04-06" description="Public sharing">
  ### Shareable report links

  Every project gets a short `nano_id` share URL. Public endpoints return the full rendered payload — widgets, branding, theme, white label — in a single request, with no authentication required.

  * `GET /v1/public/resolve/:nano_id` — resolve a short link
  * `GET /v1/public/report/:account_id/:client_id/:project_id` — full render payload
  * `GET /v1/public/og-meta/:nano_id` — OG tags for link previews
</Update>
