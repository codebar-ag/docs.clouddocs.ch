# Documents Configuration

This guide describes how to **generate and configure the JSON files** used to define **document sections**, including:

- Detail view display
- Table columns and filters

---

## JSON File Structure

```json
{
  "show": {
    "title_identifier": "TITLE",
    "subtitle_identifier": "DOCUMENT_TYPE",
    "infolist": {
      "enabled": true,
      "collapsed_by_default": true,
      "entries": [ /* Fields */ ]
    }
  },
  "index": {
    "table": {
      "columns": [ /* Columns */ ],
      "filters": [ /* Filters */ ]
    }
  }
}
```

---

## Top-Level Properties

| Property                             | Type      | Description                                                          |
|--------------------------------------|-----------|----------------------------------------------------------------------|
| `show`                               | `object`  | Detail view configuration.                                           |
| `show.title_identifier`              | `string`  | Main title field.                                                    |
| `show.subtitle_identifier`           | `string`  | Subtitle field.                                                      |
| `show.infolist`                      | `object`  | Sidebar fields.                                                      |
| `show.infolist.enabled`              | `boolean` | Whether the sidebar is shown.                                        |
| `show.infolist.collapsed_by_default` | `boolean` | Whether the sidebar starts collapsed.                                |
| `show.infolist.entries`              | `array`   | Fields in the infolist.                                              |
| `index`                              | `object`  | List view configuration.                                             |
| `index.table.columns`                | `array`   | Table columns.                                                       |
| `index.table.filters`                | `array`   | Table filters.                                                       |

---

## Field Properties

| Property     | Type                  | Description                             |
|--------------|-----------------------|-----------------------------------------|
| `type`       | `string`              | Field type.                             |
| `label`      | `string` or `object`  | Label (string or translations).         |
| `identifier` | `string`              | Unique field key.                       |
| `sortable`   | `boolean`             | Enable sorting (columns only).          |
| `multiple`   | `boolean`             | Allow multiple selection (filters).     |
| `default`    | `array` or `object`   | Default values for filters.             |

---

## Supported Field Types

| Type       | Notes                    |
|------------|--------------------------|
| `string`   | Text.                    |
| `integer`  | Numeric.                 |
| `date`     | Date `d.m.Y`.            |
| `textarea` | Multiline text.          |
| `select`   | Dropdown (filters only). |

---

## Label Translation

Same as Uploads—see example above.

---

## `index.table.columns` Example

```json
"columns": [
  {
    "type": "string",
    "label": "Type",
    "sortable": true,
    "identifier": "DOCUMENT_TYPE"
  },
  {
    "type": "date",
    "label": "Date",
    "sortable": true,
    "identifier": "DOCUMENT_DATE"
  }
]
```

---

## `index.table.filters` Example

```json
"filters": [
  {
    "type": "select",
    "label": "Type",
    "default": ["Contract"],
    "multiple": true,
    "identifier": "DOCUMENT_TYPE"
  },
  {
    "type": "date",
    "label": "Date",
    "default": { "from": "2022-01-01", "to": "2022-12-31" },
    "identifier": "DOCUMENT_DATE"
  }
]
```

---

## `show.infolist.entries` Example

```json
"entries": [
  {
    "type": "date",
    "label": "Date",
    "identifier": "DOCUMENT_DATE"
  },
  {
    "type": "string",
    "label": "Subject",
    "identifier": "TITLE"
  }
]
```

---

## Additional Notes

- `sortable` is optional.
- `identifier` must match data keys.
