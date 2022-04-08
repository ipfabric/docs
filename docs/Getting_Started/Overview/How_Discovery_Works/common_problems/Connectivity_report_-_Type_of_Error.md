# Connectivity Report - Type of Error

| **Error message**                                         | **Type of Error**                              | **Description / mitigation**                        |
|:------------------------------------------------------|:-----------------------------------------------|:----------------------------------------------------|
|                                                       | Ambiguous or Incomplete command                |                                                     |
| All configured authentication methods failed          | Authentication error                           | Unable to authenticate to the destination host      |
| Authentication failed                                 | Authentication error                           | Unable to authenticate to the destination host      |
| Authentication failed - login prompt appeared again   | Authentication error                           | Unable to authenticate to the destination host      |
| Command "enable" authorization failed, tried 2x       | Command authorization failure                  | The command wasn't authorized. **Increase command authorization failure retries** or increase the timer value (ms) |
|                                                       | Command not executed for prevented reasons     | Excluded for specific reason (bug with specific)    |
|                                                       | Command result mapping failure                 |                                                     |
| SSH client not received any data for last 120000 ms! cmd => show vrrp  \| e #^$ | Command timeout      | The command timed out. Increase **device session timeout.**                                                        |
| Can't detect prompt                                   | Command timeout                                | Unable to detect CLI prompt. Increase **network device login timeout.**                                            |
| connect ETIMEDOUT XX.XX.XX.XX:22                      | Connection error                               | Received no response from the destination.                                                                         |
| connect ECONNREFUSED XX.XX.XX.XX:22                   | Connection error                               | The connection to the destination is being blocked by an access-list or firewall.                                  |
|                                                       | Fatal error                                    | Contact the support team                                                                                           |
|                                                       | Invalid command                                |                                                     |
|                                                       | No credentials provided                        |                                                     |
|                                                       | Parsing command failure                        |                                                     |
|                                                       | Parsing failures (per command)                 |                                                     |
|                                                       | Possible device issue (during command mapping) |                                                     |
|                                                       | Possible device issue (during parsing)         |                                                     |
|                                                       | Possible device issue (during task mapping)    |                                                     |
|                                                       | Request failed                                 |                                                     |
|                                                       | Result mapping failures (per command)          |                                                     |
|                                                       | Result mapping failures (per task)             |                                                     |
|                                                       | SSH credentials requires username              |                                                     |
|                                                       | Task result mapping failure                    | *tasks/sn Error: Can't find sn for IOS-XR:* missing information, command did not provide the expected result       |
|                                                       | Unknown device version                         |                                                     |
|                                                       | Unspecified command                            |                                                     |
|                                                       | Unsupported device                             | This device is not yet supported by IP Fabric       |
