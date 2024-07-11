---
description: In this section, you will find known issues with specific vendors or the IP Fabric platform itself.
---

# Overview

**The search function at the top of the page can assist you in finding the most
relevant information for your inquiries.**

## Vendor-Specific Known Issues

IP Fabric is a **read-only** platform. However, due to bugs in a vendor's code,
running certain commands may cause unexpected consequences in your environment.
If our team has verified a known issue like this, we will disable the tasks for
the known affected platforms/versions.

!!! example "Example: Unexpected Device Issues"

    Collecting transceiver information from certain Cisco devices and versions
    may cause device reloads on certain Cisco versions.

Vendor bugs can also affect the collection of data during the discovery process.
This can cause downstream issues in the platform, affecting not only table data
but also graphing and path lookup simulations.

!!! example "Example: Incomplete Data"

    A good example of this scenario can be seen on Arista devices running
    version `4.26.4M`, where the `show spanning-tree vlan detail` command stops
    when it hits a VLAN that is configured but not assigned to any ports.

## IP Fabric Known Issues

Also documented here are known issues with the IP Fabric platform itself. These
pages provide possible explanations for the causes of issues and, if applicable,
solutions for addressing the issues.

!!! example "Example: `Error: AQL: internal error - in index`"

    The documentation page for this error contains two possible solutions to get
    your IP Fabric instance back up and running (running Maintenance Task and/or
    restarting ArangoDB).

Bugs that have been fixed are documented on the
[Releases](../../releases/index.md) page, either under the `Release notes` or
the `Release notes low level`.
