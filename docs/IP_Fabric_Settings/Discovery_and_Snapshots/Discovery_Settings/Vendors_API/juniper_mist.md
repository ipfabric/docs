---
description: This section contains information on how to set up API discovery for Juniper Mist.
---

# Juniper Mist

Starting with version `4.4.0`, IP Fabric supports the Juniper Mist API.

Juniper Mist devices are discovered only through the API.

## Generate API Token

1. Log in to the [Juniper Mist website](https://manage.mist.com/signin.html#!signin):

   ![Juniper Mist login page](mist/mist_login.png)

   ![Juniper Mist main GUI](mist/mist_gui.png)

2. Once logged in, open a new tab in the same browser and go to the [API token generation](https://api.mist.com/api/v1/self/apitokens) page:

   ![Create API token](mist/mist_api_token.png)

3. Once generated, the API token can be used in the IP Fabric GUI.

   ![Create API token - copy generated API token](mist/mist_api_create.png)

4. In the IP Fabric GUI, go to **Settings --> Discovery & Snapshots -->
   Discovery Settings --> Vendors API**, click **+ Add**, select `Juniper Mist`
   from the list, and fill in the fields:

   ![Add Connection - Juniper Mist](mist/mist_ipf_settings.png)

## Known Issues

- **Routing table** -- In the current setup, there is no routing table for API endpoints, so it is created only from the directly connected routes.

- **ARP table** -- Cannot be fetched in the current setup as the API endpoint requires higher privileges.

- **Rate limiting** -- The current rate limiting is [5000 API calls per hour](https://www.mist.com/documentation/api-rate-limiting/) and is reset at the hourly boundary. This can affect discovery speed and accuracy (some devices might not be discovered). If you need more information, please contact Juniper support at <support@mist.com>.
