---
description: IP Fabric supports Juniper Mist API. Juniper Mist devices are discovered only through API. Some settings to be applied that we go through on this section.
---

# Juniper Mist

Starting version **4.4.0** IP Fabric supports Juniper Mist API.

Juniper Mist devices are discovered only through API.

To add Juniper Mist to discovery global settings, go to **Settings → Advanced → Vendors API** and press the **+Add** button

## Generate API Token

1. Login to the [Juniper Mist website](https://manage.mist.com/signin.html#!signin)

   ![login](mist/mist_login.png)

   ![main gui](mist/mist_gui.png)

2. Once logged in you may proceed to open a new tab in the same browser and go to [API token generation.](https://api.mist.com/api/v1/self/apitokens)

   ![Mist API token](mist/mist_api_token.png)

3. Once generated, the API token can be used in the IP Fabric GUI.

   ![Create API token](mist/mist_api_create.png)

4. Fill in login details in the **Settings → Advanced → Vendors API** menu pressing the **+Add** button in the IP Fabric:

   ![IP Fabric API settings](mist/mist_ipf_settings.png)

## Known Issues

**Routing table** -- In the current setup there is no routing table for API endpoints so it is being created only from directly connected routes.

**ARP table** -- Cannot be fetched in the current setup as the API endpoint requires higher privileges.

**Rate limiting** -- The current rate limiting is [5000 API calls per hour](https://www.mist.com/documentation/api-rate-limiting/) and is reset at the hourly boundary. This can affect discovery speed and accuracy (some device might not be discovered). If you need more, please contact Juniper support at support@mist.com.
