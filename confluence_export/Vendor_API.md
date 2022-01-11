# Vendor API

## Meraki API

Starting the version 3.5.0, IP Fabric supports API based discovery for
Cisco Meraki.

Meraki requires the following settings to be applied:

-   API key - Generated in [Meraki
    dashboard](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API)

-   Organizations ID - You can specify which organization will be
    included in the discovery process. If you do not specify, all
    available IDs will be used

-   Version - Meraki currently provides only a v0 version of their API.
    This version has a lot of limitations ([Meraki known
    issues](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/968032257/Meraki))

-   Base URL - URL is supported in the following
    format [https://nXYZ.meraki.com/api.](https://nXYZ.meraki.com/api) Be
    aware that the dashboard can redirect communication to a different
    URL

## CheckPoint API

<div>

<div>

We use API only to collect information that cannot be retrieved from CLI
logs.

To discover CheckPoint devices, CLI access also needs to be available.

</div>

</div>

Checkpoint requires the following settings to be applied:

-   API Key - Available in version R80.40 and above (API v1.6). To
    generate the key, use CheckPoint SmartConsole, and select "API Key"
    as user's Authentication method  
    **or**

-   Username - Username to access API data

-   Password - Password to access API data  

-   Base URL - Base URL for API calls
    (ie: [https://management.server.domain.tld).](https://management.server.domain.tld) If
    the API isn't available on the default port 443, add a port part to
    the URL (ie: <https://server:4443/>)

-   Collect following domains - Mandatory only if the "Base URL" points
    to a Multi-Domain Server. Please verify, that all selected domains
    can be accessed by the provided credentials.  

Don't forget to add IPF appliance to the list of allowed clients. In
SmartConsole, go to Manage & Settings \> Blades and click on "Advanced
Settings..." in the “Management API“ section to verify, from where are
API calls allowed. In case that you use setting "All IP addresses that
can be used for GUI clients", don't forget to add IPF appliance address
to Manage & Settings \> Permissions & Administrators \> Trusted Clients.
In case you use Multi-Domain server, all necessary settings are in Multi
Domain menu (ie: Multi Domain \> Blades)

## VERSA API

Starting version 3.8.0 IP Fabric supports Versa SD-WAN API. API is based
on HTTPS authentication. Versa requires the following settings to be
applied:

-   Username - Username to Versa Director to access API data

-   Password - Password to Versa Director access API data

-   Base URL - Base URL of Versa Director. If the API isn't available on
    the default port 9182, add a port part to the URL (ie:
    <https://server:4443/>)

<div>

<div>

OAuth authentication credentials to Versa Director are not supported at
the moment to access API  

</div>

</div>

## AWS (Amazon Web Services) API

Starting version 3.8.0 IP Fabric supports AWS API.

To add AWS to the discovery you will need an access key & secret access
key from your AWS account.

Those keys can be found/generated under your account in the AWS
dashboard.

<img src="attachments/2691563521/2691596295.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596295.png" data-height="345" data-width="1676" data-unresolved-comment-count="0" data-linked-resource-id="2691596295" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (8).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="7" data-media-id="e1a158d2-3d1b-41b0-9ffe-ccecea18f047" data-media-type="file" width="340" />

Click on “My Security Credentials” and open “Access keys” tab.

<img src="attachments/2691563521/2691596301.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596301.png" data-height="756" data-width="1694" data-unresolved-comment-count="0" data-linked-resource-id="2691596301" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (10).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="7" data-media-id="d120ae20-ebe5-4241-b2e5-42728b98f30b" data-media-type="file" width="340" />

To generate keys click on “Create New Access Key” and your keys will be
generated. These access keys are available globally for all of yours AWS
regions.

<img src="attachments/2691563521/2691596307.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596307.png" data-height="673" data-width="1679" data-unresolved-comment-count="0" data-linked-resource-id="2691596307" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (11).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="7" data-media-id="28eaf95c-1d5f-4667-aae3-d9ce15b24932" data-media-type="file" width="340" />

Copy those keys to the AWS API settings in your IP Fabric and don't
forget to **fill the region where the devices which you want to discover
are**.

<img src="attachments/2691563521/2691596313.png" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596313.png" data-height="290" data-width="401" data-unresolved-comment-count="0" data-linked-resource-id="2691596313" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2021-05-04 165124.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="7" data-media-id="f6c00564-395f-4a9a-b509-b54f718cf3b5" data-media-type="file" />

<div>

<div>

To ensure that IP Fabric can retrieve all the required data to model the
AWS networks, a series of specific policies are required to be applied
to the user account or role used for the API key. The attached file
contains a JSON description of the required IAM policies:

</div>

</div>

[<img src="attachments/thumbnails/2691563521/2691399704" height="250" />](attachments/2691563521/2691399704.json)

## Viptela API

Starting version 4.1.0 IP Fabric supports Viptela API.

Viptela devices are discovered only through API.

To add Viptela to discovery global settings, go to **Settings → Advanced
→ Vendors API** and press **+Add** button

<img src="attachments/2809626625/2809888769.png?width=204" class="image-center" loading="lazy" data-image-src="attachments/2809626625/2809888769.png" data-height="829" data-width="1248" data-unresolved-comment-count="0" data-linked-resource-id="2809888769" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20211118-105748.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2809626625" data-linked-resource-container-version="5" data-media-id="de93a3da-5924-47c0-8dde-aa2989f36dce" data-media-type="file" width="204" />

Afterwards, choose Viptela API from the list and fill in

-   **Username and password** used to log in to vManage

-   **Base URL** of vManage server (https://vmanage-ip-address)

<img src="attachments/2809626625/2809954305.png" class="image-center" loading="lazy" data-image-src="attachments/2809626625/2809954305.png" data-height="402" data-width="601" data-unresolved-comment-count="0" data-linked-resource-id="2809954305" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20211118-111744.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2809626625" data-linked-resource-container-version="5" data-media-id="02b21588-b923-430b-b57a-3c35073f88cb" data-media-type="file" />

  

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[mds-user.png](attachments/1005649930/1646329857.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Screenshot 2021-05-04
165124.png](attachments/1005649930/2336817155.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [image
(8).png](attachments/1005649930/2336915465.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [image
(10).png](attachments/1005649930/2336849923.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [image
(11).png](attachments/1005649930/2336915471.png) (image/png)  

</div>
