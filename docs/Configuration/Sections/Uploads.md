# 📤 Uploads Configuration

This guide describes how to **generate and configure the JSON files** that define **file upload behavior** for sections such as tasks and documents.

Uploads configuration controls:

- Whether uploads are allowed
- Which fields are collected during upload
- How validation rules are applied

---

## 🗂️ JSON File Structure

The upload configuration is defined within the `show.uploads` section of your section JSON.  
Here is the overall structure:

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

Each part is explained in detail below.

---

## ✨ Top-Level Properties

| Property               | Type       | Description                                                           |
|------------------------|------------|-----------------------------------------------------------------------|
| `enabled`              | `boolean`  | Whether the uploads section is shown.                                |
| `collapsed_by_default` | `boolean`  | Whether the upload form is collapsed initially.                      |
| `form`                 | `object`   | Defines the form fields used when uploading files.                   |
| `rules`                | `array`    | Validation rules applied to the uploaded files array.                |

---

## 🗂️ `form.providable`

The `providable` section contains **metadata about how files are stored**.

| Property     | Type       | Description                                    |
|--------------|------------|------------------------------------------------|
| `vault_guid` | `string`   | Optional GUID of the vault to use for storage.|

*Example:*

```json
"providable": {
  "vault_guid": null
}
```

---

## 📝 `form.fields`

Defines **metadata fields collected when uploading a file**.

### Common Field Properties

| Property     | Type                 | Description                                                            |
|--------------|----------------------|------------------------------------------------------------------------|
| `type`       | `string`             | Field type (see [Supported Types](#supported-types)).                 |
| `label`      | `object` or `string` | Field label (plain string or translations).                           |
| `identifier` | `string`             | Unique field key.                                                      |
| `rules`      | `array`              | Validation rules (e.g., `["nullable", "max:254"]`).                    |
| `value`      | `string` or `boolean`| Default value or `true` to auto-fill (e.g., `{{CLIENT_KEY}}`).         |

---

## 📘 Supported Types

| Type       | Usage             | Notes                                          |
|------------|-------------------|------------------------------------------------|
| `string`   | All fields        | Displays as a text input.                      |
| `textarea` | All fields        | For longer text input.                         |
| `hidden`   | All fields        | Hidden input field with a pre-filled value.    |

---

## 🧩 Label Translation

For `label`, you can use either:

- A **string** (e.g., `"Subject"`)
- An **object with translations**:

```json
"label": {
  "en_CH": "Subject",
  "de_CH": "Betrteff"
}
```

The current locale determines which label is shown.

---

## 🖥️ Upload Field Example

Example configuration of upload fields:

```json
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
```

---

## ✅ `rules` (Upload Validation Rules)

These validation rules apply to the **whole uploaded files array**.

### Example

```json
"rules": [
  "required",
  "min:1",
  "max:5"
]
```

**Behavior:**

- `required`: User must upload at least one file.
- `min:1`: Minimum 1 file required.
- `max:5`: Maximum 5 files allowed.

---

## 🛠️ Full Example Configuration

Below is a **complete example `uploads` configuration**:

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
```

---

## 🪧 Additional Notes

- If `enabled` is `false`, the upload UI will not be displayed.
- All `identifier` values must match your expected data keys.
- Hidden fields (`hidden`) are typically used to pass system metadata automatically.
- Validation `rules` follow the same format as Laravel validation.
