# ARP table contains only master `VSYS 0` entries

## Known Affected Software Versions

R80.30 and R80.40

## Description

Command `show arp dynamic all` on VSx always (by mistake) shows ARP only for the `“master VSYS 0` regardless of active `VSYS`.

It is a confirmed bug on the Checkpoint firewalls.
