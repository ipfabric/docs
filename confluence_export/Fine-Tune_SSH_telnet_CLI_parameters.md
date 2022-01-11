# Fine-Tune SSH/telnet CLI parameters

The IP Fabric's discovery is primarily using Command Line Interface
(CLI) to discover network elements. There are certain default CLI
parameters that can be found in ***Settings → Advanced → SSH/TELNET:***

<img src="attachments/2844262432/2844262446" class="image-center" loading="lazy" data-image-src="attachments/2844262432/2844262446" data-height="600" data-width="1458" data-unresolved-comment-count="0" data-linked-resource-id="2844262446" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-1-14_15-7-35.png?version=1&amp;modificationDate=1610633257496&amp;cacheVersion=1&amp;api=v2&amp;effects=drop-shadow&amp;height=400" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="2844262432" data-linked-resource-container-version="3" data-media-id="672f1954-af13-4194-a4c6-642015e1ff51" data-media-type="file" />

According to the summary of issues in the very first completed snapshot,
the CLI Settings can be adjusted. Here are some of the most common
errors and adjustments:

<div class="table-wrap">

|                                                                                 |                               |                                                                                                                    |
|---------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Error                                                                           | Error Type                    | How to mitigate                                                                                                    |
| connect ETIMEDOUT XX.XX.XX.XX:22                                                | Connection error              | Received no response from the destination.                                                                         |
| connect ECONNREFUSED XX.XX.XX.XX:22                                             | Connection error              | The connection to the destination is being blocked by an access-list or firewall.                                  |
| read ECONNRESET                                                                 | Connection error              | Connection reset by FW or destination                                                                              |
| All configured authentication methods failed                                    | Authentication error          | Unable to authenticate to the destination host                                                                     |
| Authentication failed                                                           | Authentication error          | Unable to authenticate to the destination host                                                                     |
| Authentication failed - login prompt appeared again                             | Authentication error          | Unable to authenticate to the destination host                                                                     |
| SSH client not received any data for last 120000 ms! cmd => show vrrp  \| e #^$ | Command timeout               | The command 'show vrrp  \| e #^$' timed out. Increase **device session timeout.**                                  |
| Can't detect prompt                                                             | Command timeout               | Unable to detect CLI prompt. Increase **network device login timeout.**                                            |
| Command "enable" authorization failed, tried 2x                                 | Command authorization failure | The command wasn't authorized. **Increase command authorization failure retries** or increase the timer value (ms) |

</div>

### Network device login timeout

Timeout before the logging prompt is received. It may take longer for
remote branches over low-speed lines, or destined to overloaded devices.

### Network device session timeout

Too many ***Command Timeout*** errors during the Discovery process may
indicate that ***Network device session timeout*** is too short and it
may be necessary to expect a delay for a response to arrive.

### Maximum number of parallel sessions

To prevent flooding your network with too many SSH/TELNET sessions set
***Maximum number of parallel sessions***. This setting can be also
helpful if the AAA server (TACACS/Radius) has a limit of parallel AAA
requests for users.

In rare cases, the Cisco ISE or similar systems may rate limit the
command authorization. When there are too many authorization failures
and Cisco ISE is in place, try to limit the number of parallel sessions
down to 10 and steadily increase.

### Basic failure

How many times to retry a connection for any error, except
authentication failure.

### Authentication failure

***Authentication failure*** can occur even if a user is authorized to
login but may happen, for example, when an AAA server is overloaded or
an authentication packet is lost.

### Command Authorization Failure retries

If you see many examples of ***Authentication error*** during the
Discovery process, please adjust ***Authentication failure ***and
***Command Authorization Failure retries***.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2021-1-14_15-7-35.png?version=1&modificationDate=1610633257496&cacheVersion=1&api=v2&effects=drop-shadow&height=400](attachments/2844262432/2844262446)
(image/jpeg)  

</div>
