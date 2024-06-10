---
description: This page provides an overview of the First Boot Wizard.
---

# Overview

The **First Boot Wizard** automatically starts during the initial boot of the IP
Fabric appliance and must be completed to proceed with the appliance's
deployment.

It introduces the configuration of basic network parameters, including:

- IP Fabric's IP address and subnet
- DNS servers
- proxy server

If some initial parameters need to be modified after the deployment is
completed, you may re-run the First Boot Wizard with the following command (with
one or more options) in the CLI as `osadmin`:

```shell
sudo ipf-cli-config
```

## Documentation

To see more command options, log in to the CLI and run:

```shell
ipf-cli-config -h
```

```shell
osadmin@ipfabric:~# ipf-cli-config -h
IP Fabric network configuration wizard.
Usage: /usr/local/bin/ipf-cli-config [-a] [-n] [-p] [-s] [-t] [-b] [-h]
	-a	configure all services (network, proxy, SSL cert., osadmin user)
	-n	network
	-p	proxy
	-s	SSL certificates (web)
	-t	osadmin troubleshooting user
	-b	used for start during boot
	-h	displays basic help
```

## Run Full First Boot Wizard

To re-run the _full_ First Boot Wizard as described in
[First Boot Wizard](../../platform_first_steps/02-boot_wizard.md), use this
command:

`sudo ipf-cli-config -a`
