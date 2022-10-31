# FMC REST API Calls Returns HTTP Error Code 500

As per the Cisco bug [CSCvz26998](https://bst.cisco.com/bugsearch/bug/CSCvz26998), when multiple processes are using the same credentials and generating separate auth token continuously for REST API access, it could return http error code 500 occasionally.

Multiple processes are using same credentials and generating separate auth token continuously for REST API access.

Known workaround is to upgrade the FMC to known fixed release.
