# Local time inconsistencies

When setting a time for automatic snapshots and other recurring tasks,
UTC time is used in IP Fabric.

This will change in the upcoming 4.2.0 release.

After this release, the time for all recurring tasks will be in the
timezone defined during the initial setup, except for API that will
always return data in UTC time.
