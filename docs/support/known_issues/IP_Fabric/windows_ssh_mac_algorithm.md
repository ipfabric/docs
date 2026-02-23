---
description: This page describes a known issue with the Windows SSH client using incompatible MAC algorithms when connecting to IP Fabric.
---

# Windows SSH Client - Incorrect MAC Algorithm

When connecting to IP Fabric using the built-in Windows SSH client (OpenSSH for Windows), the connection may fail with the following error:

```
Corrupted MAC on input.
ssh_dispatch_run_fatal: Connection to x.x.x.x port 22: message authentication code incorrect
```

This is a known bug in the Windows SSH client (OpenSSH for Windows), which may
negotiate the `umac-128-etm@openssh.com` or `umac-128@openssh.com` MAC (Message
Authentication Code) algorithms incorrectly. The issue is not caused by
IP Fabric but by the Windows SSH client's handling of these MAC algorithms.

## Fix

To resolve this issue, explicitly specify a compatible MAC algorithm using the
`-m` option when connecting:

```shell
ssh -m hmac-sha2-512-etm@openssh.com osadmin@<IP_FABRIC_ADDRESS>
```

This forces the SSH client to use the `hmac-sha2-512-etm@openssh.com` algorithm,
which is fully supported and avoids the error.

!!! tip "Persistent Configuration"

    To avoid specifying the `-m` option every time, you can add the following to
    your SSH configuration file (`%USERPROFILE%\.ssh\config`):

    ```
    Host <IP_FABRIC_ADDRESS>
        MACs hmac-sha2-512-etm@openssh.com
    ```
