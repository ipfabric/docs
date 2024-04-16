---
description: The Routing analysis give you two options, a Detailed analysis of individual routes or a Routing consistency and stability analysis.
---

# Routing Analysis

## Individual Routes

Detailed analysis of individual routes can be performed through a
cumulative routing table for parameters such as route presence in a
routing instance, next-hop redundancy, route source and metrics, or next-hop
interfaces. The cumulative routing table contains all entries from all
routing tables and all VRFs collected from all managed network devices
with L3 routing capability. Each line represents a corresponding entry
from the source routing table, normalized into a standard terse view.
The table can be filtered per site, per device, per route, number of next
hops, lowest metric of next hops, or other next-hop information.
Individual routes can be looked up as a string or as a route for a
specific IP address. For example, the IP address `10.0.0.1` will return
routes `10.0.0.0/24` and `0.0.0.0/0` but not `10.0.1.0/24`.

## Routing Consistency

Routing consistency and stability analysis can be performed using the
routing stability table. The table lists all unique routed networks, the
number of times a route is observed, expressed in absolute and percentage
values, and the percentage of routes that have a next-hop age below a certain
threshold signifying convergence. The table can be used to verify if
similar routes are present in the same number of the routing tables,
find starting point for troubleshooting convergence, or check route
distribution across the network, including verifying the presence of a
default route.
