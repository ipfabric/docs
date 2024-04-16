---
description: This page provides OVA distribution details.
---

# OVA Distribution Details

The appliance is built on top of Debian 11, which has been officially supported since [ESXi Version 7.0](https://www.vmware.com/resources/compatibility/detail.php?deviceCategory=Software&productid=54075&vcl=true&supRel=396,448,508,518,578,589,615,617,649,650&testConfig=16).

The minimal required `Virtual Hardware Version` is `vmx-17`, supported by ESXi 7.0, Fusion 12.x, Workstation Pro 16.x,
and Workstation Player 16.x. For details, see the VMware KB articles [1003746](https://kb.vmware.com/s/article/1003746) and [2007240](https://kb.vmware.com/s/article/2007240).

We require this system type because of the `virtio` drivers for network and storage.

Note that we also have requirements about the processor itself: [Hardware Requirements](../index.md#hardware-requirements). These cannot be described through the OVA image definition.

!!! danger "If you do not use the virtio/paravirtualized drivers for network and storage, performance will be degraded."

## Setting the Virtual Machine From Scratch -- Importing the `vmdk`

!!! success "Importing `vmdk` is the recommended way."

If you do not have access to an `ESXi` host for importing, you can try to import the disk (`vmdk`) and set up the machine manually. Ensure the following are configured correctly:

- `Virtual Hardware Version` is at least `vmx-17`
- virtio/paravirtualized drivers
  - [`PVSCSI`](https://kb.vmware.com/s/article/1010398) (Paravirtual SCSI) storage driver
  - [`VMXNET 3`](https://kb.vmware.com/s/article/1001805) networking driver

## Deploying through vSphere or VxRail (converting to SHA1 image)

Customers may experience problems deploying through vSphere/VxRail. vSphere/VxRail is refusing the SHA256 version of our OVA image. When trying to create a virtual machine using the SHA1-based OVA image, customers are experiencing problems importing the OVA image, because of unsupported "hardware". In this case, please see the next paragraph about deploying manually.

VMware's KB article on converting OVA images:
["The OVF package is invalid and cannot be deployed" error when deploying the OVA (2151537)](https://kb.vmware.com/s/article/2151537)

!!! warning "Importing the SHA1-Based OVA Image"

    This might lead to unexpected results, such as wrong hardware assignments, degraded performance, etc.

!!! tip "`operation not supported on this object`"

    This states the inability to deploy the OVA image with the required hardware requirements through itself (vSphere).
    However, if the same OVA image is deployed through `ESXi`, no warnings are present while creating the virtual machine.
