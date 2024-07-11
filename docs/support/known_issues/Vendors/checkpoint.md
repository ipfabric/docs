---
description: This page describes known issues with Check Point and how to fix them.
---

# Check Point

## `fw ctl pstat` Command Requires Admin Rights

**Known affected platforms:** all

**Result:** Without the output from this command, no memory utilization data
will be available.

## ARP Table Contains Only Master `VSYS 0` Entries

**Known affected software versions:** `R80.30` and `R80.40`

**Result:** The `show arp dynamic all` command on VSx mistakenly shows ARP
entries only for the `master VSYS 0`, regardless of the active `VSYS`. This is a confirmed bug on Check Point firewalls.

## Discovery of Security Policies

- Dynamic objects and negated services are not supported.

- **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors API**
  in the IP Fabric GUI: If the base URL points to a multi-domain server address,
  the domains must be specified.

## Identity Awareness support

Starting with version `6.5`, IP Fabric supports collecting data from the `pdpd`
daemon. Since the `pdp` command isn't available by default in CLISH, an extended
command must be defined first (on appliances where the PDP daemon is running).

The extended command can be defined from CLISH, but the path depends on the OS
version currently installed. For example, if the OS version is `R80.40`, the
command would be:

```commandline
> add command ipf_pdp path /opt/CPsuite-R80.40/fw1/bin/pdp description "PDP for IP Fabric"
> save config
```

Alternatively, you can define the extended command from expert mode by using the environment variable `$FWDIR`. The `-s` option saves the configuration:

```commandline
# clish -s -c "add command ipf_pdp path $FWDIR/bin/pdp description \"PDP for IP Fabric\""
```

Don't forget to update the related role and add the `ipf_pdp` extended command
to it if needed. See the
[official Check Point documentation](https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_ScalablePlatforms_Gaia_AdminGuide/Topics-SP-Gaia/User-Defined-Extended-Commands.htm?tocpath=Introduction%20to%20the%20Command%20Line%20Interface%7C_____8).

IP Fabric uses the `ipf_pdp monitor all` command to collect information about
active users. Log in to the Check Point Gaia appliance with the credentials used
by IP Fabric discovery and run the command to verify the configuration.

## Required Permissions for Successful Discovery Over CLI

To successfully discover a Check Point Gateway, the correct role must be
assigned to the user. IP Fabric requires role features to be set as read-only,
except for "Virtual-System", where read-write is needed (only if VSX firewalls
are in your network; otherwise, read-only is sufficient).

![Check Point - Edit Role - ipfRole](checkpoint/checkpoint_role.png)

### How To Setup Role From Web GUI

1. Open the Check Point Gaia web interface.

2. In the left menu, navigate to **User Management --> Roles**.

3. Click **Add** and fill in the name. In the **Features** tab, select all items
   and mark them as **Read-Only**. The following permissions from the **Extended
   Commands** tab are needed (only if Gaia acts as a management server): `fwm`
   and `ipf_pdp`.

4. If you have a VSX firewall in your network, you must set the
   **Virtual-System** feature to **Read-Write** (we call `set virtual-system
   \<ID>` to switch to the proper virtual system). This allows IP Fabric to
   change context but cannot be used for anything else.

5. Assign the role to the user used for IP Fabric discovery.

!!! info

    Not all features are needed for IP Fabric, but as we add support for new
    features, this may change. Here is a list of currently required features for
    a minimal working setup (IP Fabric `4.0`, Gaia `R81`):

    > Advanced VRRP, ARP, BGP, Cluster, Display Configuration, Domain Name, Host Name, Management Interface, Netflow Export, Network Interfaces, Network Management, NTP, OSPF, Route, Routing Monitor, SNMP, System Configuration, Virtual-System, VRRP, VSX.
