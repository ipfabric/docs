# Overview

This post is intended to explain the use of the IP Fabric Path Lookup API request, remodeled as part of the change in diagrams heralded by version `4.0.2` in October 2021.

## Python SDK

For IP Fabric version `4.0.x` - `4.2.x` diagramming has been built into `python-ipfabric`

- [https://github.com/community-fabric/python-ipfabric](https://github.com/community-fabric/python-ipfabric)
- `pip install ipfabric`

For IP Fabric version 4.3.x diagramming has been built into `python-ipfabric-diagrams` and is the recommended method for graphing via the API.

- [https://github.com/community-fabric/python-ipfabric-diagrams](https://github.com/community-fabric/python-ipfabric-diagrams)
- `pip install ipfabric-diagrams`

## API Endpoints

- `https://host.domain/api/v1/graphs` - for JSON output
- `https://host.domain/api/v1/graphs/svg` - for SVG vector image output
- `https://host.domain/api/v1/graphs/png` - for PNG bitmap image output

## POST Request

Requests are made using a `POST` to the endpoint listed above for the desired output. Headers must contain:

- `content-type: application/json`
- `X-API-Token:` (the API token provided from the IP Fabric Settings UI)

and the body of the request contains the JSON described in the next section.

### Request Body

Contains a JSON data structure with the keys

- `snapshot` *[mandatory]* - A quoted string containing the ID of the required snapshot. Can also use the reserved strings `$last`, `$prev` and `$lastLocked`
- `parameters` _[mandatory]_ - A nested JSON data structure with keys
- `positions` *[optional]* - A nested JSON data structure consisting of keys representing the serial number of devices and their positions in the completed diagram. Origin of `x=0, y=0` is the top left of the resulting image.

    !!! example "Sample position data structure"

        ``` json
        {
            "positions": {
                "SNXXXXXXXXX": {
                    "x": 40,
                    "y": 160
                }
            }
        }
        ```

- `settings` *[optional]* - A nested JSON data structure representing visualisation settings to override the default view in IP Fabric's diagram canvas. In these settings, it is possible to:
    - change edge properties like colours and thickness of lines representing protocols and groups
    - change labels on the edges and interfaces
    - hide certain device types.

        !!! example "Example settings data structure"

            ``` json
            {
                "settings": {
                    "edges": [
                        {
                            "id": "6129bb53-d19d-47ee-8f45-8829073221c1",
                            "name": "vxlan",
                            "type": "pathLookupEdge",
                            "grouped": false,
                            "style": {
                                "color": "#d4b524",
                                "pattern": "solid",
                                "thicknessThresholds": [2,4,8]
                            },
                            "visible": true,
                            "labels": ["intName","protocol"]
                        }
                    ]
                }
            }
            ```

### Response

If the PNG or SVG endpoints are selected, the request returns a binary File representing the desired output.

Using the /graphs endpoint, a successful request returns a JSON response of the form:

```json
{
    "graphResult": {...},
    "pathlookup": {...}
}
```

#### `graphResult`

The `graphResult` construct describes the detail of the topology of the end to end path through the network. It consists of three sections:

- `settings` - echoes the settings from the request body or the system settings as they apply to line styles, colours, weights and labels; hidden device types and groupings
- `boxLabels` - text labels for each of the groups
- `graphData` - a JSON construct containing a list of nodes and edges in the topological view of the path. Takes the form:

```json
{
    "nodes": {...},
    "edges": {...}
}
```

where `nodes` contains data relating to the individual nodes in the graph. Each one is assigned a `vDevice` ID but there is recorded in each its hostname as `label`, it's `position`, its serial number in the `sn` field and the device `type`. Other key:value pairs relate to the inner workings of the IP Fabric graphing process.

!!! example

    ``` json
    {
        "vDevice/111111111": {
                "boxId": "SITE1",
                "children": [],
                "graphType": "pathLookup",
                "id": "vDevice/111111111",
                "label": "HOSTNAME",
                "parentPath": null,
                "position": {
                    "x": 200,
                    "y": 160
                },
                "sn": "SNXXXXXXXX",
                "type": "switch"
    }
    ```

`edges` contains data relating to the connections between the nodes along the data path. Each one is assigned an ID consisting of a combination of the node ID and interface at each end of the edge. The JSON construct also includes labels for the ends and the centre of the line, graphical details like (x,y) positions of the line and arrowheads and the colours and style of the lines. The `severity_info` key:value pair contains the information about how the edge conforms to applied intent checks; and the `packet` subtree contains a list of the layered packet headers in the simulation as it passes through the edge.

!!! example

    ``` json
    {
        "packet": [
            {
                "dst": "dddd.dddd.dddd",
                "etherType": "ip",
                "src": "aaaa.aaaa.aaaa",
                "type": "ethernet",
                "vlan": 10
            },
            {
                "dst": [
                    "10.10.20.112"
                ],
                "protocol": "tcp",
                "src": [
                    "10.10.10.112"
                ],
                "type": "ip"
            },
            {
                "dst": [
                    "80"
                ],
                "flags": [],
                "src": [
                    "10000"
                ],
                "type": "tcp"
            }
        ]
    }
    ```

#### `pathlookup`

The `pathlookup` construct describes the hop-by-hop forwarding and policy decisions that have been taken to get from source to destination. Notable key:value pairs within that construct include:

  - `eventSummary` - which highlights the success or failure of the path and the cause of any issues along the way.

    - `flags` will show if any policy has caused the traffic to fail to reach the destination (e.g. `acl-deny` or `zone-deny`)

    - `topics` is a construct to represent the "Result" tab in the UI - it shows whether there have been ACL or firewall policies affecting the path, or any issues with forwarding behaviour. Positive values for the "0" key show that the decision has allowed traffic to pass; positive values for any of the other keys indicate a failure in the evaluation at some point

  - `decisions` - contains a record for each device in the path and the forwarding and policy decision it has to make in the path. For each device:

    - `trafficIn` is a representation of the ingress interface and the edge that it is connected to
    - `trafficOut` represents the egress interface and the edge that it sends traffic along towards the destination
    - `traces` contains the data to represent how that decision was taken - for example that might include:

        - a `switching-nexthop` decision in a switch will require a MAC address table match;
        - an `ip-routing` decision in a router will require a routing table lookup and an ARP table ;
        - an `ip-routing` decision in a zone-based firewall will add in a security check to validate that policy allows the packet to pass;
        - an `mpls-switching` decision will validate the VRF, MPLS labels and push/pop behaviour in the label stack; and so on.

I've not given any specific examples here as they vary wildly depending on the specifics of your environment. There are also numerous additional fields in the `pathlookup` construct which will also be dependent on your particular path check. And there are some key:value pairs which have specific internal usage. But by using trial and error, you should be able to get a good handle on the behaviour of the path lookup using this guidance.

From this note, you can see just how much thought and detail has gone into the development of the path lookup process. Hopefully it illustrates how closely IP Fabric models the behaviour of the data plane of network devices to give an accurate view of the impact of the network on forwarding behaviour.

!!! note

    If you are interested in multicast or host-to-gateway path lookups, take a look at our other tech notes. The result will be the same but request body will use different parameters.
