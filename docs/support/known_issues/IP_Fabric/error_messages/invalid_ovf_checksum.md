---
description: This is a known issue with some older ESXi/vSphere not recognizing the SHA256 checksum of the IP Fabric OVA image.
---

# Error: Invalid OVF checksum algorithm: SHA256

When importing the IP Fabric OVA image on vSphere/ESXi, the following error
might occur:

![OVA error](ova_error.png)

The cause is that our OVA image is hashed with the SHA256 algorithm and some
older versions of vSphere/ESXi might not be fully compatible with it.

We use the SHA256 algorithm as SHA1 is no longer considered secure.

To fix this issue, you need to convert the OVA file and hash it with the SHA1
algorithm. See
["The OVF package is invalid and cannot be deployed" error when deploying the OVA (2151537)](https://kb.vmware.com/s/article/2151537).
