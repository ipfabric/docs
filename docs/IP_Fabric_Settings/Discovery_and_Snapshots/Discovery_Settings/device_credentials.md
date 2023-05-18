---
description: Platform interacts with the network infrastructure devices by running show commands through CLI using SSH or Telnet. Credentials added in the...
---

# Device Credentials

IP Fabric interacts with the network infrastructure devices by running show
commands through CLI using SSH or Telnet. Credentials added in the
Authentication section will be used by IP Fabric to access the CLI of the
network devices.

## Credential Selection Logic

If more credentials are specified, a top-down algorithm is used when trying to
login to a network device or the credentials priority can be changed using drag
and drop.

```mermaid
flowchart TD
    A([Start]) --> discoveryHistory{Is IP in<br/>`Management ><br/>Discovery History`<br/>table?}
    discoveryHistory --> |Yes|previousUsername[Try previously discovered username.]
    discoveryHistory --> |No|configuredAuth{Does IP fall within<br/>'Use in subnets' range in<br/>`Settings > Authentication`<br/>table?}
    configuredAuth --> |Yes|tryAuth[Try configured Authentications<br/>starting from top to bottom.]
    configuredAuth --> |No|loginFailed([<b>Login Failed.</b>])
    tryAuth --> |Login Success|loginSuccess([<b>Login Success.</b>])
    tryAuth --> |Login Failed|otherCreds{Are there other<br/>credentials to try?}
    previousUsername --> |Login Success|loginSuccess
    previousUsername --> |Login Failed|configuredAuth
    otherCreds --> |Yes|tryNext[Try next credential.]
    otherCreds --> |No|loginFailed
    tryNext --> |Login Success|loginSuccess
    tryNext --> |Login Failed|otherCreds

    style loginFailed fill:#dd3300
    style loginSuccess fill:#33dd00
    linkStyle 2,4,6,8,10,12 stroke:red;
    linkStyle 1,3,5,7,9,11 stroke:green;
```

## Configure Network Infrastructure Access

Read-only (Privilege 1) credentials are sufficient for basic functionality.
Security sensitive operations and advanced functionality might require higher
privilege. See the
[full list of used command in the documentation](https://matrix.ipfabric.io/).

When adding new credentials, you can limit the validity of the credentials just
for a part of your network using **Use in subnets**
and **Don't use in subnets** fields.

![Add new CLI credential](1935310852.png)

Provided credentials can be used for configuration change tracking and saved
configuration consistency (i.e. they allow commands such as **show run** and
**show start**).

To use this credentials for configuration change tracking, please
check [Use for configuration management](../../configuration_management.md)
box.

## (Optional) Passwords for Enable Mode

Privileged credentials are generally only necessary for configuration
management. However, some platforms require privileged credentials to access
basic network state information, such as MST spanning-tree state or 802.1X
session information.

![Privileges](1935245322.png)
