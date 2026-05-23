> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Permanently Delete

> Remove archived items from your account forever.

Permanently deleting an archived item is **irreversible** — the row is removed from the database along with all its children (a client's projects, a project's widgets, etc). Use it to:

* Free up plan quota immediately rather than waiting for the retention window
* Remove sensitive data after a client requests GDPR/CCPA erasure
* Clean up test data with certainty

<Warning>
  There is no undo. Once an item is permanently deleted, it cannot be recovered — not even by Oviond support.
</Warning>

<Steps>
  <Step title="Open Archive">
    From **Account → Archive**.
  </Step>

  <Step title="Filter and select">
    Narrow to the type you want to purge, then check each item.
  </Step>

  <Step title="Click Permanently Delete">
    Confirm by typing a verification word when prompted.
  </Step>
</Steps>

## Automatic purge

Archived items older than the retention window (90 days by default) are **automatically purged** by a background job. You don't need to manually delete them — they're cleaned up periodically on Oviond's end.
