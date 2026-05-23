> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload Media

> Upload images and files into the Oviond Media library.

The **Media library** is where every image, logo, icon, and file referenced from widgets, reports, and share pages lives. Uploads go straight to S3-backed storage — Oviond generates a pre-signed URL, the file uploads directly from your browser, and the metadata row is committed once upload finishes.

<Steps>
  <Step title="Open the Media library">
    Click **Media** in the left sidebar.
  </Step>

  <Step title="Click Upload">
    Opens a file picker — or drag files straight onto the Media grid.
  </Step>

  <Step title="Pick files">
    Images (PNG, JPG, SVG, WebP) and common file types are all supported. Multi-select works — every file uploads in parallel.
  </Step>

  <Step title="Optional: drop into a folder">
    If you opened Media from inside a folder, uploads land in that folder. Otherwise they go to the unorganized pool.
  </Step>
</Steps>

## Supported formats

| Type     | Formats                  |
| -------- | ------------------------ |
| Image    | PNG, JPG, SVG, WebP, GIF |
| Document | PDF                      |

## Size limits

Individual files up to **25 MB**. For larger uploads, chunk them or host externally and reference the URL directly from the widget.

<Tip>
  For logos and branding, prefer **SVG** — they stay crisp at every report resolution and render cleanly in PDF export.
</Tip>
