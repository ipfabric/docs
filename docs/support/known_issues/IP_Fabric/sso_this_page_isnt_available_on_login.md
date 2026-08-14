---
description: After logging in via SSO (OIDC), users may briefly see a "This page isn't available" page before being automatically redirected to the Dashboard.
---

# SSO: "This page isn't available" on login

After logging in via SSO (OIDC), users may see a **"This page isn't available"**
page for about 2 seconds before the application redirects them to the Dashboard.

This is expected behavior. After SSO authentication, IP Fabric creates the user profile
without any permissions. It then assigns permissions based on the configured
[group/role mapping](../../../IP_Fabric_Settings/administration/sso.md#role-assignments).
During this brief resolution period, the application displays the default error
page because the user does not yet have access to any resource.

The impact is cosmetic only — the redirect to the Dashboard occurs automatically.

## Workaround

None required. Wait for the automatic redirect (~2 seconds).
