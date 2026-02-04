---
description: 'This page describes the current limitation in IP Fabric regarding support for RFC 5549 (IPv4 routes with an IPv6 next hop).'
---

# IPv4 NLRI with IPv6 Next Hop (RFC 5549)

IP Fabric currently does not support routing tables that follow [RFC 5549](https://datatracker.ietf.org/doc/html/rfc5549), where IPv4 routes are advertised with an IPv6 next hop using MP-BGP.

The current routing model in IP Fabric assumes that:

- IPv4 routes use an IPv4 next hop
- IPv6 routes use an IPv6 next hop

As a result, routing information that relies on [RFC 5549](https://datatracker.ietf.org/doc/html/rfc5549) is not correctly represented and may be missing or incomplete in routing tables, path lookup, and reachability analysis.
