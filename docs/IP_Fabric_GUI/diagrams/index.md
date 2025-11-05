---
description: This page provides an overview of diagrams and how they help to visualize the network state information.
---

# Overview

Diagrams help visualize the network state information.

We had to change how the diagrams work to bring more functionalities
soon. One of the key changes in the processing of the diagrams is done
in the backend, which means you will be able to collect diagram
information via the API, where it wasn't possible before.

## Diagram Types

### Network

By default, when you click Network, all networks are displayed along with
the relationships between them. They are grouped into sites represented
by a cloud for better visibility. You can double-click a cloud to
explore further that specific site.

For more details on using the diagrams, check [Network Viewer](network_viewer.md).

### Sites Diagrams

Site diagrams display all devices discovered per site. Sites are automatically calculated based on the administrative domain boundaries, such as carrier networks and unmanaged infrastructure. Site boundary calculation can be [configured in settings](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/site_separation.md).

For more details on using the diagrams, check [Network Viewer](network_viewer.md).

### Routing

Routing diagrams display contiguously interconnected routers
to form a routing domain.

### Switching

Switching diagrams display individual spanning-tree instances or a
composite switching domain. A unique Root ID identifies spanning-tree
instances. The switching domain is composed of contiguously connected
spanning-tree instances, representing the maximum possible fault
propagation in a Layer 2 failure domain.

### End-to-End Path

End-to-end path diagram displays a complete path between any two network
endpoints or networks. Only the actual network path is displayed, and
missing parts denote unavailable network information necessary for
completing the routing process.

The end-to-end path can be found in **Diagrams --> End to end path** or
in any diagram using the **Path Lookup** menu on the left (see the picture
below).

![End to end](../../images/diagrams/IP_Fabric_GUI-diagrams_diagrams_end_end.png)

For more details, check [How To Use Path Lookup](how_to_use_path-lookup.md).

### Host-to-Gateway Path

The host-to-gateway path diagram displays the Layer 2 path from every
identified endpoint in the network to its active gateway router.

The host-to-gateway path can be found in **Diagrams --> Host to gateway
path** or in any diagram using the **Path Lookup** menu on the left and
selecting **Host To Gateway** (see the picture below).

![Host to gateway](../../images/diagrams/IP_Fabric_GUI-diagrams_diagrams_host_gateway.png)

For more details, check [How To Use Path Lookup](how_to_use_path-lookup.md).
