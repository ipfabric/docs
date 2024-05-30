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

    The `osadmin` password cannot be changed with `cloud-init` or `passwd`. To
    change the `osadmin` password, please use the `nimpee-net-config -t`
    command.

--8<-- "snippets/cli_root_access.md"
