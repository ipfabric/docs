---
description: This page describes how to configure Quagga / FRR to work with IP Fabric.
---

# Configuring Quagga / FRR to Work With IP Fabric

When running discovery, IP Fabric needs to connect directly to the device
console. Because of that, to discover Quagga/FRR devices, a separate user with a
specific shell needs to be created on a device.

The Quagga / FRR shell usually runs in `/usr/bin/vtysh`.

A new user with direct access to the Quagga / FRR shell needs to be created as
follows in the bash:

``` bash
useradd -s /usr/bin/vtysh username
```

Afterwards, you will be prompted to set up a password. Add this username and
password to IP Fabric credentials used for discovery.
