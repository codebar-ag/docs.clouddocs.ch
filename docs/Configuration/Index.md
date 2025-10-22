

# Index Section Configuration

<!-- TOC -->
* [Index Section Configuration](#index-section-configuration)
  * [JSON Structure (`index`)](#json-structure-index)
  * [Columns Configuration](#columns-configuration)
    * [Properties](#properties)
    * [Field Properties](#field-properties)
    * [Supported Field Types](#supported-field-types)
    * [Example](#example)
    * [Notes](#notes)
  * [Filters Configuration](#filters-configuration)
    * [Properties](#properties-1)
    * [Field Properties](#field-properties-1)
    * [Supported Field Types](#supported-field-types-1)
    * [Example](#example-1)
    * [Notes](#notes-1)
<!-- TOC -->

## JSON Structure (`index`)

```json
"index": {
  "table": {
    "columns": [
      /* Columns */
    ],
    "filters": [
      /* Filters */
    ]
  }
}
```

---

## Columns Configuration

### Properties

| Property              | Type      | Description                     |
|-----------------------|-----------|---------------------------------|
| `index.table.columns` | `array`   | Columns shown in the table.     |

---

### Field Properties

Each item in `columns` supports:

| Property     | Type                 | Description                                     |
|--------------|----------------------|-------------------------------------------------|
| `type`       | `string`             | Field type (see **Supported Field Types**).     |
| `label`      | `string` or `object` | Field label (string or translations).           |
| `identifier` | `string`             | Unique field key.                               |
| `sortable`   | `boolean`            | Whether the field can be sorted.                |
| `order`      | `integer`            | Display order (1 = first, higher numbers = lower priority). |

---

### Supported Field Types

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

### Example

```json
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
    "label": "Date",
    "sortable": false,
    "identifier": "DOCUMENT_DATE",
    "order": 2
  }
]
```

---

### Notes

- `sortable` is optional.
- `identifier` must match data keys.
- `order` determines the display order: 1 is ordered first, higher numbers appear lower in the list.

---

## Filters Configuration

### Properties

| Property              | Type      | Description                     |
|-----------------------|-----------|---------------------------------|
| `index.table.filters` | `array`   | Filters available in the table. |

---

### Field Properties

Each item in `filters` supports:

| Property     | Type                    | Description                                                                                                      |
|--------------|-------------------------|------------------------------------------------------------------------------------------------------------------|
| `type`       | `string`                | Field type (see **Supported Field Types**).                                                                      |
| `label`      | `string` or `object`    | Field label (string or translations).                                                                            |
| `identifier` | `string`                | Unique field key.                                                                                                |
| `multiple`   | `boolean`               | Allow multiple selection.                                                                                        |
| `options`    | `object` or undefinable | Options for the *select filter only* when not used, the select filter will auto-fill with data from the database |
| `default`    | `array` or `string`     | Default values.                                                                                                  |
| `order`      | `integer`               | Display order (1 = first, higher numbers = lower priority).                                                      |

---

### Supported Field Types

| Type       | Notes                    |
|------------|--------------------------|
| `date`     | Date `d.m.Y`.            |
| `select`   | Dropdown selection.      |

---

### Example

```json
"filters": [
  {
    "type": "select",
    "label": "Type",
    "identifier": "DOCUMENT_TYPE",
    "default": ["Contract"],
    "multiple": false,
    "order": 1
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
    "multiple": true,
    "order": 2
  },
  {
    "type": "date",
    "label": "Date",
    "identifier": "DOCUMENT_DATE",
    "default": {
      "from": "2022-01-01",
      "to": "2022-12-31"
    },
    "order": 3
  }
]
```

---

### Notes

- `identifier` must match data keys.
- `options` is optional for `select` filters; if not provided, it will auto-fill from the database.
- `multiple` allows selecting multiple values in the filter.
- `default` can be a single value or an array for multiple selections or an object with `from` and `to` for date ranges.
- `order` determines the display order: 1 is ordered first, higher numbers appear lower in the list.
