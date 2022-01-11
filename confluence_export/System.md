# System

## Clear DB

<div>

<div>

### Backup

Before erasing databases, make sure that the [backup](Backup) is
available!

</div>

</div>

In rare cases, it may be necessary to delete and recreate the IP
Fabric's database. Go to ***Settings → Advanced → System ***and click
***Clear DB***.

When running Clear DB, all loaded snapshots are automatically unloaded
and the database recreated.

<div>

<div>

We recommend unloading all your snapshots before running Clear DB.

</div>

</div>

<img src="attachments/102432867/2828599305.png" class="image-center" loading="lazy" data-image-src="attachments/102432867/2828599305.png" data-height="600" data-width="1110" data-unresolved-comment-count="0" data-linked-resource-id="2828599305" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-12-8_15-24-38.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102432867" data-linked-resource-container-version="10" data-media-id="70c042c8-39f3-4cf6-9d40-dc2e887cb8ef" data-media-type="file" />

There is two-way confirmation.

<img src="attachments/102432867/2829352961.png" class="image-center" loading="lazy" data-image-src="attachments/102432867/2829352961.png" data-height="191" data-width="501" data-unresolved-comment-count="0" data-linked-resource-id="2829352961" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-12-8_15-26-3.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102432867" data-linked-resource-container-version="10" data-media-id="944456fe-1dd4-44fa-9b4d-1bdbeb18c59b" data-media-type="file" />

In the second screen, you can choose from clear (reset) everything or
keep settings.

<div>

<div>

We recommend keeping settings.

</div>

</div>

Discovery settings data will be lost and the system setting will be
reset to defaults **except**:

-   Certification authorities

-   [User settings](User_Management)

-   [LDAP settings](LDAP_Authentication)

-   [Custom filters and colors](Navigate_in_Tables)

-   [Custom URL (custom view)](Navigate_in_Tables)

-   Reports settings

-   Dashboard settings

## Certification authorities

By default, the IP Fabric only trusts certificates issued by CAs listed
in the
[nodejs](https://github.com/nodejs/node/blob/master/src/node_root_certs.h). Because
internal systems typically use certificates signed by an internal CA,
the root certificate of this certification authority needs to be
uploaded.

For example, establishing a secure connection between IP Fabric and LDAP
server requires a trusted certificate chain.

**Upload root CA certificate**

1.  Go to ***Settings → Advanced → System → Certification
    Authorities**.*

2.  Click ***Upload CA***.

3.  Enter root CA certificate ***Name*** (it's only your overview)

4.  ***Choose file***

5.  Click ***Save***

**Delete root CA certificate**

1.  Go to ***Settings → Advanced → System → Certification
    Authorities**.*

2.  Select certificate and click ***Delete*** on the right.

3.  Confirm delete using the ***Delete*** button.

**Rename root CA certificate**

1.  Go to ***Settings → Advanced → System → Certification
    Authorities**.*

2.  Select certificate and click ***Edit ***on the right.

3.  Change ***Name***

4.  Click ***Save***

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2021-12-8_15-24-38.png](attachments/102432867/2828599305.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2021-12-8_15-26-3.png](attachments/102432867/2829352961.png)
(image/png)  

</div>
