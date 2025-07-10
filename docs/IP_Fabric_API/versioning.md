---
description: Information about how we implement versioning of our API endpoints.
---

# Versioning

Starting with version `5.0`, we have adopted a rather fast-moving API versioning
schema. This allows for tighter control over the changes and provides an
opportunity for maintaining backward compatibility for a manageable time frame.

The design still leverages API version directly in the URL over alternative approaches,
such as the extended Accept header. This allows for unambiguous exchange of state
between IP Fabric and customers; nothing more than the URL is needed to identify the
resource being accessed.



## URL Schema a Version in URL

!!! warning "Deprecation of the path-based API versioning"

    We are deprecating the path-based API version identifier (/v7.x) in favor of header-based versioning.
    This change will be announced in the next release, together with migration steps and full documentation.

    Starting with IPF 7.5, any request whose URL contains /v7.x will still behave exactly as before, 
    but the response will now include the following HTTP response headers:

    - **Deprecation: true** — signals that the endpoint is deprecated.

    - **Sunset** — indicates the date after which the deprecated behavior may be removed.

The URL schema looks like:

```shell
https://{hostname}/api/v{major}.{minor}/{resource_path}
```

we use the following shortened version throughout the documentation:

```shell
/api/{api_version}/{resource_path}
```

where:

- `major` and `minor` follow the release version of the platform. So, if
  version `4.4.3` of the IP Fabric platform is deployed, its latest API path
  would be `/api/v4.4/`.

- The whole `.{minor}` is optional, and it is treated as `0` if omitted.

- `{api_version}` stands for the complete version string. For example, `v5.1`.
  Please mind the `v` prefix.

## API Version Deprecation and Allowed Changes

IP Fabric commits to keeping support for all `minor` versions within the particular
`major` version (so, for example, in version `5.4.3`, we allow `/api/v5.1/`
calls). But API may break between major releases.

We call a major release a release that introduces some complex functionality.
This typically means a large code refactoring, changes to the data model, etc.
Keeping backward compatibility is frequently not feasible in such
cases (for example, `v3` brought support for snapshots, `v4` brought graphs, `v5` RBAC).

Naturally, backward-compatible changes (typically addition of a new attribute)
don't need to be gated and can appear in responses even when an older API version
is used within the request.

Changes and depreciations are communicated via the API documentation
and [release notes](../releases/index.md). We will mark attributes
as `deprecated: true` in the OpenAPI schema when we fully migrate to the OpenAPI
3.0+ Specification.

Responses made with `minor < release_minor` will contain a custom header warning
the client about the use of a potentially old API. We leverage
the [IETF Draft for Deprecation header](https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-deprecation-header). It is included and set to `true` (`Deprecation: true`) in every response to
a call made with an older than the current API version.

Requests made with `major < release_major` (obsolete version) will be refused
with the HTTP code `410 Gone` (`406 Not Acceptable` would also be reasonable, but we
explicitly mention this in the apidoc in relationship with the `Accept` header; so
not to confuse these two, the `410` was selected).

Requests made with an API version newer than the currently supported version are
also refused with `410 Gone` (while `404` or `406` would be probably closer
semantically, we don't want to confuse clients and keep `410` for all
version-related errors).

The error body, in both cases, is a JSON depicting current platform version as well
as the current API version:

```json
{
  "message": "Unsupported API version used.",
  "release_version": "5.4.2+1",
  "api_version": "v5.4"
}
```

This may look excessive at first, but it is to promote the client code to be
changed with every update, as to keep track with all small changes and updates
we bring. But in reality, clients would typically be fine if they update the API
version when moving to the new major release only. Frequently, the client code
will not change, except for the API version. Thus, we recommend using a global
constant for it.
