# 🛠️ Shared Configuration Reference

This document describes **shared configuration features** used across all sections (Tasks, Documents, Uploads, etc.).  
Use this as a reference when building or reviewing your configuration JSON files.

---

## 📘 Universal `index.table.filters`

The `filters` array in `index.table` is **supported for all index tables**, regardless of section type.

### Example

```json
"filters": [
  {
    "type": "select",
    "label": {
      "en_CH": "Type",
      "de_CH": "Typ"
    },
    "default": ["Sonstiges"],
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

### Behavior

✅ **Select Filters**
- If `multiple` is `true`, users can pick multiple options.
- If `options` is omitted, unique values are detected automatically.
- If `default` is provided, the filter is pre-filled.

✅ **Date Filters**
- Renders a `from` and `to` date range picker.
- Filters records between the specified dates.

---

## 🌍 Label Translation

**Labels** (`label`) support multilingual configurations:

| Format         | Example                                  |
|----------------|------------------------------------------|
| String         | `"label": "Subject"`                    |
| Translations   | `"label": { "en_CH": "Subject", "de_CH": "Betrteff" }` |

**How it works:**
- The application selects the label matching the user’s locale.
- If no matching locale is found, it falls back to displaying the raw object.

---

## ✨ Common Field Properties

Most field definitions—whether for **columns**, **filters**, **infolist entries**, or **form fields**—support the following properties:

| Property      | Type                 | Description                                                |
|---------------|----------------------|------------------------------------------------------------|
| `type`        | `string`             | Field type (see below).                                   |
| `label`       | `string` or `object` | Field label (plain string or translations).              |
| `identifier`  | `string`             | Unique field key (must match your data source).          |
| `sortable`    | `boolean`            | *(Columns only)* Enable sorting.                          |
| `multiple`    | `boolean`            | *(Select filters only)* Allow multiple selections.       |
| `default`     | `array` or `object`  | *(Filters only)* Default selected values or ranges.      |
| `rules`       | `array`              | *(Forms/Uploads only)* Validation rules.                 |
| `value`       | `string` or `boolean`| *(Forms/Uploads only)* Default value or `true` to auto-fill. |

---

## 🧩 Supported Field Types

Below is the list of supported `type` values across all sections:

| Type       | Where Used                | Notes                                      |
|------------|---------------------------|--------------------------------------------|
| `string`   | Columns, Filters, Forms   | Standard text.                             |
| `integer`  | Columns, Infolist         | Numeric values.                            |
| `date`     | Columns, Filters, Infolist| Dates formatted as `d.m.Y`.                |
| `select`   | Filters                    | Dropdown selection.                        |
| `textarea` | Infolist, Forms           | Longer text (description, comments).       |
| `hidden`   | Forms, Uploads            | Hidden field with static or dynamic value. |

---

## 📂 Default Behaviors

- **Sorting**  
  If `sortable: true`, the column becomes sortable. For `date` columns, sorting uses the `STR_TO_DATE` function if stored as string.

- **Searching**  
  All table columns are **searchable by default**.

- **Default Filter Values**  
  Filters with a `default` are pre-selected when the page loads.

---

## 🪧 Best Practices

✅ **Keep identifiers consistent**  
Always ensure your `identifier` values match the data keys returned by your backend.

✅ **Avoid unused fields**  
Only define fields that will be rendered in your UI.

✅ **Leverage translations**  
Use multilingual `label` objects to provide a localized experience.

✅ **Validate uploads**  
Use `rules` on upload fields to enforce constraints (e.g., max length).
