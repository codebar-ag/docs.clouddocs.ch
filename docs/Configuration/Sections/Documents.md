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

---

## ✨ Top-Level Properties

| Property                             | Type      | Description                                                          |
|--------------------------------------|-----------|----------------------------------------------------------------------|
| `show`                               | `object`  | Defines the **detail view configuration** for individual records.    |
| `show.title_identifier`              | `string`  | Field used as the main title in the detail view.                     |
| `show.subtitle_identifier`           | `string`  | Field used as the subtitle in the detail view.                       |
| `show.infolist`                      | `object`  | Defines which fields are shown in the sidebar.                       |
| `show.infolist.enabled`              | `boolean` | Whether the infolist sidebar is shown.                               |
| `show.infolist.collapsed_by_default` | `boolean` | Whether the infolist starts collapsed.                               |
| `show.infolist.entries`              | `array`   | Array of fields displayed in the infolist.                           |
| `index`                              | `object`  | Defines the **list view configuration** (table columns and filters). |
| `index.table`                        | `object`  | Table configuration object.                                          |
| `index.table.columns`                | `array`   | Array of table columns.                                              |
| `index.table.filters`                | `array`   | Array of filters applied to the list.                                |

> **Tip:** For supported field types, filters, label translations, and validation rules, see [Shared Configurations](./SharedConfigurations.md).

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

> See [Shared Configurations](./SharedConfigurations.md) for filter types, behaviors, and examples.

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
- `collapsed_by_default` controls whether the sidebar is initially expanded.
- `sortable` is optional; default is `false`.
- The `identifier` must match your data keys exactly.
- For supported field types, filters, label translations, and validation rules, see [Shared Configurations](./SharedConfigurations.md).
