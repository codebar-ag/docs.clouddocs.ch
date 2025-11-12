# Query

<!-- TOC -->
* [Query](#query)
  * [Introduction](#introduction)
  * [Quick Start](#quick-start)
    * [Basic Filter Structure](#basic-filter-structure)
    * [Minimal Example](#minimal-example)
  * [Filter Structure](#filter-structure)
    * [Required Fields](#required-fields)
    * [Attribute Rules](#attribute-rules)
  * [Operators Reference](#operators-reference)
    * [WHERE Operator](#where-operator)
    * [WHEREIN Operator](#wherein-operator)
    * [WHERENOTIN Operator](#wherenotin-operator)
    * [WHERENULL Operator](#wherenull-operator)
    * [WHERENOTNULL Operator](#wherenotnull-operator)
    * [CONTAINS Operator](#contains-operator)
<!-- TOC -->

## Introduction

Query filters provide a powerful way to filter items by querying JSON fields stored in the `fields` column. This guide provides quick reference examples and common patterns for using query filters effectively.

**Key Points:**
- Filters are applied at Tenant → Client → Section levels (in order)
- All filters use AND logic (all conditions must match)
- Operators are case-insensitive
- Supports dynamic value injection based on current user/client context

---

## Quick Start

### Basic Filter Structure

```json
{
  "filters": [
    {
      "attribute": "DOCU_WARE_FIELD_NAME",
      "operator": "OPERATOR",
      "value": "value_if_needed"
    }
  ]
}
```

### Minimal Example

```json
{
  "filters": [
    {
      "attribute": "DOCU_WARE_STATUS",
      "operator": "WHERE",
      "value": "active"
    }
  ]
}
```

---

## Filter Structure

### Required Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `attribute` | string | ✅ Yes | Field name in JSON `fields` column |
| `operator` | string | ✅ Yes | Comparison operator (case-insensitive) |
| `value` | mixed | ⚠️ Conditional | Required for WHERE, WHEREIN, WHERENOTIN, CONTAINS |

### Attribute Rules

- Alphanumeric characters (a-z, A-Z, 0-9)
- Underscores (`_`)
- Hyphens (`-`)
- Periods (`.`)
- Examples: `"OBJEKT"`, `"CLOUD_DOCS_USER_IDENTIFIERS"`, `"1306"`, `"field.name"`

---

## Operators Reference

### WHERE Operator

**Purpose:** Exact equality match

**Requires Value:** ✅ Yes

**Example:**
```json
{
  "filters": [
    {
      "attribute": "DOCU_WARE_STATUS",
      "operator": "WHERE",
      "value": "active"
    }
  ]
}
```

**Use Cases:**
- Exact string matching
- Boolean values (use `"true"` or `"false"` as strings)
- Numeric values
- With injected field values

**Examples:**

```json
// String value
{"attribute": "NAME", "operator": "WHERE", "value": "John Doe"}

// Boolean (use string "true" or "false")
{"attribute": "PUBLISHED", "operator": "WHERE", "value": "true"}

// With injected value
{"attribute": "CLIENT_ID", "operator": "WHERE", "value": "CLIENT::IDENTIFIER"}

// Numeric
{"attribute": "PRIORITY", "operator": "WHERE", "value": "5"}
```

**SQL Equivalent:**
```sql
WHERE fields->>'DOCU_WARE_STATUS' = 'active'
```

---

### WHEREIN Operator

**Purpose:** Check if field value is in a list

**Requires Value:** ✅ Yes (must be array)

**Example:**
```json
{
  "filters": [
    {
      "attribute": "STATUS",
      "operator": "WHEREIN",
      "value": ["active", "pending", "review"]
    }
  ]
}
```

**Use Cases:**
- Multiple possible values
- Status filtering
- Category filtering

**Examples:**

```json
// Multiple statuses
{"attribute": "STATUS", "operator": "WHEREIN", "value": ["active", "pending"]}

// With injected values
{"attribute": "CLIENT_ID", "operator": "WHEREIN", "value": ["CLIENT::IDENTIFIER", "other_id"]}

// Single value (still use array)
{"attribute": "TYPE", "operator": "WHEREIN", "value": ["document"]}
```

**SQL Equivalent:**
```sql
WHERE fields->'STATUS' IN ('active', 'pending', 'review')
```

**⚠️ Important:** Value must be an array, even for single values.

---

### WHERENOTIN Operator

**Purpose:** Check if field value is NOT in a list

**Requires Value:** ✅ Yes (must be array)

**Example:**
```json
{
  "filters": [
    {
      "attribute": "STATUS",
      "operator": "WHERENOTIN",
      "value": ["archived", "deleted"]
    }
  ]
}
```

**Use Cases:**
- Excluding specific values
- Filtering out archived/deleted items
- Negative filtering

**Examples:**

```json
// Exclude archived items
{"attribute": "STATUS", "operator": "WHERENOTIN", "value": ["archived", "deleted"]}

// Exclude specific IDs
{"attribute": "ITEM_ID", "operator": "WHERENOTIN", "value": ["123", "456"]}
```

**SQL Equivalent:**
```sql
WHERE fields->'STATUS' NOT IN ('archived', 'deleted')
```

**⚠️ Important:** Value must be an array.

---

### WHERENULL Operator

**Purpose:** Check if field is null or missing

**Requires Value:** ❌ No

**Example:**
```json
{
  "filters": [
    {
      "attribute": "OBJEKT",
      "operator": "WHERENULL"
    }
  ]
}
```

**Use Cases:**
- Finding incomplete records
- Missing data detection
- Optional field filtering

**Examples:**

```json
// Single null check
{"attribute": "EMAIL", "operator": "WHERENULL"}

// Multiple null checks (all must be null)
{
  "filters": [
    {"attribute": "OBJEKT", "operator": "WHERENULL"},
    {"attribute": "MIETER", "operator": "WHERENULL"},
    {"attribute": "MIETVERHALTNIS", "operator": "WHERENULL"}
  ]
}
```

**SQL Equivalent:**
```sql
WHERE fields->'OBJEKT' IS NULL
```

**Note:** The `value` field is ignored for this operator.

---

### WHERENOTNULL Operator

**Purpose:** Check if field exists and is not null

**Requires Value:** ❌ No

**Example:**
```json
{
  "filters": [
    {
      "attribute": "EMAIL",
      "operator": "WHERENOTNULL"
    }
  ]
}
```

**Use Cases:**
- Ensuring required fields exist
- Filtering complete records
- Data validation

**Examples:**

```json
// Check field exists
{"attribute": "ASSIGNED_TO", "operator": "WHERENOTNULL"}

// Ensure multiple fields exist
{
  "filters": [
    {"attribute": "NAME", "operator": "WHERENOTNULL"},
    {"attribute": "EMAIL", "operator": "WHERENOTNULL"},
    {"attribute": "PHONE", "operator": "WHERENOTNULL"}
  ]
}
```

**SQL Equivalent:**
```sql
WHERE fields->'EMAIL' IS NOT NULL
```

**Note:** The `value` field is ignored for this operator.

---

### CONTAINS Operator

**Purpose:** Check if JSON array field contains a value

**Requires Value:** ✅ Yes (single value, not array)

**Example:**
```json
{
  "filters": [
    {
      "attribute": "CLOUD_DOCS_USER_IDENTIFIERS",
      "operator": "CONTAINS",
      "value": "USER_CLIENT::IDENTIFIER"
    }
  ]
}
```

**Use Cases:**
- Array membership checks
- Tag filtering
- User identifier arrays
- Multi-value field searches

**Examples:**

```json
// Check array contains value
{"attribute": "TAGS", "operator": "CONTAINS", "value": "important"}

// With injected value
{"attribute": "USER_IDS", "operator": "CONTAINS", "value": "USER::UUID"}

// Check user identifier in array
{"attribute": "CLOUD_DOCS_USER_IDENTIFIERS", "operator": "CONTAINS", "value": "USER_CLIENT::IDENTIFIER"}
```

**SQL Equivalent:**
```sql
WHERE JSON_CONTAINS(fields->'CLOUD_DOCS_USER_IDENTIFIERS', '"value"')
```

**⚠️ Important:**
- The field must be a JSON array
- Value should be a single value (string, number), not an array
- Works with injected field values

---
