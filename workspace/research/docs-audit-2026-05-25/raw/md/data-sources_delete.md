> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Data Source

> Remove an OAuth connection from your account.

Deleting a data source revokes its OAuth token and removes it from the account — every client that had it linked loses access, and every widget referencing it shows *Data source unavailable* until re-wired.

<Warning>
  If the data source is currently feeding automations or active reports, deleting it will break them on the next render. Unlink it from clients first if you want a softer path — see [Link to Client](/data-sources/link).
</Warning>

<Steps>
  <Step title="Open Data Sources">
    From the sidebar.
  </Step>

  <Step title="Open the source's menu">
    Click the three-dot menu on the integration card.
  </Step>

  <Step title="Choose Delete">
    Confirm when prompted.
  </Step>

  <Step title="Optional: revoke in the source platform">
    Oviond revokes its own access token, but if you want to be extra-thorough, remove Oviond from the authorized-apps list in the source platform too (e.g. Google Account → Third-party apps).
  </Step>
</Steps>
