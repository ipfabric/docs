---
description: OVA distribution details
---

# OVA distribution details

The appliance is built on top of Debian 11. Debian 11 has officially been supported since [ESXi Version 7.0](https://www.vmware.com/resources/compatibility/detail.php?deviceCategory=Software&productid=54075&vcl=true&supRel=396,448,508,518,578,589,615,617,649,650&testConfig=16).

The minimal required `Virtual Hardware Version` is `vmx-17`, supported by ESXi 7.0, Fusion 12.x, Workstation Pro 16.x,
and Workstation Player 16.x. See [VMware KB](https://kb.vmware.com/s/article/1003746) for details.
[ESXi/ESX hosts and compatible virtual machine hardware versions list (2007240)](https://kb.vmware.com/s/article/2007240).

We require this system type because of `virtio` drivers for network and storage.

Note that we have also requirements about processor itself: [Hardware Requirements](../index.md#hardware-requirements),
those cannot be described through `ova` definition.

!!! danger "If you do not use virtio/paravirtualized drivers for network and storage, performance will be degraded."

## Setting the virtual machine from scratch -- importing the `vmdk`

!!! success "Importing `vmdk` is the recommended way."

If you do not have access to an `ESXi` host for importing. You can try to import the disk (`vmdk`) and set up the machine manually. Ensure the following is configured correctly:

- `Virtual Hardware Version` is at least `vmx-17`
- virtio/paravirtualized drivers
  - [`PVSCSI`](https://kb.vmware.com/s/article/1010398) (Paravirtual SCSI) storage driver
  - [`VMXNET 3`](https://kb.vmware.com/s/article/1001805) networking driver

## Deploying through vSphere or VxRail (converting to SHA1 image)

Customers may experience deploying through vSphere/VxRail to be problematic. vSphere/VxRail is refusing the `SHA256` version of our `ova`. When trying to create a virtual machine using the `SHA1` based `ova`, customers are experiencing problems importing the ova, because of unsupported "hardware". In this case please see the next paragraph about deploying manually.

VMware's KB on converting OVA images:
["The OVF package is invalid and cannot be deployed" error when deploying the OVA (2151537)](https://kb.vmware.com/s/article/2151537).

!!! warning "Importing the SHA1 based OVA"

    This might lead into unexpected results, like wrong hardware assignments, degraded performance, etc.

!!! tip "operation not supported on this object"

    This states the inability to deploy the `ova` with the required hardware requirements through itself (vSphere).
    But if the same `ova` is deployed through `ESXi` no warnings are present while creating the virtual machine.
