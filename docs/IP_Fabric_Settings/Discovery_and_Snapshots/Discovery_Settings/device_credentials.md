---
description: IP Fabric interacts with the network infrastructure devices by running show commands through CLI using SSH or Telnet.
---

# Device Credentials

IP Fabric interacts with the network infrastructure devices by running show
commands through CLI using SSH or Telnet. Credentials added in **Settings -->
Discovery & Snapshots --> Discovery Settings --> Device Credentials** will be
used by IP Fabric to access the CLI of the network devices.

## Credential Selection Logic

The credential priority can be changed using drag and drop. The credential 
selection algorithm will match the device's IP address to the subnets specified
in the credential's **Use in subnets** field, and will try the credentials in the 
order of the longest prefix match. Within the same prefix match length, the 
credentials are tried in top-down order.

```mermaid
flowchart TD
    A([Start]) --> discoveryHistory{Is the IP address in<br/>the <strong>Management →<br/>Discovery History</strong><br/>table?}
    discoveryHistory --> |Yes|previousUsername[Try the previously discovered username.]
    discoveryHistory --> |No|configuredAuth{Does the IP address fall within<br/>the <strong>Use in subnets</strong> range in<br/>the <strong>Settings → Discovery & Snapshots →<br/>Discovery Settings → Device Credentials</strong><br/>table?}
    configuredAuth --> |Yes|tryAuth[Try the configured <strong>Device Credentials,</strong><br/>starting from the longest prefix match and<br/>using top-to-bottom order as a tie-breaker.]
    configuredAuth --> |No|loginFailed([<strong>Login failed.</strong>])
    tryAuth --> |Login succeeded|loginSucceeded([<strong>Login succeeded.</strong>])
    tryAuth --> |Login failed|otherCreds{Are there other<br/>credentials to try?}
    previousUsername --> |Login succeeded|loginSucceeded
    previousUsername --> |Login failed|configuredAuth
    otherCreds --> |Yes|tryNext[Try the next credential.]
    otherCreds --> |No|loginFailed
    tryNext --> |Login succeeded|loginSucceeded
    tryNext --> |Login failed|otherCreds

    style loginFailed fill:#dd3300
    style loginSucceeded fill:#33dd00
    linkStyle 2,4,6,8,10,12 stroke:red;
    linkStyle 1,3,5,7,9,11 stroke:green;
```

## Configure Network Infrastructure Access

Read-only (Privilege 1) credentials are sufficient for basic functionality.
Security-sensitive operations and advanced functionality might require higher
privileges. See the
[full list of used command in the documentation](https://matrix.ipfabric.io/).

When adding new credentials, you can limit the validity of the credentials just
for a part of your network using the **Use in subnets**
and **Don't use in subnets** fields. Please be aware that the **Use in subnets** 
field will also affect the credential selection algorithm.

![Add new CLI credential](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Discovery_Settings_add-new-cli-credential.webp)

Provided credentials can be used for configuration change tracking and saved
configuration consistency (i.e., they allow commands such as `show run` and
`show start`).

To use these credentials for configuration change tracking, please
check the [Use for configuration management](../../configuration_management.md)
box.

!!! warning "Password Character Restrictions"

    The password will only be decrypted if ASCII characters are used. If you are
    using special characters, please make sure that the password is within the
    ```[A-Za-z0-9+-!?@#$%^&*()_`~[]{}<>,./|\:;'" ]``` range.

## (Optional) Passwords for Enable Mode

Privileged credentials are generally only necessary for configuration
management. However, some platforms require privileged credentials to access
basic network state information, such as MST spanning-tree state or 802.1X
session information.

![Passwords for enable mode](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Discovery_Settings_passwords-for-enable-mode.webp)
