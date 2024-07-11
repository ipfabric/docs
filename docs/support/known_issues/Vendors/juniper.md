---
description: This page describes known issues with Juniper and how to fix them.
---

# Juniper

- Route leaks defined by reference to another VRF are not supported, but route
  leaks with policy are supported.

- Juniper devices cannot be discovered using a root account, as such an account
  does not go straight to the CLI prompt. Please use a non-root account instead.

---

**Known affected platforms:** Juniper SRX300

**Description:** The `show ethernet-switching interface detail` command can
cause an infinite loop output.

**Result:**

Version `3.1.1` and earlier:

- Endless command execution can cause device control plane overutilization
  issues that might also affect other control plane protocol operations (e.g.,
  BFD). Furthermore, it increases the time of IP Fabric device/network discovery
  and can result in not discovering the device and gathering information from
  it.
- We recommend removing such devices from the scope of IP Fabric discovery
  (placing these devices on the discovery exclude list).

Version `3.1.2` and above:

- The `show ethernet-switching interfaces detail` command is no longer used and
  has been replaced by other commands, including `show ethernet-switching
  interfaces`. Furthermore, the `show ethernet-switching interfaces` command is
  only executed on devices discovered as EX or QFX switches.

---

**Known affected platforms:** SRX, MX

**Description:** The `show ntp associations no-resolve` command times out.

**Result:** <https://kb.juniper.net/InfoCenter/index?page=content&id=KB11436>

---

**Known affected platforms:** all

**Description:** The Link-Layer Discovery Protocol (LLDP) links are not
displayed in diagrams.

**Result:** To display LLDP links in diagrams correctly, the IP address of the
neighbor must be present in the `show lldp neighbor interface xx-x/x/x` command.
The IP address is only present when configured with the `set lldp
management-address xx.xx.xx.xx` command in configuration mode. More details can
be found at
<https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/management-address-edit-protocols-lldp.html>.

---

**Known affected platforms:** all

**Description:** Information gathered from running-config doesn't reflect
apply-groups.

**Result:** Some information gathered from running-config might be missing.
Since version `6.3`, tasks such as Zone Firewall, NAT44, and ACL aren't
affected; however, other tasks like SNMP and Syslog are still affected. More
information can be found at
<https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/apply-groups.html>.

---

**Known affected platforms:** all

**Description:** The `fw ctl pstat` command requires admin rights.

**Result:** Without the output from this command, no memory utilization data
will be available.

---

**Known affected platforms:** all

**Description:** The routing table doesn't reflect ECMP settings. Information is gathered with the `show route active-path` command. The actual forwarding table
can contain fewer next hops.

**Result:** The end-to-end path can show more paths when ECMP is disabled. For
additional information, check
<https://serverfault.com/questions/209657/ecmp-load-balancing-in-junos>.

---

# Discovery of Security Policies

- Wildcard & Dynamic objects and negated services are not supported.

- **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors API**
  in the IP Fabric GUI: If the base URL points to a multi-domain server address,
  domains must be specified.
