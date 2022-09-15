# Policy

## Prefix Lists

Prefix lists section contains definitions of all prefix lists. There are 2 tabs according to address family -- IPv4 and IPv6

## Routing

This section contains information about routing policies, their definition and where they are applied. Currently only route maps are supported and present here.

There are 2 tabs -- Policies and Interfaces.

### Policies

Policies tab contains definition of routing policies, their names, sequence numbers, matching conditions, set actions etc.

In case match condition uses reference to ACL or Prefix list, it is a hyperlink to appropriate ACL/Prefix list in its section.

### Interfaces

Interfaces tab contains information about interfaces which have assigned some routing policy on them (used for policy based routing). Optionally there is also information about used address-family or status of routing policy.
