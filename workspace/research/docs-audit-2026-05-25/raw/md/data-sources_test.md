> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Connection

> Verify a data-source authorization is still valid.

Test Connection pings the data source's API with the stored OAuth token and reports back success or failure. Use it when:

* A widget shows *Integration error* and you want to check if re-auth is needed
* You just reconnected a data source and want to confirm it's working
* You're debugging a failed automation that depends on this data source

<Steps>
  <Step title="Open Data Sources">
    From the sidebar.
  </Step>

  <Step title="Open the data source">
    Click the integration you want to test.
  </Step>

  <Step title="Click Test Connection">
    Oviond hits the provider's API using the stored token.
  </Step>

  <Step title="Read the result">
    **Success** — token is valid, data should flow. **Failed** — token expired or was revoked; reconnect.
  </Step>
</Steps>

## If the test fails

* Click **Reconnect** to kick off a fresh OAuth flow. The existing profile selections are preserved.
* If reconnect doesn't resolve it, the authorizing user's access in the source platform may have been revoked — check the source platform's admin for the token's status.
