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

> **Tip:** For supported field types, filters, label translations, and validation rules, see [Shared Configurations](./SharedConfigurations.md).

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

> See [Shared Configurations](./SharedConfigurations.md) for filter types, behaviors, and examples.

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

## Additional Notes

- If `uploads.enabled` is `false`, the upload section is hidden.
- `collapsed_by_default` controls whether sections start collapsed.
- If a `form` field has validation `rules`, they apply when saving.
- The `identifier` must exactly match your data keys.
- For supported field types, filters, label translations, and validation rules, see [Shared Configurations](./SharedConfigurations.md).
