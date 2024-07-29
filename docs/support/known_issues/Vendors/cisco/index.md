---
description: This page describes known issues with Cisco and how to fix them.
---

# Overview

**Affected platforms:** 15.1(4)M4, 15.1(4)M4.7, 15.1(4)M5, 12.2(50)SE3, 6.0(2)N2(3), 15.5(3.0l)M

**Description:** The `show transceivers` command can cause fatal issues on some Cisco platforms, including device crashes. It takes several minutes to finish the command on some platforms.

**Result:** Affected platforms are removed from collection, and the `Transceivers task` is disabled by default in IP Fabric. Before enabling it, ensure that your devices are not affected. If they are, remove them from the task settings.

**Resources:**

- [CSCua29548](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCua29548)
- [CSCtg41473](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCtg41473)
- [CSCuq13396](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuq13396)
- [CSCva00194](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCva00194)

---

**Affected platforms:** all IOS-family switches

**Description:** The `show spanning-tree mst` command requires an enable password. It is currently not supported for the IOS family (only SG and ASA).

**Result:** MST is not collected, leading to false positives in the STP inconsistency check.

**Workaround:** Use privilege 15 authorization on login or `show spanning-tree mst` command authorization.

---

**Affected platforms:** SG family, sf302-08pp-k9 platform

**Description:**  The `sh spa d` command returns misformatted output (forgetting newline characters and repeating the output with an offset).

**Result:** STP detail is not collected.

---

**Affected platforms:** Cisco ASA

**Description:** Some Cisco ASA and Firepower hardware platforms can run either Cisco ASA software or Firepower Threat Defense software. Depending on the software in use, these devices are detected either as Cisco ASA or Cisco FTD. For example, Cisco Firepower 2100 can be detected as `asa` when running ASA software or as `ftd` when running FTD software.

---

**Affected platforms:** Cisco Nexus 5000, 6000, and 9000

**Description:** Several Cisco Nexus platforms allow setting MTU on a per-service basis. The interface MTU shown in the IP Fabric GUI is only interface-specific (e.g., inventory/interfaces table). Therefore, the interface MTU value for Nexus 5k/6k/9k can only be displayed if the network-qos system policy defines the same MTU for all services or when no network-qos system policy is active. The `show policy-map system type network-qos` command is used to determine the network-qos system policy.
The MTU value displayed in the `show interface` command is assumed to be the default value. Note: class-fcoe is not considered when comparing different services' MTUs.

**Resource:** [CSCsl21529](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCsl21529)

---

**Affected platforms:** ASA- and FTD-family firewalls

**Description:** Currently, interface security levels are not supported.

**Result:** End-to-end path security policy check is only based on ACLs.

---

**Affected platforms:** ASA- and FTD-family firewalls

**Description:** VLAN ID detection for interfaces -- If the `show interface detail` command doesn't provide the VLAN ID, but the interface name suggests VLAN presence (e.g., interface names like vlan100 or sub-interfaces like Gi0/1.100 or Po1.100, etc.), this VLAN will be used.

**Result:** In rare cases, the VLAN ID for an interface might not be determined correctly.

---

**Affected platforms:** FTD-family firewalls

**Description:** When using FTD, if you run the `show ntp` command, a password prompt will appear in the command line. This will break the discovery of FTD.

**Result:** The NTP discovery task is disabled by default for FTD. If your FTD is not affected by this bug, you can safely enable it.

**Resource:** [CSCvt01938](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt01938)
