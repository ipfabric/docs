---
description: This page contains information why FMC REST API migth return HTTP Error Code 500 on discovery.
---

# FMC REST API Calls Returns HTTP Error Code 500

As per the Cisco bug [CSCvz26998](https://bst.cisco.com/bugsearch/bug/CSCvz26998), when multiple processes are using the same credentials and generating separate auth token continuously for REST API access, it could occasionally return HTTP error code 500.

Multiple processes are using the same credentials and generating separate auth token continuously for REST API access.

The workaround is to upgrade the FMC to a known fixed release.
