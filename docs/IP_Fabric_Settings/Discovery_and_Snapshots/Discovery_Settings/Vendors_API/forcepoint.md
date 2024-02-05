---
description: IP Fabric supports Forcepoint SMC API. Forcepoint devices are discovered though CLI and only configuration references like security rules are downloaded via the SMC API.
---

# Forcepoint

Starting version `6.1.0`, IP Fabric supports Forcepoint SMC API. Forcepoint devices are discovered though CLI and only configuration references like security rules are downloaded via the SMC API.

## How to Add Forcepoint SMC to IP Fabric

### Generate API Token

1. Log in to the Forcepoint SMC Web UI.

   ![Forcepoint login page](forcepoint/smc/forcepoint_login_page.png)

2. Generate API tokens

   - Click **Configuration**.
   - Open **Configuration --> Administration --> Access Rights --> API Clients** and select **New**.

   ![location where to find the API key generation](forcepoint/smc/forcepoint_generate_api_token.png)

3. Add some name for the newly created entry and **copy the token**. When the settings are saved, the **token will be hidden**. Also add read access privileges.

   ![creating new API key](forcepoint/smc/forcepoint_generate_token.png)

4. API endpoint needs to be enabled explicitly, as it is disabled by default.

   - Click **Home**
   - Go to **Other** section on the left sidebar.
   - Find your management server that you will use to query the data.
   - Go to **SMC API** section where in the tab, you must enable it, and you can also specify other parameters.

   ![enabling SMC API](forcepoint/smc/forcepoint_enable_api.png)

### Add Forcepoint to Vendors API in IP Fabric

To add Forcepoint to discovery global settings, go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors API** in IP Fabric, click **+ Add**, select `Forcepoint` from the list and fill in:

- **Base URL** -- URL which you specified when enabling the SMC API, for example `http://X.X.X.X:8082`.
- **Authentication Key** -- generated authentication API key from the SMC.
- [**Slug**](index.md#slug-and-comment)

  ![adding vendor](forcepoint/smc/forcepoint_ipf_add_vendor.png)

## Known Issue

`ip_list` -- Output data cannot be used as when tried, SMC API is returning unusable data.
