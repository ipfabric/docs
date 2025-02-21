---
description: This page describes how to fix problem with devices in subnet `172.17.0.0/16` not being discovered.
---

# Unable to discover devices in `172.17.0.0/16` subnet

!!! info
    This article applies only to IP Fabric appliances running version `7.0` and later.

The issue arises because the default `docker` bridge subnet is assigned the `172.17.0.0/16` range. This large range
accommodates all extension images and provides headroom for potential future "dockerization" of the IP Fabric product.

Here's a quick guide on how to fix the issue:

1. Identify an unused `/16` subnet in your network and split it into two `/17` subnets.
2. Log in to the IP Fabric appliance using `osadmin` credentials and switch to the `root` prompt with `sudo -i`.
3. Run the following command to update the default `docker` bridge subnet with your chosen subnet (replace `xx` as needed):
```shell
jq -n '{
  "userns-remap": "ipf-docker:ipf-docker",
  "bip": "xx.xx.0.1/17",
  "default-address-pools": [
    {
      "base": "xx.xx.128.0/17",
      "size": 24
    }
  ]
}' > /etc/docker/daemon.json
```
4. Restart the `docker` service using `systemctl restart docker.service`.
5. Verify that the new route has been installed by running `ip route show`.
