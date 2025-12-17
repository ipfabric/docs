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

Starting with version `7.0`, we are using the `pepd` daemon to collect
additional information.

The extended command can be defined from CLISH, but the path depends on the OS
version currently installed. For example, if the OS version is `R80.40`, the
command would be:

```commandline
> add command ipf_pdp path /opt/CPsuite-R80.40/fw1/bin/pdp description "PDP for IP Fabric"
> add command ipf_pep path /opt/CPsuite-R80.40/fw1/bin/pep description "PEP for IP Fabric"
> save config
```

Alternatively, you can define the extended command from expert mode by using the environment variable `$FWDIR`. The `-s` option saves the configuration:

```commandline
# clish -s -c "add command ipf_pdp path $FWDIR/bin/pdp description \"PDP for IP Fabric\""
# clish -s -c "add command pep path $FWDIR/bin/pep description \"PEP for IP Fabric\""
```

Don't forget to update the related role and add the `ipf_pdp` and `ipf_pep`
extended commands to it if needed. See the
[official Check Point documentation](https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_ScalablePlatforms_Gaia_AdminGuide/Topics-SP-Gaia/User-Defined-Extended-Commands.htm?tocpath=Introduction%20to%20the%20Command%20Line%20Interface%7C_____8).

IP Fabric uses the `ipf_pdp monitor all` and `ipf_pep show user all` commands to
collect information about active users. Log in to the Check Point Gaia appliance
with the credentials used by IP Fabric discovery and run the command to verify
the configuration.

## Extend command to get better NTP results

On Check Point Gaia, IP Fabric uses the CLISH command `show ntp servers` to collect data about NTP sources. Unfortunately, this command doesn’t provide enough detail to populate the API and the related Technology table.

To obtain detailed information about NTP sources (for example, stratum, reference ID, or timers), IP Fabric can execute the `ntpq` command, which is available only in Expert mode. Instead of accessing Expert mode directly, IP Fabric supports extended commands.

To make `ntpq` available from CLISH, the command must be extended (either from CLISH or directly from Expert mode).

From the CLISH:

```commandline
> add command ntpq path /sbin/ntpq description "ntpq for IP Fabric"
> save config
```

If you prefer extending from the Expert mode, run the following command:

```
# clish -s -c "add command ntpq path /sbin/ntpq description \"ntpq for IP Fabric\""
```

!!! info

    Verify the `ntpq` command path. It might differ depending on the Gaia OS version.

    Both commands above can be also extended as `ipf_ntpq`. IP Fabric will try both.

    Don’t forget to adjust permissions for the role assigned to the SSH user. See the instructions below.

## Required Permissions for Successful Discovery Over CLI

To successfully discover a Check Point Gateway, the correct role must be
assigned to the user. IP Fabric requires role features to be set as read-only,
except for "Virtual-System", where read-write is needed (only if VSx firewalls
are in your network; otherwise, read-only is sufficient).

![Check Point - Edit Role - ipfRole](../../../images/support/support-known_issues-Vendors-checkpoint_checkpoint_role.webp)

Running some commands requires elevated permissions. See the example below:

```commandline
gaia> show cluster state

/tmp/.CPprofile.sh: line 1: /opt/CPshrd-R81.10/scripts/cpprofile_functions.sh: Permission denied
```

The `show cluster *` commands call the `cphaprob` utility, which has the
following permissions and ownership:

```
[Expert@gaia:0]# ls -al `which cphaprob`
-rwxr-x--- 1 admin bin 303196 Jan 27  2020 /opt/CPsuite-R81.10/fw1/bin/cphaprob
```

So ensure that the user used for IP Fabric discovery has sufficient permissions
configured -- the user should be in the group `bin` (recommended) or be `admin`
(have UID 0; less recommended).

### How To Setup Role From Web GUI

1. Open the Check Point Gaia web interface.

2. In the left menu, navigate to **User Management --> Roles**.

3. Click **Add** and fill in the name. In the **Features** tab, select all items
   and mark them as **Read-Only**. The following permissions from the **Extended
   Commands** tab are needed (only if Gaia acts as a management server): `fwm`,
   `ipf_pdp`, `ipf_pep` and `ntpq` (alternatively `ipf_ntpq`) for all Gaia appliances.

4. If you have a VSx firewall in your network, you must set the
   **Virtual-System** feature to **Read-Write** (we call `set virtual-system
\<ID>` to switch to the proper virtual system). This allows IP Fabric to
   change context but cannot be used for anything else.

5. Assign the role to the user used for IP Fabric discovery.

!!! info

    Not all features are needed for IP Fabric, but as we add support for new
    features, this may change. Here is a list of currently required features for
    a minimal working setup (IP Fabric `4.0`, Gaia `R81`):

    > Advanced VRRP, ARP, BGP, Cluster, Display Configuration, Domain Name, Host Name, Management Interface, Netflow Export, Network Interfaces, Network Management, NTP, OSPF, Route, Routing Monitor, SNMP, System Configuration, Virtual-System, VRRP, VSx.
