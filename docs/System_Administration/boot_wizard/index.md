---
description: The Boot Wizard needs to be completed during the IP Fabric virtual server deployment before the image installation begins.
---

# System 'Boot Wizard'

## Overview

The Boot Wizard is automatically started during the installation process and
must be completed during the IP Fabric virtual server deployment before the
image installation begins. The Boot Wizard introduces the configuration of basic
network parameters, including:

- IP Fabric's IP address and subnet
- Time Zone
- NTP servers
- DNS servers
- Proxy server

Suppose some initial parameters need to be modified after the installation is
complete. In that case, the IP Fabric administrator may restart the Boot Wizard
by running `nimpee-net-config` from the CLI as `osadmin`.

## Documentation

To see more command options, log in and run `nimpee-net-config -h`.

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

To rerun the _full_ Boot Wizard as described
in [First Boot Wizard](../Getting_Started/Platform_First_Steps/02-boot_wizard):

- Run `nimpee-net-config -a`
- Edit `/opt/nimpee/conf.d/sys-nimpee.conf`, change `firstrun="yes"`, and reboot.
```shell
osadmin@ipfabric:~$ grep firstrun /opt/nimpee/conf.d/sys-nimpee.conf
firstrun="yes"
```
