# How To Use Path Look-Up

## Unicast Path-Lookup

![Unicast form](unicast.png)

Enter the details:

-   Source IP / CIDR

-   Port (Source Port)

-   VRF (Virtual Routing and Forwarding Instance)

-   Destination IP / CIDR

-   Port (Destination Port)

-   Protocol: TCP/UDP/ICMP

-   Flags: None/ACK/FIN/SYN/RST/PSH/URG

If you’ve used a network instead of a single IP, you will have the
option between:

– **Network Mode**: simulation stats and ends with whole networks,
individual hosts are not considered

– **Host Mode**: simulation starts and ends with each host. It is
limited to 255 hosts, source and destination combined.

Then click on submit:

![Path look-up example](example.png)


## Path Controls

With the mouse right-click, more options are enabled:
![Path controls](path_controls.png)

After opening the details, we can select the destination link to proceed with packet analysis:
![Path detail](path_detail.png)

## Understand The Path Selection

To understand the decision taken by a device, right-click on the device
and "show detail". You will then be presented with the details. If you
have more than one interface where the flow can come from, you will need
to select the interface you want to look at. Similarly, if you have
several interfaces that can be used to forward the traffic, you will
have to choose one. Then in the middle of the table, you will see the
forwarding decision:

![Forwarding decision](forwarding_decision.png)

In this example, we are looking at the device L33R4, which has 2
incoming interfaces and one forwarding for this flow:

![Forwarding decision animation](forwarding_decision_animation.gif)

## Multicast Tree Look-Up

You want to understand how a certain multicast flow is used, you can use
the Multicast Tree Look-Up. For that, just select the correct option and
enter the relevant details

![Multicast form](multicast.png)

You will then see the Multicast Tree:

![Multicast example](multicast_example.png)

And you will have access to a lot of information regarding the Multicast
forwarding decision:

![Multicast path inspector](multicast_path_inspector.png)

## Host To Gateway

To find out more details between a host and its network gateway, you can
use this menu: Host To Gateway. You only need to provide the host, and
you will the details:

![Host to gateway form](host_to_gw.png)

## Visualization Setup

You can set up what you want to prioritize in the view. Just simply move
the bars up or down.

![Visualization setup](visualization_setup.png)

## Improvements from 4.3 version

From version 4.3, IP Fabric supports more granular path lookup.

### First Hop Algorithm
First hop algorithm can be defined - when **Automatic** option is selected,
source VRF can be automatically detected, or selected manually.

![First hop algorithm](first_hop_algorithm.png)

Also your source network device and its interface can be selected when choosing
**User defined** First Hop Algorithm.

### Source/Destination IP Address and Port

By default, ICMP protocol and Echo request is chosen for path lookup.

![Source and destination](pathlookup_src_dst.jpeg)

When switched to Web HTTP/HTTPS, TCP destination port 80 and 443 with (web|http|https) application is selected by default.

![HTTP default](pathlookup_http_default.jpeg)

When extending details, transport protocol and range of ports can be specified for a source and for a destination. When more destination ports are specified, IP Fabric will analyze all of them individually during the pathlookup.

![Source and destination ports](pathlookup_src_dst_port.png)

### TTL and Fragment Offset

In **More details**, **TTL** (Time to live ) and **Fragment offset** can be set - thus affecting path lookup - default TTL is 128 and Fragment offset is set to 0

![TTL and Fragmentation](pathlookup_ttl_fragment.png)

### Application

When evaluating security rules and security appliances on the path check traffic on L7, an application can be checked on the path lookup.

It’s almost impossible to standardize application names across all vendors. You can define your own application name with regular expressions.

An application name input is just a string, so it needs to be defined exactly as in a security rule!

![Application](pathlookup_application.png)

### Source/Destination IP Regions

When testing access to or from the internet, source or destination IP regions can be set.

Example: Europe, China, etc.

![Regions](pathlookup_src_dst_regions.png)
