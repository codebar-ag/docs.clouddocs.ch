# API Documentation

<!-- TOC -->
* [API Documentation](#api-documentation)
  * [Introduction](#introduction)
  * [Environment Variables](#environment-variables)
  * [Authentication](#authentication)
  * [Base URL](#base-url)
  * [Postman Collection](#postman-collection)
  * [API Endpoints](#api-endpoints)
<!-- TOC -->

## Introduction

This section provides comprehensive documentation for the CloudDocs API. The API allows you to programmatically manage tenants, clients, and other resources in the CloudDocs system.

All API requests require authentication using Bearer tokens. The API follows RESTful conventions and returns JSON responses.

---

## Environment Variables

To use the API, you need to configure the following environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `API_URL` | Base URL for the API | `https://api.portal.clouddocs.test` |
| `API_VERSION` | API version | `v1` |
| `API_USERNAME` | Username for authentication | `info@codebar.ch` |
| `API_TOKEN` | Bearer token for API authentication | `12|dlvRcU2HwHMisU2ZJZELsqxJTwHhhPSAIZ5mLpcQ0cc5b871` |

**Note:** For local development, use `https://api.portal.clouddocs.test`. For production, use the appropriate production API URL.

---

## Authentication

All API requests require authentication using a Bearer token. Include the token in the `Authorization` header:

```
Authorization: Bearer {{API_TOKEN}}
```

The `{{API_TOKEN}}` should be replaced with your actual API token from the environment variables.

**Example Request Header:**
```
Authorization: Bearer 12|dlvRcU2HwHMisU2ZJZELsqxJTwHhhPSAIZ5mLpcQ0cc5b871
Content-Type: application/json
```

---

## Base URL

The API base URL is constructed as follows:

```
{{API_URL}}/{{API_VERSION}}
```

**Example:**
```
https://api.portal.clouddocs.test/v1
```

All endpoints are relative to this base URL. For example:
- Create Tenant: `POST {{API_URL}}/{{API_VERSION}}/resources/tenants/store`
- Full URL: `POST https://api.portal.clouddocs.test/v1/resources/tenants/store`

---

## Postman Collection

We provide a Postman collection with pre-configured requests and environment variables.

**Postman Collection:** [View in Postman](https://clouddocs.postman.co/workspace/CloudDocs-AG~4511def7-f2a1-4315-bff9-2d1ddba11056/collection/25610371-c29039fa-8f93-4188-82bf-11767ffe6133?action=share&source=copy-link&creator=25610371)

To use the Postman collection:

1. Import the collection into Postman
2. Set up the environment variables:
   - `API_URL`: Your API base URL
   - `API_VERSION`: API version (typically `v1`)
   - `API_USERNAME`: Your username
   - `API_TOKEN`: Your Bearer token
3. Select the appropriate environment (e.g., "00 - LOCAL | portal.clouddocs.test")
4. Start making API requests

---

## API Endpoints

- [Tenants API](Tenants.md) - Manage tenants

