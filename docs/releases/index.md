---
description: In this section, we publish release notes and low-level release notes of IP Fabric.
---

# IP Fabric Releases

--8<-- "snippets/upgrade_version_policy.md"

Our release naming follows [semantic versioning](https://semver.org/), where
the components of the version are:

```
major.minor.patch+build
```

- The `major` version changes if we introduce a (typically backwards
  incompatible) change affecting APIs, deployment, or key component of the
  platform.
- The `minor` version means a significant change, typically a new feature being
  added. These are typically backwards compatible, and we also keep the promise
  of API compatibility.
- `patch` releases are frequently bugfix releases.
- `build` is an internal version that increases with every internal build and
  can thus be a large number. It is used to distinguish between different
  packages.

--8<-- "snippets/clear_browser_cache.md"

### Update Process

Our update process is based on Debian's `apt` package resolving. As a result, we
remove any configured `apt` repositories during the update. If you have manually
configured any repositories, the update process will remove them. Please note
that we aim to keep the appliance as small and thin as possible, so any
unwanted packages may be automatically removed.
