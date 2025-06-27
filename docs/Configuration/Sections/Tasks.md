# 📝 Tasks Configuration

This guide describes how to **generate and configure the JSON files** used to define **tasks sections**, including:

- Detail view metadata
- Editable fields
- File upload configuration
- List (index) columns

These configurations are typically stored in JSON files and loaded dynamically by your application to build the **Tasks UI**.

---

## 🗂️ JSON File Structure

Your configuration file includes two main sections:

- `show`: Controls **detail view**, form fields, and uploads.
- `index`: Defines **table columns** when listing tasks.

Below is the overall structure:

```json
{
  "show": {
    "title_identifier": "TITLE",
    "subtitle_identifier": "DOCUMENT_TYPE",
    "infolist": {
      "enabled": true,
      "entries": [ /* Array of infolist fields */ ],
      "collapsed_by_default": true
    },
    "form": {
      "collapsed_by_default": true,
      "fields": [ /* Array of form fields */ ]
    },
    "uploads": {
      "enabled": true,
      "collapsed_by_default": true,
      "form": {
        "providable": {
          "vault_guid": null
        },
        "fields": [ /* Array of upload fields */ ]
      },
      "rules": [ /* Array of upload validation rules */ ]
    }
  },
  "index": {
    "table": {
      "columns": [ /* Array of table columns */ ]
    }
  }
}
```

Each array (`entries`, `fields`, `columns`) contains field definitions, described in detail below.

---

## ✨ Field Properties

### Common Field Properties

Every field (infolist entry, form field, upload field, column) can define:

| Property      | Type                 | Description                                                  |
|---------------|----------------------|--------------------------------------------------------------|
| `type`        | `string`             | Field type (see [Supported Types](#supported-types)).       |
| `label`       | `object` or `string` | Field label (plain string or translations).                 |
| `identifier`  | `string`             | Unique field key (matches your data source).                |
| `rules`       | `array`              | *(Form/Upload only)* Validation rules (e.g., `["nullable","max:512"]`). |
| `value`       | `string` or `boolean`| *(Upload only)* Default value or `true` to auto-fill.       |

---

## 📘 Supported Types

| Type       | Usage             | Notes                                          |
|------------|-------------------|------------------------------------------------|
| `string`   | All sections      | Displays as plain text or input field.         |
| `textarea` | Form, Infolist    | For longer text, description, or comments.     |
| `integer`  | Infolist, Columns | Displays as numeric value.                     |
| `date`     | All sections      | Displays or edits date.                        |
| `hidden`   | Upload fields     | Hidden field with static value.                |

---

## 🖥️ `index.table.columns`

Defines **table columns** shown in the tasks list.

### Example

```json
"columns": [
  {
    "type": "string",
    "label": {
      "en_CH": "Type",
      "de_CH": "Typ"
    },
    "identifier": "DOCUMENT_TYPE"
  },
  {
    "type": "date",
    "label": "Date",
    "identifier": "DOCUMENT_DATE"
  },
  {
    "type": "string",
    "label": "Subject",
    "identifier": "TITLE"
  },
  {
    "type": "date",
    "label": "Deadline",
    "identifier": "DEADLINE_DATE"
  }
]
```

---

## 📝 `show.infolist.entries`

Defines **read-only fields** shown in the detail view sidebar.

### Example

```json
"infolist": {
  "enabled": true,
  "collapsed_by_default": true,
  "entries": [
    {
      "type": "string",
      "label": "Type",
      "identifier": "DOCUMENT_TYPE"
    },
    {
      "type": "date",
      "label": "Date",
      "identifier": "DOCUMENT_DATE"
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
    },
    {
      "type": "date",
      "label": "Deadline",
      "identifier": "DEADLINE_DATE"
    }
  ]
}
```

---

## ✏️ `show.form.fields`

Defines **editable fields** when updating a task (e.g., comment).

### Example

```json
"form": {
  "collapsed_by_default": true,
  "fields": [
    {
      "type": "textarea",
      "label": "Comment",
      "rules": [
        "nullable",
        "string",
        "max:512"
      ],
      "identifier": "COMMENT"
    }
  ]
}
```

---

## 📤 `show.uploads`

Controls **file uploads associated with a task**.

### Properties

| Property              | Type     | Description                                  |
|-----------------------|----------|----------------------------------------------|
| `enabled`             | `boolean`| Whether uploads are enabled.                 |
| `collapsed_by_default`| `boolean`| Whether upload form is collapsed by default. |
| `form`                | `object` | Defines upload fields.                       |
| `rules`               | `array`  | Validation rules for uploads.               |

---

### Example

```json
"uploads": {
  "enabled": true,
  "collapsed_by_default": true,
  "form": {
    "providable": {
      "vault_guid": null
    },
    "fields": [
      {
        "type": "string",
        "label": "Subject",
        "rules": [
          "nullable",
          "string",
          "max:254"
        ],
        "value": true,
        "identifier": "TITLE"
      },
      {
        "type": "textarea",
        "label": "Comment",
        "rules": [
          "nullable",
          "string",
          "max:512"
        ],
        "value": true,
        "identifier": "COMMENT"
      },
      {
        "type": "hidden",
        "label": "Client Key",
        "rules": [],
        "value": "{{CLIENT_KEY}}",
        "identifier": "CLIENT_KEY"
      },
      {
        "type": "hidden",
        "label": "UUID",
        "rules": [],
        "value": "{{UUID}}",
        "identifier": "UUID"
      }
    ]
  },
  "rules": [
    "required",
    "min:1",
    "max:5"
  ]
}
```

---

## 🧩 Label Translation

For `label`, you can provide either:

- A **string** (e.g., `"Subject"`)
- An **object with translations**:

```json
"label": {
  "en_CH": "Subject",
  "de_CH": "Betrteff"
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
    "subtitle_identifier": null,
    "infolist": {
      "enabled": true,
      "collapsed_by_default": true,
      "entries": [
        {
          "type": "string",
          "label": "Type",
          "identifier": "DOCUMENT_TYPE"
        },
        {
          "type": "date",
          "label": "Date",
          "identifier": "DOCUMENT_DATE"
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
        },
        {
          "type": "date",
          "label": "Deadline",
          "identifier": "DEADLINE_DATE"
        }
      ]
    },
    "form": {
      "collapsed_by_default": true,
      "fields": [
        {
          "type": "textarea",
          "label": "Comment",
          "rules": ["nullable", "string", "max:512"],
          "identifier": "COMMENT"
        }
      ]
    },
    "uploads": {
      "enabled": true,
      "collapsed_by_default": true,
      "form": {
        "providable": {
          "vault_guid": null
        },
        "fields": [
          {
            "type": "string",
            "label": "Subject",
            "rules": ["nullable", "string", "max:254"],
            "value": true,
            "identifier": "TITLE"
          },
          {
            "type": "textarea",
            "label": "Comment",
            "rules": ["nullable", "string", "max:512"],
            "value": true,
            "identifier": "COMMENT"
          },
          {
            "type": "hidden",
            "label": "Client Key",
            "rules": [],
            "value": "{{CLIENT_KEY}}",
            "identifier": "CLIENT_KEY"
          },
          {
            "type": "hidden",
            "label": "UUID",
            "rules": [],
            "value": "{{UUID}}",
            "identifier": "UUID"
          }
        ]
      },
      "rules": ["required", "min:1", "max:5"]
    }
  },
  "index": {
    "table": {
      "columns": [
        {
          "type": "string",
          "label": "Type",
          "identifier": "DOCUMENT_TYPE"
        },
        {
          "type": "date",
          "label": "Date",
          "identifier": "DOCUMENT_DATE"
        },
        {
          "type": "string",
          "label": "Subject",
          "identifier": "TITLE"
        },
        {
          "type": "date",
          "label": "Deadline",
          "identifier": "DEADLINE_DATE"
        }
      ]
    }
  }
}
```

---

## 🪧 Additional Notes

- If `uploads.enabled` is `false`, the upload section is hidden.
- If a `form` field has validation `rules`, they apply when saving.
- The `identifier` must exactly match the data keys.
