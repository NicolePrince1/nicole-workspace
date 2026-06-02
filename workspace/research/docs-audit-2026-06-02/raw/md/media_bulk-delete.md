> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Delete

> Soft-delete multiple media items at once.

Bulk delete is the fastest way to clean up leftover screenshots, duplicate uploads, or files from an offboarded client.

<Warning>
  Deleted media items are **soft-deleted** — the S3 file stays in place and the row is retained until the retention window expires. Widgets that reference a deleted item will show a broken image until the item is restored or re-wired to a different file. Review widget references first if you're removing a file currently in use.
</Warning>

<Steps>
  <Step title="Open Media">
    From the left sidebar.
  </Step>

  <Step title="Enter selection mode">
    Hover a tile and click the checkbox that appears, or toggle **Select** mode in the toolbar.
  </Step>

  <Step title="Pick the items">
    Check every media item you want to delete. Select-all works per folder view.
  </Step>

  <Step title="Delete">
    Click **Delete selected** in the action bar. Items move to the Archive.
  </Step>
</Steps>

## Undo a bulk delete

From the [Archive](/archive/view), filter to **Media**, select the items you just deleted, and click **Restore**. They reappear in the Media library with their original names and folders.
