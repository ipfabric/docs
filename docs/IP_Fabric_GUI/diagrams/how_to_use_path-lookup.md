---
description: This page explains how to use path lookup.
---

# How To Use Path Lookup

## Unicast Path Lookup

![Unicast form](pathlookup/unicast.png)

### First Hop Algorithm And VRF

The **First Hop Algorithm** adds the possibility to start the path lookup simulation from a different device than the closest one.

If the **Automatic** option is selected, IP Fabric initiates the path lookup simulation from the closest possible device. VRF is also automatically selected by default but can be changed manually.

![First hop algorithm](pathlookup/first_hop_algorithm.png)

The **User defined** First Hop Algorithm can be useful when simulating a flow where the source network is not known by IP Fabric.

To simulate such a flow, it is necessary to specify the starting point by entering the name of the device and the interface which will be used to start the path lookup.

Packets will use the indicated source IP address.

!!! Example "User-Defined First Hop Algorithm"

    In the example below, the source network `10.25.25.0/24` is not known by IP Fabric. To show the path between a client in this network and a server in a network known by IP Fabric:

    ![User Defined First hop algorithm example](pathlookup/user_defined_first_hop_algorithm_example_drawing.png){: style="height:150px"}

    1. Select the **User defined** First Hop Algorithm.
    2. Search for the device where you want to start the path: `L43EXR1`.
    3. Select the source interface: `Et0/1`.
    4. Enter the source IP from the network outside the scope of IP Fabric: `10.25.25.10`.
    5. Finally, enter the destination IP: `10.66.122.110`.

    ![User Defined First hop algorithm](pathlookup/user_defined_first_hop_algorithm.png)

    This is the result you will get:

    ![User Defined First hop algorithm Result](pathlookup/user_defined_first_hop_algorithm_result.png)

### Source/Destination IP Address and Port

A plain IP address or a CIDR (Classless Inter-Domain Routing) can be used as a source/destination IP address, for example, when simulating path lookup from a host to a network.

By default, the `ICMP` protocol and the `Echo request` option are chosen for path lookup.

![Source and destination](pathlookup/pathlookup_src_dst.png)

When switched to `Web HTTP/HTTPS`, TCP destination ports `80` and `443` with the `(web|http|https)` application are set by default.

![HTTP default](pathlookup/pathlookup_http_default.png)

When extending details, the transport protocol and range of ports can be specified for a source and for a destination. When more destination ports are specified, IP Fabric will analyze all of them individually during the path lookup.

![Source and destination ports](pathlookup/pathlookup_src_dst_port.png)

The port can be changed to an arbitrary one for TCP/UDP protocols.

The following flags can also be set for TCP traffic: `None` / `ACK` / `FIN` / `SYN` / `RST` / `PSH` / `URG`.

### TTL and Fragment Offset

In **More details**, **TTL** (Time to live) and **Fragment offset** can be set -- thus affecting the path lookup output. The default TTL is 128 and Fragment offset is set to 0.

![TTL and Fragmentation](pathlookup/pathlookup_ttl_fragment.png)

### Application

When evaluating security rules and security appliances on the path check traffic on `L7`, an application can be checked on the path lookup.

It's almost impossible to standardize application names across all vendors. You can define your own application name with regular expressions.


!!! info

    The application name input is simply a string, so it must be defined
    exactly as it appears in a security rule!

![Application](pathlookup/pathlookup_application.png)

### Source/Destination IP Regions

When testing access to or from the internet, source or destination IP regions can be set.

Example: Europe, China, etc.

By default, IP regions are not evaluated.

!!! info

    IP regions are represented as strings, so they must be defined exactly as
    they are appear in a security rule!

![Regions](pathlookup/pathlookup_src_dst_regions.png)

### Path Lookup Mode

If you've used a network CIDR instead of a single IP address, you will have the option between:

- **Network Mode** -- Simulation starts and ends with whole networks; individual
  hosts are not considered.

- **Host Mode** -- Simulation starts and ends with each host. It is limited to
  255 hosts, source and destination combined.

Then click **Submit**.

This is how the path lookup might look:

![Path lookup example](pathlookup/example.png)

### Security Rules

![Path lookup drop](pathlookup/pathlookup_drop.png)

If **Drop** is selected, the path lookup will stop when a security rule denies
traffic.

![Path lookup continue](pathlookup/pathlookup_continue.png)

If **Continue** is selected, the path lookup continues and does not apply the 
policy's deny; in the detail pane, it is labeled as `(not applied)`.

## Multicast Tree Lookup

If you want to understand how a certain multicast flow is used, you can use
the **Multicast Tree Lookup** tab. Just select the correct option and
enter the relevant details.

![Multicast form](pathlookup/multicast.png)

You will then see the Multicast Tree:

![Multicast example](pathlookup/multicast_example.png)

And you will have access to a lot of information regarding the Multicast
forwarding decision:

![Multicast path inspector](pathlookup/multicast_path_inspector.png)

## Host To Gateway

To find out more details between a host and its network gateway, you can
use the **Host To Gateway** tab. You only need to provide the host, and
you will the details:

![Host To Gateway form](pathlookup/host_to_gw.png)

## Inspecting and Adjusting Path Lookup

### Path Controls

With the right mouse click, more options are enabled:

![Path controls](pathlookup/path_controls.png)

After opening the details with `Explore`, you can select the destination link to proceed with packet analysis:

![Path detail](pathlookup/path_detail.png)

### Understand the Path Selection

To understand the decision taken by a device, right-click the device
and click `Explore`. You will then be presented with the details. If you
have more than one interface where the flow can come from, you will need
to select the interface you want to look at. Similarly, if you have
several interfaces that can be used to forward the traffic, you will
have to choose one. Then, in the middle of the table, you will see the
forwarding decision:

![Forwarding decision](pathlookup/forwarding_decision.png)

In this example, we are looking at the device `L21C11`, which has 2
incoming interfaces and one forwarding for this flow:

![Forwarding decision animation](pathlookup/forwarding_decision_animation.gif)

### Visualization Setup

You can set up what you want to prioritize in the view. Simply move
the bars up or down.

![Visualization setup](pathlookup/visualization_setup_movable.png)
