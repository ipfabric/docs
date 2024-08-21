---
description: This section contains information on how to add Debian system repositories for updates.
---

# How To Add Debian System Repositories

Our appliance provides a script to prepare the `/etc/apt/sources.list` with
the Debian system repositories configuration. The default content of
`/etc/apt/sources.list` is either empty or a banner asking the user to place
configuration to file in `/etc/apt/sources.list.d/` directory - depending on
the first version deployed.

--8<-- "snippets/cli_root_access.md"

```shell title="Enable system repositories"
/opt/ipf-debian-repositories/bin/ipf-debian-repositories.sh
```

```shell title="Install updates"
apt-get update
apt-get upgrade
```
