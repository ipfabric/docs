# Overview

The command-line interface is a secondary service interface in IP Fabric VM which serves troubleshooting and testing purposes. For example, for testing authentication credentials from the specific IP address of IP
Fabric VM, in case of address-restricted access. The CLI interface is the main tool in servicing the system by the support teams.

Command-line also allows the use of the standard networking tools, such as telnet, ssh, traceroute, ping or tcpdump.

From 5.0 release, `osadmin` account is no longer restricted to `chroot` only and have access to the whole system.

The `osadmin` account has `sudo` rights with `osadmin` password and a standard 5 minutes retention.

!!! note

    Password cannot be changed via `cloudinit` or `passwd`, please run command `nimpee-net-config -t` to change `osadmin` password.

!!! warning

    Any action on the CLI as a `root`, `osadmin` and/or `autoboss` user may severely damage the product and/or the system itself. Such actions taken without direct communication with the IP Fabric Support or Solution Architect teams can render the system unusable.