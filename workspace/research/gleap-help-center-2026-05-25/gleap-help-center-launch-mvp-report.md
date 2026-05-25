# Gleap Help Center Launch MVP — 2026-05-25

## Outcome

Built a clean launch-ready starting point for `help.oviond.com` in Gleap after the full help center reset.

The goal was not to recreate the technical Mintlify docs. The goal was a small, consumer-friendly in-app help center for customers and Gleap/KAI-style support answers.

## Live structure created

Created **9 collections** and **46 published articles**.

### Getting Started

- What is Oviond?
- Quick start checklist
- Key terms in Oviond
- Create your first client report
- Where to get help

### Clients

- Add a client
- Edit client details
- Organize clients with folders
- Refresh a client screenshot
- Archive or delete a client

### Data Sources

- What are data sources?
- Connect a data source
- Choose the right account or profile
- Reconnect an expired data source
- Troubleshoot missing data

### Reports & Dashboards

- Reports vs dashboards
- Create a report or dashboard
- Add and organize pages
- Add widgets
- Share a report
- Export a report as PDF

### Templates, Themes & Media

- Use a template
- Create or update a template
- Apply a theme
- Upload and manage media
- Troubleshoot branding not showing

### Automations & Email Delivery

- Schedule report delivery
- Test an automation
- Pause or resume an automation
- Troubleshoot failed scheduled reports
- Set up branded email sending

### White Label & Sharing

- What white label means in Oviond
- Set up a custom domain
- Check custom domain status
- Remove a custom domain
- Share links safely

### Team, Account & Billing

- Invite a team member
- User roles and permissions
- Update company settings
- View usage and plan limits
- Billing, invoices, and subscription help

### Troubleshooting

- I cannot log in
- My integration account is not appearing
- Widgets are empty or showing zero
- A report link is not working
- PDF export or email delivery failed

## Source-of-truth approach

Used the live API/documentation work as the capability map, especially:

- `https://api.oviond.com/openapi.json`
- Existing Mintlify user-doc crawl from `docs.oviond.com`
- Previous docs audit findings around terminology, internal language leaks, destructive actions, and customer-friendly wording

I deliberately kept the Gleap articles non-technical:

- No OpenAPI/Swagger language
- No internal implementation/vendor stack names
- No raw database/API-field terminology
- No over-specific UI claims where the source was not strong enough
- Destructive actions include cautionary guidance

## QA performed

Verified through the Gleap API:

- Collections: 9
- Articles: 46
- All articles are `isDraft: false`
- No duplicate article titles
- No article below the minimum useful length threshold
- No banned/internal terms detected in public article title, description, or plain text:
  - Supabase
  - S3
  - SQS
  - Resend
  - Vercel
  - cron
  - raw_data
  - resource_type/resource_id
  - users table/accounts row
  - upstream API
  - JWT/OpenAPI/Swagger

QA artifacts:

- `gleap-help-center-live-export.json`
- `gleap-help-center-qa.json`
- `gleap-help-center-launch-mvp-summary.json`

## Notes

I did not need to log into the product UI for this first-pass build because the required product truth was available from the live API capability map and the existing docs crawl. I avoided writing any article that depended on unverified UI microcopy or exact screen layout.

Next improvement pass should happen after the team has tested the new app and Michelle/support see real customer questions. That pass should add screenshots, exact UI paths, and deeper troubleshooting for the most common tickets.
