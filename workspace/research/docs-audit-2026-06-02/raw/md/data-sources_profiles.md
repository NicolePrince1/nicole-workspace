> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Profiles

> Pick which ad account, property, or page to report on for each connected data source.

A **profile** is the specific account, property, page, or view inside a data source. When you connect Google Ads you get access to every ad account the authorizing user can see — a profile is how you tell Oviond *which* ad account to report on per client.

## Why profiles matter

Without a profile selection, Oviond doesn't know which numbers to pull:

* **Google Ads** has a Customer ID per ad account
* **Google Analytics 4** has a Property per site
* **Facebook Ads** has an Ad Account per business
* **LinkedIn** has a Page per brand

Profiles resolve that ambiguity — each client's data source is anchored to one profile.

## Manage profiles

<Steps>
  <Step title="Open Data Sources">
    From the sidebar.
  </Step>

  <Step title="Pick the data source">
    Click a connected integration to see its available profiles.
  </Step>

  <Step title="Select a profile">
    Click the profile the client uses. Widgets configured with this data source now pull from the selected profile.
  </Step>

  <Step title="Rename if needed">
    Give each profile a friendly label (e.g. *Acme — Main Site*) so your team picks the right one when building widgets.
  </Step>
</Steps>
