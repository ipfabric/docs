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

Requests for an invalid or unsupported version will receive an `HTTP 410 Gone` response.
We use `HTTP 410 Gone` consistently for all version-related errors to provide a distinct signal,
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


## API Version in URL Path [Deprecated]

We are deprecating the path-based API version identifier (`/v7.x`) in favor of header-based versioning.

Starting with IP Fabric `7.5`, any request whose URL contains `/v7.x` will still behave exactly as before, 
but the response will now include the following HTTP response headers:

- **Deprecation: true** -- signals that the endpoint is deprecated.

- **Sunset** -- indicates the date after which the deprecated behavior may be removed.

After the sunset date, the endpoint may return the HTTP `410 Gone` without further notice.

### What is Changing

|                                 | **Previously (Deprecated)**                             | **Currently (Supported)**                                                                |
|---------------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Endpoint**                    | `https://your_ipf_instance/api/v7.5/snapshots`          | `https://your_ipf_instance/api/snapshots`                                                |
| **Additional response headers** | `Deprecation: true`  <br>`Sunset: 2026-02-01T00:00:00Z` | `X‑API‑Version: 1`  <br>`X-API-Versions-Supported: 1`  <br>`X-Product-Version: v7.5` |
| **Response payload**            | _Unchanged_                                             | _Unchanged_                                                                              |

No functional behaviour is altered -- you can migrate by **simply removing** `/v7.x` from the path.

### Migration Guide

1. **Remove the `/v7.5` segment** from every request URL.
2. **Verify** that your integration treats the response identically (payloads are unchanged).
3. **Update SDKs or client wrappers** if they hard‑code the version segment.
4. **Monitor** for any warnings or errors during testing.

#### Example

```http
# Deprecated request
GET /api/v7.5/snapshots HTTP/1.1
Host: localhost
```

```http
# Preferred request
GET /api/snapshots HTTP/1.1
Host: localhost
```

### Timeline

- **Jul 1, 2025** -- deprecation announced. `Deprecation: true` and `Sunset` headers activated.
- **Feb 1, 2026 00:00 UTC** -- sunset date. The `/v7.5` path **may be removed** at, or any time after this point.

We strongly recommend completing your migration **well before** the sunset date.

### Frequently Asked Questions

**Will anything break before the sunset date?**

No. Until the sunset date, requests containing `/v7.x` continue to work unchanged.

**Do I need to set a new header?**

No. You only need to remove `/v7.x` from the request path. No additional headers are required on your side.

**How can I test now?**

Issue calls **without** the version segment in your staging or sandbox environment.
The responses are identical, so you can compare outputs directly.

**Where can I get help?**

For assistance and related questions, reach out to our team for [Technical Support](https://docs.ipfabric.io/main/support).
