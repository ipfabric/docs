---
description: In this section, we publish release notes and low-level release notes of IP Fabric.
---

# IP Fabric Releases

--8<-- "snippets/6.6.3_online_upgrade_issue.md"

--8<-- "snippets/upgrade_version_policy.md"

!!! important "Current Release"

    The current major release is `6.7`. Please check the
    [detailed release notes](release_notes/6.7.md) for this release.

Our release naming follows [semantic versioning](https://semver.org/). Where
components of the version are `major.minor.patch+build`:

- `major` version changes if we introduce a change (typically backwards
  incompatible) touching APIs, deployment or key component of the platform.
- `minor` version means a significant change, typically a new feature being
  added. These are typically backwards compatible, and we also keep the promise
  of API compatibility.
- `patch` releases are frequently bugfix releases.
- `build` is an internal version which increases with every internal build, thus
  can be pretty large number. It is used to distinguish between different
  packages.

--8<-- "snippets/clear_browser_cache.md"

### Update Process

Our update process is based on Debian apt package resolving. As a result, we
remove any configured apt repositories during the update. If you have manually
configured any repositories, the update process will remove them. Please note
that we are trying to keep the appliance as small and thin as possible, so any
unwanted packages may be automatically removed.
