---
description: This page describes how to repair a non-starting jumphost even if you have set everything correctly.
---

# Missing `lsof` Package

The IP Fabric OVA image version `5.0.x` is missing the `lsof` diagnostic tool
package, which causes jumpshot startup issues.

To resolve this issue, download the `lsof` package using the following command:

```shell
cd /tmp/ && curl -O http://deb.debian.org/debian/pool/main/l/lsof/lsof_4.93.2+dfsg-1.1_amd64.deb
```

You can verify the package location by visiting the
[Debian package database](https://packages.debian.org/bullseye/lsof). Once
downloaded, you can install it with the following command:

```shell
sudo dpkg -i /tmp/lsof_4.93.2+dfsg-1.1_amd64.deb
```
