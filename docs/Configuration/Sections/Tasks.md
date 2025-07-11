# Tasks Configuration

<!-- TOC -->
* [Tasks Configuration](#tasks-configuration)
  * [Index Section Configuration](#index-section-configuration)
  * [Show Section Configuration](#show-section-configuration)
    * [JSON Structure](#json-structure)
    * [Properties](#properties)
    * [Infolist Configuration](#infolist-configuration)
      * [JSON Structure](#json-structure-1)
      * [Properties](#properties-1)
      * [Field Properties](#field-properties)
      * [Supported Field Types](#supported-field-types)
    * [Form Configuration](#form-configuration)
      * [JSON Structure](#json-structure-2)
      * [Properties](#properties-2)
      * [Field Properties](#field-properties-1)
      * [Supported Field Types](#supported-field-types-1)
    * [Uploads Configuration](#uploads-configuration)
      * [JSON Structure](#json-structure-3)
      * [Properties](#properties-3)
      * [Field Properties](#field-properties-2)
  * [Full Example](#full-example)
  * [Notes](#notes)
<!-- TOC -->

This guide describes how to **generate and configure the JSON files** used to define **tasks sections**, including:

- Detail view metadata
- Editable fields
- File upload configuration
- List (index) columns and filters

---

## Index Section Configuration

- See [Index Configuration](../Index.md) for details on the index section.

---

## Show Section Configuration

### JSON Structure

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

### Properties

| Property                             | Type      | Description                                               |
|--------------------------------------|-----------|-----------------------------------------------------------|
| `show`                               | `object`  | Detail view configuration.                                |
| `show.title_identifier`              | `string`  | Field to use as the main title.                           |
| `show.subtitle_identifier`           | `string`  | Field to use as the subtitle.                             |
| `show.infolist`                      | `object`  | Infolist fields configuration.                            |
| `show.form`                          | `object`  | Editable form fields configuration.                       |
| `show.uploads`                       | `object`  | Upload behavior and fields configuration.                 |

---

### Infolist Configuration

Defines **read-only fields shown in the detail view sidebar**.

#### JSON Structure

```json
"infolist": {
  "enabled": true,
  "collapsed_by_default": true,
  "entries": [ /* Fields */ ]
}
```

---

#### Properties

| Property                             | Type      | Description                                       |
|--------------------------------------|-----------|---------------------------------------------------|
| `enabled`                            | `boolean` | Whether the infolist sidebar is shown.            |
| `collapsed_by_default`               | `boolean` | Whether the sidebar starts collapsed.             |
| `entries`                            | `array`   | Fields displayed in the infolist.                 |

---

#### Field Properties

Each item in `entries` supports:

| Property     | Type                 | Description                                 |
|--------------|----------------------|---------------------------------------------|
| `type`       | `string`             | Field type (see **Supported Field Types**). |
| `label`      | `string` or `object` | Field label (string or translations).       |
| `identifier` | `string`             | Field key that identifies the field.        |
| `order`      | `integer`            | Display order (1 = first, higher numbers = lower priority). |

---

#### Supported Field Types

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

**Note:** `order` determines the display order: 1 is ordered first, higher numbers appear lower in the list.

---

### Form Configuration

Defines **editable fields when updating a task**.

#### JSON Structure

```json
"form": {
  "collapsed_by_default": true,
  "fields": [ /* Fields */ ]
}
```

---

#### Properties

| Property               | Type      | Description                              |
|------------------------|-----------|------------------------------------------|
| `collapsed_by_default` | `boolean` | Whether the form is collapsed initially. |
| `fields`               | `array`   | Editable form fields.                    |

---

#### Field Properties

Each item in `fields` supports:

| Property     | Type                  | Description                                 |
|--------------|-----------------------|---------------------------------------------|
| `type`       | `string`              | Field type (see **Supported Field Types**). |
| `label`      | `string` or `object`  | Field label (string or translations).       |
| `identifier` | `string`              | Unique field key.                           |
| `rules`      | `array`               | Validation rules.                           |
| `value`      | `string` or `boolean` | Default value or autofill flag.             |
| `order`      | `integer`             | Display order (1 = first, higher numbers = lower priority). |

---

#### Supported Field Types

Same as Infolist.

---

**Note:** `order` determines the display order: 1 is ordered first, higher numbers appear lower in the list.

---

### Uploads Configuration

Controls **file uploads associated with a task**.

#### JSON Structure

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

#### Properties

| Property               | Type      | Description                                     |
|------------------------|-----------|-------------------------------------------------|
| `enabled`              | `boolean` | Whether uploads are allowed.                    |
| `collapsed_by_default` | `boolean` | Whether the upload form is collapsed initially. |
| `form`                 | `object`  | Upload form configuration.                      |
| `rules`                | `array`   | Validation rules applied to uploaded files.     |

---

#### Field Properties

Same as Form.

---

**Note:** `order` determines the display order: 1 is ordered first, higher numbers appear lower in the list.

---

## Full Example

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
          "label": {
            "de_CH": "Date",
            "en_CH": "Date"
          },
          "identifier": "DOCUMENT_DATE",
          "order": 1
        },
        {
          "type": "string",
          "label": "Author",
          "identifier": "AUTHOR",
          "order": 2
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
          "rules": ["required"],
          "order": 1
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
            "identifier": "UPLOAD_FILE",
            "order": 1
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
          "identifier": "DOCUMENT_TYPE",
          "order": 1
        },
        {
          "type": "date",
          "label": {
            "de_CH": "Date",
            "en_CH": "Date"
          },
          "sortable": false,
          "identifier": "DOCUMENT_DATE",
          "order": 2
        }
      ],
      "filters": [
        {
          "type": "select",
          "label": "Type",
          "identifier": "DOCUMENT_TYPE",
          "default": ["Contract"],
          "multiple": true,
          "order": 1
        },
        {
          "type": "date",
          "label": "Date",
          "identifier": "DOCUMENT_DATE",
          "default": { "from": "2022-01-01", "to": "2022-12-31" },
          "order": 2
        }
      ]
    }
  }
}
```

---

## Notes

- `identifier` must match your data keys.
- Labels can be strings or translation objects. [See Translations Guide](../Translations.md).
