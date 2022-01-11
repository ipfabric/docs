# 06 - CLI Settings

<img src="attachments/2393473066/2393342011.png" class="image-center" loading="lazy" data-image-src="attachments/2393473066/2393342011.png" data-height="110" data-width="752" data-unresolved-comment-count="0" data-linked-resource-id="2393342011" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210513-232231.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2393473066" data-linked-resource-container-version="3" data-media-id="42d55cb9-d4b6-4a8e-9bfb-980c43156f55" data-media-type="file" />

## Fine-Tune SSH/telnet CLI parameters

The IP Fabric's discovery is primarily using Command Line Interface
(CLI) to discover network elements. There are certain default CLI
parameters that can be found in ***Settings → Advanced → SSH/TELNET:***

<img src="attachments/2393473236/2396258368" class="image-center" loading="lazy" data-image-src="attachments/2393473236/2396258368" data-height="600" data-width="1458" data-unresolved-comment-count="0" data-linked-resource-id="2396258368" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-1-14_15-7-35.png?version=1&amp;modificationDate=1610633257496&amp;cacheVersion=1&amp;api=v2&amp;effects=drop-shadow&amp;height=400" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="2393473236" data-linked-resource-container-version="3" data-media-id="0c3093f3-557a-441d-98cd-fba45b86cd1e" data-media-type="file" />

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

### Example of error message in Connectivity Report

According to the summary of issues in the very first completed snapshot,
the CLI Settings can be adjusted. Here are some of the most common
errors and adjustments:

<div class="table-wrap">

|                                                                                 |                               |                                                                                                                    |
|---------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Error                                                                           | Error Type                    | How to mitigate                                                                                                    |
| connect ETIMEDOUT XX.XX.XX.XX:22                                                | Connection error              | Received no response from the destination.                                                                         |
| connect ECONNREFUSED XX.XX.XX.XX:22                                             | Connection error              | The connection to the destination is being blocked by an access-list or firewall.                                  |
| All configured authentication methods failed                                    | Authentication error          | Unable to authenticate to the destination host                                                                     |
| Authentication failed                                                           | Authentication error          | Unable to authenticate to the destination host                                                                     |
| Authentication failed - login prompt appeared again                             | Authentication error          | Unable to authenticate to the destination host                                                                     |
| SSH client not received any data for last 120000 ms! cmd => show vrrp  \| e #^$ | Command timeout               | The command 'show vrrp  \| e #^$' timed out. Increase **device session timeout.**                                  |
| Can't detect prompt                                                             | Command timeout               | Unable to detect CLI prompt. Increase **network device login timeout.**                                            |
| Command "enable" authorization failed, tried 2x                                 | Command authorization failure | The command wasn't authorized. **Increase command authorization failure retries** or increase the timer value (ms) |

</div>

## Jump host

<div>

<div>

**Jumphost** allows to set-up connection to the server which can be used
as a **proxy server for discovery** purposes. IP Fabric uses an ssh
connection to the jumphost server and python on the client and server
side. Please check the following [requirements for the jumphost
server.](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/13369453/Network+Connectivity+Requirements#Jumphost-server-requirements)

</div>

</div>

<div>

<div>

Please bear in mind, that once the connection is established, it will be
enabled permanently, until disabled or removed! If there are any network
issues, IP Fabric software will try to establish a connection
periodically.

</div>

</div>

<div>

<div>

At least one seed IP address has to be provided as a starting point
behind Jumphost in seed configuration.

</div>

</div>

## Setting up Jump host

1.  Open jump host settings, using item ***Settings → Advanced →
    SSH/TELNET***

2.  At the bottom of the page, please select ***Add*** button

    <img src="attachments/1384841217/1384480773.png" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384480773.png" data-height="285" data-width="1207" data-unresolved-comment-count="0" data-linked-resource-id="1384480773" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-110419.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="10" data-media-id="c0989c3c-d811-429e-b3b8-568c3b91a790" data-media-type="file" />

3.  Fill in all necessary data

    1.  **Label** - the name for configuration (mandatory)

    2.  **Jump host Address** - IP address of FQDN name (mandatory)

    3.  **IPv4 subnets** - subnet in CIDR representation, allows adding
        more than open, separated with spaces (mandatory)

    4.  **Exclude IPv4 subnets** - subnet to exclude in CIDR
        representation, allows to add more than open, separated with
        spaces (optional)

    5.  **Login type**

        1.  **Use credentials** - require to provide username and
            password

        2.  **Use SSH keys** - if you copied ssh public key to the proxy
            server, it won’t require providing a password (please jump
            to the *SSH key configuration* section)

    6.  **Username** - Username for authentication (mandatory)

    7.  **Password** - password for authentication (mandatory if ‘Use
        credentials’ is used)  
          
        i.e., refer to the picture below  

        <img src="attachments/1384841217/1384480780.png?width=408" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384480780.png" data-height="485" data-width="600" data-unresolved-comment-count="0" data-linked-resource-id="1384480780" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-111606.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="10" data-media-id="1cbf974f-1a48-4931-9b07-a0bf4e8dba54" data-media-type="file" width="408" />

4.  Click ***Add*** button

5.  If a connection is open, you will see the ***Running*** status in
    Jumphost list

    <img src="attachments/1384841217/1384513560.png?width=646" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384513560.png" data-height="296" data-width="1210" data-unresolved-comment-count="0" data-linked-resource-id="1384513560" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-111927.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="10" data-media-id="b1a96833-a943-4674-99c1-73640cfaee48" data-media-type="file" width="646" />

<div>

<div>

If you use 0.0.0.0/0 or another subnet that includes your network from
which you are connecting to IP Fabric, make sure you put your network to
***“Exclude IPv4 subnet”***. Otherwise, your IP connection will be lost
and you will have to recover from the console.

</div>

</div>

## SSH key configuration

<div>

<div>

Adding ssh key to proxy server allows you to avoid using passwords for
authentication

</div>

</div>

1.  Download ssh key from Jumphost settings

    <img src="attachments/1384841217/1384153110.png" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384153110.png" data-height="270" data-width="1213" data-unresolved-comment-count="0" data-linked-resource-id="1384153110" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-112330.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="10" data-media-id="4d862cd3-5a13-404f-bdee-f9140a82e860" data-media-type="file" />

2.  Save ***jumphost-public-key.pub***

3.  Copy file content to ***authorized_keys*** file of the user that
    will authenticate with Jumphost server. Please follow official
    [ssh.com](http://ssh.com) documentation
    <https://www.ssh.com/ssh/authorized-key>

4.  Restart **sshd** service to apply settings

5.  If the key has been copied you can use the option *‘Use SSH keys'*
    while adding a new Jumphost server, instead of *'Use credentials’*

## Disabling Jumphost connection

1.  Edit configuration that needs to be disabled, i.e.

    <img src="attachments/1384841217/1384972305.png?width=646" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384972305.png" data-height="346" data-width="1202" data-unresolved-comment-count="0" data-linked-resource-id="1384972305" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-113802.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="10" data-media-id="0371bc71-d5a8-4ee6-88fa-2b6190def421" data-media-type="file" width="646" />

2.  Change the setting to ***Disabled***,

3.  Click the ***Update*** button

    <img src="attachments/1384841217/1384906766.png?width=306" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384906766.png" data-height="523" data-width="600" data-unresolved-comment-count="0" data-linked-resource-id="1384906766" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-113901.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="10" data-media-id="3d5eb7e0-a711-4c22-91dc-19978967853b" data-media-type="file" width="306" />

## Remove Jumphost configuration

1.  On Jumphost servers list, check configuration that needs to be
    removed

2.  Click ***Delete*** button  

    <img src="attachments/1384841217/1384939529.png" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384939529.png" data-height="341" data-width="1208" data-unresolved-comment-count="0" data-linked-resource-id="1384939529" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-114142.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="10" data-media-id="3d876a89-3540-4c62-82b6-4048dc3414ea" data-media-type="file" />

## Discovery with Jumphost issues

<div>

<div>

Only TCP connections work through the Jump host. Traceroute with ICMP is
not supported so the discovery process might not be able to get over the
unreachable part of the network (for example sites separated by the
provider’s network). In this case, you will have to add at least one IP
from each site to the seeds settings.

</div>

</div>

## Custom SSH/Telnet ports

<div>

<div>

Custom SSH/Telnet ports settings enable the discovery process to use
different than standard ports for connecting. The standard for SSH is
port 22 and 23 for Telnet.

</div>

</div>

In the following example we will configure the discovery process to use
port 8080 for SSH connections towards firewall sitting behind
192.168.168.10 IP address:

<img src="attachments/1642790935/1643053081.png" class="image-center" loading="lazy" data-image-src="attachments/1642790935/1643053081.png" data-height="415" data-width="599" data-unresolved-comment-count="0" data-linked-resource-id="1643053081" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20201109-161918.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1642790935" data-linked-resource-container-version="3" data-media-id="dba4f812-a5c3-4323-a86e-03cbc6a5a4fc" data-media-type="file" />

As a result of such configuration, we would create a new item under the
‘Custom SSH/Telnet ports’ configuration, which will be applied to every
new snapshot created by IP Fabric.

<img src="attachments/1642790935/1634435145.png" class="image-center" loading="lazy" data-image-src="attachments/1642790935/1634435145.png" data-height="290" data-width="1214" data-unresolved-comment-count="0" data-linked-resource-id="1634435145" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20201109-162107.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1642790935" data-linked-resource-container-version="3" data-media-id="750fc140-b2f8-46cb-8d13-e2d0a680ce94" data-media-type="file" />

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210513-232231.png](attachments/2393473066/2393342011.png)
(image/png)  

</div>
