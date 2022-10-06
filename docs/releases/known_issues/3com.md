---
description: IP Fabric describes known affected issues for 3Com and how to fix them.
---

# 3Com

**Known Affected platforms**: All

**Description**: By default, trap information is sent to the terminal
session. This can break processing and parsing of outputs from the
device. IP Fabric has clearing procedures in place but we cannot
guarantee their 100% reliability and these outputs can also affect
discovery performance. We strongly advise disabling terminal trapping.  

**Fix**: Run command `undo terminal trapping`
