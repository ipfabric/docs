---
description: This page describes how to enable feature flags on the IP Fabric appliance.
---

# Feature Flags

Since `6.4`, IP Fabric supports feature flags.

Feature flags, also known as feature toggles, are used in software development to enable or disable functionality without deploying new code.

Instead of deploying new features to everyone at once, feature flags allow the gradual roll out of functionality.

Features can be enabled for a small subset of users to collect feedback, and then their availability can be expanded.

Feature flags allow early access to beta features, bug fixes, and features that might cause issues or errors, enabling quick rollbacks by disabling the problematic functionality.

In IP Fabric version `6.7`, we introduced a simple way how to enable/disable feature flags using the `EnvironmentFile=` of services.

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

Since `6.4`, ACI service graphs can be enabled by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_ACI_SERVICEGRAPHS_ENDPOINTS=true
```

Support for Layer 2 (L2) path lookup in ACI service graphs was introduced in version `7.3`.

After updating the Environment file, restart the IP Fabric application:

```
sudo systemctl restart ipf-appliance
```

### Download of FMC ICMP Object Definitions 1 by 1

The FMC API has a bug returning malformed data for the `/objects/icmpv4objects?expanded=true` endpoint.

Since `6.5`, a new feature flag was introduced to download ICMP object definitions 1 by 1.

This can be done by adding the following line to the `tasker` environment file `/etc/default/ipf-discovery-tasker-local`:

```
ENABLE_FMC_NONEXPANDED_ICMP_CALL=true
```

### Non-Paralel Download of FMC Interface-Related Tasks

IP Fabric receives `Error 400` in customers' networks without any further details during attempts to download the list of interfaces on Firepower devices via API. This might be caused by the current approach using parallel calls while obtaining this information.

Therefore, in `6.7`, a new feature flag was introduced to change this behavior and call all interface-related requests 1 by 1.

This can be done by adding the following line to the `tasker` environment file `/etc/default/ipf-discovery-tasker-local`:

```
ENABLE_FMC_SERIAL_INTERFACE_DOWNLOAD=true
```

### Discovery of FMC Hosted by Cisco Defense Orchestrator

When FMC is hosted by Cisco Defense Orchestrator, discovery and data collection has to be handled differently. The main difference is in using an API key instead of a username/password.

Since `6.7`, it is possible to enable API key authentication for FMC by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_FMC_TOKEN_AUTH=true
```

After updating the environment file, you must restart IP Fabric application by running the following command:

```
sudo systemctl restart ipf-appliance
```

### VeloCloud Discovery

Since `6.9`, VeloCloud devices can be discovered by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_DISCOVERY_DEVICES_VELOCLOUD=true
```

After updating the environment file, you must restart IP Fabric application by running the following command:

```
sudo systemctl restart ipf-appliance
```

### Nokia SROS Discovery

Since `6.5`, Nokia SROS (Service Router Operating System) devices can be discovered by adding the following line to the `worker` environment file `/etc/default/ipf-discovery-worker-local`:

```
ENABLE_DISCOVERY_DEVICES_NOKIA=true
```
### Opengear ACM/CM/OM Support

Since `7.0`, Opengear ACM/CM/OM devices can be discovered by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_DISCOVERY_DEVICES_OPENGEAR_OM_CM_ACM=true
```

After updating the Environment file, restart the IP Fabric application:

```
sudo systemctl restart ipf-appliance
```

### Extensions

Since `7.0`, Extensions can be enabled by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_EXTENSIONS=true
```

This feature flag enables the Extensions functionality, which allows users to add and customize their IP Fabric instance with tailored functionality through containerized applications. Extensions can be managed through the IP Fabric UI under the **Extensions** menu.

!!! warning "Docker Default Subnet"

    As of version `7.0.14`, the Docker service, which is used for extensions, is **disabled and stopped by default** to prevent potential subnet conflicts in its default configuration (`172.17.0.0/16`). This subnet may collide with existing network infrastructure.

    **To customize the Docker subnet:**

    1. Edit the configuration in `/etc/docker/daemon.json`, [see](../../support/known_issues/IP_Fabric/unable_to_discover_devices_in_172_17_0_0_16_subnet.md) OR 
    2. Contact our customer support team via the [support portal](https://support.ipfabric.io)

    **To use Docker with the default subnet** (only if `172.17.0.0/16` is unused in your environment) run: 

    ```bash
    sudo systemctl enable docker && sudo systemctl start docker
    ```

For more information about Extensions, see the [7.0 Release Notes](../../releases/release_notes/previous_releases/IP_Fabric_v7.x.x/7.0.md#extensions-engineering-preview) for more information.

After updating the environment file, you must restart IP Fabric application by running the following command:

```bash
sudo systemctl restart ipf-appliance
```

### Configuration Management Optimizations

Starting in version `7.2`, you can enable additional configuration management performance optimizations by adding the following entries to the
syslogworker environment file at `/etc/default/ipf-discovery-syslogworker-local`.

Remember to restart the syslogworker after modifying the environment file:

```bash
sudo systemctl restart ipf-discovery-syslogworker
```

#### Git File Commit Optimization

This feature accelerates file history retrieval operations. It improves performance scaling as Git repositories grow.

```bash
ENABLE_EXPERIMENTAL_GIT_FILE_COMMIT=true
```

#### Git Repository Configuration

Applies Git configuration enhancements including:

- In-memory Git index preloading
- Commit graph files for faster history traversal
- Automatic commit graph maintenance

These settings optimize Git operation performance with minimal overhead.

```bash
ENABLE_EXPERIMENTAL_GIT_CONFIGURE_REPOSITORY=true
```

#### Git Repository Optimization

Performs repository optimization during worker initialization stage including:

- Comprehensive garbage collection
- Storage-optimized repository repacking
- Commit graph generation for accelerated traversal

This optimization significantly increases startup time but improves runtime performance.

```bash
ENABLE_EXPERIMENTAL_GIT_OPTIMIZE_REPOSITORY=true
```

#### Performance Logging

Enables detailed execution time tracking for critical operations:

- Configuration updates
- Git operations
- Database queries
- Device connections

```bash
ENABLE_EXPERIMENTAL_SYSLOGWORKER_PERFORMANCE_LOGGING=true
```

### Enable Manual Links / Transparent Firewall

This configuration flag enable manual link configuration option in both global and snapshot settings.
For more information about feature, see the [7.3 Release Notes](../../releases/release_notes/previous_releases/IP_Fabric_v7.x.x/7.3.md#transparent-firewalls).

Since `7.3`, the manual link support can be enabled by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_MANUAL_LINKS=true
```

After updating the Environment file, restart the IP Fabric application:

```
sudo systemctl restart ipf-appliance
```

### Palo Alto External Dynamic Lists

Starting in version `7.3`, these feature flags enable downloading content from configured External Dynamic Lists.

The associated files contain IP address or URL lists, which are then passed to the firewall rules on a device.

To enable collection of respective lists, following lines need to be added to the `worker` environment file `/etc/default/ipf-discovery-worker-local`:

```
ENABLE_PALOALTO_EDL_IPLIST=true
ENABLE_PALOALTO_EDL_URLLIST=true
```

## Deprecated Feature Flags

### ACI `fvTenant` API Endpoint (Removed in `7.5`)

Prior to version `6.5`, IP Fabric used a single `fvTenant` API call to retrieve all necessary subtree classes for discovery.

In large environments, the size of the output could cause this API call -- and consequently the entire APIC discovery process -- to fail.

Starting in version `6.5`, IP Fabric defaults to using separate API calls for each required subtree class of `fvTenant`.

The previous behavior (retrieving all data via a single `fvTenant` API call) could be re-enabled by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_ACI_FVTENANT_ENDPOINT=true
```

This option was removed in `7.5` release. The current implementation exclusively uses separate API calls for each `fvTenant` subtree class.

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

### Citrix NetScaler ADC Discovery (Removed in `6.9`)

Since `6.8.0`, Citrix NetScaler devices can be discovered by adding the following line to the `worker` environment file `/etc/default/ipf-discovery-worker-local`:

```
ENABLE_DISCOVERY_DEVICES_CITRIX=true
```

This feature was permanently added to the product in the `6.9` release.

### Fortinet FortiSwitch Discovery (Removed in `6.8`)

Since `6.7.0`, Fortinet FortiSwitch devices can be discovered by adding the following line to the `worker` environment file `/etc/default/ipf-discovery-worker-local`:

```
ENABLE_DISCOVERY_DEVICES_FORTISWITCH=true
```

This feature was permanently added to the product in the `6.8` release.

