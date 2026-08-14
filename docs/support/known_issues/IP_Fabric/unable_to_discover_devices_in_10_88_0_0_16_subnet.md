---
description: This page describes how to fix problem with devices in subnet `10.88.0.0/16` not being discovered.
---

# Unable to discover devices in `10.88.0.0/16` subnet

!!! info
    This article applies only to IP Fabric appliances running version `8.0` and later.

The issue arises because `podman` assigns the `10.88.0.0/16` range as the default bridge subnet. This large range accommodates all extension images and provides headroom for future containerization of IP Fabric.

Follow these steps to fix the issue:

1. Identify an unused `/16` subnet in your network and split it into two `/17` subnets.
2. Log in to the IP Fabric appliance using `osadmin` credentials. Switch to the `root` prompt with `sudo -i`.
3. Run the following command to update the default `podman` bridge subnet with your chosen subnet (replace `xx` as needed):
```shell
mkdir -p /etc/containers/containers.conf.d/
cat <<END > /etc/containers/containers.conf.d/subnet.conf
[network]
default_subnet = "xx.xx.0.0/17"
default_subnet_pools = [
    { base = "xx.xx.128.0/17", size = 24 }
]
END
ufw route allow in on podman0 out on eth0 from xx.xx.0.0/16
podman network reload --all
```
4. Restart the `podman` service using `systemctl restart podman.service podman.socket`.
5. Verify that the new route appears by running `ip route show`. At least one container must be running.
