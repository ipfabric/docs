---
description: This will guide you through installing IP Fabric in your environment.
---

# Quick Start Installation Guide

## Operational Requirements

Please reference [Operational Requirements](../overview/index.md#operational-requirements) for important requirements pertaining to:

1. [Hardware Requirements](../overview/index.md#hardware-requirements)
2. [Network Connectivity Requirements](../overview/index.md#network-connectivity-requirements)
3. [Network Access Credentials Requirements](../overview/index.md#network-access-credentials-requirements)

## Images

IP Fabric Images can be found on our [Releases Page](https://releases.ipfabric.io/ipfabric/current/).
Access is restricted to registered customers only.

!!! note "Image Access"

    If you are a current customer please contact your Solution Architect
    or [Support](../support/index.md) for access instructions.

    Please contact our [sales representative](mailto:sales@ipfabric.io)
    if you are interested in a trial of IP Fabric.

We provide two different images listed below along with links to installation
instructions.

1. OVA can deployed on:
   1. [Deploying VMware](01-deployment.md#deploying-on-vmware-ova-virtual-machine)
   2. [Deploying Nutanix](01-deployment.md#deploying-a-virtual-machine-to-nutanix)
   3. [Deploying VirtualBox](01-deployment.md#deploying-a-virtual-machine-on-virtualbox)
2. QCOW2 can be deployed on:
   1. [Deploying Hyper-V](01-deployment.md#deploying-on-hyper-v-virtual-machine)
   2. [Deploying KVM](01-deployment.md#deploying-a-virtual-machine-on-kvm)

!!! important "Hardware Requirements"

    Please ensure after deploying the VM you verify it has been configured
    correctly per the [Hardware Requirements](../overview/index.md#hardware-requirements).
    Importing the OVA will use the base requirements of 4 CPU, 16GB RAM,
    and 90GB HDD.

## First Time Boot Wizard

The Boot Wizard needs to be completed during the IP Fabric virtual machine's
initial deployment. The Boot Wizard introduces the configuration of basic
network parameters, including time zone, NTP, IP address, DNS or Proxy settings.

Follow instructions at [CLI Boot Wizard](02-boot_wizard.md)

## Accessing User Interface

Prior to accessing the main IP Fabric UI, you will need to create an `admin`
account in the System Administration
page: [Creating The First IP Fabric User](03-access_ui.md#accessing-the-main-user-interface)

## Applying IP Fabric License

In order to access the main IP Fabric user interface, a license must be uploaded
to IP Fabric. Please contact your salesperson for the license key and follow the
instructions
at [Accessing The Main User Interface](03-access_ui.md#accessing-the-main-user-interface)

!!! important "Licensing"

    A valid license must be applied to continue in this Quick Start Guide.

## Configuration

The simplest way for first time configuration of IP Fabric is through the use of
the [Configuration Wizard](04-configuration_wizard.md) which will guide you
through the process of adding device credentials, discovery seeds, networks
to include/exclude in discovery and Advanced CLI settings.

If you would like to change these settings after initial configuration,
please see [IP Fabric Settings](../settings/configuration_management.md). Alternatively, there
are also
[snapshot-specific settings](../gui/discovery_snapshot.md#snapshot-specific-settings)
which are useful for testing small changes prior to changing Global Settings.

!!! note "Site Separation"

    After completing the steps in the **Configuration Wizard**, you may also set
    **Site Separation** rules (in **Settings --> Discovery & Snapshots -->
    Discovery Settings --> Site Separation**). This can be done before, or after
    the first discovery. Some customers find it easier to set that up after a
    discovery -- as it will be possible to check to which Site an already
    discovered device would belong to using the "regex tester" on the **Site
    Separation** page.

    Please see documentation located at [Site Separation](../settings/Discovery_and_Snapshots/Discovery_Settings/site_separation.md).

## Discovery

If you followed the **Configuration Wizard**, the last step will ask you to
**Start Discovery**. You can also start discoveries by using the
[Discovery Snapshot](../gui/discovery_snapshot.md) menu. This is
where the magic of IP Fabric happens where it will go out to your devices, find
neighbors, and collect information.

Here are some great resources for explaining the Discovery process:

- [How CLI Discovery Works](../overview/How_Discovery_Works/CLI_discovery.md)
- [How API Discovery Works](../overview/How_Discovery_Works/API_discovery.md)

## Troubleshooting Discovery

Finally, please read through the
[Troubleshooting Discovery](../overview/How_Discovery_Works/troubleshooting_discovery.md)
page that will guide you through the most common issues seen during the initial
discovery process. It explains how discovery works, how to view logs, and which
settings to change to include (or exclude) devices among other useful tips.

If you are working with a Solution Architect in a Proof of Concept deployment
they will also work with you in troubleshooting any issues that may arise.