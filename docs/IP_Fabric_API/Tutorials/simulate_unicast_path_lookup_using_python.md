---
description: A quick tutorial about how to use IP Fabric’s API with python-ipfabric-diagrams Python module.
---

# Simulate Unicast Path Lookup In IP Fabric Using Python

A quick tutorial about how to use IP Fabric’s API with [python-ipfabric](https://pypi.org/project/ipfabric/) Python module.

## Prerequisites

We strongly recommend using a virtual environment for development. To Install the Python package in your environment:

```bash
pip install ipfabric
```

## Code Snippet

There are more examples in our Git, but we will test unicast path simulation with the following code snippet:

```py
"""
Unicast path simulation with IP Fabric's Python package (valid for version 4.3 and later)
"""
# from ipfabric_diagrams import IPFDiagram, PathLookupSettings, Unicast, Algorithm, EntryPoint, OtherOptions  # SDK < v6.2
from ipfabric.diagrams import IPFDiagram, PathLookupSettings, Unicast, Algorithm, EntryPoint, OtherOptions  # SDK >= v6.2

if __name__ == '__main__':
    ipf = IPFDiagram(base_url='https://ipfabric_fqdn/', token='api_token', verify=False, timeout=15)

    print('  \nStarting with path simulation..')
    uni = Unicast(
        startingPoint='10.38.115.1',
        destinationPoint='10.66.126.1',
        protocol='tcp',
        srcPorts='10000',
        dstPorts='80',
        ttl=64,
        fragmentOffset=0
    )

    json_data = ipf.diagram_json(uni)

    path_result = json_data['pathlookup']['passingTraffic']

    print("""
    Simulation finished. Legend:
    - all = all traffic is reaching destination
    - part = some traffic is reaching destination
    - none = some traffic is reaching destination
    """)

    print('  Result is : {}'.format(path_result))
    print()

    ipf.close()
```

More examples at [this link](https://gitlab.com/ip-fabric/integrations/python-ipfabric/-/tree/develop/examples/graphs)
