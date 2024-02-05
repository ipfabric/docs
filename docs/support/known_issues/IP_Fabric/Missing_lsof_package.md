---
description: This page contains information how to repair non-starting jumphost even if you set everything correctly.
---

# Missing `lsof` Package

The IP Fabric OVA image version `5.0.x` is missing the `lsof` diagnostic tool
package, causing jumpshot startup issues.

To fix the missing package issue, download the `lsof` package with the following
command:

```
cd /tmp/ && curl -O http://deb.debian.org/debian/pool/main/l/lsof/lsof_4.93.2+dfsg-1.1_amd64.deb
```

You can verify the location of the package by visiting
[Debian package database](https://packages.debian.org/bullseye/lsof). After
downloading it, you can install it with this command:

```
sudo dpkg -i /tmp/lsof_4.93.2+dfsg-1.1_amd64.deb
```
