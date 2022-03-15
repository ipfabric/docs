# Network Connectivity Requirements

During the snapshot operations, the user can control network bandwidth limit which never exceeds an aggregate of set bandwidths in any direction to provide an additional safety measure.

IP Fabric should be connected to a network that has direct connectivity to managed devices. [Jumphost server](Jumphost_settings) can also be set up and used.

## Inbound Flow List

| Source port (remote)  |Destination port (local)   |Protocol   |Description   |
|---|---|---|---|
|>1024   |443   |TCP   |User Interface   |
|>1024   |8443   |TCP   |Administrative Interface   |
|443   |>1024   |TCP   |Network Infrastructure Interaction - API, Support, Updates (Optional)   |
|22    |>1024   |TCP   |Network Infrastructure Interaction - SSH    |
|23    |>1024   |TCP   |Network Infrastructure Interaction - Telnet    |
|N/A   |N/A   |ICMP   |Network Infrastructure Interaction - Traceroute   |

## Outbound Flow List

|Source port (local)  |Destination port (remote)  |Protocol  |Description  |
|---|---|---|---|
|443  |>1024  |TCP  |User Interface  |
|8443  |>1024  |TCP  |Administrative Interface  |
|>1024  |443  |TCP  |Network Infrastructure Interaction - API, Support, Updates (Optional)  |
|>1024  |22  |TCP  |Network Infrastructure Interaction - SSH  |
|>1024  |23  |TCP  |Network Infrastructure Interaction - Telnet  |
|N/A  |N/A  |ICMP  |Network Infrastructure Interaction - Traceroute  |

Internet connectivity is used to check product updates, upgrades, setup support VPN, send error reports, and submit support tickets.

## Jumphost Server Requirements

|  Python version    | Support     |
|--------------------|-------------|
| 2.7                | supported   |
| 3.5                | supported   |
| 3.6                | supported   |
| 3.7                | supported   |
| 3.8                | unsupported |
| 3.9                | unsupported |
