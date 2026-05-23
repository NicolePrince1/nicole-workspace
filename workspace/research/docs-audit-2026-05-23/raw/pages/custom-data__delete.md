> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Custom Data

> Permanently remove an uploaded CSV dataset.

Deleting a dataset removes its rows and the dataset metadata. Widgets that referenced the dataset show *Data source unavailable* until re-wired to a different source.

<Warning>
  Deletion is permanent — there's no Archive recovery for Custom Data. Download the CSV back from the dataset preview first if you want a backup.
</Warning>

<Steps>
  <Step title="Open Custom Data">
    From the sidebar.
  </Step>

  <Step title="Open the dataset's menu">
    Click the three-dot menu.
  </Step>

  <Step title="Choose Delete">
    Confirm when prompted.
  </Step>
</Steps>

## If the dataset is in use

Oviond warns you if the dataset is referenced by any active widget before deletion. Review the list of dependent widgets — you may want to swap their data source first rather than leaving broken widgets.
