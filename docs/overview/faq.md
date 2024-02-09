---
description: We have a selection of the most frequently asked questions that you can check out here!
---

# Frequently Asked Questions -- FAQ

## Business Goals

**Q:** What is the IP Fabric platform?

A: IP Fabric is a **network analytics platform** for multi-vendor environments that automates network discovery, network topology diagrams at a protocol level, network security compliance audit, and network documentation. The platform **enables an intent-based approach to network management** and instant application path simulation over large-scale networks.

**Q:** Why should we use IP Fabric?

A: IP Fabric serves as a **single point of truth** for all network inventory and protocol data and provides up-to-date network topology diagrams. It speeds up **troubleshooting** and **root-cause analysis** processes with simple network search and end-to-end application path testing.

Apart from significant benefits to network administrators, it enhances collaboration with other teams and systems via its standard interfaces and helps automate network provisioning and the **detection of inconsistent protocol states**, network loops **or security issues** based on user-defined rules.

**Q:** Is IP Fabric a monitoring solution?

A: The IP Fabric platform collects data from the network regularly to provide in-depth analytics. The output of the data collection is a digital snapshot of the entire network at the time of discovery. However, IP Fabric does not monitor the network in real-time.

**Q:** Why use an analytical platform, isn't our monitoring suite enough?

A: Monitoring tools are still crucial to your network operations processes; raised alerts and alarms will notify engineers when there is something to be assessed or investigated.

Network analytics will give you the ability to compare past states of the network, compare changes, analyze the full route cause of issues to prevent future repeats of the same issues, and improve efficiency of troubleshooting processes through an automated toolset.

## Installation

**Q:** What is needed for IP Fabric deployment?

A: IP Fabric must be deployed to a dedicated virtual machine. See [Operational Requirements](index.md#operational-requirements).

**Q:** Is IP Fabric a cloud-based or on-premises solution?

A: IP Fabric is, **in most cases, deployed as an on-premises solution**. It does not require any Internet connectivity to operate or verify the license or run discovery. Alternatively, it can be deployed in the cloud and discover networks via private tunnels.

**Q:** Do we need to install any additional virtual machines?

A: No additional supporting servers or licenses are needed for successful deployment.

**Q:** Do we need a hardware appliance to install IP Fabric?

A: IP Fabric is a virtual appliance that runs on various virtualization platforms. It does not need a standalone hardware appliance by design. See [Operational Requirements](index.md#operational-requirements) for more details.

**Q:** How is the product licensed?

A: The product is licensed on a subscription basis (including support). The only factor we account for in the license price is the number of active network devices (switches, routers, firewalls, load balancers, wireless controllers) in the target network. Wireless Access-Points are not included in the license.

## Operation & Maintenance

**Q:** How many engineers should we allocate to test your solution?

A: One engineer is enough to handle the task of deployment and testing.

**Q:** How should we prepare our network for successful discovery?

A: IP Fabric collects data via Command-Line Interface (CLI) with SSH/Telnet directly from each network device individually. The best location for virtual machine installation is in the management part of the network with enabled security path over the SSH/Telnet protocol from the server's IP address as a source IP for all session requests. Access-Lists, Firewall filters or related Security policies should be adjusted to enable the connection.

**Q:** What is the impact on the network during discovery?

A: The overall impact is **very low on network resources**. IP Fabric reads all data from a device with a single SSH session in a similar way as the administrator, only faster.

It is very common for IP Fabric to run discovery during business hours when little to no irregularities are observed in monitoring.

**Q:** How does the platform collect data from the network?

A: IP Fabric collects data only **via Command-Line Interface (CLI)** with a set of known operational commands on supported network devices. Read-only access is sufficient for discovery. Additionally, the platform uses APIs to communicate with vendor controllers (Versa, Viptela) or cloud vendors (AWS, Azure, NSX-T).

**Q:** Are you providing real-time information?

A: The platform itself provides all analytics information based on regular network scans (the snapshots). It is not a real-time monitoring solution but an analytical tool.

**Q:** What kind of data are you able to collect?

A: The platform collects a variety of data specific to each network device, starting with basic inventory, protocol states, detailed protocol tables or links. To provide full transparency, all operational commands used for each vendor/platform are [well documented](https://matrix.ipfabric.io).

**Q:** Does the IP Fabric platform use SNMP to collect data?

A: No, IP Fabric doesn’t collect any SNMP data from active network devices. Our CLI-based approach achieves a greater level of detail compared to SNMP.

**Q:** What is needed to start the very first network discovery?

A: For the very first network discovery, IP Fabric needs to be deployed with the OVA image (provided by us upon request). Then, the platform needs to have **correct credentials to access active network devices** via SSH/Telnet. The security perimeter needs to **enable communication from the IP Fabric platform to network devices** for the mentioned CLI protocols. Optionally, you can provide a single IP address as a starting point for discovery.

**Q:** What types of network devices can IP Fabric discover?

A: IP Fabric can discover **all supported IP-based active network devices**. In general, these are switches, routers, firewalls, load-balancers, WAN concentrators, wireless controllers, and wireless access-points.

## Supported Manufacturers

**Q:** What network vendors are currently supported?

A: IP Fabric is a powerful tool for multi-vendor, large-scale networks. The network vendor list is ever-expanding with new items added each release and can be found at [matrix.ipfabric.io](https://matrix.ipfabric.io).

**Q:** What if we have an unsupported vendor in our network?

A: If there is a vendor in your network that is currently not included in the supported matrix, it won't be discovered and will be listed as an unmanaged neighbor in the platform. We are implementing new vendors with almost every release, so feel free to ask your IP Fabric sales or technical representative about the roadmap priorities for the next phase. Support for the vendor in question may have already been road-mapped.

## Data at Rest Encryption

**Q:** Is IP Fabric's VM encrypted?

A: No, it isn't. It would add an unnecessary level of complexity for both IP Fabric engineers and customers. Encryption key provisioning would need to be solved in case the filesystem or underlying block device is encrypted. This would require either a passphrase prompt on every boot or integration into secret store on the deployment infrastructure side. We recommend to customers to handle encryption at the storage level (e.g., VMware Datastore).

**Q:** Is IP Fabric storing everything as plain text?

A: No, it isn't. Passwords at rest in the database and techsupports are encrypted to ensure the safety of customers' private data.
