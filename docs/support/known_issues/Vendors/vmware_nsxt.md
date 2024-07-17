---
description: This page describes known issues with VMware NSX-T and how to fix them.
---

# VMware NSX-T


## NSX-T `2.x` and Earlier Not Supported

**Known affected platforms:** `2.x` and earlier

**Description:** IP Fabric officially supports NSX-T versions `3.x.x` and later.
Versions `2.x` and earlier are not supported, as they may have different API
endpoint outputs that may cause discovery to fail or get stuck.

**Fix:** Remove or disable the affected NSX-T controllers in **Settings -->
Discovery & Snapshots --> Discovery Settings --> Vendors API**.

## Endpoint `GET /api/v1/ns-groups/<group-id>/effective-ip-address-members` Not Responding

**Known affected platforms:** `3.2.2.0.0.20737190`

**Description:** Vendor API discovery may fail to retrieve any data from the API
endpoint `GET /api/v1/ns-groups/<group-id>/effective-ip-address-members`. This
endpoint always returns either error code `500` (`UNKNOWN: Unknown error`) or
`429` (`Client '<username>' exceeded request rate of 100 per second`). IP Fabric
stops NSX-T discovery after 10 consecutive `429` errors and reports a `Client
destroyed` error in the **Summary of Issues**.

**Fix:** Add (i.e., disable) the `ACL` task for the NSX-T platform version
`3.2.2` in **Settings --> Discovery & Snapshots --> Discovery Settings -->
Disabled Discovery Tasks**.
