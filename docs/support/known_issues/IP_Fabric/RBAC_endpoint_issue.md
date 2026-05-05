---
description: RBAC configuration may cause intermittent 403 errors on the Support Status page when the `/support/status` endpoint is excluded from API scope.
---

# Support Status Page Endpoint Error

#### Affects versions `7.9` and higher

When a policy excludes the `GET /support/status` endpoint in API scope, the Support Status page may load correctly or show a `403` `Failed to load data` error.

#### Workaround:
Include `GET /support/status` in the policy. This allows access to hardware information while still restricting actions such as service restarts.
