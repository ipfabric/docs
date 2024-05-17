---
description: This section contains information on how to set up API discovery for Versa. Versa devices are discovered through the API (or the combination of API and CLI).
---

# Versa Networks SD-WAN

Starting with version `3.8.0`, IP Fabric supports the Versa SD-WAN API. The API is based on HTTPS authentication.

Since version `6.8.0`, IP Fabric supports discovering Versa devices in combined (hybrid) mode.

To add Versa to the global discovery settings, go to **Settings --> Discovery &
Snapshots --> Discovery Settings --> Vendors API**, click **+ Add**, and select
`Versa` from the list.

Versa requires the following settings to be applied:

- **Username** -- Username for Versa Director to access API data.
- **Password** -- Password for Versa Director access API data.
- **Base URL** -- Base URL of Versa Director. If the API isn't available on
  the default port `9182`, add a port part to the URL (e.g., `https://server:4443/`).
- [**Slug**](index.md#slug-and-comment)

Optionally, you may enable **Allow API+CLI combined discovery**, which allows the retrieval of data partially using API calls and partially using CLI commands.

!!! note

    OAuth-based authentication for Versa Director is not supported.

## Known Issue

- [HTTP 500 Error `AsyncRequestTimeoutException`](../../../../support/known_issues/Vendors/versa.md)
