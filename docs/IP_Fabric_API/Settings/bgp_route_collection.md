---
description: This section describes the BGP route collection feature capabilities.
---

# BGP Route Collection Enhancements

Since release `7.2`, IP Fabric provides a filtered **BGP route collection** mechanism across [supported platforms](#supported-platforms). Network administrators can explicitly define which networks to collect, enabling focused BGP route analysis while optimizing system resources.

## Supported Platforms

- **Cisco IOS / IOS-XE**
- **Cisco IOS-XR**
- **Cisco NX-OS**
- **Juniper JunOS**
- **Arista EOS**

API endpoints for managing route collection settings are available at both **snapshot** and **global** levels.

### Snapshot-Level Configuration

Control route collection settings for specific snapshots through the following endpoints:

#### List all existing route definitions
```http
GET /snapshots/{snapshotId}/show-routes/
```

#### Create a new route definition
```http
POST /snapshots/{snapshotId}/show-routes/
```

#### Retrieve configuration details for a specific route definition
```http
GET /snapshots/{snapshotId}/show-routes/{showRouteId}
```

#### Remove a route definition from the snapshot
```http
DELETE /snapshots/{snapshotId}/show-routes/{showRouteId}
```

### Global Settings

Manage organization-wide route collection configurations via these endpoints:

#### Retrieve all global route definitions
```http
GET /settings/show-routes
```

#### Create a new global route definition
```http
POST /settings/show-routes
```

#### Access configuration details for a specific global route definition
```http
GET /settings/show-routes/{id}
```

#### Remove a global route definition
```http
DELETE /settings/show-routes/{id}
```
