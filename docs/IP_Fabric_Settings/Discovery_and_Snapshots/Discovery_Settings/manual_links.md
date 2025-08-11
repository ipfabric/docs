---
description: This feature allows you to manually create links that cannot be discovered by IPF. In some cases, links cannot be detected, such as when LLDP/CDP is missing or in transparent L2 topologies.
---
# Table Structure
The main table displays links with the following columns:
  
- **SN**: Source device SN
- **Interface**: Source device physical interface 
- **Remote SN**: Destination device SN
- **Remote interface**: Destination device physical interface
- **Type**: Link type (`L1` or `L2`)
  
# Interface Selection Logic
- After `hostname` is entered, available interfaces become visible.
- Only `L1` and `L2` interfaces are available for selection.
  
# Link Status Monitoring
- Link status is visible under `Discovery Snapshots` → `Snapshot Settings`.
- A **Failed** status indicates the device is not discovered.
- Status reflects the real-time discovery state.
  
# Manual Link Types
  
## L1 Links
- Visible only in the UI.
- Intended for customer reference.
  
## L2 Links  
- Visible in the UI.
- Used in E2E calculations.
- Applied for transparent firewalls and similar scenarios.
  
# Visualization
- Manual links are clearly distinguished from topology-calculated links.
- Visual differentiation ensures clear link source identification.
  
  
## E2E Changes
- E2E calculations are updated after taking a snapshot or after unloading and reloading a snapshot to trigger recalculations and display `L2` links.
- Changes applied with new snapshot generation
 
