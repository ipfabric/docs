---
description: This page describes how to enable feature flags on the IP Fabric appliance.
---

# Feature Flags

Since `6.4.0`, IP Fabric supports feature flags.

Feature flags, also known as feature toggles, are used in software development to enable or disable functionality without deploying new code.

Instead of deploying new features to everyone at once, feature flags allow the gradual roll out of functionality.

Features can be enabled for a small subset of users to collect feedback, and then their availability can be expanded.

Feature flags allow early access to beta features, bug fixes, and features that might cause issues or errors, enabling quick rollbacks by disabling the problematic functionality.

In IP Fabric version `6.7.0`, we introduced a simple way how to enable/disable feature flags using the `EnvironmentFile=` of services.

When enabling or disabling a feature flag, a global or service-related `EnvironmentFile=` needs to be created, edited, or removed.

### `EnvironmentFile=` Locations

Global environment file:

```
/etc/default/ipf-appliance-local
```

Discovery worker environment file:

```
/etc/default/ipf-discovery-worker-local
```

Discovery tasker environment file:

```
/etc/default/ipf-discovery-tasker-local
```

## Current Feature Flags

### ACI Service Graphs

Since `6.4.0`, ACI service graphs can be enabled by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_ACI_SERVICEGRAPHS_ENDPOINTS=true
```

### ACI `fvTenant` API Endpoint Replacement

Until `6.5.0`, IP Fabric used a single `fvTenant` API call to retrieve all
subtree classes needed for discovery.

In large environments, due to the size of the output, the API call, and
subsequently the entire APIC discovery process, may fail.

Since `6.5.0`, IP Fabric, by default, uses a separate API call for each
`fvTenant`'s subtree class needed.

Downloading all data using a single `fvTenant` API call can be re-enabled by
adding the following line to the global environment file
`/etc/default/ipf-appliance-local`:

```
ENABLE_ACI_FVTENANT_ENDPOINT=true
```

### Download of FMC ICMP Object Definitions 1 by 1

The FMC API has a bug returning malformed data for the `/objects/icmpv4objects?expanded=true` endpoint.

Since `6.5.0`, a new feature flag was introduced to download ICMP object definitions 1 by 1.

This can be done by adding the following line to the `tasker` environment file `/etc/default/ipf-discovery-tasker-local`:

```
ENABLE_FMC_NONEXPANDED_ICMP_CALL=true
```

### Non-Paralel Download of FMC Interface-Related Tasks

IP Fabric receives `Error 400` in customers' networks without any further details during attempts to download the list of interfaces on Firepower devices via API. This might be caused by the current approach using parallel calls while obtaining this information.

Therefore, in `6.7.0`, a new feature flag was introduced to change this behavior and call all interface-related requests 1 by 1.

This can be done by adding the following line to the `tasker` environment file `/etc/default/ipf-discovery-tasker-local`:

```
ENABLE_FMC_SERIAL_INTERFACE_DOWNLOAD=true
```

### Discovery of FMC Hosted by Cisco Defense Orchestrator

When FMC is hosted by Cisco Defense Orchestrator, discovery and data collection has to be handled differently. The main difference is in using an API key instead of a username/password.

Since `6.7.0`, it is possible to enable API key authentication for FMC by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_FMC_TOKEN_AUTH=true
```

### VeloCloud Discovery

Since `6.9.0`, VeloCloud devices can be discovered by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_DISCOVERY_DEVICES_VELOCLOUD=true
```

### Nokia SROS Discovery

Since `6.5.0`, Nokia SROS (Service Router Operating System) devices can be discovered by adding the following line to the `worker` environment file `/etc/default/ipf-discovery-worker-local`:

```
ENABLE_DISCOVERY_DEVICES_NOKIA=true
```

### Opengear `$` Prompt Detection

Opengear can be configured with only the `$` sign as a prompt. As this is too general and also some Linux systems use the same prompt, this feature is hidden behind a feature flag.

Since `6.7.0`, the `$` prompt can be enabled for Opengear devices by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_OPENGEAR_DOLLAR_PROMPT=true
```

## Deprecated Feature Flags

### GCP Discovery (Removed in `7.0`)

Since `6.5.0`, GCP (Google Cloud Platform) devices can be discovered by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_DISCOVERY_DEVICES_GCP=true
```

This feature was permanently added to the product in the `7.0` release.

### Stormshield Discovery (Removed in `7.0`)

Since `6.5.0`, Stormshield devices can be discovered by adding the following line to the `worker` environment file `/etc/default/ipf-discovery-worker-local`:

```
ENABLE_DISCOVERY_DEVICES_STORMSHIELD=true
```

This feature was permanently added to the product in the `7.0` release.

### Fortinet FortiSwitch Discovery (Removed in `6.8`)

Since `6.7.0`, Fortinet FortiSwitch devices can be discovered by adding the following line to the `worker` environment file `/etc/default/ipf-discovery-worker-local`:

```
ENABLE_DISCOVERY_DEVICES_FORTISWITCH=true
```

This feature was permanently added to the product in the `6.8` release.

### Citrix NetScaler ADC Discovery (Removed in `6.9`)

Since `6.8.0`, Citrix NetScaler devices can be discovered by adding the following line to the `worker` environment file `/etc/default/ipf-discovery-worker-local`:

```
ENABLE_DISCOVERY_DEVICES_CITRIX=true
```

This feature was permanently added to the product in the `6.9` release.
