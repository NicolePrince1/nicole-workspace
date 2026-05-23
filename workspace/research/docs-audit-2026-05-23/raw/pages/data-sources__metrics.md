> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metrics

> Saved and calculated metrics you can reuse across widgets.

Oviond gives you three tools for extending the default metrics that come with each integration: **calculated metrics** let you define your own formulas, **saved metrics** let you bookmark a metric configuration for quick reuse, and **custom data** lets you upload datasets that aren't available through any integration. Each tool is available from the **Metrics** section in the left sidebar.

***

## Calculated metrics

A calculated metric is a user-defined formula that combines one or more existing metrics into a new value. For example, you can create a click-through rate metric by dividing clicks by impressions and multiplying by 100, or a cost-per-lead metric by dividing spend by the number of leads. Calculated metrics appear alongside native metrics when you configure a widget.

### Create a calculated metric

<Steps>
  <Step title="Open Metrics">
    Click **Metrics** in the left sidebar, then select the **Calculated Metrics** tab.
  </Step>

  <Step title="Click New Calculated Metric">
    Click **+ New Calculated Metric**.
  </Step>

  <Step title="Name the metric">
    Enter a name in the **Metric name** field. Choose a name that makes the formula's purpose clear (for example, "CTR %" or "Cost per Lead").
  </Step>

  <Step title="Write the formula">
    In the **Formula** field, build your calculation using the metric picker and standard operators (`+`, `-`, `*`, `/`, and parentheses for grouping). Start typing a metric name to search and insert it.

    Example formula for click-through rate:

    ```
    (Clicks / Impressions) * 100
    ```
  </Step>

  <Step title="Set the unit">
    Choose the unit that matches the output of your formula: **Number**, **Percentage**, or **Currency**. This controls how the value is formatted in widgets.
  </Step>

  <Step title="Save the metric">
    Click **Save**. The calculated metric is now available across all your clients and reports.
  </Step>
</Steps>

### Edit a calculated metric

1. Go to **Metrics** > **Calculated Metrics**.
2. Find the metric you want to update and click the three-dot menu next to it.
3. Select **Edit**.
4. Update the name, formula, or unit as needed and click **Save**.

<Warning>
  Editing a calculated metric updates it everywhere it is used. Any widgets that display this metric will immediately reflect the new formula.
</Warning>

### Duplicate a calculated metric

1. Go to **Metrics** > **Calculated Metrics**.
2. Click the three-dot menu next to the metric and select **Duplicate**.
3. Oviond creates a copy prefixed with "Copy of". Open the copy, rename it, and adjust the formula as needed.

### Use a calculated metric in a widget

When adding or editing a widget in the report builder, open the **Metrics** selector. Your calculated metrics appear in the list alongside native metrics from connected integrations. Select the calculated metric as you would any other metric.

***

## Saved metrics

A saved metric is a bookmark for a specific metric configuration — including the metric itself, any filters applied, and the visualization type. Instead of re-configuring the same combination each time you add a widget, you save it once and select it from a list when building reports.

For example, you might save "Google Ads — Conversions (last 30 days, search campaigns only, displayed as KPI)" as a saved metric so you can drop it into any report in a few clicks.

### Create a saved metric

<Steps>
  <Step title="Open Metrics">
    Click **Metrics** in the left sidebar, then select the **Saved Metrics** tab.
  </Step>

  <Step title="Click New Saved Metric">
    Click **+ New Saved Metric**.
  </Step>

  <Step title="Choose the metric">
    Select the platform, then choose the metric you want to save from the dropdown.
  </Step>

  <Step title="Apply filters">
    Add any filters you want to lock in — for example, filtering by campaign type, device, or date range. Filters set here are applied every time this saved metric is used in a widget.
  </Step>

  <Step title="Choose a visualization type">
    Select the default visualization for this metric: **KPI**, **Line chart**, **Bar chart**, or **Table**.
  </Step>

  <Step title="Name and save">
    Enter a descriptive name and click **Save**.
  </Step>
</Steps>

### Use a saved metric when adding a widget

1. In the report builder, click **+ Add Widget**.
2. In the widget configuration panel, switch to the **Saved Metrics** tab.
3. Select the saved metric from the list. Oviond pre-fills the widget with the metric, filters, and visualization you defined.
4. Adjust any settings that need to differ for this specific widget, then click **Add Widget**.

***

## Custom data

Custom data lets you upload your own datasets into Oviond as data sources. This is useful for data that doesn't flow through any integration — such as offline conversions, manually tracked budget sheets, lead quality scores, or any other dataset your clients provide as a spreadsheet.

Each custom data source accepts up to **10,000 rows** per dataset. Once uploaded, a custom data source appears in the widget builder alongside your integration data, so you can visualize it in charts, tables, and KPI tiles.

### Upload a CSV as a custom data source

<Steps>
  <Step title="Open Metrics">
    Click **Metrics** in the left sidebar, then select the **Custom Data** tab.
  </Step>

  <Step title="Click New Custom Data">
    Click **+ New Custom Data**.
  </Step>

  <Step title="Name the dataset">
    Enter a name that identifies the dataset (for example, "Offline Conversions — Q1 2025" or "Monthly Budget Sheet").
  </Step>

  <Step title="Upload your CSV">
    Click **Upload CSV** and select your file. The CSV must include a header row. Oviond reads the column names from the header and uses them as the available fields in the widget builder.
  </Step>

  <Step title="Map column types">
    For each column, confirm or set the data type: **Text**, **Number**, **Date**, or **Currency**. Setting the correct type ensures Oviond can aggregate and visualize the data properly.
  </Step>

  <Step title="Save the data source">
    Click **Save**. The dataset is now available as a data source when building widgets.
  </Step>
</Steps>

<Note>
  Custom data sources support up to 10,000 rows per dataset. If your CSV exceeds this limit, split it into multiple files and upload each as a separate data source.
</Note>

### Edit a custom data source

To update the data in an existing custom data source — for example, to add new rows for the current month:

1. Go to **Metrics** > **Custom Data** and find the dataset.
2. Click the three-dot menu and select **Edit**.
3. Upload a new CSV to replace the existing data, or edit the column type mappings.
4. Click **Save**. Widgets using this data source update automatically.

### Delete a custom data source

<Warning>
  Deleting a custom data source permanently removes the dataset and disconnects any widgets that use it. Those widgets will stop displaying data. This cannot be undone.
</Warning>

1. Go to **Metrics** > **Custom Data**.
2. Click the three-dot menu next to the dataset and select **Delete**.
3. Confirm the deletion.

### Use custom data in a widget

1. In the report builder, click **+ Add Widget**.
2. In the widget configuration panel, open the **Data Source** dropdown and select your custom data source from the list (it appears under the **Custom Data** section).
3. Choose the columns you want to display or aggregate.
4. Configure the visualization and click **Add Widget**.
