# 03 - Starting point for the discovery (optional)

If you know a particular starting point for discovering the network, the information can be entered at **Settings → Discovery Seed**. This option does not exclude any networks from discovery (for this option see next step).

The starting points can be management IP addresses or networks, or existing inventory data can also be imported.

If no seed information is entered, the discovery will begin from the current default gateway. The system will try to trace `RFC6890` subnets (by default) to determine the immediate next hops to log in to.

![Discovery seed](seed.png)
