---
description: This page provides you with the list of valid ICMP types and codes.
---

# Path Lookup ICMP Decoder

Please see below for the valid ICMP types and codes.

| ICMP Name                                   | Type | Code |
| :------------------------------------------ | :--- | :--- |
| `ECHO_REPLY`                                | 0    | 0    |
| `NET_UNREACHABLE`                           | 3    | 0    |
| `HOST_UNREACHABLE`                          | 3    | 1    |
| `PROTOCOL_UNREACHABLE`                      | 3    | 2    |
| `PORT_UNREACHABLE`                          | 3    | 3    |
| `FRAGMENTATION_NEEDED`                      | 3    | 4    |
| `SOURCE_ROUTE_FAILED`                       | 3    | 5    |
| `DESTINATION_NETWORK_UNKNOWN`               | 3    | 6    |
| `DESTINATION_HOST_UNKNOWN`                  | 3    | 7    |
| `SOURCE_HOST_ISOLATED`                      | 3    | 8    |
| `DESTINATION_NETWORK_ADMIN_PROHIBITED`      | 3    | 9    |
| `DESTINATION_HOST_ADMIN_PROHIBITED`         | 3    | 10   |
| `DESTINATION_NETWORK_UNREACHABLE_FOR_TOS`   | 3    | 11   |
| `DESTINATION_HOST_UNREACHABLE_FOR_TOS`      | 3    | 12   |
| `COMMUNICATION_ADMINISTRATIVELY_PROHIBITED` | 3    | 13   |
| `HOST_PRECEDENCE_VIOLATION`                 | 3    | 14   |
| `PRECEDENCE_CUTOFF_IN_EFFECT`               | 3    | 15   |
| `SOURCE_QUENCH`                             | 4    | 0    |
| `REDIRECT_DATAGRAM_FOR_THE_NETWORK`         | 5    | 0    |
| `REDIRECT_DATAGRAM_FOR_THE_HOST`            | 5    | 1    |
| `REDIRECT_DATAGRAM_FOR_THE_TOS_AND_NETWORK` | 5    | 2    |
| `REDIRECT_DATAGRAM_FOR_THE_TOS_AND_HOST`    | 5    | 3    |
| `ALTERNATE_ADDRESS_FOR_HOST`                | 6    | 0    |
| `ECHO_REQUEST`                              | 8    | 0    |
| `NORMAL_ROUTER_ADVERTISEMENT`               | 9    | 0    |
| `DOES_NOT_ROUTE_COMMON_TRAFFIC`             | 9    | 16   |
| `ROUTER_SOLICITATION`                       | 10   | 0    |
| `TIME_TO_LIVE_EXCEEDED_IN_TRANSIT`          | 11   | 0    |
| `FRAGMENT_REASSEMBLY_TIME_EXCEEDED`         | 11   | 1    |
| `POINTER_INDICATES_THE_ERROR`               | 12   | 0    |
| `MISSING_A_REQUIRED_OPTION`                 | 12   | 1    |
| `BAD_LENGTH`                                | 12   | 2    |
| `TIMESTAMP_REQUEST`                         | 13   | 0    |
| `TIMESTAMP_REPLY`                           | 14   | 0    |
| `INFORMATION_REQUEST`                       | 15   | 0    |
| `INFORMATION_REPLY`                         | 16   | 0    |
| `MASK_REQUEST`                              | 17   | 0    |
| `MASK_REPLY`                                | 18   | 0    |
| `BAD_SPI`                                   | 40   | 0    |
| `AUTHENTICATION_FAILED`                     | 40   | 1    |
| `DECOMPRESSION_FAILED`                      | 40   | 2    |
| `DECRYPTION_FAILED`                         | 40   | 3    |
| `NEED_AUTHENTICATION`                       | 40   | 4    |
| `NEED_AUTHORIZATION`                        | 40   | 5    |
