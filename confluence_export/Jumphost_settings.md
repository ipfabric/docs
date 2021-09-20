# Jumphost settings

<div>

<div>

**Jump host** allows to set-up connection to the server which can be
used as a **proxy server for discovery** purposes. For connecting, IP
Fabric uses the ‘sshuttle’ library that has the [following requirements
for the jump
host.](https://sshuttle.readthedocs.io/en/stable/requirements.html#client-side-requirements)

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

    <img src="attachments/1384841217/1384480773.png" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384480773.png" data-height="285" data-width="1207" data-unresolved-comment-count="0" data-linked-resource-id="1384480773" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-110419.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="6" data-media-id="c0989c3c-d811-429e-b3b8-568c3b91a790" data-media-type="file" />

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

        <img src="attachments/1384841217/1384480780.png?width=408" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384480780.png" data-height="485" data-width="600" data-unresolved-comment-count="0" data-linked-resource-id="1384480780" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-111606.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="6" data-media-id="1cbf974f-1a48-4931-9b07-a0bf4e8dba54" data-media-type="file" width="408" />

4.  Click ***Add*** button

5.  If a connection is open, you will see the ***Running*** status in
    Jumphost list

    <img src="attachments/1384841217/1384513560.png?width=646" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384513560.png" data-height="296" data-width="1210" data-unresolved-comment-count="0" data-linked-resource-id="1384513560" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-111927.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="6" data-media-id="b1a96833-a943-4674-99c1-73640cfaee48" data-media-type="file" width="646" />

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

    <img src="attachments/1384841217/1384153110.png" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384153110.png" data-height="270" data-width="1213" data-unresolved-comment-count="0" data-linked-resource-id="1384153110" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-112330.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="6" data-media-id="4d862cd3-5a13-404f-bdee-f9140a82e860" data-media-type="file" />

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

    <img src="attachments/1384841217/1384972305.png?width=646" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384972305.png" data-height="346" data-width="1202" data-unresolved-comment-count="0" data-linked-resource-id="1384972305" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-113802.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="6" data-media-id="0371bc71-d5a8-4ee6-88fa-2b6190def421" data-media-type="file" width="646" />

2.  Change the setting to ***Disabled***,

3.  Click the ***Update*** button

    <img src="attachments/1384841217/1384906766.png?width=306" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384906766.png" data-height="523" data-width="600" data-unresolved-comment-count="0" data-linked-resource-id="1384906766" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-113901.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="6" data-media-id="3d5eb7e0-a711-4c22-91dc-19978967853b" data-media-type="file" width="306" />

## Remove Jumphost configuration

1.  On Jumphost servers list, check configuration that needs to be
    removed

2.  Click ***Delete*** button  

    <img src="attachments/1384841217/1384939529.png" class="image-center" loading="lazy" data-image-src="attachments/1384841217/1384939529.png" data-height="341" data-width="1208" data-unresolved-comment-count="0" data-linked-resource-id="1384939529" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200805-114142.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1384841217" data-linked-resource-container-version="6" data-media-id="3d876a89-3540-4c62-82b6-4048dc3414ea" data-media-type="file" />

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

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200805-110419.png](attachments/1384841217/1384480773.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200805-111606.png](attachments/1384841217/1384480780.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200805-111900.png](attachments/1384841217/1384873994.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200805-111927.png](attachments/1384841217/1384513560.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200805-112330.png](attachments/1384841217/1384153110.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200805-113802.png](attachments/1384841217/1384972305.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200805-113901.png](attachments/1384841217/1384906766.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200805-114142.png](attachments/1384841217/1384939529.png)
(image/png)  

</div>
