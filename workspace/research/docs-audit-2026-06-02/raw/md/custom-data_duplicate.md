> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Duplicate Custom Data

> Copy a dataset under a new name.

Duplicating clones a Custom Data dataset — rows, columns, and metadata — under a new name. Useful for:

* Creating a variant with different filtering or data transformations applied downstream
* Forking a dataset before a risky update, so you can compare side-by-side
* Spinning up test data from a verified production dataset

<Steps>
  <Step title="Open Custom Data">
    From the sidebar.
  </Step>

  <Step title="Open the dataset's menu">
    Click the three-dot menu on the row.
  </Step>

  <Step title="Choose Duplicate">
    The copy appears in the list as `Copy of [original]`.
  </Step>

  <Step title="Rename">
    Open the copy and give it a meaningful name.
  </Step>
</Steps>

<Note>
  Widgets continue pointing at the original dataset — duplicating doesn't re-wire anything. If you want widgets to use the new dataset, open each widget and update its data source.
</Note>
