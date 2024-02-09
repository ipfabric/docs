---
description: This is a glossary of terms used throughout the documentation.
---

# IP Fabric Glossary

_An explanation of terms used in the IP Fabric documentation and product interface._

## Behavior

**Snapshot**

: The data stored on an IP Fabric appliance represents the inventory, configuration, state, and topology of a group of network devices within a given time window. It can be:

    - **Scheduled** or **ad hoc** -- Settings in the IP Fabric UI allow a user to determine a regular schedule of snapshot creation; it is also possible to create additional snapshots on a one-off basis.

    - **Full** or **partial** -- The snapshot creation process is bounded by providing starting points (seeds), whitelisting and blacklisting subnets to crawl, providing credentials and jumphost information. Assuming that no part of the network is blacklisted, and all other information is available, a snapshot will discover as much of the network as it is able to authenticate against. This is considered a **full** snapshot. If a **partial** snapshot is required, only containing certain devices -- perhaps to validate a change outcome -- it is possible to select a set of existing devices against which a new snapshot can be created in the diagrams UI, or over API by specifying a list of serial numbers.

    - **Refreshed** -- If the data relating to one or more devices has changed, it is possible to update a snapshot to contain the new inventory, config, and state data from that device by selecting it/them and refreshing the snapshot.

**Model**

: Model can refer to:

    - (n) the database representation of network object inventory, configuration, state, and topology contained within an IP Fabric snapshot

    - (v) the actions involved in the second phase of Snapshot Creation

**Snapshot Creation**

: IP Fabric's uniquely accurate process of discovering and documenting the network's behavior. It has three phases: Discovery, Modelling, and Assurance Engine.

**Discovery**

: The process of crawling through the network -- device by device or using APIs to gather from a controller -- collecting raw configuration and state data, then parsing, normalizing, and structuring the data ready to process. IP Fabric uses internal tasks to gather the appropriate data from different types of devices and then assembles the data ready for use in the second stage.

**Modelling**

: The mechanism of processing the device data from the Discovery phase is to insert them into the database model and to uncover and document groupings, classifications, and relationships between devices.

**Assurance Engine**

: Running the Assurance Engine takes the database data from the model, applies business logic to it to create insight from the data, and prepares enhanced network topology views. Recently, IP Fabric introduced an option to disable elements of this phase to speed up the release of the data to the API. Settings to enable and disable Assurance Engine processes are described in [the Assurance Engine documentation section](../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/assurance_engine.md).

  !!! note

      Disabling these options will affect the UI display of data in IP Fabric -- diagrams, path lookups, changes between snapshots, and/or intent rules may not be displayed as a result.

**Device Authentication**

: The only mandatory configuration setting that IP Fabric needs to begin discovery. The user configures IP Fabric to use one or more sets of credentials, and it will then use them in turn to attempt to log in to devices it discovers, recording the username it successfully uses in its discovery history.

**Seed**

: IP address of a device to be used as a starting point for the discovery process. It may be necessary to have more than one seed to fully discover a segmented network.

  !!! note

      A seed is not necessary for snapshot discovery. If IP Fabric has successfully discovered a snapshot previously, it will use its discovery history to provide seeds for future discovery. If there is no discovery history and no other seeds are provided, IP Fabric will start at its default gateway.

**Crawl**

: The process of logging in to network devices, discovering which devices are connected, then subsequently logging in to those to continue the exploration of the network. This equates to the same process a network engineer would manually attempt to find out how an unfamiliar network was interconnected.

**OUI**

: The fundamental means by which IP Fabric identifies that a node in the network is a supported network device. The first three bytes of an Ethernet MAC address are called the `Organizationally Unique Identifier` and are assigned to a specific vendor of network equipment. Under the Settings menu, IP Fabric contains a list of OUIs as allocated by IEEE and flags the ones used for network discovery.

**Excluded Subnets**

: The network ranges explicitly blacklisted from the discovery process. If a network node is uncovered in an excluded subnet, it will not be accessed but highlighted in the platform as an "unmanaged device".

**Included Subnets**

: The network address ranges explicitly whitelisted in the discovery process. Combined with the excluded subnets, these ranges effectively bound the discovery.

**Scan**

: This is a "brute force" process for finding devices of interest in a network by attempting to connect with every node in a range of IP addresses in turn. Many other tools use this method of discovery, but it is extremely inefficient, often resulting in triggering security alerts in a customer's network monitoring tools. IP Fabric does not use this method by default but if enabled, it uses a smart approach, attempting to connect to the most likely used IP addresses first before filling in the gaps, speeding up the process significantly and reducing the chance of triggering alerts.

**Jumphosts**

: When a group of network devices are not directly accessible from the IP Fabric appliance, the snapshot creation process can use one or more SSH jumphosts to access a range of subnets using SSH tunneling.

**Attributes**

: Additional pieces of custom context data that users can associate with their network devices. They will be used to group and filter data in the platform and provide ways of enhancing existing UI capability with data from outside of the platform. They can be classed as:

    - **Global** -- A settings table for attributes to be deployed to snapshots as they are created.

    - **Local** -- A localized table in each snapshot that contains the attributes mapped to each device in that snapshot when that snapshot was created or last updated.

**Site Separation**

: This is a special use case for IP Fabric attributes -- it is possible to create rules to assign devices with a `siteName` attribute (based, for example, on a regex search of `hostname`). That attribute has a specific use in the platform to provide grouping and filtering of device based on location in tables and diagrams.

## User Interface

**Inventory** and **Technology Tables**

: This area of the product UI presents the raw data relating to the inventory contained within a snapshot, the configuration and behavior of technologies deployed on the nodes in the network model, and the relationships between those devices.

**Intent Rules** (aka **Intent Verification Rules**, **Intent Checks**)

: User-configurable rules to provide a measure of compliance for values in the database with the customer's intent. For example -- NTP is configured with the correct server IP and is reachable; MTU matches at both ends of a link; BGP is established and exchanging prefixes. These rules are displayed above the related table in the UI.

**Dashboard**

: This user-configurable reporting view displays the collection of intent rules, including the RAG representation, radar graphs, bar charts, or graphs representing change over time.

**Device Explorer**

: This UI feature of IP Fabric shows a tabbed view of all the data collected for a given device. Tabs can be added for each deployed technology, and then the filtered data from the master technology table is displayed, along with a link to retrieve the raw data as collected from the device.

**Path Inspector**

: This UI feature of IP Fabric is used to give the details of behavior of individual nodes or edges in the path lookup simulation. It contains headers for the simulated ingress and egress packets and a decision table representing how the node's forwarding and policy behavior.

**Diagram Canvas**

: The scrollable, zoomable UI component on which IP Fabric draws topology and path lookup diagrams. Nodes can be placed according to user preference, and the Visualization Setup allows users to specify which elements are to be seen and how they are represented. Canvas actions include collapsing or hiding certain nodes, additional layout options, saving and loading layouts to be shared with other platform users, refreshing snapshots for selected nodes, exporting output to SVG or PNG, and displaying API information used to generate the output on the canvas.

**Management Tables**

: Management tables present three areas of the product:

    - Device **configuration** collection and diffs between them.

    - **Changes** -- Allowing the user to compare inventory, managed IP addresses, and connectivity matrix between snapshots.

    - **Discovery History** -- Information about devices previously discovered in earlier snapshots.

**Reports**

: The Reports menu houses two sample report types created by the Assurance Engine phase of snapshot creation:

    - **Network Analysis Report** -- A Word document containing all the details from the intent check dashboard.

    - **Site Low Level Design** -- A Word document created for each site in a snapshot containing connectivity matrix, VLANs, IP addressing, diagrams, and so on.
