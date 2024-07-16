---
description: This page will guide you through installing IP Fabric in your environment.
---

# Quick Start Installation Guide

<figure markdown>
  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/x3WXQFk6paY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  <figcaption>Solution Architect Dan Kelcher will guide you through the installation and configuration of IP Fabric in under 25 minutes!</figcaption>
</figure>

## Operational Requirements

Please reference [Operational Requirements](../overview/index.md#operational-requirements) for important requirements pertaining to:

1. [Hardware Requirements](../overview/index.md#hardware-requirements)
2. [Network Connectivity Requirements](../overview/index.md#network-connectivity-requirements)
3. [Network Access Credentials Requirements](../overview/index.md#network-access-credentials-requirements)

## Images

IP Fabric images can be found on our [Releases Page](https://releases.ipfabric.io/).
Access is restricted to registered customers only.

!!! note "Image Access"

    If you are a current customer, please contact your Solution Architect
    or [Support](../support/index.md) for access instructions.

    Please contact our [sales representative](mailto:sales@ipfabric.io)
    if you are interested in a trial of IP Fabric.

We provide two different images listed below along with links to installation
instructions.

1. OVA can be deployed on:
   1. [VMware](01-deployment.md#deploying-on-vmware-ova-virtual-machine)
   2. [VirtualBox](01-deployment.md#deploying-a-virtual-machine-on-virtualbox)
2. VMDK can be deployed on:
   1. [VMware](01-deployment.md#deploying-virtual-machine-on-vmware-esxi-using-vmdk-image)
   2. [Nutanix](01-deployment.md#deploying-a-virtual-machine-to-nutanix)
3. qcow2 can be deployed on:
   1. [Hyper-V](01-deployment.md#deploying-on-hyper-v-virtual-machine)
   2. [Azure](01-deployment.md#deploying-a-virtual-machine-on-microsoft-azure)
   3. [KVM](01-deployment.md#deploying-a-virtual-machine-on-kvm)

!!! important "Hardware Requirements"

    After deploying the VM, please ensure that it has been configured correctly
    per the [Hardware Requirements](../overview/index.md#hardware-requirements).
    Importing the OVA will use the base requirements of 4 CPUs, 16 GB RAM, and
    90 GB HDD.

## IPF CLI Config

IPF CLI Config needs to be completed during the IP Fabric virtual machine's
initial deployment. IPF CLI Config introduces the configuration of basic network
parameters, including IP address, DNS, or proxy settings.

Follow the instructions in [IPF CLI Config](02-ipf_cli_config.md).

## Accessing User Interface

Prior to accessing the main IP Fabric UI, you will need to create an `admin`
account in the System Administration UI:
[Creating the First IP Fabric User](03-access_ui.md#accessing-the-main-user-interface)

## Applying IP Fabric License

To access the main IP Fabric user interface, a license must be uploaded to IP
Fabric. Please contact your salesperson for the license key and follow the
instructions in
[Accessing the Main User Interface](03-access_ui.md#accessing-the-main-user-interface)

!!! important "Licensing"

    A valid license must be applied to continue in this Quick Start Guide.

## Configuration

The simplest way for the first-time configuration of IP Fabric is with the
[Configuration Wizard](04-configuration_wizard.md), which will guide you through
the process of adding device credentials, discovery seeds, networks to
include/exclude in discovery, and Advanced CLI settings.

If you would like to change these settings after the initial configuration,
please see [IP Fabric Settings](../IP_Fabric_Settings/configuration_management.md). Alternatively, there
are also
[snapshot-specific settings](../IP_Fabric_GUI/discovery_snapshot.md#snapshot-specific-settings),
which are useful for testing small changes prior to changing the Global Settings.

!!! note "Site Separation"

    After completing the steps in the **Configuration Wizard**, you may also set
    **Site Separation** rules (in **Settings --> Discovery & Snapshots -->
    Discovery Settings --> Site Separation**). This can be done before, or after
    the first discovery. Some customers find it easier to set that up after a
    discovery -- as it will be possible to check to which Site an already
    discovered device would belong to using the "regex tester" on the **Site
    Separation** page.

    Please see the documentation in [Site Separation](../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/site_separation.md).

## Discovery

If you followed the **Configuration Wizard**, the last step would ask you to
**Start Discovery**. You can also start discoveries by using the
[Discovery Snapshot](../IP_Fabric_GUI/discovery_snapshot.md) menu. This is
where the magic of IP Fabric happens, where it will go out to your devices, find
neighbors, and collect information.

Here are some great resources for explaining the discovery process:

- [How CLI Discovery Works](../overview/How_Discovery_Works/CLI_discovery.md)
- [How API Discovery Works](../overview/How_Discovery_Works/API_discovery.md)

## Troubleshooting Discovery

Finally, please read through the
[Troubleshooting Discovery](../overview/How_Discovery_Works/troubleshooting_discovery.md)
page that will guide you through the most common issues seen during the initial
discovery process. It explains how discovery works, how to view logs, and which
settings to change to include (or exclude) devices, among other useful tips.

If you are working with a Solution Architect in a Proof-of-Concept deployment,
they will help you with troubleshooting any issues that may arise.
