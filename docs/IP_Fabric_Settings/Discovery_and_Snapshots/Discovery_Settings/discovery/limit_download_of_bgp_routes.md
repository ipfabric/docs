---
description: In IP Fabric platform, you can Limit Download of BGP Routes as the full routing table, including full BGP, may contain fewer than 700K records.
---

# Limit download of BGP routes

The full routing table, including full BGP, may contain more than 900K
records in 2023.

Downloading and processing such a large amount of data
is time-consuming and may not provide any relevant information about the
internal IP addressing scheme.

In cases where we expect to discover a router with a full BGP table, we
can limit the total number of BGP routes stored in the database.

You can find the threshold configuration in **Settings --> Discovery Settings
--> Discovery --> Limit download BGP routes**.

The lower limit available is currently 10000 BGP routes. The IP Fabric
will read the full routing table but will filter BGP routes per
threshold before storing them in the database.

![Limit download of BGP routes](limit-bgp-routes.png)
