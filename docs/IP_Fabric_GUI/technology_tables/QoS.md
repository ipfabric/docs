---
description: The QoS technology section provides information about all class-maps and applied policy-maps in the network, including the relationships between hierarchical policies, the class rates, and match parameters.
---

# QoS

### Overview

The **QoS** technology section provides information about all class-maps and
applied policy-maps in the network, including the relationships between
hierarchical policies, the class rates, and match parameters.

### Applied Service-Policies

The **Applied Service-Policies** tab provides details of every class of service policy applied to an
interface from each managed network device. Each line represents an
active class (which can be searched for by the offered or drop rates),
the matching parameters of the class, and the parent policy. `Site` is the
site where devices with the applied policy are located; `Hostname` is the
short name of the device with the applied policy; `Policy` is the applied
service policy name; `Type` is the type of applied service policy,
depending on the direction or hierarchy; `Interface` is the interface to which the
policy-map is applied; `Class` is the specific class name of the policy
map for which the detailed information is displayed; `Child` or `Parent policy` is
the policy-map name applied as a child to the class, or a parent policy
of a policy of a class if present; `Match` is the match parameters of the
class; `#Packets` and `#Bytes` are the number of matched packets and bytes for
each class; `Rate offered` is the bitrate of traffic attempting to pass
through the class; `Drop rate` is the bitrate of dropped traffic.

### Shaping

The **Shaping** tab details every class that has a shaping action and the specific
parameters of that class. `Site` is the site where devices with the applied
policy are located; `Hostname` is the short name of the device with the applied
policy; `Policy` is the applied service policy name; `Type` is the type of applied
service policy depending on the direction or hierarchy; `Interface` is the
interface to which the policy-map is applied; `Class` is the specific class name of the
policy map for which the detailed information is displayed; `Child policy` is the
policy-map name applied as a child to the class if present; `Parent policy` is
the policy-map name of a parent policy-map for this specific class if present;
`Match` is the match parameters of the class; `Shape type` is the Shaper bucket
calculation type, Average (`bc`) or Peak (`bc+be`); `CIR` is the Committed
Information Rate; `Bc` is the Burst Committed (or bucket size); `Be` is the Burst
Excess (or burst size); `Target rate` is the maximum rate at which traffic is expected to
leave the shaper over prolonged intervals.

### Queuing

The **Queueing** tab details every class with queuing action along with
each class's specific queuing parameters. `Site` is the site of
the devices with the applied policy; `Hostname` is the short name of the
device with the applied policy. `Policy` is the applied service policy
name; `Type` is the type of applied service policy according to direction
or hierarchy; `Interface` is the interface to which the policy-map is applied;
`Class` is the specific class name of the policy map for which detailed information
is displayed; `Child policy` is the policy-map name applied as a child
to the class if present; `Parent policy` is the policy-map name of a
parent policy-map for this specific class if present; `Match` is the match
parameters of the class; `Queue limit` is the maximum depth of the queue;
`Bandwidth` is the minimum bandwidth reservation assigned to the queue and
used by the scheduler; `Queue depth` is the current observed depth of the
queue; `#Total drops` are the number of packet drops in a class; `#Packets
output` is the number of packets sent by the class; `#Bytes output` is the
number of bytes sent by the class.

### Policing

The **Policing** tab details every class with a policing action with the specific
policing parameters. `Site` is the site where devices with the applied
policy are located; `Hostname` is the short name of the device with the
applied policy; `Policy` is the applied service policy name; `Type` is the
type of the applied service policy according to direction or hierarchy;
`Interface` is the interface to which the policy-map is applied; `Class` is the
specific class name of the policy map for which detailed information is displayed;
`Child policy` is the policy-map name applied as a child to the class
if present; `Parent policy` is the policy-map name of a parent policy-map
for this specific class if present; `Match` is the match parameters of the
class; `Police type` is the method of rate calculation; `CIR` is the
Committed Information Rate; `Bc` is the burst committed; `Action` is the
policing actions (or colors); `Conformed` is the number of packets, bytes,
or rate in bits per second of traffic below the policing rate; `Exceeded`
is the number of packets, bytes, or rate in bits per second of traffic
exceeding the policing rate (or second color).

### Priority

The **Priority** tab details every class with a priority action and associated
specific priority parameters. `Site` is the site where devices with the
applied policy are located; `Hostname` is the short name of the device
with the applied policy; `Policy` is the applied service policy name; `Type`
is the type of the applied service policy according to direction or
hierarchy; `Interface` is the interface to which the policy-map is applied;
`Class` is the specific class name of the policy map for which detailed information
is displayed; `Child policy` is the policy-map name applied as a child
to the class if present; `Parent polic`y is the policy-map name of a
parent policy-map for a specific class if present; `Match` is the match
parameters of the class; `Strict priority` is the level or limit of
prioritization; `#Drops` is the number of packets dropped due to the
excessive offered rate.

### Marking

The **Marking** tab details every class with a marking action along with specific
marking parameters. `Site` is the site where devices with the applied
policy are located. `Hostname` is the short name of the device with the
applied policy; `Policy` is the applied service policy name; `Type` is the
type of the applied service policy according to the direction or
hierarchy; `Interface` is the interface to which the policy-map is applied;
`Class` is the specific class name of the policy map for which detailed
information is displayed; `Child policy` is the policy-map name
applied as a child to the class if present; `Parent policy` is the
policy-map name of a parent policy-map for this specific class if
present; `Match` is the match parameters of the class; `Set` is the QoS bit
specification standard; `Value` is the bit value being set; `#Packets` is the
number of packets marked by the class.

### Random Drops

The **Random Drops** tab details every class with a random early drop detection action
and associated specific random drop parameters. `Site` is the site where
devices with the applied policy are located. `Hostname` is the short name
of the device with the applied policy; `Policy` is the applied service
policy name; `Type` is the type of applied service policy according to
direction or hierarchy; `Interface` is the interface to which the policy-map is
applied; `Class` is the specific class name of the policy map for which
detailed information is displayed; `Child policy` is the policy-map name
applied as a child to the class if present; `Parent policy` is the
policy-map name of a parent policy-map for a specific class if present;
`Match` is the class's match parameters; `Random` is the type of random drop
used in a class; `Min` is the minimum probability queue depth threshold to
consider for a random drop; `Max` is the maximum probability queue depth
threshold to consider for a random drop; `ProbDrop` is the maximum probability
of a drop to occur from the total number of packets being queued; `Tx Pkts`
is the number of transmitted packets by class; `Tx Bytes` is the
number of transmitted bytes by class; `Random drops packets` is the number
of packets dropped by the algorithm; `Random drops bytes` is the number of
bytes dropped by the algorithm; `Tail drops packets` is the number of
packets dropped due to queue saturation; `Tail drops bytes` is the number
of bytes dropped due to queue saturation.
