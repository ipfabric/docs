---
description: This page explains how to configure IP Fabric to be monitored with the SNMP protocol.
---

# SNMP

The IP Fabric appliance can be monitored using the SNMP protocol. CPU, memory,
hard drives, and network interfaces can be monitored. The IP Fabric appliance
uses standard Linux OS OIDs.

To enable SNMP on IP Fabric, go to **Settings --> System --> SNMP**, click the
**on/off** toggle and select `2c` or `3` from the **Version** list:

![SNMP](snmp/enable_snmp.png)

!!! check "Security note"

    Only IP addresses specified in the **NMS IPs** field are enabled to have
    access to SNMP port `161/udp`.

If you selected version `2c`, please configure:

1. **NMS IPs** -- IP addresses of remote monitoring servers
2. **Locality** -- location of IP Fabric appliance
3. **System Contact** -- contact details (e.g. email) of a responsible person or department
4. **Community string** -- must match community string configured on monitoring
   server
5. Click **Save**

![Version 2c](snmp/version_2c.png)

If you selected version `3`, please configure:

!!! info "SNMP v3"

    For user authentication, only SHA is supported. For data privacy, AES is
    used.

1. **NMS IPs** -- IP addresses of remote monitoring servers
2. **Locality** -- location of IP Fabric appliance
3. **System Contact** -- contact details (e.g. email) of a responsible person or department
4. **Username** -- SNMPv3 user
5. **Passphrase** -- authentication passphrase
6. **Encryption Passphrase** -- privacy passphrase
7. Click **Save**

![Version 3](snmp/version_3.png)

--8<-- "snippets/username_password_regex.md"
