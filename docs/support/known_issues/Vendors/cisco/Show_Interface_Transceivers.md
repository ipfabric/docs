---
description: This page provides information that executing some commands to get transceiver-related information may cause issues on some devices.
---

# Show Interface Transceivers

Executing some commands to get transceiver related information may cause
issues on some devices. In the worst case, a device may crash and
reload. To prevent disruptions of your network, IPF uses a transceiver
task execution control system.

**Known bugs**:

**Cisco IOS** -- Router crash when issuing a command: `show interface
transceiver`

- Bug ID: CSCua29548
- Affected versions: 15.1(4)M4, 15.1(4)M4.7, 15.1(4)M5

Note: IPF tries to prevent task execution on all Cisco IOS devices not
considered Catalyst or IE switches.

**Cisco IOS** -- Memory leak in \*dead\* memory

- Bug ID: CSCtg41473
- Affected versions: 12.2(50)SE3

Note: IPF tries to prevent task execution on all Cisco IOS devices considered
Catalyst or IE switches.

**Cisco NX-OS** -- Nexus 5500 ethpc hap reset -
SYSMGR_DEATH_REASON_FAILURE_HEARTBEAT

- Bug ID: CSCuq13396
- Affected versions: 6.0(2)N2(3)

**Cisco IOS** -- Router crash when issue a command: "show interface
transceiver"

- Bug ID: CSCva00194
- Affected versions: 15.5(3.0l)M

**Cisco IOS-XE** -- C3850: show interface transceiver slow in response,
console/VTY may hang

- Bug ID: CSCuw38988
- Affected versions: 3.7.5E

Note: IPF tries to prevent task execution on all Cisco IOS-XE devices
considered to belong to the cat3k_caa platform.
