---
description: This page describes how to enable configuration flags on the IP Fabric appliance.
---

# Configuration Flags

In IP Fabric, we introduced a simple way how to enable/disable configuration toggles using the `EnvironmentFile=` of services.

Configuration flags, also known as configuration toggles, are used in software development to enable or disable functionality without deploying new code.

A special configuration can be enabled for a small subset of users and not impact others.

When enabling or disabling a configuration flag, a global or service-related `EnvironmentFile=` needs to be created, edited, or removed.

### `EnvironmentFile=` Location

Global environment file:

```
/etc/default/ipf-appliance-local
```

## Current Configuration Flags

### Opengear `$` Prompt Detection

Opengear can be configured with only the `$` sign as a prompt. As this is too general and also some Linux systems use the same prompt, this feature is hidden behind a feature flag.

Since `6.7`, the `$` prompt can be enabled for Opengear devices by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_OPENGEAR_DOLLAR_PROMPT=true
```

After updating the Environment file, restart the IP Fabric application:

```
sudo systemctl restart ipf-appliance
```

### Opengear `#` Prompt Detection

Opengear can be configured with only the `#` sign as a prompt. As this is too general and also some Linux systems use the same prompt, this feature is hidden behind a feature flag.

Since `7.2`, the `#` prompt can be enabled for Opengear devices by adding the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_OPENGEAR_HASH_PROMPT=true
```

After updating the Environment file, restart the IP Fabric application:

```
sudo systemctl restart ipf-appliance
```

### Meraki Catalyst Switches Discovery

Starting with version `7.3`, cloud-managed Cisco Catalyst switches can be discovered via the Meraki API.

**Identification criteria**: Firmware starting with `CS` and Monitoring Version set to `n/a`.

Discovery is enabled by default. To disable it, add the following line to the global environment file `/etc/default/ipf-appliance-local`:

```
DISABLE_DISCOVERY_CLOUD_MANAGED_CATALYST_SWITCHES=true
```

After updating the Environment file, restart the IP Fabric application:

```
sudo systemctl restart ipf-appliance
```

### Versa VOS Forwarding Table

Since `7.3`, this Configuration Flag allows you to configure the limit for the Versa VOS forwarding table length. By default, it is set to 5000000, which corresponds to approximately 100,000 forwarding table records.
To change the limit, add the following line to the global environment file at `/etc/default/ipf-appliance-local`:

```
VERSA_FORWARDING_TABLE_LIMIT=your_new_limit
```

After updating the Environment file, restart the IP Fabric application:

```
sudo systemctl restart ipf-appliance
```

### Disable Network Bandwidth Shaper

Starting in version `7.5`, this feature flag allows removal of bandwidth shaper limitations during the discovery process.

When shaper is disabled, workers still internally calculate bandwidth at 100 Mb/s -- this only affects the maximum number of concurrent sessions/requests but removes interface limitations.

This is useful for troubleshooting connectivity issues (isolates shaper-related problems vs. other issues).

To disable network bandwidth shaper, add the following line to the `global` environment file `/etc/default/ipf-appliance-local`:

```
ENABLE_SHAPER_DISABLING=true
```

After updating the Environment file, restart the IP Fabric application:

```
sudo systemctl restart ipf-appliance
```

### BGP ASplain Notation

Since `7.8` we support a new Configuration Flag allows you to change the default representation of BGP AS numbers from [ASdot](https://notes.networklessons.com/bgp-4-byte-as-number-asdot-notation)
to [ASplain](https://notes.networklessons.com/bgp-4-byte-as-number-asplain-notation) (plain integer representation).

By default, IP Fabric uses the ASdot format. If you prefer the ASplain format, you can enable it by adding the following
line to the global environment file at `/etc/default/ipf-appliance-local`:

```
ENABLE_BGP_ASPLAIN_FORMAT=true
```

After updating the Environment file, restart the IP Fabric application:

```
sudo systemctl restart ipf-appliance
```

To apply this format also in diagrams showing AS numbers on BGP line caps, please reload the snapshot after restarting.

## Deprecated Configuration Flags

At this moment, we did not decprecated any Configuration Flags, yet.
