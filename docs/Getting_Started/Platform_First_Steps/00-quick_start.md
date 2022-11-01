---
description: This will guide you through installing IP Fabric in your environment
---

# Quick Start Installation Guide

## Operational Requirements

Please reference [Operational Requirements](../Overview/index.md#operational-requirements) for important requirements pertaining to:

1. [Hardware Requirements](../Overview/index.md#hardware-requirements)
2. [Network Connectivity Requirements](../Overview/index.md#network-connectivity-requirements)
3. [Network Access Credentials Requirements](../Overview/index.md#network-access-credentials-requirements)

## Images

IP Fabric Images can be found on our [Releases Page](https://releases.ipfabric.io/ipfabric/current/).
Access is restricted to registered customers only.

!!! note "Image Access"

    If you are a current customer please contact your Solution Architect
    or [Support](../../support/index.md) for access instructions.

    Please contact our [sales representative](mailto:sales@ipfabric.io)
    if you are interested in a trial of IP Fabric.

We provide two different images listed below along with links to installation
instructions.

1. OVA can deployed on:
   1. [Deploying VMware](01-deployment.md#deploying-on-vmware-ova-virtual-machine)
   2. [Deploying Nutanix](01-deployment.md#deploying-a-virtual-machine-to-nutanix)
2. QCOW2 can be deployed on:
   1. [Deploying Hyper-V](01-deployment.md#deploying-on-hyper-v-virtual-machine)
   2. [Deploying KVM](01-deployment.md#deploying-a-virtual-machine-on-kvm)

!!! important "Hardware Requirements"

    Please ensure after deploying the VM you verify it has been configured
    correctly per the [Hardware Requirements](../Overview/index.md#hardware-requirements).
    Importing the OVA will use the base requirements of 4 CPU, 16GB RAM,
    and 90GB HDD.

## First Time Boot Wizard

The Boot Wizard needs to be completed during the IP Fabric virtual server
initial deployment. The Boot Wizard introduces the configuration of basic
network parameters, including time zone, NTP, IP address, DNS or Proxy settings.

Follow instructions at [CLI Boot Wizard](02-boot_wizard.md)

## Accessing User Interface

Prior to accessing the main IP Fabric UI you will need to create an `admin`
account in the System Administration
page: [Creating The First IP Fabric User](03-access_ui.md#accessing-the-main-user-interface)

## Applying IP Fabric License

In order to access the Main IP Fabric User Interface a License must be uploaded
to IP Fabric. Please contact your salesperson for the license key and follow
instructions
at [Accessing The Main User Interface](03-access_ui.md#accessing-the-main-user-interface)

!!! important "Licensing"

    A valid license must be applied to continue in this Quick Start Guide.

## Configuration

The simplest way for first time configuration of IP Fabric is through the use of
the [Configuration Wizard](Configuration_Wizard/index.md) which will guide you
through the process of adding device authentication, discovery seeds, networks
to include/exclude in discovery, Vendor API setup, along with other settings.

If after initial configuration you would like to change or edit these settings
please see [IP Fabric Settings](../../IP_Fabric_Settings/api_tokens.md). Alternatively there
are also
[Snapshot Specific Settings](../../IP_Fabric_GUI/Discovery_Snapshot.md#snapshot-specific-settings)
which are useful for testing small changes prior to changing Global Settings.

!!! note "Site Separation"

    During the Configuration Wizard it will also ask you to set up Site
    Separation rules. This can be done during the setup or alternatively after
    the first discovery. Some customers find it easier after a discovery
    and using the "regex tester" that will show you to which site a
    device would belong to.

    Please see documentation located at [Site Separation](../../IP_Fabric_Settings/site_separation.md).

## Discovery

If you followed the Configuration Wizard the last step will ask you to
"Start Discovery". You can also start discoveries by using the
[Discovery Snapshot](../../IP_Fabric_GUI/Discovery_Snapshot.md) menu. This is
where the magic of IP Fabric happens where it will go out to your devices, find
neighbors, and collect information.

Here are some great resources for explaining the Discovery process:

- [How CLI Discovery Works](../Overview/How_Discovery_Works/CLI_discovery.md)
- [How API Discovery Works](../Overview/How_Discovery_Works/API_discovery.md)

## Troubleshooting Discovery

Finally, please read through the
[Troubleshooting Discovery](../Overview/How_Discovery_Works/troubleshooting_discovery.md)
page that will guide you through the most common issues seen during the initial
discovery process. It explains how discovery works, how to view logs, and which
settings to change to include (or exclude) devices among other useful tips.

If you are working with a Solution Architect in a Proof of Concept deployment
they will also work with you in troubleshooting any issues that may arise.
