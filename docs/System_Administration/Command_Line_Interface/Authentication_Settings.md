---
description: This section describes the Authentication Settings available in the IP Fabric CLI.
---

# Authentication Settings

--8<-- "snippets/cli_root_access.md"

Several IP Fabric authentication settings can be modified via the CLI. 

## Disabling Local Authentication

In case you don't want to use local authentication (username/password) and want
to log in only via SSO or LDAP, you can disable it via the CLI settings (both
token and basic authentication will be disabled). Please note that
[API Tokens](../../IP_Fabric_Settings/integration/api_tokens.md) will still work.

This will remove the username and password fields from the login page (unless LDAP is configured on the appliance).

1. Log in to the IP Fabric CLI as `osadmin`.
2. Elevate to root using `sudo -s` and `osadmin` password.
3. Create a new file `/opt/ipf-api/conf.d/api.json` or extend the existing one
   with the below JSON:

   ```json
   {
     "app": {
       "enableLocalAuthentication": false
     }
   }
   ```

4. Change file permissions: `chmod 644 /opt/ipf-api/conf.d/api.json`
5. Restart the API: `systemctl restart ipf-api.service`

## Changing Default JSON Web Token (JWT) Expiration

The default JSON Web Token (JWT) expiration is as follows:

- `accessToken` -- 30 minutes (1800 seconds)
- `refreshToken` -- 24 hours (86400 seconds)

Many company standards require shorter expiration times, and this can be
accomplished via the CLI settings.

1. Log in to the IP Fabric CLI as `osadmin`.
2. Elevate to root using `sudo -s` and `osadmin` password.
3. Create a new file `/opt/ipf-api/conf.d/api.json` or extend the existing one
   with the below JSON. In this example, the `accessToken` expires in 10
   minutes, and the `refreshToken` expires in 15 minutes:

   ```json
   {
     "app": {
       "accessToken": {
         "expiresIn": 600
       },
       "refreshToken": {
         "expiresIn": 900,
         "length": 80
       }
     }
   }
   ```

4. Change file permissions: `chmod 644 /opt/ipf-api/conf.d/api.json`
5. Restart the API: `systemctl restart ipf-api.service`
