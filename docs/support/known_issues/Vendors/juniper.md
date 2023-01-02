---
description: IP Fabric describes known affected issues for Juniper and how to fix them.
---

# Juniper

- Route leak defined by reference to another VRF is not supported.
  Route leak with the policy is supported.

---

**_Known Affected platforms_**: Juniper SRX300

**_Description_**: `show ethernet-switching interface detail` can cause
infinite loop output

**_Result_**:

Version 3.1.1 and earlier.

- Endless command execution can cause device control plane
  overutilization issues that might also affect other control plane
  protocol operations (e.g. BFD). Further, it increases the time of
  IPF device/network discovery and can result in not discovering the
  device and gathering information from it.
- We recommend removing such devices from the scope of IPF discovery
  (putting these devices to discovery exclude list).

Version 3.1.2 and above

- Command `show ethernet-switching interfaces detail` is no longer
  used and was substituted by other commands including `show ethernet-switching interfaces`. Further `show ethernet-switching interfaces` command is only executed on devices discovered as EX or
  QFX switches.

---

**_Known Affected platforms_**: SRX, MX

**_Description_**: `show ntp associations no-resolve` command timeouts

**_Result_**: <https://kb.juniper.net/InfoCenter/index?page=content&id=KB11436>

---

**_Known Affected platforms_**: ALL - valid for version 3.1.1 and
earlier

**_Description_**: The platform doesn't discover Juniper devices with the
`root` login. The `root` enters the shell prompt (`%`) and not the
operational mode directly.

**_Result_**:

Version 3.1.1 and earlier - the `root` login cannot be used for
discovery.

Version 3.1.2 and above - the `root` login may be used for discovery.

---

**_Known Affected platforms_**: ALL

**_Description_**: The Link-Layer Discovery Protocol (LLDP) links are not
displayed in diagrams.

**_Result_**: To display LLDP links in diagrams correctly, the IP address
of the neighbor has to be present in `show lldp neighbor interface xx-x/x/x` command. The IP address is present only when configured with
the `set lldp management-address xx.xx.xx.xx` command in the
configuration mode. More
at: <https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/management-address-edit-protocols-lldp.html>.

---

**_Known Affected platforms_**: ALL

**_Description_**: Information gathered from running-config doesn't
reflect apply-groups.

**_Result_**: Some information gathered from running-config can be
missing. It affect all tasks using running config - for example firewall
filters, snmp, syslog.  
More
at: <https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/apply-groups.html>

---

**_Known Affected platforms_**: All

**_Description_**: `fw ctl pstat` command requires admin rights

**_Result_**: Without this command collected no memory utilization will be
present

---

**_Known Affected platforms_**: ALL

**_Description_**: Routing table doesn't reflect ECMP settings. Information is gathered with `show route active-path`. Actual forwarding table can contain less next hops.

**_Result_**: E2E path can show more paths when ECMP is disabled.

Check <https://serverfault.com/questions/209657/ecmp-load-balancing-in-junos> for additional information.

---

# Discovery of Security Policies

- Wildcard & Dynamic objects and negated services are not supported
- Settings > Advanced > Vendor API: In case that base URL points to a
  multi-domain server address, domains have to be specified
