---
description: This section explains the Duplicate IPs discovery option (how to discover devices with duplicate IPs).
---

# Duplicate IPs Discovery

## How To Discover Devices With Duplicate IP Addresses

By default, IP Fabric excludes CLI jobs from the discovery process based on
already discovered devices and their local interface IP addresses. If you have
duplicate IP addresses in your network, it can be worthwhile to allowlist some
subnets.

In **Settings --> Discovery & Snapshots --> Discovery Settings --> Discovery -->
Duplicate IPs discovery**, enter one or more subnets to *disable* the test for
duplicate IP addresses for specific networks (so devices with duplicate IP
addresses in those networks will be discovered).

![Duplicate IPs discovery](../../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Discovery_Settings-discovery_duplicate_ips_discovery.webp)

!!! info

    This option was added to the GUI in version `7.0`.

    Between versions `6.4` and `6.9`, this option was experimental and could be
    configured only via the environment variable 
    `SUBNETS_TO_ALLOW_PROCESSING_DUPLICIT_IP`. Since version `7.0`, this 
    environment variable no longer has any effect. A previously configured
    `SUBNETS_TO_ALLOW_PROCESSING_DUPLICIT_IP` is not automatically migrated to
    the GUI.

    Thus, if you configured `SUBNETS_TO_ALLOW_PROCESSING_DUPLICIT_IP` before 
    version `7.0`, you will have to manually set the subnets in the GUI again.
