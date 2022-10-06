---
description: The inventory provides a list overview of sites, devices, modules, interfaces, and users discovered within the network.
---

# Inventory

## Overview

The inventory provides a list overview of sites, devices, modules, interfaces, and users discovered within the network.

## Sites

The site inventory provides an overview of discovered sites, the number of devices and users present at the site, and enables the generation of site-specific reports and diagrams. Sites are automatically calculated based on the administrative domain boundaries, such as carrier networks and other unmanaged infrastructure. A single, unmanaged `traceroute` hop is not considered a site boundary, so unmanaged infrastructure is reconstructed from the probes. The specific method of site boundary calculation can be changed in the settings.

An unknown site is either a collection of isolated devices or when a device forms a single-device site.

## Devices

The device inventory represents all logical managed network infrastructure devices that have been discovered and analyzed. Each entry provides the following information:

- `Site` is the logical grouping to which device belongs to, while single-site or isolated devices belong to an unknown site.
- `Routing domain` is an IP Fabric generated separation based upon the contiguous layer 3 routing domain to which the device belongs to.
- `Switching domain` is an IP Fabric generated separation based upon contiguous layer 2 switching domain the device belongs to.
- `Hostname` is the short name of the device.
- `Hostname original` is the original hostname which was acquired from the device.
- `Hostname processed` is hostname which we parsed from original hostname (if there isn't any parsing, it's the same as `Hostname original`); when applicable -- logical device name -- e.g. firewall `context` or `vsys` name -- can be added as a suffix to the hostname.
- `Domain` is the device domain name.
- `FQDN` is the device fully qualified domain name (`hostnameProcessed.domain`).
- `Serial Number` is the serial number of the device (API column name is `snHw`).
- `Unique serial number` is the serial number IP Fabric assigns to the device this could be different from the Hardware SN especially in cases of virtualized equipment (API column name is `sn`).
- `Login IP` is the IP address used to connect to the device.
- `Management Protocol` is the protocol used to connect to the device.
- `Uptime` is the time since the device's last boot.
- `Reload reason` is the reason why the device has booted.
- `Vendor` is the vendor of the device.
- `Platform` is the hardware platform of the device.
- `Family` is the software family of the device.
- `Version` is the operating system the device is running with.
- `Image` is the path to the operating system image file.
- `Processor` is the hardware CPU family name.
- `Memory` is the amount of RAM memory available on the device.

## Modules and Part Numbers

The part numbers inventory provides information about every identifiable module through device inventories.

## OS Versions

The operating system versions inventory provides an overview of the unique operating systems used in the network and their variation.

## Interfaces

The interface inventory provides information about every unique network interface discovered and includes information such as state, description, speed, duplex, and media type.

## Hosts

The hosts' inventory provides information about every discovered host and user utilizing network infrastructure. A host is any unique IP or MAC address, or an IP/MAC tuple, that is not part of the network infrastructure. Following rules may
prevent the IP addresses from the ARP to be included in the Hosts' inventory:

- There can't be any route pointing to that interface
- No CDP/LLDP information should be coming from that IP
- The MAC shouldn't be in the OUI flagged as "Enabled for Discovery"

## End of Life Milestones

EoX reports provide an overview of the announced end-of-life milestones. Network infrastructure vendors use end-of-life milestones to communicate stages of the product life cycle, allowing sufficient time to migrate to next-generation products.
