# Providers Configuration

This guide describes how to **generate and configure the provider JSON file** for importing files and metadata.

---

## JSON File Structure

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

| Property                        | Type       | Description                                                    |
|---------------------------------|------------|----------------------------------------------------------------|
| `storage_path`                  | `string`   | Source storage path or identifier.                             |
| `files_filter_exclude`          | `string[]` | Extensions to exclude.                                         |
| `fields_filter`                 | `string[]` | Metadata fields to include.                                    |
| `section_fields_filter_exclude` | `string[]` | Fields to exclude from section context.                        |
| `item_identifier`               | `string`   | Unique field key for identifying items.                        |
| `target_identifier`             | `string`   | Target storage identifier.                                     |

---

## Example

```json
{
  "storage_path": "vault-uuid",
  "files_filter_exclude": [
    "txt"
  ],
  "fields_filter": [
    "TITLE",
    "DOCUMENT_DATE",
    "CLIENT"
  ],
  "section_fields_filter_exclude": [
    "CLIENT"
  ],
  "item_identifier": "DWDOCID",
  "target_identifier": "vault-uuid"
}
```

---

## Best Practices

- Keep `fields_filter` minimal.
- Use a stable `item_identifier`.
- Make sure `target_identifier` matches your storage.
- Make sure the values in `section_fields_filter_exclude` are also defined in `fields_filter`.

---
