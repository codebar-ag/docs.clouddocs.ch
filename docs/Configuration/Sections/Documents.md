# 📄 Documents Configuration

This guide describes how to **generate and configure the JSON files** used to define **document sections**, including:

- Detail view display
- Table columns and filters

These configurations are stored as JSON and dynamically loaded by your application to build the **Documents UI**.

---

## 🗂️ JSON File Structure

Your configuration file includes two main sections:

- `show`: Controls the **detail view** of a document.
- `index`: Defines **table columns and filters** for listing documents.

Below is the overall structure:

```json
{
  "show": {
    "title_identifier": "TITLE",
    "subtitle_identifier": "DOCUMENT_TYPE",
    "infolist": {
      "enabled": true,
      "collapsed_by_default": true,
      "entries": [ /* Array of infolist fields */ ]
    }
  },
  "index": {
    "table": {
      "columns": [ /* Array of table columns */ ],
      "filters": [ /* Array of table filters */ ]
    }
  }
}
```

Each array (`entries`, `columns`, `filters`) contains field definitions as described below.

---

## ✨ Field Properties

### Common Field Properties

All fields (infolist entries, table columns, filters) can define:

| Property      | Type                 | Description                                                  |
|---------------|----------------------|--------------------------------------------------------------|
| `type`        | `string`             | Field type (see [Supported Types](#supported-types)).       |
| `label`       | `object` or `string` | Field label (plain string or translations).                 |
| `identifier`  | `string`             | Unique field key (must match your data source).             |
| `sortable`    | `boolean`            | *(Columns only)* Whether the column is sortable.            |
| `multiple`    | `boolean`            | *(Filters only)* Whether multiple values can be selected.   |
| `default`     | `array` or `object`  | *(Filters only)* Default selected values or range.          |

---

## 📘 Supported Types

| Type       | Usage             | Notes                                          |
|------------|-------------------|------------------------------------------------|
| `string`   | Columns, Filters  | Displays as plain text.                        |
| `date`     | Columns, Filters  | Displays date in `d.m.Y` format.               |
| `integer`  | Infolist          | Displays numeric values.                       |
| `textarea` | Infolist          | Shows longer text fields.                      |
| `select`   | Filters           | Renders dropdown with selectable options.      |

---

## 🖥️ `index.table.columns`

Defines **table columns** shown in the documents list.

### Example

```json
"columns": [
  {
    "type": "string",
    "label": {
      "en_CH": "Type",
      "de_CH": "Typ"
    },
    "sortable": true,
    "identifier": "DOCUMENT_TYPE"
  },
  {
    "type": "date",
    "label": "Date",
    "sortable": true,
    "identifier": "DOCUMENT_DATE"
  },
  {
    "type": "string",
    "label": "Subject",
    "sortable": false,
    "identifier": "TITLE"
  }
]
```

---

## 🗄️ `index.table.filters`

Defines **filters applied to the document list**.

### Example

```json
"filters": [
  {
    "type": "select",
    "label": {
      "en_CH": "Type",
      "de_CH": "Typ"
    },
    "default": ["Sonstiges", "contract"],
    "multiple": true,
    "identifier": "DOCUMENT_TYPE"
  },
  {
    "type": "date",
    "label": "Date",
    "default": {
      "from": "2020-01-01",
      "to": "2024-12-31"
    },
    "identifier": "DOCUMENT_DATE"
  }
]
```

---

### Filter Behavior

#### Select Filters
- If `multiple` is `true`, users can pick several options.
- If `options` are omitted, unique values are auto-detected.

#### Date Filters
- Renders a date range picker.
- Filters records between `from` and `to` dates.

---

## 📝 `show.infolist.entries`

Defines **read-only fields shown in the detail view** of a document.

### Example

```json
"infolist": {
  "enabled": true,
  "collapsed_by_default": true,
  "entries": [
    {
      "type": "date",
      "label": "Date",
      "identifier": "DOCUMENT_DATE"
    },
    {
      "type": "integer",
      "label": "Year",
      "identifier": "YEAR"
    },
    {
      "type": "string",
      "label": "Subject",
      "identifier": "TITLE"
    },
    {
      "type": "textarea",
      "label": "Description",
      "identifier": "DESCRIPTION"
    }
  ]
}
```

---

## 🧩 Label Translation

For `label`, you can provide either:

- A **string** (e.g., `"Date"`)
- An **object with translations**:

```json
"label": {
  "en_CH": "Date",
  "de_CH": "Datum"
}
```

The user’s locale determines which label is shown.

---

## 🛠️ Full Example Configuration

Below is a **complete example JSON** combining all sections:

```json
{
  "show": {
    "title_identifier": "TITLE",
    "subtitle_identifier": "DOCUMENT_TYPE",
    "infolist": {
      "enabled": true,
      "collapsed_by_default": true,
      "entries": [
        {
          "type": "date",
          "label": "Date",
          "identifier": "DOCUMENT_DATE"
        },
        {
          "type": "integer",
          "label": "Year",
          "identifier": "YEAR"
        },
        {
          "type": "string",
          "label": "Subject",
          "identifier": "TITLE"
        },
        {
          "type": "textarea",
          "label": "Description",
          "identifier": "DESCRIPTION"
        }
      ]
    }
  },
  "index": {
    "table": {
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
        },
        {
          "type": "string",
          "label": "Subject",
          "sortable": false,
          "identifier": "TITLE"
        }
      ],
      "filters": [
        {
          "type": "select",
          "label": "Type",
          "default": ["Sonstiges", "contract"],
          "multiple": true,
          "identifier": "DOCUMENT_TYPE"
        },
        {
          "type": "date",
          "label": "Date",
          "default": {
            "from": "2020-01-01",
            "to": "2024-12-31"
          },
          "identifier": "DOCUMENT_DATE"
        }
      ]
    }
  }
}
```

---

## 🪧 Additional Notes

- If `infolist.enabled` is `false`, the detail sidebar is hidden.
- `sortable` is optional; default is `false`.
- The `identifier` must match your data keys exactly.
