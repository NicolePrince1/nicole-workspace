> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build Your First Report

> A complete walkthrough from creating a client to publishing a shared link.

This guide takes you from a fresh Oviond account to a live, shareable report for your first client. Expect it to take \~20 minutes end-to-end.

## Before you start

* You've signed up for Oviond and completed the [onboarding](/onboarding/overview) (full name, company name, website, client count).
* You have OAuth access to at least one data source (Google Ads, Google Analytics 4, Facebook Ads, etc).

## 1. Add a client

See [Add Client](/clients/add). At minimum, enter the client's **name** and **website**. Oviond auto-generates a thumbnail from the website URL.

## 2. Connect a data source

From the client's workspace:

<Steps>
  <Step title="Open Data Sources">
    Inside the client, click **Data Sources** in the sidebar.
  </Step>

  <Step title="Pick an integration">
    Click a tile — e.g. Google Analytics 4 — and run the OAuth flow. See [Connect](/data-sources/connect).
  </Step>

  <Step title="Pick the profile">
    Select which GA4 property belongs to this client. See [Profiles](/data-sources/profiles).
  </Step>
</Steps>

## 3. Create the report

See [Add Project](/projects/add). Pick **Report** as the type (not Dashboard) and name it *Acme — Monthly Performance* or similar. Start from a [template](/templates/apply) if one matches your needs, otherwise blank.

## 4. Add pages and widgets

<Steps>
  <Step title="Add a page">
    The project starts with one page. See [Pages](/projects/pages) to add and rename.
  </Step>

  <Step title="Add your first widget">
    Click **+ Add Widget**. Pick a **KPI tile** for a quick win — e.g. *Total Sessions, Last 30 Days*.
  </Step>

  <Step title="Add a chart">
    Next, a **line chart** showing Sessions trended over the last 30 days — it pairs well with the KPI above.
  </Step>

  <Step title="Save">
    Click **Save** in the top-right. See [Widgets](/projects/widgets).
  </Step>
</Steps>

## 5. Apply a theme

To make the report feel on-brand:

<Steps>
  <Step title="Create a theme">
    See [Add Theme](/themes/add). Set your client's primary color — Oviond auto-derives the full chart palette.
  </Step>

  <Step title="Apply it to the project">
    See [Apply Theme](/themes/apply).
  </Step>
</Steps>

## 6. Share it

See [Share Project](/projects/share). Enable the public link, copy the short URL, and send it to your client. The client opens the link in any browser — no Oviond account needed.

## Next steps

* [Schedule a Monthly Report](/guides/monthly-report) — automate delivery to your client's inbox.
* [Connect Google Analytics 4](/guides/connect-ga4) — the full GA4-specific setup.
* [Templates](/templates/add) — save this report's layout so you can spin up the same thing for your next client in minutes.
