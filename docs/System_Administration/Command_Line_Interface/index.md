---
description: The command-line interface is a secondary service interface in IP Fabric VM which serves troubleshooting and testing purposes.
---

# Overview

The command-line interface is a secondary service interface in IP Fabric VM which serves troubleshooting and testing purposes. For example, for testing authentication credentials from the specific IP address of IP
Fabric VM, in case of address-restricted access. The CLI interface is the main tool in servicing the system by the support teams.

The command line also allows the use of the standard networking tools, such as `telnet`, `ssh`, `traceroute`, `ping` or `tcpdump`.

From `5.0` release, the `osadmin` account is no longer restricted to `chroot` only and has access to the whole system.

The `osadmin` account has `sudo` rights with the `osadmin` password and a standard 5 minutes retention.

!!! note

    Password cannot be changed via `cloud-init` or `passwd`, please run command `nimpee-net-config -t` to change `osadmin` password.

--8<-- "snippets/cli_root_access.md"
