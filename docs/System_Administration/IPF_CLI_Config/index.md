---
description: This page provides an overview of IPF CLI Config.
---

# Overview

**IPF CLI Config** automatically starts during the initial boot of the IP Fabric
appliance and must be completed to proceed with the appliance's deployment.

It introduces the configuration of basic network parameters, including:

- IP Fabric's IP address and subnet
- DNS servers
- proxy server

If some initial parameters need to be modified after completing the deployment,
you may re-run IPF CLI Config with the following command (with one or more
options) as `osadmin`:

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
IPF CLI Config.
Usage: /usr/local/bin/ipf-cli-config [-a] [-n] [-p] [-s] [-t] [-b] [-h]
	-a	configure all services (network, proxy, SSL cert., osadmin user)
	-n	network
	-p	proxy
	-s	SSL certificates (web)
	-t	osadmin troubleshooting user
	-b	used for start during boot
	-h	displays basic help
```

## Run Full IPF CLI Config

To re-run the _full_ IPF CLI Config as described in
[IPF CLI Config](../../platform_first_steps/02-ipf_cli_config.md), use this
command:

```shell
sudo ipf-cli-config -a
```
