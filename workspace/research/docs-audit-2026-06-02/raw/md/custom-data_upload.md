> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload Custom Data

> Upload a CSV dataset to report on data that doesn't live in a connected integration.

**Custom Data** lets you upload your own CSV files and use them alongside data from connected integrations. Useful for:

* Offline sales, lead lists, or CRM exports
* Revenue forecasts and targets
* Any KPI that lives outside the integrations we support natively

## How it works

<Steps>
  <Step title="Upload a CSV">
    From **Data → Custom Data**, click **Upload** and pick a CSV. Oviond parses the headers into columns and stores the rows.
  </Step>

  <Step title="Reference it in a widget">
    In any widget, pick **Custom Data** as the datasource, then select your uploaded dataset and the column you want to visualize.
  </Step>

  <Step title="Update the data">
    Re-upload a CSV with the same structure to refresh the underlying rows — all widgets that reference the dataset update automatically.
  </Step>
</Steps>

<Note>
  Custom Data is account-level — any client's project can reference any custom dataset you've uploaded. Combine it with integration data in the same widget using **Calculated Metrics**.
</Note>

## When to use Custom Data vs a Data Source

* **Data Sources** (Google Ads, Facebook, etc.) — live data pulled from a connected marketing platform.
* **Custom Data** — static or periodically-refreshed data you upload yourself.
