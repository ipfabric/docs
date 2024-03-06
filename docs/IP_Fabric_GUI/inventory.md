---
description: The inventory provides an overview list of sites, devices, modules, interfaces, and users discovered within the network.
---

# Inventory

## Overview

The inventory provides an overview list of sites, devices, modules, interfaces,
and users discovered within the network.

## Sites

The site inventory provides an overview of discovered sites, the number of
devices and users present at each site. It enables the generation of
site-specific reports and diagrams. Sites are automatically calculated based on
the administrative domain boundaries, such as carrier networks and other
unmanaged infrastructure. A single unmanaged `traceroute` hop is not considered
a site boundary; therefore, unmanaged infrastructure is reconstructed from the probes.
The specific method of site boundary calculation can be changed in the settings.

An unknown site is either a collection of isolated devices or when a device
forms a single-device site.

## Devices

The device inventory represents all logical managed network infrastructure
devices that have been discovered and analyzed. Each entry provides the
following information (`Human Readable Name (apiColumnName)`):

- `Hostname (hostname)` is the device's short name.
- `Hostname original (hostnameOriginal)` is the original hostname acquired from
  the device.
- `Hostname processed (hostnameProcessed)` is the hostname parsed from the
  original hostname (if no parsing occurs, it is the same as `hostnameOriginal`); when
  applicable -- logical device name -- e.g., firewall `context` or `vsys` name --
  can be added as a suffix to the hostname.
- `FQDN (fqdn)` is the device fully qualified domain
  name (`hostnameProcessed.domain`).
- `Domain (domain)` is the device's domain name.
- `Site (siteName)` is the logical grouping to which the device belongs, while
  single-site or isolated devices belong to an unknown site.
- `Routing domain (rd)` is an IP Fabric-generated separation based on the
  contiguous layer 3 routing domain to which the device belongs.
- `Switching domain (stpDomain)` is an IP Fabric-generated separation based on
  the contiguous layer 2 switching domain to which the device belongs.
- `Serial Number (snHw)` is the device's serial number.
- `Unique serial number (sn)` is the serial number IP Fabric assigns to the
  device. This can differ from the Hardware SN, especially in cases of
  virtualized equipment.
- `Vendor (vendor)` is the device's vendor.
- `Family (family)` is the device's software family.
- `Platform (platform)` is the device's hardware platform.
- `Model (model)` is the device's model.
- `Login IP (loginIp)` is the IP address used to connect to the device.
- `Management Protocol (loginType)` is the protocol used to connect to the
  device.
- `MAC Address (mac)` is the device's MAC address.
- `Uptime (uptime)` is the time since the device's last boot.
- `Reload Reason (reload)` is the reason why the device has booted.
- `Image (image)` is the path to the operating system image file.
- `Version (version)` is the operating system with which the device is running.
- `Configuration Register (configReg)` is the Configuration Register set on the
  device.
- `Processor (processor)` is the hardware CPU family name.
- `Memory Total (memoryTotalBytes)` is the total amount of RAM memory available
  on the device.
- `Memory Used (memoryUsedBytes)` is the amount of RAM memory in use at the time
  of discovery.
- `Memory % (memoryUtilization)` is the utilization of RAM memory at the time of
  discovery (memoryUsedBytes / memoryTotalBytes).
- `Type (devType)` is a logical Device Type that IP Fabric assigns to the
  device (i.e., a Firewall is labeled `fw` and a Wireless Access Point as `ap`).
  This is used for internal decisions such as the device icon to display in
  diagrams and cannot be changed. To set a custom type, please
  see [Device Attributes](../IP_Fabric_Settings/Discovery_and_Snapshots/Global_Configuration/device_attributes.md).
- `Object Id (objectId)` is a Unique ID for API devices used during discovery.

API-only Columns:

- `id` is the unique ID for the row of data.
- `taskKey` is a UUID used to download the specific device log file for
  a snapshot.

## Modules and Part Numbers

The part numbers inventory provides information about every identifiable module
through device inventories.

## OS Versions

The operating system versions inventory provides an overview of the unique
operating systems used in the network and their variations.

## Interfaces

The interface inventory provides information about every unique network
interface discovered and includes information such as state, description, speed,
duplex, and media type.

## Hosts

The hosts' inventory provides information about every discovered host and user
utilizing network infrastructure. A host is any unique IP or MAC address, or an
IP/MAC tuple, that is not part of the network infrastructure. The following rules
may prevent the inclusion of IP addresses from the ARP in the Hosts' inventory:

- There cannot be any route pointing to that interface.
- No CDP/LLDP information should be coming from that IP.
- The MAC shouldn't be in the OUI flagged as "Enabled for Discovery".

## End of Life Milestones

EoX reports provide an overview of the announced end-of-life milestones. Network
infrastructure vendors use end-of-life milestones to communicate stages of the
product life cycle, allowing sufficient time to migrate to next-generation
products.

IP Fabric currently collects EoL information on the following Vendors:

- Arista
- Aruba Networks
- Check Point
- Cisco
- Cisco Meraki
- Extreme
- F5
- Fortinet
- HP/H3C/3COM
- Juniper
- Palo Alto
- Riverbed
