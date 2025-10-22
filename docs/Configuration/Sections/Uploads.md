# Uploads Configuration

<!-- TOC -->
* [Uploads Configuration](#uploads-configuration)
  * [Uploads Section Configuration](#uploads-section-configuration)
    * [JSON File Structure](#json-file-structure)
    * [Properties](#properties)
      * [`form.providable`](#formprovidable)
    * [Upload Fields Configuration](#upload-fields-configuration)
      * [Field Properties](#field-properties)
      * [Supported Field Types](#supported-field-types)
      * [Upload Fields Example](#upload-fields-example)
    * [Rules](#rules)
  * [Full Example](#full-example)
  * [Notes](#notes)
<!-- TOC -->

This guide describes how to **generate and configure the JSON files** that define **file upload behavior** for sections such as tasks and documents.

Uploads configuration controls:

- Whether uploads are allowed
- Which fields are collected during upload
- How validation rules are applied

---

## Uploads Section Configuration

### JSON File Structure

The upload configuration is defined within the `show.uploads` section of your JSON.  
Here is the overall structure:

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

### Properties

| Property               | Type      | Description                                     |
|------------------------|-----------|-------------------------------------------------|
| `enabled`              | `boolean` | Whether the uploads section is shown.           |
| `collapsed_by_default` | `boolean` | Whether the upload form is collapsed initially. |
| `form`                 | `object`  | Upload form configuration.                      |
| `rules`                | `array`   | Validation rules applied to the uploaded files. |

---

#### `form.providable`

Metadata about how files are stored.

| Property     | Type     | Description                          |
|--------------|----------|--------------------------------------|
| `vault_guid` | `string` | Optional GUID of the vault to use.   |

**Example:**

```json
"providable": {
  "vault_guid": null
}
```

---

### Upload Fields Configuration

Defines **metadata fields collected when uploading a file**.

#### Field Properties

Each item in `fields` supports:

| Property     | Type                  | Description                                 |
|--------------|-----------------------|---------------------------------------------|
| `type`       | `string`              | Field type (see **Supported Field Types**). |
| `label`      | `string` or `object`  | Field label (plain string or translations). |
| `identifier` | `string`              | Unique field key.                           |
| `rules`      | `array`               | Validation rules applied to the field.      |
| `value`      | `string` or `boolean` | Default value or `true` to auto-fill.       |

---

#### Supported Field Types

| Type       | Notes                    |
|------------|--------------------------|
| `string`   | Text.                    |
| `text`     | Text.                    |
| `textarea` | Multiline Text.          |
| `integer`  | Numeric.                 |
| `numeric`  | Numeric.                 |
| `select`   | Select Dropdown.         |
| `date`     | Date `d.m.Y`.            |
| `dateTime` | Date Time `d.m.Y H:i:s`. |
| `time`     | Time `H:i:s`.            |
| `hidden`   | Hidden Field.            |

---

#### Upload Fields Example

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
        "type": "select",
        "label": {
            "de_CH": "Type",
            "en_CH": "Type"
        },
        "options": [
            {
              "value": "cv",
              "label": {
                "de_CH": "Lebenslauf",
                "en_CH": "CV"
              }
            },
            {
              "value": "cover-letter",
              "label": {
                "de_CH": "Anschreiben",
                "en_CH": "Cover Letter"
              }
            }
        ],
        "value": "cv",
        "rules": [
            "required",
            "string",
            "in:cv,cover-letter",
        ],
        "identifier": "YEAR"
    },
    {
        "type": "hidden",
        "label": "Client Identifier",
        "rules": [],
        "value": "CLIENT::IDENTIFIER",
        "identifier": "CLIENT_KEY"
    },
    {
        "type": "hidden",
        "label": "UUID",
        "rules": [],
        "value": "USER_UPLOAD_REQUEST_FILE::UUID",
        "identifier": "UUID"
    }
]
```

---

### DocuWare: Data Type
For DocuWare, you must specify the data_type property in your form or metadata configuration. This defines how the data will be stored and interpreted within the system.

| Value    | Member   |
|-----------|----------|
| string    | Text     |
| numeric   | Numeric  |
| decimal   | Decimal  |
| date      | Date     |
| datetime  | DateTime |
| keyword   | Keyword  |

### M-Files: Data Type
For M-Files, you must specify the data_type property in your form or metadata configuration. This defines how the data will be stored and interpreted within the system.

| Value | Member             |
|-------|--------------------|
| 0     | Uninitialized      |
| 1     | Text               |
| 2     | Integer            |
| 3     | Floating           |
| 5     | Date               |
| 6     | Time               |
| 7     | Timestamp          |
| 8     | Boolean            |
| 9     | Lookup             |
| 10    | MultiSelectLookup  |
| 11    | Integer64          |
| 12    | FILETIME           |
| 13    | MultiLineText      |
| 14    | ACL    

#### Example
```json
"fields": [
    {
        "data_type": 1,
        "type": "string",
        "label": "Subject",
        "rules": ["nullable", "string", "max:254"],
        "value": true,
        "identifier": "TITLE"
    },
    {
        "data_type": 13,
        "type": "textarea",
        "label": "Comment",
        "rules": ["nullable", "string", "max:512"],
        "value": true,
        "identifier": "COMMENT"
    }
]
```

### Rules

We use [laravel validation rules](https://laravel.com/docs/12.x/validation#available-validation-rules) to define how uploaded files are validated.


## Full Example

```json
{
  "create": {
    "form": {
      "fields": [
        {
          "type": "select",
          "label": {
            "de_CH": "Date",
            "en_CH": "Date"
          },
          "options": [
            { "value": "2026", "label": "2026" },
            { "value": "2025", "label": "2025" },
            { "value": "2024", "label": "2024" }
          ],
          "value": "2025",
          "rules": [
            "required",
            "string",
            "in:2024,2025,2026",
            "max:254"
          ],
          "identifier": "YEAR"
        },
        {
          "type": "textarea",
          "label": {
            "de_CH": "Bemerkung",
            "en_CH": "Description"
          },
          "rules": [
            "required",
            "string",
            "max:756"
          ],
          "identifier": "DESCRIPTION"
        },
        {
          "type": "hidden",
          "label": "Client Identifier",
          "rules": [],
          "value": "CLIENT::IDENTIFIER",
          "identifier": "CLIENT_KEY"
        },
        {
          "type": "hidden",
          "label": "UUID",
          "rules": [],
          "value": "USER_UPLOAD_REQUEST_FILE::UUID",
          "identifier": "UUID"
        }
      ]
    },
    "uploads": {
      "rules": [
        "required",
        "min:1",
        "max:5"
      ]
    }
  }
}
```

---

## Notes

- If `enabled` is `false`, the upload UI will not be displayed.
- All `identifier` values must match your data keys exactly.
- Labels can be strings or translation objects. [See Translations Guide](../Translations.md).
