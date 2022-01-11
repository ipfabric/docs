# Traceroute settings

# Traceroute settings

Traceroute is used when next hop is not available for SSH/telnet.
Devices discovered using traceroute are marked as *unmanaged* in IP
Fabric site diagrams.  More information about traceroute as a protocol
can be found on [Wikipedia](https://en.wikipedia.org/wiki/Traceroute).

For traceroute configuration go to  ***Settings → Advanced → Discovery
→ Traceroute settings.***

***Trace scope ***- limits traceroute scope to the defined subnets. This
prevents scan networks outside an internal network.

***RFC6890*** - this button resets ***Trace scope*** setting to subnets
defined in this RFC.

***Protocol*** - the protocol used for traceroute can be selected from
the options of ICMP (MS Windows like), UDP (Linux like), and TCP.

***Port*** - in case of UDP and TCP, the destination port can be
specified.
