---
description: This page describes a known issue with URL unsafe and reserved characters in authenticated proxy password for IP Fabric.
---

# URL __Unsafe__ and __Reserved__ Characters in Password for ___Authenticated Proxy___

## URL Unsafe Characters

If your password for authenticated proxy contains unsafe characters ``[]{}|\\`"~#<>`` or
a whitespace, the authentication process will fail because these characters can be misinterpreted.

!!! warning "Issue cannot be resolved from IP Fabric's end."

    These characters are prohibited. If your password utilizes these characters,
    please change it on the proxy side.

## URL Reserved Characters

URL reserved characters `:/?#[]@!$&'()*+,;=`, although they can be [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding)
and utilized with the remote proxy, are not supported due to a method of obtaining the
password in IP Fabric's backend.

If you are affected by this issue, please change your password to one that does not contain
these characters. The fix is scheduled to be released in version `7.1`.
