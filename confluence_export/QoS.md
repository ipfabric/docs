# QoS

## QoS

### Overview

The QoS technology section provides information about all class-maps and
applied policy-maps in the network, including the relationships between
hierarchical policies, the class rates, and match parameters.

### Applied Service-Policies

These provide details of every class of service policy applied to an
interface from each managed network device. Each line represents an
active class (which can be searched for by the offered or drop rates),
the matching parameters of the class, and the parent policy. Site is the
site where devices with the applied policy are located; Hostname is the
short name of the device with the applied policy; Policy is the applied
service policy name; Type is the type of applied service policy,
depending on the direction or hierarchy; Interface is the interface the
policy-map is applied to; Class is the specific class name of the policy
map the detailed information is displayed for; Child or Parent policy is
the policy-map name applied as a child to the class, or a parent policy
of a policy of a class if present; Match is the match parameters of the
class; Packets and Bytes are the number of matched packets and bytes for
each class; Rate Offered is the bitrate of traffic attempting to pass
through the class; Drop rate is the bitrate of dropped traffic.

### Shaping

The shaping table details every class that has shaping action and the
specific parameters of that class. Site is the site where devices with
the applied policy is located at; Hostname is the short name of the
device with the applied policy; Policy is the applied service policy
name; Type is the type of applied service policy depending on the
direction or hierarchy; Interface is the interface the policy-map is
applied to; Class is the specific class name of the policy map the
detailed information is displayed for; Child Policy is the policy-map
name applied as a child to the class if present; Parent Policy is the
policy-map name of a parent policy-map for this specific class if
present; Match is the match parameters of the class; Shape Type is the
Shaper bucket calculation type, Avegare (bc) or Peak (bc+be); CIR is the
Committed Information Rate; BC is the Burst Committed (or bucket size);
BE is the Burst Excess (or burst size); Target Rate is the maximum rate
traffic is expected to leave the shaper over prolonged intervals.

### Queuing

The queuing table details every class with queuing action along with
each class's specific queuing parameters. Site is the site location of
the devices with the applied policy; Hostname is the short name of the
device with the applied policy. Policy is the Applied service policy
name; Type is the Type of applied service policy according to direction
or hierarchy; Interface is the interface the policy-map is applied to;
Class is the Specific class name of the policy map detailed information
is displayed for; Child policy is the policy-map name applied as a child
to the class if present; Parent policy is the policy-map name of a
parent policy-map for this specific class if present; Match is the match
parameters of the class; Queue Limit is the Maximum depth of the queue;
Bandwidth is the Minimum bandwidth reservation assigned to the queue and
used by the scheduler; Queue depth is the current observed depth of the
queue; Total Drops are the number of packet drops in a class; Packets
Output is the number of packets sent by the class; Bytes Output is the
number of bytes sent by the class.

### Policing

This table details every class with a policing action with the specific
policing parameters. Site is the site where devices with the applied
policy are located; Hostname is the short name of the device with the
applied policy; Policy is the applied service policy name; Type is the
Type of the applied service policy according to direction or hierarchy;
Interface is the interface the policy-map is applied to; Class is the
specific class name of the policy map detailed information is displayed
for; Child policy is the policy-map name applied as a child to the class
if present; Parent Policy is the policy-map name of a parent policy-map
for this specific class if present; Match is the match parameters of the
class; Police type is the method of rate calculation; CIR is the
committed information rate; BC is the burst committed; Action is the
policing actions (or colors); Conformed is the number of packets, bytes,
or rate in bits per second of traffic below the policing rate; Exceeded
is the number of packets, bytes, or rate in bits per second of traffic
exceeding the policing rate (or second color).

### Priority

This table details every class with a priority action and associated
specific priority parameters. Site is the site where devices with the
applied policy are located; Hostname is the short name of the device
with the applied policy; Policy is the Applied service policy name; Type
is the type of the applied service policy according to direction or
hierarchy; Interface is the interface the policy-map is applied to;
Class is the specific class name of the policy map detailed information
is displayed for; Child policy is the policy-map name applied as a child
to the class, if present; Parent policy is the policy-map name of a
parent policy-map for a specific class if present; Match is the match
parameters of the class; Strict priority is the level or limit of
prioritization; Drops is the number of packets dropped due to the
excessive offered rate.

### Marking

This table details every class with a marking action along with specific
marking parameters. Site is the site where devices with the applied
policy are located. Hostname is the short name of the device with the
applied policy; Policy is the Applied service policy name; Type is the
Type of the applied service policy according to the direction or
hierarchy; Interface is the interface the policy-map is applied to;
Class is the specific class name of the policy map the detailed
information is displayed for; Child Policy is the policy-map name
applied as a child to the class if present; Parent Policy is the
policy-map name of a parent policy-map for this specific class if
present; Match is the match parameters of the class; Set is the QoS bit
specification standard; Value is the bit value being set; Packets is the
number of packets marked by the class.

### Random Drops

This table details every class with a random early drop detection action
and associated specific random drop parameters. Site is the site where
devices with the applied policy are located. Hostname is the short name
of the device with the applied policy; Policy is the Applied service
policy name; Type is the type of applied service policy according to
direction or hierarchy; Interface is the interface the policy-map is
applied to; Class is the specific class name of the policy map the
detailed information displayed for; Child policy is the policy-map name
applied as a child to the class if present; Parent Policy is the
policy-map name of a parent policy-map for a specific class if present;
Match is the class's match parameters; Random is the type of random drop
used in a class; Min is the minimum probability queue depth threshold to
consider a random drop; Max is the maximum probability queue depth
threshold to consider for a random drop; Prob is the maximum probability
of a drop to occur from the total number of packets being queued; Tx
Pkts is the number of transmitted packets by class; Tx Bytes is the
number of transmitted bytes by class; Random Drops Packets is the number
of packets dropped by the algorithm; Random drops bytes is the number of
bytes dropped by the algorithm; Tail Drops Packets is the number of
packets dropped due to queue saturation; Tail Drops Bytes is the number
of bytes dropped due to queue saturation.
