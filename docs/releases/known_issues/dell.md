# Dell

**IP Fabric Version:** All

**Known Affected platforms**: Dell SmartFabric OS10

**Description**: The command `show license status` is only available for
`sysadmin` user role.  This command is required to detect the serial number
and discover the device.

**Fix**: User must be added to the `sysadmin` role for discovery to occur.
