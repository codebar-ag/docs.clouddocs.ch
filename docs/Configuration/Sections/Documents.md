# Documents Configuration

<!-- TOC -->
* [Documents Configuration](#documents-configuration)
  * [Index Section Configuration](#index-section-configuration)
  * [Show Section Configuration](#show-section-configuration)
    * [JSON Structure (`show`)](#json-structure-show)
    * [Properties](#properties)
    * [Field Properties](#field-properties)
    * [Supported Field Types](#supported-field-types)
    * [Example](#example)
    * [Notes](#notes)
  * [Full Example](#full-example)
  * [Notes](#notes-1)
<!-- TOC -->

This guide describes how to **generate and configure the JSON files** used to define **document sections**, including:

- Detail view display
- Table columns and filters

---

## Index Section Configuration

- See [Index Configuration](../Index.md) for details on the index section.

---

## Show Section Configuration

### JSON Structure (`show`)

```json
"show": {
    "title_identifier": /* Idendifier that should be used as title */,
    "subtitle_identifier": /* Identifier that should be used as subtitle */",
    "infolist": {
        "enabled": true,
        "collapsed_by_default": true,
        "entries": [
          /* Fields */
        ]
    }
}
```

---

### Properties

| Property                             | Type                  | Description                                               |
|--------------------------------------|-----------------------|-----------------------------------------------------------|
| `show`                               | `object`              | Detail view configuration.                                |
| `show.title_identifier`              | `string`              | Field to use as the main title.                           |
| `show.subtitle_identifier`           | `string`              | Field to use as the subtitle.                             |
| `show.infolist`                      | `object`              | Infolist fields configuration.                            |
| `show.infolist.enabled`              | `boolean`             | Whether the section is visible.                           |
| `show.infolist.collapsed_by_default` | `boolean`             | Whether the section is collapsed by default.              |
| `show.infolist.entries`              | `array`               | Fields displayed in the infolist.                         |

---

### Field Properties

Each item in `entries` supports:

| Property     | Type                 | Description                                 |
|--------------|----------------------|---------------------------------------------|
| `type`       | `string`             | Field type (see **Supported Field Types**). |
| `label`      | `string` or `object` | Label (string or translations).             |
| `identifier` | `string`             | Field key that identifies the field.        |

---

### Supported Field Types

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

### Example

```json
"entries": [
  {
    "type": "date",
    "label": "Date",
    "identifier": "DOCUMENT_DATE"
  },
  {
    "type": "string",
    "label": "Subject",
    "identifier": "TITLE"
  }
]
```

---

### Notes

- `identifier` must match your data keys.
- Labels can be strings or translation objects. [See Translations Guide](../Translations.md).

---

## Full Example

```json
{
  "show": {
    "title_identifier": "TITLE",
    "subtitle_identifier": "DOCUMENT_DATE",
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
          "identifier": "DOCUMENT_DATE"
        },
        {
          "type": "string",
          "label": "Subject",
          "identifier": "TITLE"
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
          "label": {
            "de_CH": "Date",
            "en_CH": "Date"
          },
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
          "type": "select",
          "label": "Month",
          "identifier": "MONTH",
          "options": [
            {
              "value": "jan",
              "label": {
                "de_CH": "Januar",
                "en_CH": "January"
              }
            },
            {
              "value": "feb",
              "label": {
                "de_CH": "Februar",
                "en_CH": "February"
              }
            },
            {
              "value": "march",
              "label": {
                "de_CH": "Marsch",
                "en_CH": "March"
              }
            }
          ],
          "default": ["jan", "feb"],
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
    }
  }
}
```

---

## Notes

- `identifier` must match data keys.
- Labels can be strings or translation objects. [See Translations Guide](../Translations.md).
