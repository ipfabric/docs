---
description: IP Fabric uses API only to collect information that cannot be retrieved from CLI logs. To discover Check Point devices, CLI access also needs to be...
---

# Check Point

We use API only to collect information that cannot be retrieved from CLI logs. To discover Check Point devices, CLI access also needs to be available. Check Point requires the following settings to be applied:

- **API Key** -- Available in version `R80.40` and above (API `v1.6`). To generate the key, use Check Point SmartConsole, and select **API Key** as user's Authentication method **or**
- **Username** -- Username to access API data
- **Password** -- Password to access API data
- **Base URL** -- Base URL for API calls, for example `https://management.server.domain.tld`. If the API isn't available on the default port 443, add a port part to the URL (`https://server:4443/`)
- **Collect following domains** -- Mandatory only if the **Base URL** points to a Multi-Domain Server. Please verify, that all selected domains can be accessed by the provided credentials.
- [**Slug**](index.md#slug-and-comment)

Don't forget to add IPF appliance to the list of allowed clients.

In SmartConsole, go to **Manage & Settings --> Blades** and click **Advanced Settings** in the **Management API** section to verify, from where are API calls allowed.

In case that you use setting **All IP addresses that can be used for GUI clients**, don't forget to add IPF appliance address to **Manage & Settings --> Permissions** and **Administrators --> Trusted Clients**.

In case you use Multi-Domain server, all necessary settings are in Multi Domain menu (i.e.: **Multi Domain --> Blades**)
