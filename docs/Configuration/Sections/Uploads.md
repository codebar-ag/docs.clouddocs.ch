# Uploads Configuration

This guide describes how to **generate and configure the JSON files** that define **file upload behavior** for sections such as tasks and documents.

Uploads configuration controls:

- Whether uploads are allowed
- Which fields are collected during upload
- How validation rules are applied

---

## JSON File Structure

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
    "fields": [ /* Array of upload fields */ ]
  },
  "rules": [ /* Array of validation rules */ ]
}
```

---

## Top-Level Properties

| Property               | Type      | Description                                           |
|------------------------|-----------|-------------------------------------------------------|
| `enabled`              | `boolean` | Whether the uploads section is shown.                 |
| `collapsed_by_default` | `boolean` | Whether the upload form is collapsed initially.       |
| `form`                 | `object`  | Defines the form fields used when uploading files.    |
| `rules`                | `array`   | Validation rules applied to the uploaded files array. |

---

## `form.providable`

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

---

## `form.fields`

Defines **metadata fields collected when uploading a file**.

### Common Field Properties

| Property     | Type                  | Description                                 |
|--------------|-----------------------|---------------------------------------------|
| `type`       | `string`              | Field type (see Supported Field Types).     |
| `label`      | `string` or `object`  | Field label (plain string or translations). |
| `identifier` | `string`              | Unique field key.                           |
| `rules`      | `array`               | Validation rules.                           |
| `value`      | `string` or `boolean` | Default value or `true` to auto-fill.       |

---

## Supported Field Types

| Type       | Notes                                      |
|------------|--------------------------------------------|
| `string`   | Text input field.                          |
| `textarea` | Multiline text input.                      |
| `hidden`   | Hidden field with static or dynamic value. |

---

## Label Translation

Labels support translations:

Example string:

```json
"label": "Subject"
```

Example translations:

```json
"label": {
  "en_CH": "Subject",
  "de_CH": "Betreff"
}
```

The current locale determines which label is shown.

---

## Upload Field Example

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
  }
]
```

---

## `rules` (Upload Validation Rules)

These rules validate the **whole uploaded files array**.

Supported rules:

- `"required"`
- `"nullable"`
- `"min:value"`
- `"max:value"`
- `"array"`
- `"size:value"`

Example:

```json
"rules": ["required", "min:1", "max:5"]
```

---

## Full Example Configuration

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
      }
    ]
  },
  "rules": ["required", "min:1", "max:5"]
}
```

---

## Additional Notes

- If `enabled` is `false`, the upload UI will not be displayed.
- All `identifier` values must match your data keys.
