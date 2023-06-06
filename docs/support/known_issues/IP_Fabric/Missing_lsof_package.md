---
description: This page contains information how to repair non-starting jumphost even if you set everything correctly.
---

# Missing `lsof` Package

IP Fabric OVA images version 5.0.x are missing `lsof` diagnostic tool package causing jumpshot startup issues.

To fix missing package issue, download `lsof` package with the following command:

```
cd /tmp/ && curl -O http://deb.debian.org/debian/pool/main/l/lsof/lsof_4.93.2+dfsg-1.1_amd64.deb
```

You can verify location of the package visiting [Debian package database](https://packages.debian.org/bullseye/lsof). After download, you can install it with the command:

```
sudo dpkg -i /tmp/lsof_4.93.2+dfsg-1.1_amd64.deb
```

