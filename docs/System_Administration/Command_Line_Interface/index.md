---
description: This section provides an overview of the IP Fabric CLI, which can be used for testing and troubleshooting.
---

# Overview

The Command-Line Interface (CLI) is a secondary service interface in the IP
Fabric VM, which serves troubleshooting and testing purposes. For example, it is
used for testing authentication credentials from the specific IP address of the
IP Fabric VM in case of address-restricted access. The CLI is the main tool for
servicing the system by our Support team.

The CLI also allows the use of standard networking tools, such as `telnet`,
`ssh`, `traceroute`, `ping`, or `tcpdump`.

From the `5.0` release, the `osadmin` account is no longer restricted to
`chroot` only and has access to the whole system.

The `osadmin` account has `sudo` rights with the `osadmin` password and a
standard 5-minute retention.

!!! note

    The `osadmin` password cannot be changed with `cloud-init` or `passwd`.

    To change the `osadmin` password, please use the following command:

    ```shell
    sudo ipf-cli-config -t
    ```

--8<-- "snippets/cli_root_access.md"

## Security Hardening

### Default Home Directory Permissions

Newly created user home directories are assigned permissions of `0700` (`rwx------`), making them accessible only by the owning user.

Home directories frequently contain sensitive data such as SSH keys, configuration files, credentials, and application state.
Allowing read or execute access by other local users increases the risk of information disclosure, privilege escalation, and lateral movement in multi-user systems.

Restricting home directories to the owning user aligns with security best practices and commonly accepted hardening standards.

#### Security Impact

- Files stored in `/home/<user>` are now **private by default**.
- Data previously shared between users via home directories will no longer be accessible unless permissions are explicitly relaxed.
- Applications or scripts that rely on cross-user access to files in `/home` may fail and must be reviewed.

#### Impact on Single Sign-On (SAML)

If you are using SAML for SSO, ensure that the certificate is **not** stored in `/home/autoboss`. Use a preferred location such as `/opt/ipf-dex/etc/` and update the `ipf-dex`
configuration to point to the new certificate location.

For more information, see [Single Sign-On (SSO) - SAML Connector](../../IP_Fabric_Settings/administration/sso.md#saml-connector).
