---
description: This page describes known issue for Versa vendor and how to fix it.
---

# Forwarding Table Duplicate Output

**Known affected platforms:** all

**Description**: The device may start sending multiple duplicates of the forwarding table. In such cases, it can overload the parser and potentially cause a crash.
To prevent this, we set a limit of 100,000 records—if the output exceeds this limit, it is not parsed.
This limitation is configurable via a [Feature Flag](../../../../System_Administration/Command_Line_Interface/Feature_Flags.md#versa-vos-forwarding-table).
