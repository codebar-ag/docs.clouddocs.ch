# Tenants API

<!-- TOC -->
* [Tenants API](#tenants-api)
  * [Introduction](#introduction)
  * [Create Tenant](#create-tenant)
    * [Endpoint](#endpoint)
    * [Request](#request)
    * [Response](#response)
    * [Status Codes](#status-codes)
<!-- TOC -->

## Introduction

This section documents the Tenants API endpoints for managing tenants in the CloudDocs system. Tenants represent organizations or companies that use the CloudDocs platform.

For general API information, authentication, and environment setup, see the [API Documentation](API.md).

---

## Create Tenant

Create a new tenant in the system.

### Endpoint

```
POST {{API_URL}}/{{API_VERSION}}/resources/tenants/store
```

**Full URL Example:**
```
POST https://api.portal.clouddocs.test/v1/resources/tenants/store
```

### Request

**Headers:**

| Header | Value |
|--------|-------|
| `Authorization` | `Bearer {{API_TOKEN}}` |
| `Content-Type` | `application/json` |

**Request Body:**

```json
{
  "name": "codebar Solutions AG",
  "street": "Langegasse 39",
  "postcode": "4104",
  "place": "Oberwil",
  "uid": "CHE-257.955.682",
  "website": "https://www.codebar.ch",
  "email": "info@codebar.ch",
  "phone": "+41 61 515 60 90",
  "configuration": null,
  "query": {
    "filters": [
      {
        "value": "Ja",
        "operator": "where",
        "attribute": "CLOUD_DOCS_ENABLED"
      }
    ]
  }
}
```

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | ✅ Yes | Tenant name |
| `street` | string | ✅ Yes | Street address |
| `postcode` | string | ✅ Yes | Postal code |
| `place` | string | ✅ Yes | City/Place |
| `uid` | string | ⚠️ Optional | UID identifier (e.g., CHE-257.955.682) |
| `website` | string | ⚠️ Optional | Website URL |
| `email` | string | ⚠️ Optional | Email address |
| `phone` | string | ⚠️ Optional | Phone number |
| `configuration` | object/null | ⚠️ Optional | Configuration object |
| `query` | object | ⚠️ Optional | Query filters configuration. See [Query Configuration](../Configuration/Sections/Query.md) for details |

---

### Response

**Success Response (201 Created):**

```json
{
  "data": {
    "id": 20,
    "uuid": "019a784d-b58d-7030-b544-01308c74a581",
    "name": "codebar Solutions AG",
    "street": "Langegasse 39",
    "postcode": "4104",
    "place": "Oberwil",
    "uid": "CHE-257.955.682",
    "website": "https://www.codebar.ch",
    "email": "info@codebar.ch",
    "email_label": null,
    "phone": "+41 61 515 60 90",
    "phone_label": null,
    "configuration": null,
    "query": {
      "filters": [
        {
          "value": "Ja",
          "operator": "where",
          "attribute": "CLOUD_DOCS_ENABLED"
        }
      ]
    },
    "created_at": "2025-11-12T13:42:30.000000Z",
    "updated_at": "2025-11-12T13:42:30.000000Z"
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `data.id` | integer | Internal tenant ID |
| `data.uuid` | string | Unique tenant identifier (UUID) |
| `data.name` | string | Tenant name |
| `data.street` | string | Street address |
| `data.postcode` | string | Postal code |
| `data.place` | string | City/Place |
| `data.uid` | string | UID identifier |
| `data.website` | string | Website URL |
| `data.email` | string | Email address |
| `data.email_label` | string/null | Email label |
| `data.phone` | string | Phone number |
| `data.phone_label` | string/null | Phone label |
| `data.configuration` | object/null | Configuration object |
| `data.query` | object | Query filters configuration |
| `data.created_at` | string | Creation timestamp (ISO 8601 format) |
| `data.updated_at` | string | Last update timestamp (ISO 8601 format) |

---

### Status Codes

| Status Code | Description |
|-------------|-------------|
| `201 Created` | Tenant successfully created |
| `400 Bad Request` | Invalid request data or validation errors |
| `401 Unauthorized` | Missing or invalid authentication token |
| `422 Unprocessable Entity` | Validation failed for one or more fields |

**Error Response Example (422):**

```json
{
  "message": "The given data was invalid.",
  "errors": {
    "name": ["The name field is required."],
    "email": ["The email must be a valid email address."]
  }
}
```

**Notes:**

- The `query` object follows the same structure as described in the [Query Configuration](../Configuration/Sections/Query.md) documentation.
- The `operator` value in query filters is case-insensitive (e.g., `"where"` is equivalent to `"WHERE"`).
- The `uuid` field is automatically generated and can be used as a unique identifier for the tenant.
- All timestamps are returned in ISO 8601 format (UTC).

