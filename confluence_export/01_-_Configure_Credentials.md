# 01 - Configure Credentials

## Configure Credentials

Network infrastructure credentials are stored in ***Settings
→ Authentication**.* These credentials use IP Fabric to access the CLI
of the network devices. Read-only (privilege level 1) credentials are
sufficient for the discovery.

<img src="attachments/2251457025/2390327297.png" class="image-center" loading="lazy" data-image-src="attachments/2251457025/2390327297.png" data-height="280" data-width="884" data-unresolved-comment-count="0" data-linked-resource-id="2390327297" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210513-101959.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2251457025" data-linked-resource-container-version="6" data-media-id="13a8056e-83c6-4fee-b0d6-2e04f328e3f3" data-media-type="file" />

If credentials are provided for configuration changes tracking and saved
configuration consistency (i.e. they allow commands such as show
run and show start), mark this set of credentials using the
checkbox [Use for configuration management](Configuration). 

<img src="attachments/2251457025/2390163472.png" class="image-center" loading="lazy" data-image-src="attachments/2251457025/2390163472.png" data-height="270" data-width="659" data-unresolved-comment-count="0" data-linked-resource-id="2390163472" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210513-103307.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2251457025" data-linked-resource-container-version="6" data-media-id="baee854e-0f7c-4948-a59d-3ac6722768cc" data-media-type="file" />

You can limit the validity of the credentials just for a part of your
network by ***Use in subnet*** field. If more credentials are specified,
a top-down algorithm is used when trying to login into a network device
or the credentials priority can be changed using drag and drop.

<img src="attachments/2251457025/2251457047.jpg?width=204" class="image-center" loading="lazy" data-image-src="attachments/2251457025/2251457047.jpg" data-height="474" data-width="737" data-unresolved-comment-count="0" data-linked-resource-id="2251457047" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="NIMPEE-login-diagram.jpg" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="2251457025" data-linked-resource-container-version="6" data-media-id="799a65a1-0c9a-4b39-91d0-70d8d8525324" data-media-type="file" width="204" />

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210401-072201.png](attachments/2251457025/2251457044.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[NIMPEE-login-diagram.jpg](attachments/2251457025/2251457047.jpg)
(image/jpeg)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-07-24 11_44_15-Authentication - IP Fabric network infrastructure
controller - IPFabric.png](attachments/2251457025/2251457050.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-07-24 11_43_58-Authentication - IP Fabric network infrastructure
controller - IPFabric.png](attachments/2251457025/2251457053.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210513-101959.png](attachments/2251457025/2390327297.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210513-103307.png](attachments/2251457025/2390163472.png)
(image/png)  

</div>
