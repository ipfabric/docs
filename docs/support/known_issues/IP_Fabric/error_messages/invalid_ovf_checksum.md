---
description: This is a known error with OVF having the wrong checksum for some older ESXi/vSphere hosts.
---

# Error: Invalid OVF checksum algorithm: SHA256

When importing IP Fabrics OVA on vSphere/ESXi, the following error might occur:

![ova error](ova_error.png)

The cause is that our OVA is hashed with the SHA256 algorithm and some older versions of vSphere/ESXi might not be fully compatible with it.

This was done because of security, as SHA1 is no longer considered secure.

To fix this issue, one needs to convert the OVA file and hash it with SHA1 algorithm, see ["The OVF package is invalid and cannot be deployed" error when deploying the OVA (2151537)](https://kb.vmware.com/s/article/2151537) article or follow the other steps in the mentioned article.
