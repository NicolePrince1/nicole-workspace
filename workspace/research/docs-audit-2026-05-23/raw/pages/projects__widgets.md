> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Widgets

> Charts, KPI tiles, tables, and text blocks that populate every page.

A **widget** is an individual visualization on a page. Each widget connects to a data source and displays one metric or breakdown.

## Widget types

| Type            | Use for                                                           |
| --------------- | ----------------------------------------------------------------- |
| **KPI tile**    | A single headline metric, optional period-over-period comparison. |
| **Chart**       | Trends over time — line, bar, or area.                            |
| **Table**       | Multiple metrics or dimensions side by side.                      |
| **Pie / donut** | Breakdown of a metric by dimension (e.g. traffic by source).      |
| **Text block**  | Freeform text — headings, commentary, summaries.                  |
| **Image**       | Inline images from the Media library or a URL.                    |
| **Embed**       | Embed any iframe-compatible source.                               |
| **Goal**        | Progress bar toward a target value.                               |
| **Button**      | A CTA link (e.g. to a booking page).                              |

## Add a widget

<Steps>
  <Step title="Select the page">
    Click the page tab you want to add the widget to.
  </Step>

  <Step title="Open the widget panel">
    Click **+ Add Widget** in the toolbar.
  </Step>

  <Step title="Choose the type">
    Pick KPI, Chart, Table, etc.
  </Step>

  <Step title="Pick a data source">
    Choose the [Data Source](/data-sources/list) the widget pulls from. Only sources connected to this client are available.
  </Step>

  <Step title="Pick a metric">
    Select the metric (and optional dimension).
  </Step>

  <Step title="Set the date range">
    Fixed or relative (e.g. *Last 30 Days*) — relative ranges auto-update whenever the report is viewed.
  </Step>

  <Step title="Add to the page">
    Click **Add**. The widget appears on the canvas.
  </Step>
</Steps>

## Configure a widget

Click any widget to open its settings panel on the right:

* **Data source / metric / dimension** — swap what the widget displays.
* **Date range** — override the project-level default for this widget.
* **Chart type** — switch visualizations without losing your data config.
* **Appearance** — title, colors, per-type display options.

## Rearrange and resize

Widgets use a drag-and-drop grid:

* **Move** — drag the widget header to a new position.
* **Resize** — drag the corner handle. Widgets snap to the grid.

## Bulk delete widgets

Hold **Shift** and click each widget to multi-select, then click **Delete selected** in the toolbar.

## Saving

Oviond uses an atomic save — **every page and every widget in the project** is saved in one operation. Click **Save** in the top-right of the editor before leaving.

<Warning>
  Navigating away without saving loses every unsaved widget change. Always save first.
</Warning>
