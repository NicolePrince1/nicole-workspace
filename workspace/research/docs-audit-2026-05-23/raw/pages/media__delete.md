> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Media

> Soft-delete a single media item with restore available from the Archive.

Deleting a single media item removes it from the active library and moves it to the [Archive](/archive/view). The underlying S3 file is retained for the restore window — nothing is permanently destroyed at this step.

<Steps>
  <Step title="Open Media">
    From the left sidebar.
  </Step>

  <Step title="Open the item's menu">
    Click the three-dot menu on the tile.
  </Step>

  <Step title="Choose Delete">
    Confirm when prompted. The item disappears from the library.
  </Step>
</Steps>

## What widgets see

Widgets that referenced the deleted item show a broken-image placeholder with a **Missing Media** badge. Options:

* [Restore](/archive/restore) the item from the Archive — the widget re-renders cleanly.
* Edit the widget and pick a different media item.

## Retention

Archived media items older than the retention window (90 days by default) are **permanently purged**, including the S3 file. Restore before then if you want to keep it.
