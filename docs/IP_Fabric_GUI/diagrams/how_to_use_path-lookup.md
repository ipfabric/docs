---
description: This page explains how to use path lookup.
---

# How To Use Path Lookup

## Unicast Path Lookup

![Unicast form](pathlookup/unicast.webp)

### First Hop Algorithm And VRF

The **First Hop Algorithm** adds the possibility to start the path lookup simulation from a different device than the closest one.

If the **Automatic** option is selected, IP Fabric initiates the path lookup simulation from the closest possible device. VRF is also automatically selected by default but can be changed manually.

![First hop algorithm](pathlookup/first_hop_algorithm.webp)

The **User defined** First Hop Algorithm can be useful when simulating a flow where the source network is not known by IP Fabric.

To simulate such a flow, it is necessary to specify the starting point by entering the name of the device and the interface which will be used to start the path lookup.

Packets will use the indicated source IP address.

!!! Example "User-Defined First Hop Algorithm"

    In the example below, the source network `10.25.25.0/24` is not known by IP Fabric. To show the path between a client in this network and a server in a network known by IP Fabric:

    ![User Defined First hop algorithm example](pathlookup/user_defined_first_hop_algorithm_example_drawing.webp){: style="height:150px"}

    1. Select the **User defined** First Hop Algorithm.
    2. Search for the device where you want to start the path: `L43EXR1`.
    3. Select the source interface: `Et0/1`.
    4. Enter the source IP from the network outside the scope of IP Fabric: `10.25.25.10`.
    5. Finally, enter the destination IP: `10.66.122.110`.

    ![User Defined First hop algorithm](pathlookup/user_defined_first_hop_algorithm.webp)

    This is the result you will get:

    ![User Defined First hop algorithm Result](pathlookup/user_defined_first_hop_algorithm_result.webp)

### Source/Destination IP Address and Port

A plain IP address or a CIDR (Classless Inter-Domain Routing) can be used as a source/destination IP address, for example, when simulating path lookup from a host to a network.
Note that the global attribute filter is applied to suggestions for source and destination IP addresses, as well as hostnames when the User-Defined First Hop Algorithm is used.

By default, the `ICMP` protocol and the `Echo request` option are chosen for path lookup.

![Source and destination](pathlookup/pathlookup_src_dst.webp)

When switched to `Web HTTP/HTTPS`, TCP destination ports `80` and `443` with the `(web|http|https)` application are set by default.

![HTTP default](pathlookup/pathlookup_http_default.webp)

When extending details, the transport protocol and range of ports can be specified for a source and for a destination. When more destination ports are specified, IP Fabric will analyze all of them individually during the path lookup.

![Source and destination ports](pathlookup/pathlookup_src_dst_port.webp)

The port can be changed to an arbitrary one for TCP/UDP protocols.

The following flags can also be set for TCP traffic: `None` / `ACK` / `FIN` / `SYN` / `RST` / `PSH` / `URG`.

### TTL and Fragment Offset

In **More details**, **TTL** (Time to live) and **Fragment offset** can be set -- thus affecting the path lookup output. The default TTL is 128 and Fragment offset is set to 0.

![TTL and Fragmentation](pathlookup/pathlookup_ttl_fragment.webp)

### Application

When evaluating security rules and security appliances on the path check traffic on `L7`, an application can be checked on the path lookup.

It's almost impossible to standardize application names across all vendors. You can define your own application name with regular expressions.


!!! info

    The application name input is simply a string, so it must be defined
    exactly as it appears in a security rule!

![Application](pathlookup/pathlookup_application.webp)

### Source/Destination IP Regions

When testing access to or from the internet, source or destination IP regions can be set.

Example: Europe, China, etc.

By default, IP regions are not evaluated.

!!! info

    IP regions are represented as strings, so they must be defined exactly as
    they are appear in a security rule!

![Regions](pathlookup/pathlookup_src_dst_regions.webp)

### Path Lookup Mode

If you've used a network CIDR instead of a single IP address, you will have the option between:

- **Network Mode** -- Simulation starts and ends with whole networks; individual
  hosts are not considered.

- **Host Mode** -- Simulation starts and ends with each host. It is limited to
  255 hosts, source and destination combined.

Then click **Submit**.

This is how the path lookup might look:

![Path lookup example](pathlookup/example.webp)

### Security Rules

![Path lookup drop](pathlookup/pathlookup_drop.webp)

If **Drop** is selected, the path lookup will stop when a security rule denies
traffic.

![Path lookup continue](pathlookup/pathlookup_continue.webp)

If **Continue** is selected, the path lookup continues and does not apply the 
policy's deny; in the detail pane, it is labeled as `(not applied)`.

### IPsec & VXLAN tunnel endpoints

To simplify the identification of where IPsec and VXLAN tunnels begin and terminate, especially when spanning multiple devices, direct links between
tunnel endpoints are now displayed in path lookups. You can examine these links by right-clicking the connection and selecting `Show packet detail`.

!!! warning

    This feature is currently enabled by default and cannot be disabled.

If multiple tunnels of the same type exist between two devices (where the type is either IPsec or VXLAN), only a single tunnel of that type will be displayed.
In some cases, new connections may not be visible if a tunnel connection overlaps with an existing connection, for example:

![IPsec connection overlapping with existing connections](ipsec_edge_overlapping.webp){ width="473" .center}

To resolve this, move the middle device to a different position:

![IPsec connection overlapping resolved by moving device](ipsec_edge_overlapping_resolved.webp){ width="473" .center}

## Multicast Tree Lookup

If you want to understand how a certain multicast flow is used, you can use
the **Multicast Tree Lookup** tab. Just select the correct option and
enter the relevant details.

![Multicast form](pathlookup/multicast.webp)

You will then see the Multicast Tree:

![Multicast example](pathlookup/multicast_example.webp)

And you will have access to a lot of information regarding the Multicast
forwarding decision:

![Multicast path inspector](pathlookup/multicast_path_inspector.webp)

## Host To Gateway

To find out more details between a host and its network gateway, you can
use the **Host To Gateway** tab. You only need to provide the host, and
you will the details:

![Host To Gateway form](pathlookup/host_to_gw.webp)

## Inspecting and Adjusting Path Lookup

### Path Controls

With the right mouse click, more options are enabled:

![Path controls](pathlookup/path_controls.webp)

After opening the details with `Explore`, you can select the destination link to proceed with packet analysis:

![Path detail](pathlookup/path_detail.webp)

### Understand the Path Selection

To understand the decision taken by a device, right-click the device
and click `Explore`. You will then be presented with the details. If you
have more than one interface where the flow can come from, you will need
to select the interface you want to look at. Similarly, if you have
several interfaces that can be used to forward the traffic, you will
have to choose one. Then, in the middle of the table, you will see the
forwarding decision:

![Forwarding decision](pathlookup/forwarding_decision.webp)

In this example, we are looking at the device `L21C11`, which has 2
incoming interfaces and one forwarding for this flow:

![Forwarding decision animation](pathlookup/forwarding_decision_animation.webp)

### Visualization Setup

You can set up what you want to prioritize in the view. Simply move
the bars up or down.

![Visualization setup](pathlookup/visualization_setup_movable.webp)
