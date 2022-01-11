# Required permissions for successful discovery over CLI

<img src="attachments/2783641601/2783739907.png?width=340" class="image-wrap-right" loading="lazy" data-image-src="attachments/2783641601/2783739907.png" data-height="548" data-width="678" data-unresolved-comment-count="0" data-linked-resource-id="2783739907" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="ckp-rba.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2783641601" data-linked-resource-container-version="7" data-media-id="94c4fd1e-f557-4196-98b0-f43e05ab7f1d" data-media-type="file" width="340" />

To successfully discover a CheckPoint Gateway, correct role have to be
assigned to a user. IPF requires role features set as read-only, except
of “Virtual-System“ where read-write is needed (only if VSX firewalls
are in your network, otherwise read-only is enough).

### How to setup a role from web GUI

1.  Open CheckPoint Gaia web interface

2.  Navigate to User Management > Roles in the left menu

3.  Click Add, fill in the name. In the Features tab select all items
    and mark them as “Read-Only“. No permissions from “Extended
    Commands“ tab are needed\*.

4.  If you have VSX firewall in your network, you have to set
    “Virtual-System“ feature to “Read-Write“ (we call “set
    virtual-system \<ID>“ to switch to proper virtual system). This
    allows IPF just to change context and can’t be used for anything
    else.

5.  Assign the role to the user used for IPF discovery

\* Currently, not all the features are needed for IPF. But as we will
add support of new features, it can change. List of currently required
features for minimal working setup (IPF 4.0, Gaia R81): *Advanced VRRP,
ARP, BGP, Cluster, Display Configuration, Domain Name, Host Name,
Management Interface, Netflow Export, Network Interfaces, Network
Management, NTP, OSPF, Route, Routing Monitor, SNMP, System
Configuration, Virtual-System, VRRP, VSX*

Find the list of features with corresponding commands in the official
CheckPoint documentation:
<https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_Gaia_AdminGuide/Topics-GAG/Roles-Available-Features.htm?tocpath=User%20Management%7CRoles%7C_____3>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ckp-rba.png](attachments/2783641601/2784264193.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ckp-rba.png](attachments/2783641601/2783739907.png) (image/png)  

</div>
