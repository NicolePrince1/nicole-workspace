> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Link to Client

> Attach a connected data source to a specific client workspace.

A data source lives at the **account** level — one OAuth connection can be linked to many clients. Linking makes the source's profiles selectable inside widgets in that client's projects.

<Steps>
  <Step title="Open the client">
    From the Clients list.
  </Step>

  <Step title="Open the client's Data Sources tab">
    Inside the client workspace.
  </Step>

  <Step title="Click + Link Data Source">
    Pick from the account-level data sources you've already connected.
  </Step>

  <Step title="Pick the profile for this client">
    Choose which ad account, property, or page maps to this client. See [Profiles](/data-sources/profiles).
  </Step>

  <Step title="Save">
    Every widget you build for this client can now pull from the linked data source + profile.
  </Step>
</Steps>

## Unlink

From the client's Data Sources tab, click the three-dot menu next to a linked source and choose **Unlink**. The data source remains at the account level — it's just not available inside this specific client anymore. Widgets in this client's projects that referenced it will show *Data source unavailable*.
