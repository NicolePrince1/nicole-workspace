> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rename Media

> Change the display name of a media file.

Renaming a media item updates its display name only. The underlying S3 file keeps the same URL — widgets referencing the item don't need to be re-wired.

<Steps>
  <Step title="Open Media">
    From the left sidebar.
  </Step>

  <Step title="Open the item's menu">
    Click the three-dot menu on the tile.
  </Step>

  <Step title="Choose Rename">
    Type the new name and press **Enter**.
  </Step>
</Steps>

## What rename changes

* The display name shown in the library, in the widget picker, and in search.

## What rename doesn't change

* The file's URL (the S3 key is immutable).
* Any existing widget that references the file — it keeps working.
* The file size or mime type.

<Tip>
  Use consistent naming — e.g. `client-logo-acme.svg`, `client-logo-contoso.svg` — to make search and folder organization easier as your library grows.
</Tip>
