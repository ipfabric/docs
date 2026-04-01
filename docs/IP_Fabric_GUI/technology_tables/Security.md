---
description: The Security section contains information about access control lists and SSL certificates on the network.
---

# Security

The Security section provides visibility into security-related components across your network infrastructure.

## Access Lists

The Access Lists section contains information about access control lists on
the network. The Access Lists section details each line from each access
list present on each managed device. ACLs can be filtered by device/ACL
name, protocol, address, or port. The ACL Interfaces section details
access lists as they are applied to the interfaces.

## SSL

### Certificates

The Certificates table provides centralized visibility into managed SSL certificates associated with cloud load balancers across AWS and Azure environments.

**Key columns include:**

- **ID** -- Unique identifier for the certificate
- **Name** -- Certificate name or identifier as defined in the cloud platform
- **Status** -- Current status of the certificate (e.g., active, expired)
- **Issuer** -- Certificate authority or organization that issued the certificate
- **Common Name** -- Primary domain name for which the certificate was issued
- **Issued At** -- Timestamp when the certificate was created
- **Not Before** -- Start date of the certificate validity period
- **Not After** -- Expiration date of the certificate validity period
- **SAN List** -- Subject Alternative Names listing additional domain names covered by the certificate

