---
description: This page describes known issues with Avocent ACS and how to fix them.
---

# Avocent

## Avocent ACS -- Incomplete Output of `shell` Commands

**Known affected platforms:** ACS8016 with firmware 2.26.0 and 2.32.6

**Description:** The ACS CLI can lose the end of the output of a `shell <command>`
line. IP Fabric collects ARP entries, IPv4 and IPv6 routes, interfaces, uptime and
LLDP neighbors this way. To prevent the loss and to detect it, IP Fabric adds this
suffix to every `shell` command it sends:

```commandline
|| true && echo IPF_EOT && usleep 50000
```

`echo` prints an end marker, and `usleep` waits 50 ms before the command ends.
Neither changes anything on the device. When the marker is missing, IP Fabric sends
the command again, up to three times. If the output is still incomplete, the command
fails instead of storing partial data.

**Fix:** No action is needed.

## Avocent ACS -- LLDP Task Using `sudo` Password

**Description:** To collect LLDP information, the `sudo /usr/sbin/lldptool` command
is used. Enable passwords are used for `sudo` access.

**Fix:** Grant the discovery account `sudo` for `/usr/sbin/lldptool` and configure
its password as the enable password.
