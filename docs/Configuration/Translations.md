## Label Translation

<!-- TOC -->
  * [Label Translation](#label-translation)
    * [String Example](#string-example)
    * [Translation Object Example](#translation-object-example)
    * [Supported Locales](#supported-locales)
<!-- TOC -->

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

**Notes:**

- The application automatically selects the label that matches the user’s locale.
- All translation keys must be valid locale codes, e.g., `en_CH`, `de_CH`.
