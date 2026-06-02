> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Custom Data

> Refresh a dataset by re-uploading its CSV.

Updating replaces the dataset's rows with a new CSV. The dataset's ID and widget bindings stay intact — every widget that references the dataset re-renders with the new data.

<Steps>
  <Step title="Open the dataset">
    Click the dataset name in the Custom Data list.
  </Step>

  <Step title="Click Re-upload CSV">
    Opens the file picker.
  </Step>

  <Step title="Select the new CSV">
    Oviond parses it and replaces the existing rows.
  </Step>

  <Step title="Save">
    Widgets using this dataset pick up the new data on next render.
  </Step>
</Steps>

<Note>
  The new CSV should use the **same column structure** as the original. If you add or rename columns, widgets configured against the old column names will need to be re-wired.
</Note>

## Rename without re-uploading

To just change the dataset's display name (leaving the rows intact), use **Rename** from the row's menu in the [List Custom Data](/custom-data/list) view.
