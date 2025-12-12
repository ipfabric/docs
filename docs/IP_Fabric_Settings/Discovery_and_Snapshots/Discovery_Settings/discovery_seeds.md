---
description: A discovery seed is a device from which IP Fabric begins the auto-discovery process. These IPs can be device management IP addresses or networks.
---

# Discovery Seeds

A discovery seed is a device from which IP Fabric begins the auto-discovery process. These IPs can be device management IP addresses or networks.

If you have a specific starting point for discovering the network, you can enter
it in **Settings --> Discovery & Snapshots --> Discovery
Settings --> Discovery Seeds**. This option does not exclude any networks from
discovery.

The starting points can be management IP addresses of network devices or
network subnets. Existing inventory data can also be imported.

If no seed information is entered, discovery will begin from the current default
gateway.

## Time-Based Filtering for Discovery History Seeds

The Discovery History Seeds feature allows administrators to control which IP addresses from
the Discovery History are used as seeds for subsequent discoveries.

By default, IP Fabric uses all IP addresses stored in Management → Discovery History as seed.
This feature enables filtering by age or specific date, or disabling the reuse of historical seeds entirely.

![Discovery Seeds](../../../images/snapshot-management/overview-How_Discovery_Works-troubleshooting_discovery_seeds.webp)

### Configuring via API

This feature is configurable through a new `discoveryHistorySeeds` attribute in the existing `PATCH /settings` API. The attribute accepts an object with these properties:

- `enabled` *(required)* – Enables/disables seed reuse from Discovery History.
- `daysLimit` *(optional)* – Restricts seed reuse to IPs discovered within the last X days.
- `afterDate` *(optional)* – Restricts seed reuse to IPs discovered after a specified date.


**Use Cases**

| Scenario | Configuration |
|--|--|
| **Current Behavior** -- Use all IPs from Discovery History | `{ enabled: true }` |
| **Disable seed reuse** | `{ enabled: false }` (preserves existing `daysLimit`/`afterDate` values)|
| **Use only IPs discovered in the last 7 days** | `{ enabled: true, daysLimit: 7 }`|
| **Use only IPs discovered after June 1, 2025** | `{ enabled: true, afterDate: "2025-06-01" }` |

!!! Note

    `daysLimit` and `afterDate` are mutually exclusive — only one may be configured at a time.

!!! note
    
    It is recommended to provide multiple IP addresses of core routers as
    starting points for discovery.

!!! warning "Maximum Prefix Length"

    When you add a network to the **Discovery Seeds**, IP Fabric attempts to
    connect to all IP addresses in that network. Due to this, the **maximum
    prefix length** you can add into a discovery seed is `/23` for IPv4 and `/119` for IPv6.
