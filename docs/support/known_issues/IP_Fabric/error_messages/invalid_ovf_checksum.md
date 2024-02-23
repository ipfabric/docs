---
description: This page describes a known issue with some older ESXi/vSphere versions not recognizing the SHA256 checksum of the IP Fabric OVA image.
---

# Error: Invalid OVF checksum algorithm: SHA256

When importing the IP Fabric OVA image on vSphere/ESXi, the following error
might occur:

![OVA error](ova_error.png)

Our appliance is built on top of Debian 11. We also require the `AVX` CPU instruction. The minimal requirement
for the VMWare system type is `vmx-17`, supported by ESXi version `7.0` or newer.
See [ESXi/ESX hosts and compatible virtual machine hardware versions list (2007240)](https://kb.vmware.com/s/article/2007240).
We require this system type because of `virtio`
drivers for network and storage. All VMware applications from the same _generation_ support `SHA256`. There is a chance
that you might use an older version of the desktop VMware client application, but the host system meets the
minimal requirements. In this case, please double-check [Hardware Requirements](../../../../overview/index.md#hardware-requirements)
and convert the OVA image from `SHA256` to `SHA1` or import the `vmdk` disk. 

Make sure you selected `VMXNET 3` for network and `PVSCSI` (Paravirtual SCSI) for storage.

VMware's KB on converting OVA images:
["The OVF package is invalid and cannot be deployed" error when deploying the OVA (2151537)](https://kb.vmware.com/s/article/2151537).
