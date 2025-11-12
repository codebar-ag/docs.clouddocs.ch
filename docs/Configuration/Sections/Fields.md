# Fields

<!-- TOC -->
* [Injected Field Values](#injected-field-values)
  * [Query - Injected Field Values Matrix](#query---injected-field-values-matrix)
  * [Sections - Injected Field Values Matrix](#sections---injected-field-values-matrix)
  * [Usage](#usage)
  * [Developer Notes](#developer-notes)
<!-- TOC -->

## Injected Field Values

Injected field values are special identifiers that can be used in field configurations to automatically populate values from the system context. These values are resolved at runtime and provide access to various system entities like items, clients, users, and upload requests.

### Query - Injected Field Values Matrix

The following table shows injected field values available for **building queries** in all sections:

| Identifier | Description |
|------------|-------------|
| `CLIENT::UUID` | Client UUID |
| `CLIENT::IDENTIFIER` | Client Identifier |
| `CLIENT::IDENTIFIER_INTERNAL` | Client Identifier Internal |
| `USER::UUID` | User UUID |
| `USER::NAME` | User Name |
| `USER::EMAIL` | User Email |
| `USER_CLIENT::IDENTIFIER` | User Client Identifier |

**Example - Using Injected Field Values in Queries:**

```json
{
  "filters": [
    {
      "value": "USER::EMAIL",
      "operator": "WHERE",
      "attribute": "DOCU_WARE_USER_EMAIL"
    }
  ]
}
```

### Sections - Injected Field Values Matrix

The following table shows injected field values available for use in **section field configurations**:

| Identifier | Description |
|------------|-------------|
| `ITEM::UUID` | Item UUID |
| `ITEM::SOURCE_DOC_ID` | Item Source Doc ID |
| `ITEM::DOC_ID` | Item Doc ID |
| `CLIENT::UUID` | Client UUID |
| `CLIENT::IDENTIFIER` | Client Identifier |
| `CLIENT::IDENTIFIER_INTERNAL` | Client Identifier Internal |
| `USER::UUID` | User UUID |
| `USER::NAME` | User Name |
| `USER::EMAIL` | User Email |
| `USER_CLIENT::IDENTIFIER` | User Client Identifier |
| `USER_UPLOAD_REQUEST::UUID` | User Upload Request UUID |
| `USER_TASK_REQUEST::UUID` | User Task Request UUID |
| `USER_WORKFLOW_REQUEST::UUID` | User Workflow Request UUID |
| `USER_REQUEST_FILE::UUID` | User Request File UUID |
| `USER_REQUEST_FILE::NAME` | User Request File Name |
| `USER_REQUEST_FILE::NAME_WITHOUT_EXTENSION` | User Request File Name Without Extension |

### Usage

Injected field values can be used in the `value` property of field configurations. They are typically used in hidden fields or as default values to automatically populate fields with system context data.

**Example:**

```json
{
  "fields": [
    {
      "type": "hidden",
      "label": {
        "de_CH": "Kunde Identifikation",
        "en_CH": "Client Identifier"
      },
      "rules": [],
      "value": "CLIENT::IDENTIFIER",
      "data_type": null,
      "identifier": "CLIENT_KEY",
      "injected": true
    }
  ]
}
```

**Note:** When using injected field values, set the `value` property to the identifier string (e.g., `"CLIENT::IDENTIFIER"`). **It is crucial to set `injected: true`** - otherwise the system will skip the injected field value. The system will automatically resolve and inject the actual value at runtime when `injected: true` is set.

## Developer Notes

The logic to maintain injected field values is within the `InjectedFieldService` class:

```php
namespace App\Services;

class InjectedFieldService {}
```

The injected field value identifiers are defined in the `InjectedFieldValueEnum` enum:

```php
namespace App\Enums\App;

enum InjectedFieldValueEnum: string {}
```
