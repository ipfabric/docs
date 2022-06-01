# Frequently Asked Question - FAQ

## Business Goals

**Q:** What is the IP Fabric platform?

A: IP Fabric is a **network analytics platform** for multi-vendor environments that automates network discovery, network topology diagrams on a protocol level, network security compliance audit and network documentation.  The platform **enables an intent-based approach to network management **and instant application path simulation over large-scale networks.

**Q:** Why should I use the IP Fabric?

A: IP Fabric serves as a **single point of truth** for all network inventory and protocol data or provide up-to-date network topology diagrams. It speeds up the **troubleshooting** and **root-cause analysis** processes with simple network search and end-to-end application path testing.

Apart from significant benefits to network administrators, it elevates collaboration with other teams and systems via its standard interfaces and helps to automate network provisioning and the **detection of inconsistent protocol states**, network loops **or security issues** based on user-defined rules.

**Q:** Is the IP Fabric a monitoring solution?

A: The IP Fabric platform collects data from the network on a regular basis to provide in-depth analytics. The output of the data collection is a digital snapshot of the entire network at the time of discovery. But IP Fabric does not monitor the network in real-time.

**Q:** Why to use the analytical platform, isn't my monitoring suite enough?

A: Monitoring tools are still crucial to your network operations processes; raised alerts and alarms will let engineers know there is something to be assessed or investigated.

Analytics of the network will give you the ability to compare past states of the network, compare changes, analyze full route-cause of issues to prevent future repeats of the same issues and improve efficiency of troubleshooting processes through an automated tool-set.

## Installation

**Q:** What is needed for IP Fabric deployment?

A: IP Fabric currently operates **as a standalone virtual server** available for VMware 5.0 and later or Hyper-V hypervisors. (Other hypervisors may be available in the future.) It can be easily deployed with the OVA image provided by IP Fabric.

**Q:** Is the IP Fabric cloud based or on-premise solution?

A: IP Fabric is **in most cases deployed as an on-premise solution**. It doesn’t require any Internet connectivity to operate or verify the license or run discovery. Alternatively, it can be deployed in the cloud and discover networks via private tunnels.

**Q:** Do I need to install any additional virtual machines?

A: No additional supporting servers or licenses are needed for successful deployment.

**Q:** Do I need a hardware appliance to install IP Fabric?

A: IP Fabric is a virtual appliance that runs on VMware 6.5 or later. It doesn’t need a standalone hardware appliance by design.

**Q:** How's the product licensed?

A: The product is licensed on a subscription basis (including support).  The only factor we account for in the license price is the number of active network devices (switches, routers, firewalls, load balancers, wireless controllers) in the target network. Wireless Access-Points are not included in the license.

## Operation & Maintenance

**Q:** How many engineers should I allocate to test your solution?

A: One engineer is enough to handle the task of deployment and testing.

**Q:** How should I prepare my network for successful discovery?

A: IP Fabric collects data via Command-Line Interface (CLI) with SSH/Telnet directly from each network device individually. The best location for virtual machine installation is in the management part of the network with enabled security path over SSH/Telnet protocol from the server’s IP address as a source IP for all session requests. Access-Lists, Firewall filters or related Security policies should be adjusted to enable the connection.

**Q:** What is the impact on the network during discovery?

A: The overall impact is **very low on network resources**. IP Fabric is reading all data from a device with a single SSH session in a similar way as the administrator, only faster.

It is very common for IP Fabric to run discovery during business hours when little to no irregularities were observed in monitoring.

**Q:** How does the platform collect data from network?

A: IP Fabric collects data only **via Command-Line Interface (CLI)** with set of known operational commands on supported network devices. Read-only access is sufficient for discovery.

**Q:** Are you providing real-time information?

A: The platform itself provides all analytics information based on regular network scans (the snapshots). It is not a real-time monitoring solution but an analytical tool.

**Q:** What kind of data are you able to collect?

A: The platform collects variety of data specific to each network device. Starting with basic inventory and protocol states, detailed protocol tables or links. To provide full transparency, all operational commands used for each vendor/platform are well documented.

**Q:** Does the IP Fabric platform use SNMP to collect data?

A: No, IP Fabric doesn’t collect any SNMP data from active network devices.  Our CLI–based approach achieves a greater level of detail compared to SNMP.

**Q:** What is needed for starting the very first network discovery?

A: For the very first network discovery, IP Fabric needs to be deployed with the OVA image (provided by us on request). Then the platform needs to have **correct credentials to access active network devices** via SSH/Telnet. The security perimeter needs to **enable communication from the IP Fabric platform to network devices** for mentioned CLI protocols. And optionally, you can provide a single IP address as a starting point for discovery.

**Q:** What types of network devices can IP Fabric discover?

A: IP Fabric can discover **all supported IP based active network devices**, in general it’s switches, routers, firewalls, load-balancers, wan concentrators, wireless controllers, wireless access-points.

## Supported manufacturers

**Q:** What network vendors are currently supported?

A: IP Fabric is a powerful tool for multi-vendor, large-scale networks. The network vendor list is ever-expanding with new items added each release. Complete support matrix can be found [in our Support Matrix](https://matrix.ipfabric.io).

**Q:** What if I have unsupported vendor in my network?

A: If there is a vendor in your network that is currently not included in the supported matrix, it won’t be discovered and will be listed as unmanaged neighbor in the platform. We are implementing new vendors with almost every release, so feel free to ask your IP Fabric sales or technical representative about the road-map priorities for the next phase. Support for the vendor in question may have already been road-mapped.

## Data at Rest Encryption

**Q:** Is IP Fabric's VM encrypted?

A:No, it isn't. It would add unnecessary level of complexity for both IP Fabric engineers and the client. Encryption key provisioning would need to be solved in case that filesystem or underlying block device is encrypted. This would require either passphrase prompt on every boot or integration into secret store on the deployment infrastructure side. We recommend the client handles encryption on storage level (e.g. VMware Datastore).

**Q:** Is IP Fabric storing everything as a plain text?

A:No, it isn't. Passwords at rest in the database and techsupports are encrypted to ensure safety of the customer's private data.
