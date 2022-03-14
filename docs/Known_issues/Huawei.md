# Huawei

**Known Affected platforms**: Huawei - platforms with bridge domains

**Description**: IP Fabric currently doesn’t have a separate bridge
domain model. The bridge domain is mapped into the VLAN model. This has
limitations:

- The bridge domain number can have a maximal value of 4095 and must
  be the same as the VLAN tag

- Vlan and bridge domain with the same number is not supported

**Fix**: Currently no fix. Can be improved in future releases.
