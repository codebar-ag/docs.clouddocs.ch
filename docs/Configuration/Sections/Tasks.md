# Tasks Configuration

This guide describes how to **generate and configure the JSON files** used to define **tasks sections**, including:

- Detail view metadata
- Editable fields
- File upload configuration
- List (index) columns and filters

---

# Show Section Configuration

## JSON Structure (`show`)

```json
"show": {
  "title_identifier": "TITLE",
  "subtitle_identifier": "DOCUMENT_TYPE",
  "infolist": { /* See Infolist Section */ },
  "form": { /* See Form Section */ },
  "uploads": { /* See Uploads Section */ }
}
```

---

## Properties

| Property                             | Type      | Description                                               |
|--------------------------------------|-----------|-----------------------------------------------------------|
| `show`                               | `object`  | Detail view configuration.                                |
| `show.title_identifier`              | `string`  | Field to use as the main title.                           |
| `show.subtitle_identifier`           | `string`  | Field to use as the subtitle.                             |
| `show.infolist`                      | `object`  | Infolist fields configuration.                            |
| `show.form`                          | `object`  | Editable form fields configuration.                       |
| `show.uploads`                       | `object`  | Upload behavior and fields configuration.                 |

---

# Infolist Configuration

Defines **read-only fields shown in the detail view sidebar**.

## JSON Structure

```json
"infolist": {
  "enabled": true,
  "collapsed_by_default": true,
  "entries": [ /* Fields */ ]
}
```

---

## Properties

| Property                             | Type      | Description                                       |
|--------------------------------------|-----------|---------------------------------------------------|
| `enabled`                            | `boolean` | Whether the infolist sidebar is shown.            |
| `collapsed_by_default`               | `boolean` | Whether the sidebar starts collapsed.             |
| `entries`                            | `array`   | Fields displayed in the infolist.                 |

---

## Field Properties

Each item in `entries` supports:

| Property     | Type                 | Description                                 |
|--------------|----------------------|---------------------------------------------|
| `type`       | `string`             | Field type (see **Supported Field Types**). |
| `label`      | `string` or `object` | Field label (string or translations).       |
| `identifier` | `string`             | Field key that identifies the field.        |

---

## Supported Field Types

| Type       | Notes                    |
|------------|--------------------------|
| `string`   | Text.                    |
| `text`     | Text.                    |
| `textarea` | Multiline text.          |
| `integer`  | Numeric.                 |
| `numeric`  | Numeric.                 |
| `date`     | Date `d.m.Y`.            |
| `dateTime` | Date Time `d.m.Y H:i:s`. |
| `time`     | Time `H:i:s`.            |

---

# Form Configuration

Defines **editable fields when updating a task**.

## JSON Structure

```json
"form": {
  "collapsed_by_default": true,
  "fields": [ /* Fields */ ]
}
```

---

## Properties

| Property               | Type      | Description                              |
|------------------------|-----------|------------------------------------------|
| `collapsed_by_default` | `boolean` | Whether the form is collapsed initially. |
| `fields`               | `array`   | Editable form fields.                    |

---

## Field Properties

Each item in `fields` supports:

| Property     | Type                  | Description                                 |
|--------------|-----------------------|---------------------------------------------|
| `type`       | `string`              | Field type (see **Supported Field Types**). |
| `label`      | `string` or `object`  | Field label (string or translations).       |
| `identifier` | `string`              | Unique field key.                           |
| `rules`      | `array`               | Validation rules.                           |
| `value`      | `string` or `boolean` | Default value or autofill flag.             |

---

## Supported Field Types

Same as Infolist.

---

# Uploads Configuration

Controls **file uploads associated with a task**.

## JSON Structure

```json
"uploads": {
  "enabled": true,
  "collapsed_by_default": true,
  "form": {
    "providable": {
      "vault_guid": null
    },
    "fields": [ /* Upload fields */ ]
  },
  "rules": [ /* Validation rules */ ]
}
```

---

## Properties

| Property               | Type      | Description                                     |
|------------------------|-----------|-------------------------------------------------|
| `enabled`              | `boolean` | Whether uploads are allowed.                    |
| `collapsed_by_default` | `boolean` | Whether the upload form is collapsed initially. |
| `form`                 | `object`  | Upload form configuration.                      |
| `rules`                | `array`   | Validation rules applied to uploaded files.     |

---

## Field Properties

Same as Form.

---

# Index Section Configuration

Defines **list view (table) columns and filters**.

## JSON Structure

```json
"index": {
  "table": {
    "columns": [ /* Columns */ ],
    "filters": [ /* Filters */ ]
  }
}
```

---

# Columns Configuration

## Properties

| Property              | Type      | Description                     |
|-----------------------|-----------|---------------------------------|
| `index.table.columns` | `array`   | Columns shown in the table.     |

---

## Field Properties

Each item in `columns` supports:

| Property     | Type                 | Description                                     |
|--------------|----------------------|-------------------------------------------------|
| `type`       | `string`             | Field type (see **Supported Field Types**).     |
| `label`      | `string` or `object` | Field label (string or translations).           |
| `identifier` | `string`             | Unique field key.                               |
| `sortable`   | `boolean`            | Whether the field can be sorted.                |

---

## Supported Field Types

| Type       | Notes                    |
|------------|--------------------------|
| `string`   | Text.                    |
| `text`     | Text.                    |
| `integer`  | Numeric.                 |
| `numeric`  | Numeric.                 |
| `date`     | Date `d.m.Y`.            |
| `dateTime` | Date Time `d.m.Y H:i:s`. |
| `time`     | Time `H:i:s`.            |

---

## Example

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
    "sortable": false,
    "identifier": "DOCUMENT_DATE"
  }
]
```

---

## Notes

- `sortable` is optional.
- `identifier` must match data keys.

---

# Filters Configuration

## Properties

| Property              | Type      | Description                     |
|-----------------------|-----------|---------------------------------|
| `index.table.filters` | `array`   | Filters available in the table. |

---

## Field Properties

Each item in `filters` supports:

| Property     | Type                    | Description                                                                                                      |
|--------------|-------------------------|------------------------------------------------------------------------------------------------------------------|
| `type`       | `string`                | Field type (see **Supported Field Types**).                                                                      |
| `label`      | `string` or `object`    | Field label (string or translations).                                                                            |
| `identifier` | `string`                | Unique field key.                                                                                                |
| `multiple`   | `boolean`               | Allow multiple selection.                                                                                        |
| `options`    | `object` or undefinable | Options for the *select filter only* when not used, the select filter will auto-fill with data from the database |
| `default`    | `array` or `string`     | Default values.                                                                                                  |

---

## Supported Field Types

| Type       | Notes                    |
|------------|--------------------------|
| `date`     | Date `d.m.Y`.            |
| `select`   | Dropdown selection.      |

---

## Example

```json
"filters": [
  {
    "type": "select",
    "label": "Type",
    "identifier": "DOCUMENT_TYPE",
    "default": ["Contract"],
    "multiple": false
  },
  {
    "type": "select",
    "label": "Type",
    "identifier": "DOCUMENT_TYPE",
    "default": ["Contract"],
    "options": {
      "Contract": "Contract",
      "Agreement": "Agreement",
    },
    "multiple": true
  },
  {
    "type": "date",
    "label": "Date",
    "identifier": "DOCUMENT_DATE",
    "default": {
      "from": "2022-01-01",
      "to": "2022-12-31"
    }
  }
]
```

---

# Full Example

```json
{
  "show": {
    "title_identifier": "TITLE",
    "subtitle_identifier": "DOCUMENT_TYPE",
    "infolist": {
      "enabled": true,
      "collapsed_by_default": false,
      "entries": [
        {
          "type": "date",
          "label": "Date",
          "identifier": "DOCUMENT_DATE"
        },
        {
          "type": "string",
          "label": "Author",
          "identifier": "AUTHOR"
        }
      ]
    },
    "form": {
      "collapsed_by_default": true,
      "fields": [
        {
          "type": "text",
          "label": "Description",
          "identifier": "DESCRIPTION",
          "rules": ["required"]
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
            "type": "file",
            "label": "Upload File",
            "identifier": "UPLOAD_FILE"
          }
        ]
      },
      "rules": ["file_size:5MB"]
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
          "sortable": false,
          "identifier": "DOCUMENT_DATE"
        }
      ],
      "filters": [
        {
          "type": "select",
          "label": "Type",
          "identifier": "DOCUMENT_TYPE",
          "default": ["Contract"],
          "multiple": true
        },
        {
          "type": "date",
          "label": "Date",
          "identifier": "DOCUMENT_DATE",
          "default": { "from": "2022-01-01", "to": "2022-12-31" }
        }
      ]
    }
  }
}
```

# Notes

- `identifier` must match your data keys.
- Labels can be strings or translation objects. [See Translations Guide](../Translations.md).
