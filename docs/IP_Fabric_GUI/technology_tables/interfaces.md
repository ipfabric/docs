---
description: The Interfaces section provides detailed information about packet counters and undesired network states.
---

# Interfaces

The Interfaces section provides detailed information about packet
counters and undesired network states.

## Interface Transmission Rates

Packet loss issues due to errors and drops are detailed for each
direction, interface, and device where an issue occurs. Each packet loss
issue is assigned an impact rating, based on the amount of productivity
impact and the number of affected users, and the ratings range from
non-impactful (1-5), to minor business productivity slowdowns (6-9),
through to major productivity impacts (10+). The number of affected
users depends on the topological location of an issue, with uplinks
usually affecting more end hosts than access ports.

The transmission rates of packets per second and megabits per second are
presented for each interface and device in each direction.

## Interface State

The Half-Duplex table presents interfaces in the Half-Duplex mode. Most
network equipment supports and prefers the full duplex setting. There
are some exceptions when half duplex operation is necessary, and in such cases,
all sides must be consistently set for half-duplex operations.

The ErrDisabled table presents information about interfaces disabled due
to violations of operational parameters. Interfaces in an error state
should be self-healed by the automatic recovery timers or recovered
manually, to ensure no future repeats of the same violation.

## Connectivity Matrix

The Connectivity matrix maps connection information between devices for
the network protocols to form dynamic neighbor relationships. Each
direction of the connection is represented on a separate line. Therefore,
a bidirectional connection will be represented by two lines. The table
can be filtered by protocol, interface, or hostname.
