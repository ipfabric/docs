# Authentication

# Authentication

Platform interacts with the network infrastructure devices by running
show commands through CLI using SSH or Telnet. Credentials added in the
Authentication section will be used by IP Fabric to access the CLI of
the network devices.

## Credential Selection Logic

If more credentials are specified, a top-down algorithm is used when
trying to login to a network device or the credentials priority can be
changed using drag and drop.  

<img src="attachments/1934983169/1934983181.jpg" class="image-left" loading="lazy" data-image-src="attachments/1934983169/1934983181.jpg" data-height="474" data-width="737" data-unresolved-comment-count="0" data-linked-resource-id="1934983181" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="NIMPEE-login-diagram.jpg" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="1934983169" data-linked-resource-container-version="3" data-media-id="a1cac42b-ca9b-4725-aebd-2c776ed12181" data-media-type="file" />

## Configure Network Infrastructure Access

Read-only (Privilege 1) credentials are sufficient for basic
functionality. Security sensitive operations and advanced functionality
might require higher privilege. See the [full list of used command in
the documentation](Used_CLI_commands_for_Discovery).

When adding new credentials, you can limit the validity of the
credentials just for a part of your network using *Use in subnets*
and *Don't use in subnets* fields.

<img src="attachments/1934983169/1935310852.png?width=142" class="image-left" loading="lazy" data-image-src="attachments/1934983169/1935310852.png" data-height="531" data-width="600" data-unresolved-comment-count="0" data-linked-resource-id="1935310852" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-1-29_10-58-46.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1934983169" data-linked-resource-container-version="3" data-media-id="319548af-0d3e-4faa-95e3-935203112205" data-media-type="file" width="142" />

Provided credentials can be used for configuration change tracking and
saved configuration consistency (i.e. they allow commands such as *show
run* and *show start*).

To use this credentials for configuration change tracking,
please check [*Use for configuration management*](Configuration)* *box.

## (Optional) Passwords for enable mode

Privileged credentials are generally only necessary for configuration
management. However, some platforms require privileged credentials to
access basic network state information, such as MST spanning-tree state
or 802.1X session information.

<img src="attachments/1934983169/1935245322.png?width=680" class="image-left" loading="lazy" data-image-src="attachments/1934983169/1935245322.png" data-height="272" data-width="1526" data-unresolved-comment-count="0" data-linked-resource-id="1935245322" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-1-29_12-19-25.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1934983169" data-linked-resource-container-version="3" data-media-id="ff9cd67c-09e6-40f2-b6a9-3e301f30cad8" data-media-type="file" width="680" />

  

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[NIMPEE-login-diagram.jpg](attachments/1934983169/1934983181.jpg)
(image/jpeg)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-07-24 11_44_15-Authentication - IP Fabric network infrastructure
controller - IPFabric.png](attachments/1934983169/1934983184.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-07-24 11_43_58-Authentication - IP Fabric network infrastructure
controller - IPFabric.png](attachments/1934983169/1934983187.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2021-1-29_10-56-25.png](attachments/1934983169/1934950402.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2021-1-29_10-58-46.png](attachments/1934983169/1935310852.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2021-1-29_12-19-25.png](attachments/1934983169/1935245322.png)
(image/png)  

</div>
