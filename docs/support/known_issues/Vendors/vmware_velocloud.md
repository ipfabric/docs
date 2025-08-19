---
description: This page describes known issues with VMware VeloCloud.
---

# VMware VeloCloud


## Orchestrator versions earlier than `6.0.0` not supported

**Known affected platforms:** `6.0.0` and earlier

**Description:** IP Fabric officially supports VeloCloud Orchestrator versions `6.0.0` and later.
Earlier versions are not supported, as they may have different API
endpoint outputs that may cause discovery to fail or get stuck.

## Currently unsupported features

- VeloCloud Gateways and all related configuration (only edges are supported)
- Routes learned via BGP over non SD-WAN links
