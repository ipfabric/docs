---
description: In this section, IP Fabric publishes the most recent version releases of the Platform.
---

# IP Fabric Releases

!!! important "Current release"

    The current major release is `6.0` please check the [detailed release
    notes](release_notes/6.0.md) for this release.

Our release naming follows [semantic versioning](https://semver.org/). Where
components of the version are `major.minor.patch+build`:

- `major` version changes if we introduce a change (typically backwards
  incompatible) touching APIs, deployment or key component of the platform.
- `minor` version means a significant change, typically a new feature being
  added. These are typically backwards compatible and we also keep the promise
  of API compatibility.
- `patch` releases are frequently a bugfix releases.
- `build` is an internal version which increases with every internal build,
  thus can be pretty large number. It is used to distinguish between different
  packages.

!!! warning "Clearing Browser Cache"

    Please force refresh your browser cache after an upgrade.
    Depending on your operating system use the following key combination in your browser window:

    - Windows: `CTRL + F5`
    - Mac/Apple: `Apple + R` or `⌘ + R`
    - Linux: `CTRL + F5`
