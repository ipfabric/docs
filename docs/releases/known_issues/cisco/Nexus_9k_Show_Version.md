# Nexus 9k Show Version

**IP Fabric Version:** All

**Known Affected platforms**: Nexus 9000 Series Version `7.0(3)I7(4)`

**Description**: The command `show version` may hang on Nexus9000 platform
running `7.0(3)I7(4)`. IP Fabric requires `show version` to understand the model
and version of the device in order for discovery to know which commands to run.

Please see:
[CSCvn72588](https://quickview.cloudapps.cisco.com/quickview/bug/CSCvn72588)

**Fix**: Update Nexus devices to a newer version.
