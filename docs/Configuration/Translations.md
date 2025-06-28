## Label Translation

Labels can be defined as:

- A **plain string** (single language)
- A **translation object** mapping locales to labels

---

### String Example

```json
"label": "Subject"
```

---

### Translation Object Example

```json
"label": {
  "en_CH": "Subject",
  "de_CH": "Betreff"
}
```

---

### Supported Locales

| Locale Code | Language              |
|-------------|-----------------------|
| en_CH       | English (Switzerland) |
| de_CH       | German (Switzerland)  |

---

### Example Configuration

#### Documents Section

```json
"documents": {
  "enabled": true,
  "collapsed_by_default": false,
  "form": {
    "providable": {
      "vault_guid": null
    },
    "fields": [
      {
        "type": "string",
        "label": {
          "en_CH": "Subject",
          "de_CH": "Betreff"
        },
        "identifier": "TITLE"
      },
      {
        "type": "date",
        "label": {
          "en_CH": "Date",
          "de_CH": "Datum"
        },
        "identifier": "DOCUMENT_DATE"
      }
    ]
  },
  "rules": []
}
```

#### Uploads Section

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
        "label": {
          "en_CH": "Subject",
          "de_CH": "Betreff"
        },
        "rules": ["nullable", "string", "max:254"],
        "value": true,
        "identifier": "TITLE"
      },
      {
        "type": "textarea",
        "label": {
          "en_CH": "Comment",
          "de_CH": "Kommentar"
        },
        "rules": ["nullable", "string", "max:512"],
        "value": true,
        "identifier": "COMMENT"
      }
    ]
  },
  "rules": ["required", "min:1", "max:5"]
}
```

#### Tasks Section

```json
"tasks": {
  "enabled": true,
  "collapsed_by_default": false,
  "form": {
    "providable": {
      "vault_guid": null
    },
    "fields": [
      {
        "type": "string",
        "label": {
          "en_CH": "Task Name",
          "de_CH": "Aufgabenname"
        },
        "rules": ["required", "string", "max:254"],
        "value": true,
        "identifier": "TASK_NAME"
      },
      {
        "type": "date",
        "label": {
          "en_CH": "Due Date",
          "de_CH": "Fälligkeitsdatum"
        },
        "rules": ["nullable", "date"],
        "value": true,
        "identifier": "DUE_DATE"
      }
    ]
  },
  "rules": []
}
```

#### Filters

```json
"filters": [
  {
    "type": "select",
    "label": {
      "en_CH": "Type",
      "de_CH": "Typ"
    },
    "identifier": "DOCUMENT_TYPE",
    "default": ["Contract"],
    "multiple": true
  },
  {
    "type": "date",
    "label": {
      "en_CH": "Date",
      "de_CH": "Datum"
    },
    "identifier": "DOCUMENT_DATE",
    "default": {
      "from": "{{start_date}}",
      "to": "{{end_date}}"
    }
  }
]
```

#### Tables

```json
"table": {
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
      "label": {
        "en_CH": "Date",
        "de_CH": "Datum"
      },
      "sortable": false,
      "identifier": "DOCUMENT_DATE"
    }
  ]
}
```

---

**Notes:**

- The application automatically selects the label that matches the user’s locale.
- All translation keys must be valid locale codes, e.g., `en_CH`, `de_CH`.
