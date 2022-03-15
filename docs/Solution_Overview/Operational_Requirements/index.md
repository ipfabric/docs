# Host Hardware Requirements

The IP Fabric platform runs on Intel Xeon Nehalem CPUs or later. The
system runs in at least 4 parallel threads, but scheduling can handle
operations even down to a single thread. IP Fabric uses less than 4GB of
RAM when idle, and an additional 12GB of RAM is required for collected
network information. The base installation requires 80GB of HDD space
and an additional 50MB per device for the network.

| CPU | RAM   | HDD  |
|-----|-------|------|
| 4C  | 16 GB | 90GB |


*Table 1: Minimum hardware requirements*

The following table represents the recommended hardware requirements for
optimal performance of the platform based on the number of network
infrastructure devices in the network.

| Devices | CPU | RAM    | HDD (OS + data)      |
|---------|-----|--------|----------------------|
| 500     | 4   | 16 GB  | 90 GB (80G + 10G)    |
| 1 000   | 4   | 32 GB  | 100 GB (80G + 20G)   |
| 2 000   | 8   | 64 GB  | 200 GB (80G + 120G)  |
| 5 000   | 12  | 64 GB  | 300 GB (80G + 220G)  |
| 10 000  | 16  | 128 GB | 550 GB (80G + 470G)  |
| 20 000  | 18  | 256 GB | 1000 GB (80G + 920G) |


*Table 2: Recommended hardware requirements*

!!! info
    
    ### Additional resources requirements
    
    To make sure you have enough resources, please use the following
    formulas.

    Data **disk storage** requires 1MB per device per each snapshot
    (example: 1350 devices, plan is to keep up to 100 snapshots => 135 GB
    data storage).

    **Memory** requires 5MB of RAM per device per each **loaded** snapshot
    (example: 1200 devices, up to 100 snapshots but only 3 loaded at a time
    (1200 x 5 = 6000 x 3) => 18 GB RAM).



The recommended hardware resources may not allow running the most
demanding graph traversal functions. These functions may require a
sizable memory pool to complete successfully.

## VMware Requirements

IP Fabric OVA images are built on Hardware Version 13.

ESXi version 6.5 or newer is required.
