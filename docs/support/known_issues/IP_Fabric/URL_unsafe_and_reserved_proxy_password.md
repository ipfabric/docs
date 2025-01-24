---
description: This page describes a known issue with URL unsafe and reserved characters in authenticated proxy password for IP Fabric.
---

# URL **Unsafe** and **Reserved** Characters in Password for **_Authenticated Proxy_**

## URL Unsafe Characters

If your password for authenticated proxy contains unsafe characters ``[]{}|\\`"~#<>`` or
a whitespace, the authentication process will fail because these characters can be misinterpreted.

!!! warning "Issue cannot be resolved from IP Fabric's end."

    These characters are prohibited. If your password utilizes these characters,
    please change it on the proxy side.

## URL Reserved Characters

Prior to version `7.1`, URL reserved characters `:/?#[]@!$&'()*+,;=`, although
they can be [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding)
and utilized with the remote proxy, are not supported due to a method of obtaining the
password in IP Fabric's backend.

However, since version `7.1`, these URL reserved characters in proxy usernames and passwords
are supported and automatically encoded when the proxy is configured using the
[`ipf-cli-config`](../../../System_Administration/IPF_CLI_Config/index.md) tool.

!!! Example "Example of percent-encoded password"

    The [`ipf-cli-config`](../../../System_Administration/IPF_CLI_Config/index.md) tool
    will automatically encode the proxy password `$houldLook#Like@This!` to
    `%24houldLook%23Like%40This%21` in IP Fabric versions `7.1` and later.
