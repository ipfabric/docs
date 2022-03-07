# API Tech Note - Path Lookup ICMP Decoder

Please see below for the valid ICMP types and codes.

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ECHO_REPLY = {"type":0, "code":0}
NET_UNREACHABLE = {"type":3, "code":0}
HOST_UNREACHABLE = {"type":3, "code":1}
PROTOCOL_UNREACHABLE = {"type":3, "code":2}
PORT_UNREACHABLE = {"type":3, "code":3}
FRAGMENTATION_NEEDED = {"type":3, "code":4}
SOURCE_ROUTE_FAILED = {"type":3, "code":5}
DESTINATION_NETWORK_UNKNOWN = {"type":3, "code":6}
DESTINATION_HOST_UNKNOWN = {"type":3, "code":7}
SOURCE_HOST_ISOLATED = {"type":3, "code":8}
DESTINATION_NETWORK_ADMIN_PROHIBITED = {"type":3, "code":9}
DESTINATION_HOST_ADMIN_PROHIBITED = {"type":3, "code":10}
DESTINATION_NETWORK_UNREACHABLE_FOR_TOS = {"type":3, "code":11}
DESTINATION_HOST_UNREACHABLE_FOR_TOS = {"type":3, "code":12}
COMMUNICATION_ADMINISTRATIVELY_PROHIBITED = {"type":3, "code":13}
HOST_PRECEDENCE_VIOLATION = {"type":3, "code":14}
PRECEDENCE_CUTOFF_IN_EFFECT = {"type":3, "code":15}
SOURCE_QUENCH = {"type":4, "code":0}
REDIRECT_DATAGRAM_FOR_THE_NETWORK = {"type":5, "code":0}
REDIRECT_DATAGRAM_FOR_THE_HOST = {"type":5, "code":1}
REDIRECT_DATAGRAM_FOR_THE_TOS_AND_NETWORK = {"type":5, "code":2}
REDIRECT_DATAGRAM_FOR_THE_TOS_AND_HOST = {"type":5, "code":3}
ALTERNATE_ADDRESS_FOR_HOST = {"type":6, "code":0}
ECHO_REQUEST = {"type":8, "code":0}
NORMAL_ROUTER_ADVERTISEMENT = {"type":9, "code":0}
DOES_NOT_ROUTE_COMMON_TRAFFIC = {"type":9, "code":16}
ROUTER_SOLICITATION = {"type":10, "code":0}
TIME_TO_LIVE_EXCEEDED_IN_TRANSIT = {"type":11, "code":0}
FRAGMENT_REASSEMBLY_TIME_EXCEEDED = {"type":11, "code":1}
POINTER_INDICATES_THE_ERROR = {"type":12, "code":0}
MISSING_A_REQUIRED_OPTION = {"type":12, "code":1}
BAD_LENGTH = {"type":12, "code":2}
TIMESTAMP_REQUEST = {"type":13, "code":0}
TIMESTAMP_REPLY = {"type":14, "code":0}
INFORMATION_REQUEST = {"type":15, "code":0}
INFORMATION_REPLY = {"type":16, "code":0}
MASK_REQUEST = {"type":17, "code":0}
MASK_REPLY = {"type":18, "code":0}
BAD_SPI = {"type":40, "code":0}
AUTHENTICATION_FAILED = {"type":40, "code":1}
DECOMPRESSION_FAILED = {"type":40, "code":2}
DECRYPTION_FAILED = {"type":40, "code":3}
NEED_AUTHENTICATION = {"type":40, "code":4}
NEED_AUTHORIZATION = {"type":40, "code":5}
```

</div>

</div>
