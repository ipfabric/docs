---
description: API endpoints are available in IP Fabric. You also can take a look at the IP Fabric API documentation.
---

# Overview

IP Fabric is an API-first client, which means that every click in the user
interface (UI) has an associated API call.

## Python IP Fabric (SDK)

API-first principles allow the IP Fabric team to maintain a Software Development
Kit (SDK) that can be used for automation. While the IP Fabric main GUI is written
in TypeScript, we have chosen to write the SDK in Python, as it is the most
common language used by network engineers.

The SDK documentation can be found
at <https://gitlab.com/ip-fabric/integrations/python-ipfabric>.

While using SDK is more straightforward than calling API directly, we recommend
making yourself familiar with the rest of the documentation, as many SDK calls
map directly to API calls.

## Postman Collection

An IP Fabric Postman Collection is also available for testing API calls.
The collection can be found in the [IP Fabric Public Workspace](https://www.postman.com/ipfabric/workspace/ip-fabric-public-workspace/overview), and documentation can be found
here in [Postman Collection](../integrations/postman/index.md).

## Using API Directly

The following documentation is meant to get you started working with the API and
provide you with a tutorial on how it works.

Most of the tables within IP Fabric have a `Table description` option under the
`...` (3-dot menu) in their top-right corner. It describes how to interact with
the API, the data required in the payload, and the endpoint to send the request
to. This is the easiest way to learn how to use the API. For more information,
please see
[Table Description](../IP_Fabric_GUI/tips/navigate_in_tables.md#table-description).

Another option is to use the `Network` tab of the web
browser's `Developer tools`, which will show you the endpoints and data required
to make a successful call to the platform.

!!! example "API Blog Posts"

    Please take a look at the following blog posts about using the IP Fabric API and Python SDK:

    - [Part 1: The Basics](https://ipfabric.io/blog/api-programmability-part-1/) -- Explains creating an API token, finding the API documentation, and retrieving data using Python requests, which can be translated into other coding languages.
    - [Part 2: Python](https://ipfabric.io/blog/api-programmability-python/) -- Utilizing the official [IP Fabric Python SDK](https://pypi.org/project/ipfabric/) to retrieve data.
    - [Part 3: Webhooks](https://ipfabric.io/blog/api-programmability-part-3-webhooks/) -- Creating webhooks to further your automation journey based on IP Fabric events.
    - [Part 4: Diagramming](https://ipfabric.io/blog/api-programmability-part-4-diagramming/) -- Utilizing the official [IP Fabric Python Diagramming SDK](https://pypi.org/project/ipfabric-diagrams/) to automate the creation of Network and Path Lookup Diagrams.

## API Versioning

!!! warning "Deprecation of the path-based API versioning"

    Starting with IPF 7.5, any request whose URL contains /v7.x will still behave exactly as before,
    but the response will now include the following HTTP response headers:

    - **Deprecation: true** — signals that the endpoint is deprecated.

    - **Sunset** — indicates the date after which the deprecated behavior may be removed.

    For more information please refer to [Versioning URL schema](versioning.md#api-version-in-url-path-deprecated) section of our API documentation.

A dedicated [Versioning](versioning.md) page is now available with detailed information, including upcoming changes.

## Technology Table Endpoints

The technology tables use `POST` requests **only** for reading information, and
the payload is used to specify or filter requested data from listed tables. The
`POST` and `DELETE` requests can be used for intent verification rules at each
endpoint.

At a technology table, click `...` (3-dot button) in the top right corner of the
table and select the `Table description` option that exposes the endpoints (can
be used with filters as well):

![Table description option](table_description_option.webp)

![API Endpoint inline description](endpoint_inline_description.webp)

## Payload Definition

```jscript
{
  "attributeFilters": {},
  "columns": ["id", ...],
  "filters": {},
  "pagination": {},
  "snapshot": "<UUID|$last|$prev|$lastLocked>",
  "reports": "<FRONTEND_URL>" | ["REPORT_ID"]
}
```

- `columns` -- Specifies columns that we request for the endpoint.
- `filters` -- (Optional) Filtering options, for any column or intent
  verification.
  - Example: `"filters": {"vendor":["like","cisco"],"family":["eq","lap"],"reload":["color","eq","0"]}`
- `pagination` -- (Recommended) Specifies the pagination and response limits.
  - Example: `{"limit":1000,"start":0}`
  - It is currently recommended to query 1000 rows or fewer at a time.
- `snapshot` -- Specify the snapshot ID or use: `$last`, `$prev`
  , `$lastlocked`
  - Note: some tables (i.e., settings) do not allow the `snapshot` parameter.
- `reports` -- (Optional) Frontend URL where the reports are displayed or an
  array of report IDs as strings.
  - Examples:
    - `"reports": "/inventory/devices"`
    - `"reports": ["304796641"]`
- `attributeFilters` -- (Optional) Applies an attribute filter to the table.
  - Example: `"attributeFilters": {"siteName": ["LAB01"]}`
  - Note: some tables (i.e., settings) do not allow the `attributeFilters`
    parameter.

### Visualization of API Documentation

Refer to the example provided in the [Payload definition](#payload-definition) section for more details.

For comprehensive details on the read-only tables, please refer to our API documentation available through visual UI. It is important to note that this documentation exclusively covers API tables and does not include other endpoints.

Access the documentation at the following URL:
`https://your_ipf_instance/api/rapidoc/`
