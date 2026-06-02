> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Google Analytics 4

> End-to-end GA4 setup for a client — from OAuth to your first widget.

Google Analytics 4 is one of the most common data sources in Oviond reports. This guide walks through connecting GA4 to a client and dropping a first widget on a report.

## Before you start

* You have admin access (or higher) to the GA4 property you want to report on.
* You've already created an Oviond [client](/clients/add) for this customer.

## 1. Start the OAuth flow

<Steps>
  <Step title="Open the client">
    Click the client in your sidebar.
  </Step>

  <Step title="Open Data Sources">
    Inside the client workspace, click **Data Sources**.
  </Step>

  <Step title="Click Google Analytics 4">
    Oviond opens a Google sign-in popup.
  </Step>

  <Step title="Authorize">
    Pick the Google account that has access to the GA4 property. Approve the scopes Oviond requests — these are read-only.
  </Step>
</Steps>

## 2. Pick the profile

GA4 connections can see every property the authorizing Google account has access to. You need to tell Oviond which property belongs to *this* client:

<Steps>
  <Step title="Open the data source">
    Back in Data Sources, click the newly connected GA4 tile.
  </Step>

  <Step title="Select the property">
    From the dropdown, pick the GA4 property for this client. See [Profiles](/data-sources/profiles).
  </Step>

  <Step title="Rename the connection">
    Optionally rename the connection to something client-friendly (e.g. *Acme — Main Site*) so your team picks the right one when building widgets.
  </Step>
</Steps>

## 3. Test the connection

Before building widgets, confirm the connection works:

<Steps>
  <Step title="Click Test Connection">
    From the data source's three-dot menu. See [Test Connection](/data-sources/test).
  </Step>

  <Step title="Look for Success">
    A green tick means the OAuth token is live and GA4 is returning data.
  </Step>
</Steps>

## 4. Build your first GA4 widget

<Steps>
  <Step title="Open a project">
    Create a new [project](/projects/add) or open an existing one.
  </Step>

  <Step title="Add a KPI widget">
    Click **+ Add Widget** → **KPI**.
  </Step>

  <Step title="Pick Google Analytics 4">
    In the Data Source dropdown, select the GA4 connection you just wired up.
  </Step>

  <Step title="Pick a metric">
    Start with **Sessions** — a universal GA4 KPI that exists for every property.
  </Step>

  <Step title="Set the date range">
    **Last 30 Days (relative)** — this way the widget auto-updates every time the report is opened.
  </Step>

  <Step title="Save">
    Click **Save** in the top-right. The widget renders live data.
  </Step>
</Steps>

## Common follow-ups

* Add a **Sessions by Source / Medium** table for traffic breakdown.
* Add a **Conversions** KPI if you've set up GA4 conversion events.
* Use **Calculated Metrics** to compute engagement rate or conversion rate.

## Troubleshooting

* **"No data returned"** — the property is connected but empty. Double-check the profile selection and the date range.
* **"Integration error"** — the OAuth token expired. Run [Test Connection](/data-sources/test), and if it fails, click **Reconnect**.
* **"Property not found"** — the authorizing Google account lost access to the property in GA4. Re-authorize with a Google account that still has access.
