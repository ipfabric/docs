---
description: The Boot Wizard needs to be completed during the IP Fabric virtual server deployment before the image installation begins.
---

# Run System 'Boot Wizard'

The Boot Wizard needs to be completed during the IP Fabric virtual server
deployment before the image installation begins. The Boot Wizard introduces the
configuration of basic network parameters, including time zone, NTP, IP
address, DNS or Proxy settings. In case some initial parameters need to
be modified after the installation is complete, the IP Fabric administrator may
start the Boot Wizard or part of it by running `nimpee-net-config`.

Login as `osadmin` and run `nimpee-net-config -h` for detailed help. 
```
root@ipfabric:~# nimpee-net-config -h
IP Fabric network configuration wizard.
Usage: nimpee-net-config [-a] [-n] [-p] [-s] [-t] [-b] [-h]
	-a	configure all services (network, proxy, SSL cert., osadmin user)
	-n	network
	-p	proxy
	-s	SSL certificates (web)
	-t	nimpee troubleshooting user
	-b	used for start during boot
	-h	displays basic help

This script is started automatically if "firstrun" parameter is set to "yes" in /opt/nimpee/conf.d/sys-nimpee.conf
or user "nimpee" enables it using "nimpee-net-wizard" script.
```

Examples:

- `nimpee-net-config -a` runs _full_ Boot Wizard same way as described in [Complete (first-time) Boot Wizard](../Getting_Started/Platform_First_Steps/01-deployment.md#complete-first-time-boot-wizard)
- `nimpee-net-config -t` sets new password for `osadmin` user
