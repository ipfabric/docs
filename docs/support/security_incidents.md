---
description: This page describes our Security Incident Response policy.
---

# Security Incident Response

## Initial Source of Information

If you have any information about potential security events or incidents related
to IP Fabric, please notify us in one of the following ways:

- Email: `security@ipfabric.io` or `support@ipfabric.io`
- [IP Fabric Help Center](https://support.ipfabric.io)

In line with industry best practices, we also monitor standard data sources
including (but not limited to):

- Mitre CVE database for software vulnerabilities
- `debian-security` mailing list
- Internal monitoring (doesn't cover customers' deployments)

## Classification

We use industry-standard
[CVSS](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System)
scoring for the classification of reported/discovered vulnerabilities.

![CVSS Score](../images/support/support_cvss.webp)

The timeline and escalation path are as follows:

| CVSS Score | Qualitative Rating | SLA Rating | Reaction Time                        | Escalation    |
| ---------- | ------------------ | ---------- | ------------------------------------ | ------------- |
| 0.0        | None               |            |                                      |               |
| 0.1 – 3.9  | Low                |            |                                      |               |
| 4.0 – 6.9  | Medium             | Normal     | Next 2 working days                  | VPE, SRE      |
| 7.0 – 8.9  | High               | High       | Next working day                     | CTO, VPE, SRE |
| 9.0 – 10.0 | Critical           | Critical   | Within 4 hours during business hours | CTO, VPE, SRE |

Note that we don't show **Remediation Time** in this table, instead showing
**Reaction Time** as a metric. It is hard to predict upfront time complexity of
a particular issue or the availability of the solution (particularly in a
third-party component on which there may be a dependency). **Reaction Time**
refers to the time to reach a proposal for solving the issue with a time
estimate.

## Tracking

Every security incident has a tracking ticket, which contains:

- CVSS score
- CVE number/link (when applicable)
- Affected customers (if specific)
- `security` tag assigned

Additionally, the IP Fabric internal security Slack channel will be notified,
with a dedicated channel created for a specific incident as necessary.

We select one person to be responsible for coordinating internal communication
and to serve as an interface to the teams communicating directly with customers.
Typical candidates include: DevOps TL, Head of Development, VPE, CTO.
