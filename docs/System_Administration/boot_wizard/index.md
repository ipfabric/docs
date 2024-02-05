---
description: This page provides an overview of the System 'Boot Wizard'.
---

# System 'Boot Wizard'

## Overview

The **Boot Wizard** is automatically started during the initial boot of the IP
Fabric appliance and must be completed to proceed with the appliance's
deployment.

It introduces the configuration of basic network parameters, including:

- IP Fabric's IP address and subnet
- Time Zone
- NTP servers
- DNS servers
- Proxy server

Suppose some initial parameters need to be modified after the deployment is
completed. In that case, you may re-run the Boot Wizard with the
`sudo nimpee-net-config` command (with one or more options) in the CLI as
`osadmin`.

## Documentation

To see more command options, log in to the CLI and run `nimpee-net-config -h`.

```shell
osadmin@ipfabric:~# nimpee-net-config -h
IP Fabric network configuration wizard.
Usage: nimpee-net-config [-a] [-n] [-p] [-s] [-t] [-b] [-h]
	-a	configure all services (network, proxy, SSL cert., osadmin user)
	-n	network
	-p	proxy
	-s	SSL certificates (web)
	-t	osadmin troubleshooting user
	-b	used for start during boot
	-h	displays basic help

This script is started automatically if "firstrun" parameter is set to "yes" in /opt/nimpee/conf.d/sys-nimpee.conf
or user "osadmin" enables it using "nimpee-net-wizard" script.
```

## Run Full Boot Wizard

To re-run the _full_ Boot Wizard as described
in [First Boot Wizard](../../platform_first_steps/02-boot_wizard.md),
you may use one of these options:

- Run `sudo nimpee-net-config -a`
- Change `firstrun="no"` in `/opt/nimpee/conf.d/sys-nimpee.conf` to
  `firstrun="yes"` (for example with
  `sudo vi /opt/nimpee/conf.d/sys-nimpee.conf`), and reboot.
  ```shell
  osadmin@ipfabric:~$ grep firstrun /opt/nimpee/conf.d/sys-nimpee.conf
  firstrun="yes"
  ```
