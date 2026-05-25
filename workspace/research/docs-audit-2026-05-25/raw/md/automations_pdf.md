> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# PDF Export

> Generate a PDF from a report — on demand or attached to an automation.

Oviond can render any report as a PDF — either exported on demand from the report view, or delivered automatically as an email attachment via an automation. PDF generation runs asynchronously in the background, so large reports don't block your browser.

## On-demand PDF export

<Steps>
  <Step title="Open the report">
    Navigate to the project you want to export.
  </Step>

  <Step title="Click Export">
    In the top toolbar, click **Export → PDF**. Oviond queues the PDF generation job.
  </Step>

  <Step title="Download">
    When the PDF is ready, Oviond notifies you with a download link. Generation typically takes 15–60 seconds depending on report size.
  </Step>
</Steps>

## PDF settings

Configure PDF layout per project in **Project Settings → PDF**:

| Setting              | Options             |
| -------------------- | ------------------- |
| Page size            | A4, Letter, Legal   |
| Orientation          | Portrait, Landscape |
| Cover page           | On / Off            |
| Include page numbers | On / Off            |

<Tip>
  Landscape orientation works best for wide tables and multi-column chart layouts.
</Tip>

## Automated PDF delivery

To send PDFs on a recurring schedule, create an automation and select **PDF attachment** as the delivery method. See [Scheduled Reports](/automations/scheduled) for the full setup steps.

## Troubleshooting

**Widgets appear cut off** — Switch to landscape orientation or reduce the number of columns in your layout.

**Images or logos missing** — Ensure all image URLs in your report are publicly accessible. Private or expired URLs won't render in PDF.

**PDF generation times out** — Very large reports with many widgets can occasionally time out. Try splitting the report across multiple pages.
