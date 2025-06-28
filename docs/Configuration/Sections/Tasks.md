# Tasks Configuration

This guide describes how to **generate and configure the JSON files** used to define **tasks sections**, including:

- Detail view metadata
- Editable fields
- File upload configuration
- List (index) columns

These configurations are typically stored in JSON files and loaded dynamically by your application to build the **Tasks UI**.

---

## JSON File Structure

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
      "collapsed_by_default": true,
      "entries": [ /* Array of infolist fields */ ]
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
      "columns": [ /* Array of table columns */ ],
      "filters": [ /* Array of table filters */ ]
    }
  }
}
```

---

## Top-Level Properties

| Property                             | Type      | Description                                                          |
|--------------------------------------|-----------|----------------------------------------------------------------------|
| `show`                               | `object`  | Defines the **detail view configuration** for individual records.    |
| `show.title_identifier`              | `string`  | Field used as the main title in the detail view.                     |
| `show.subtitle_identifier`           | `string`  | Field used as the subtitle in the detail view.                       |
| `show.infolist`                      | `object`  | Defines which fields are shown in the sidebar.                       |
| `show.infolist.enabled`              | `boolean` | Whether the infolist sidebar is shown.                               |
| `show.infolist.collapsed_by_default` | `boolean` | Whether the infolist starts collapsed.                               |
| `show.infolist.entries`              | `array`   | Array of fields displayed in the infolist.                           |
| `show.form`                          | `object`  | Defines editable fields for the detail form.                         |
| `show.form.collapsed_by_default`     | `boolean` | Whether the form is collapsed initially.                             |
| `show.form.fields`                   | `array`   | Array of editable form fields.                                       |
| `show.uploads`                       | `object`  | Defines upload behavior and fields.                                  |
| `show.uploads.enabled`               | `boolean` | Whether uploads are allowed.                                         |
| `show.uploads.collapsed_by_default`  | `boolean` | Whether the upload form is collapsed initially.                      |
| `show.uploads.form`                  | `object`  | Upload form configuration.                                           |
| `show.uploads.form.fields`           | `array`   | Array of fields shown in the upload form.                            |
| `show.uploads.rules`                 | `array`   | Validation rules for the uploaded files array.                       |
| `index`                              | `object`  | Defines the **list view configuration** (table columns and filters). |
| `index.table`                        | `object`  | Table configuration object.                                          |
| `index.table.columns`                | `array`   | Array of table columns.                                              |
| `index.table.filters`                | `array`   | Array of filters applied to the list.                                |

---

## Field Properties

All field definitions—whether for columns, filters, infolist entries, or form fields—support the following properties:

| Property     | Type                  | Description                                                  |
|--------------|-----------------------|--------------------------------------------------------------|
| `type`       | `string`              | Field type (see Supported Field Types below).                |
| `label`      | `string` or `object`  | Field label (plain string or translations).                  |
| `identifier` | `string`              | Unique field key.                                            |
| `sortable`   | `boolean`             | *(Columns only)* Enable sorting.                             |
| `multiple`   | `boolean`             | *(Select filters only)* Allow multiple selections.           |
| `default`    | `array` or `object`   | *(Filters only)* Default selected values or ranges.          |
| `rules`      | `array`               | *(Forms/Uploads only)* Validation rules.                     |
| `value`      | `string` or `boolean` | *(Forms/Uploads only)* Default value or `true` to auto-fill. |

---

## Supported Field Types

Below is the list of supported `type` values across all sections:

| Type       | Where Used                 | Notes                                      |
|------------|----------------------------|--------------------------------------------|
| `string`   | Columns, Filters, Forms    | Standard text.                             |
| `integer`  | Columns, Infolist          | Numeric values.                            |
| `date`     | Columns, Filters, Infolist | Dates formatted as `d.m.Y`.                |
| `select`   | Filters                    | Dropdown selection.                        |
| `textarea` | Infolist, Forms            | Longer text (description, comments).       |
| `hidden`   | Forms, Uploads             | Hidden field with static or dynamic value. |

---

## Label Translation

Labels (`label`) support multilingual configurations:

**String example:**

```json
"label": "Subject"
```

**Translation example:**

```json
"label": {
  "en_CH": "Subject",
  "de_CH": "Betreff"
}
```

The application selects the label matching the user’s locale. If no matching locale is found, the raw object is displayed.

Supported languages: `en_CH` (Swiss-English), `de_CH` (Swiss-German)

---

---

## `index.table.columns`

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

## `index.table.filters`

Defines **filters applied to the tasks list**.

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

#### Example with Manual Options

```json
{
  "type": "select",
  "label": "Status",
  "options": {
    "Open": "Open",
    "In_Progress": "In Progress",
    "Closed": "Closed"
  },
  "multiple": false,
  "identifier": "STATUS"
}
```

**Notes:**
- If `multiple` is `true`, users can pick multiple options.
- If `default` is provided, the filter is pre-filled.
- If `options` is omitted, unique values are detected automatically using the `identifier`.
- When using manual `options`, the left side is the value used to filter, and the right side is the label displayed in the dropdown.
- Manual `options` are case-sensitive and do not support translations.
- Date filters render a `from` and `to` date range picker and filter records between the specified dates.

---

## `show.infolist.entries`

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

## `show.form.fields`

Defines **editable fields** when updating a task (for example, a comment).

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

## `show.uploads`

Controls **file uploads associated with a task**.

### JSON Structure

```json
"uploads": {
  "enabled": true,
  "collapsed_by_default": true,
  "form": {
    "providable": {
      "vault_guid": null
    },
    "fields": [ /* Array of upload fields */ ]
  },
  "rules": [ /* Array of validation rules */ ]
}
```

### Top-Level Properties

| Property               | Type      | Description                                           |
|------------------------|-----------|-------------------------------------------------------|
| `enabled`              | `boolean` | Whether the uploads section is shown.                |
| `collapsed_by_default` | `boolean` | Whether the upload form is collapsed initially.      |
| `form`                 | `object`  | Defines the form fields used when uploading files.   |
| `rules`                | `array`   | Validation rules applied to the uploaded files array.|

### `form.providable`

Metadata about how files are stored.

| Property     | Type     | Description                                    |
|--------------|----------|------------------------------------------------|
| `vault_guid` | `string` | Optional GUID of the vault to use for storage. |

Example:

```json
"providable": {
  "vault_guid": null
}
```

### `form.fields`

Defines **metadata fields collected when uploading a file**.

#### Example

```json
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
```

---

## Validation Rules

Validation rules are used in:
- `form.fields.rules`
- `uploads.rules`

All rules must be written as **plain strings**.

### Supported Validation Rules

We use laravel validation so you can use any of [Laravel's Validation Rules](https://laravel.com/docs/12.x/validation#available-validation-rules)

**Notes:**
- All rules **must be plain string values** exactly as shown below.
- You can **combine multiple rules** in an array:

```json
"rules": ["nullable", "string", "max:254"]
```

- For date rules like `after` or `before`, supply the date as a **fixed string**:

```json
"rules": ["date", "after:2024-01-01"]
```

- **Dynamic expressions or code-based rules are not supported** (e.g., generating dates in code).

---

## Full Example Configuration

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
          "type": "select",
          "label": "Subject",
          "options": ["Welcome", "Task"],
          "multiple": true,
          "identifier": "TITLE"
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

---

## Additional Notes

- If `uploads.enabled` is `false`, the upload section is hidden.
- `collapsed_by_default` controls whether sections start collapsed.
- If a `form` or upload field has validation `rules`, they apply when saving.
- The `identifier` must exactly match your data keys.
