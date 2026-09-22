---
description: Information about how we implement versioning of our API endpoints.
---

# Versioning

Starting with IP Fabric `7.5`, each API endpoint is versioned independently.
This allows us to evolve the API faster and independently on the product version,
without breaking your existing integrations.

You can select a specific endpoint version by including the `X-API-Version` header in your request.
It contains an integer value and this header should be provided for any request.

**Request Example:**

```shell
# Explicitly request version 1 of the /snapshots endpoint
curl --request GET \
     --url https://your_ipf_instance/api/snapshots \
     --header "Accept: application/json" \
     --header "X‑API‑Version: 1"
```

**Default Behavior:**

If the `X-API-Version` header is omitted, your request will automatically use the default version of the endpoint.

## Understanding Changes

A new endpoint version is created only when a change breaks backward compatibility.

- Breaking Changes: Examples include removing/renaming a parameter or a response field. Endpoints that have never had a breaking change remain at version 1.

- Non-Breaking Changes: Backward-compatible changes, like adding a new attribute to a response, do not result in a new version.

**Best Practice:** Your application should be designed to gracefully handle and ignore any unexpected fields in API responses.


## Tracking Versions

Every API response includes headers to help you track which version was used:

- `X-API-Versions-Supported`: A comma-separated list of all versions the endpoint supports (e.g., `1,2,3`).

- `X-API-Version-Used`: The specific version that processed your request.

- `X-Product-Version`: The version of the IP Fabric product that handled the request (e.g., `v7.5`).

## Error Handling

A request with an invalid or unsupported `X-API-Version` header receives an `HTTP 410 Gone` response.
We use `HTTP 410 Gone` consistently for endpoint version errors to provide a distinct signal,
avoiding confusion with other statuses like `HTTP 404 Not Found` and `HTTP 406 Not Acceptable`.

The error response body is a JSON object containing the latest supported version for that endpoint:

```json
{
  "message": "Unsupported API version requested.",
  "release_version": "7.5.0+1",
  "api_version": "2"
}
```

## Deprecation Strategy

To allow us to move forward and improve the overall quality of an API we will occasionally need to deprecate
certain API endpoints and their older versions.

We are communicating these changes via API documentation
and [release notes](../releases/index.md) with an every new release. We will mark attributes
as `deprecated: true` in the OpenAPI schema when we fully migrate to the OpenAPI 3.0+ Specification.

While a deprecated version is still callable, each such response includes headers:

- `Deprecation` returns boolean value indicating that a requested version entered a deprecation cycle.
- `Sunset` returns the exact date in the RFC3339 format after which the version might be permanently unavailable without further notice.
