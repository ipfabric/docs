---
description: In this section we go through the IP Scope and how to include and exclude networks from discovery. By default, there are no limitations on discovery.
---

# IP Scope

## Including And Excluding Networks From Discovery

By default, there are no limitations on discovery and all IP addresses
are allowed (i.e. *Include scope* is `0.0.0.0/0`)

Discovery can be limited to one or more subnets using **Settings →
Advanced → Discovery → IP Scope → IP networks to include in discovery**
and analysis. Enter one or more subnets to limit the discovery process
to addresses from particular networks.

Specific parts of the network can be also excluded from discovery
using **Settings → Advanced → Discovery →  IP Scope → IP networks to
exclude from discovery** and analysis.  

!!! warning "Priority"

    Exclude option takes precedence over include.

    IP Scope settings are not applied to Vendors discovered using API
    (everything is downloaded and used in discovery)

***Example***:

*IP networks to include in discovery and analysis:*  `10.0.0.0/8`

*IP networks to exclude from discovery and analysis:* `10.24.0.0/16`

*Result:* Only network `10.0.0.0/8` is scanned excluding `10.24.0.0/16`
subnet.
