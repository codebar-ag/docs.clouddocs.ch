# Providers Configuration

This guide describes how to **generate and configure the provider JSON file**, which controls **import behavior**, including file filtering, field selection, and unique identification of items during import.

This configuration is consumed internally by processes like the `ItemsSyncJob` (or equivalent services).  
It allows your application to **automate importing and associating files and metadata** from external sources into your storage or database.

> **Note:** This configuration must be stored as JSON and passed into your application logic wherever you define import sources.

---

## JSON File Structure

Your configuration file follows this structure:

```json
{
  "storage_path": "string",
  "files_filter_exclude": ["string", "..."],
  "fields_filter": ["string", "..."],
  "section_fields_filter_exclude": ["string", "..."],
  "item_identifier": "string",
  "target_identifier": "string"
}
```

---

## Properties

| Property                        | Type       | Description                                                                                                                                              |
|---------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `storage_path`                  | `string`   | The **unique identifier or path to the source storage** (e.g., an external vault or file repository).                                                    |
| `files_filter_exclude`          | `string[]` | List of **file extensions** to exclude before processing (e.g., `["txt", "csv"]`). This filtering happens early, so excluded files are ignored entirely. |
| `fields_filter`                 | `string[]` | List of **metadata fields to extract** for each file or record. Only the fields listed here are included in the resulting dataset.                       |
| `section_fields_filter_exclude` | `string[]` | List of fields to **omit when associating the item with a section** (e.g., client identifiers that shouldn't be attached at the section level).          |
| `item_identifier`               | `string`   | The **unique field key** that identifies each imported item. This is used to detect duplicates or updates during synchronization.                        |
| `target_identifier`             | `string`   | The identifier of the **target storage location** where the processed data and files will be saved.                                                      |

---

## How It Works

1. **Source Resolution**
   - The `storage_path` is used to locate and connect to the external system or vault containing files.

2. **File Filtering**
   - `files_filter_exclude` is applied to skip files with excluded extensions **before any metadata is loaded**.

3. **Metadata Extraction**
   - For each file, metadata fields are loaded.
   - `fields_filter` determines which metadata keys are included.
   - Any field not listed in `fields_filter` is discarded.

4. **Section Association**
   - When linking files to sections (for example, documents or tasks), the system removes any keys in `section_fields_filter_exclude` from the item metadata **only for the section context**.

5. **Identification and Deduplication**
   - `item_identifier` is used to provide a unique reference to the external data.

6. **Target Storage**
   - `target_identifier` tells the system where to store:
      - The file itself.
      - The final metadata.

---

## Example Configuration (Tasks)

Below is an example for importing **Tasks**:

```json
{
  "storage_path": "fb510539-5efb-4c4b-8f0b-2fa529d7b590",
  "files_filter_exclude": ["txt"],
  "fields_filter": [
    "DWDOCID",
    "SECTION",
    "STATUS",
    "TITLE",
    "DOCUMENT_DATE",
    "COMMENT",
    "DOCUMENT_TYPE",
    "CLOUD_DOCS_ENABLED",
    "CLIENT",
    "CLIENT_KEY",
    "DEADLINE_DATE"
  ],
  "section_fields_filter_exclude": [
    "CLOUD_DOCS_ENABLED",
    "CLIENT",
    "CLIENT_KEY"
  ],
  "item_identifier": "DWDOCID",
  "target_identifier": "fb510539-5efb-4c4b-8f0b-2fa529d7b590"
}
```

---

## Multiple Providers

You can create separate JSON configuration files for different data sources or purposes. For example:

- `dw_immo_demo_import_providers_tasks.json`
- `dw_immo_demo_import_providers_documents.json`

---

## Best Practices

- **Keep `fields_filter` minimal:** Only include fields you need.
- **Use clear `item_identifier` values:** Choose stable, unique keys.
- **Ensure `target_identifier` matches your storage strategy:** For example, to separate documents and tasks.

---

## Quick Start Checklist

- Create a JSON file for each provider.
- Define `storage_path` to locate the source files.
- Add `files_filter_exclude` to skip unwanted files.
- Specify `fields_filter` with the metadata keys to import.
- Optionally define `section_fields_filter_exclude`.
- Set `item_identifier` for uniqueness.
- Set `target_identifier` for target storage.
