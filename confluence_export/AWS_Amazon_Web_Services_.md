# AWS (Amazon Web Services)

# AWS (Amazon Web Services)

Starting version 3.8.0 IP Fabric supports AWS API.

To add AWS to the discovery you will need an access key & secret access
key from your AWS account.

Those keys can be found/generated under your account in the AWS
dashboard.

<img src="attachments/2691563521/2691596295.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596295.png" data-height="345" data-width="1676" data-unresolved-comment-count="0" data-linked-resource-id="2691596295" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (8).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="e1a158d2-3d1b-41b0-9ffe-ccecea18f047" data-media-type="file" width="340" />

Click on “My Security Credentials” and open “Access keys” tab.

<img src="attachments/2691563521/2691596301.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596301.png" data-height="756" data-width="1694" data-unresolved-comment-count="0" data-linked-resource-id="2691596301" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (10).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="d120ae20-ebe5-4241-b2e5-42728b98f30b" data-media-type="file" width="340" />

To generate keys click on “Create New Access Key” and your keys will be
generated. These access keys are available globally for all of yours AWS
regions.

<img src="attachments/2691563521/2691596307.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596307.png" data-height="673" data-width="1679" data-unresolved-comment-count="0" data-linked-resource-id="2691596307" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (11).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="28eaf95c-1d5f-4667-aae3-d9ce15b24932" data-media-type="file" width="340" />

Copy those keys to the AWS API settings in your IP Fabric and don't
forget to **fill the region where the devices which you want to discover
are**.

<img src="attachments/2691563521/2691596313.png" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596313.png" data-height="290" data-width="401" data-unresolved-comment-count="0" data-linked-resource-id="2691596313" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2021-05-04 165124.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="f6c00564-395f-4a9a-b509-b54f718cf3b5" data-media-type="file" />

<div>

<div>

To ensure that IP Fabric can retrieve all the required data to model the
AWS networks, a series of specific policies are required to be applied
to the user account or role used for the API key. The attached file
contains a JSON description of the required IAM policies:

</div>

</div>

[<img src="attachments/thumbnails/2691563521/2691399704" height="250" />](attachments/2691563521/2691399704.json)

# AWS AssumeRole

From version 4.3, IP Fabric enables you to add AssumeRole to AWS API
configuration. AssumeRole basically sets higher permissions that may be
required for the discovery process in some environments.

AssumeRole is a standard way how to obtain additional rights when
talking to AWS API. It returns a set of temporary security credentials
that you can use to access AWS resources that you might not normally
have access to. These temporary credentials consist of an access key ID,
a secret access key, and a security token. Typically, you use
`AssumeRole` within your account or for cross-account access. For more
information about AssumeRole see
<https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html>

<img src="attachments/2691563521/2913828865.png" class="image-center" loading="lazy" data-image-src="attachments/2691563521/2913828865.png" data-height="537" data-width="603" data-unresolved-comment-count="0" data-linked-resource-id="2913828865" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Snímek obrazovky 2022-03-02 v 14.54.49.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="e41e6a4a-875d-49b0-b2a4-5a21b2408167" data-media-type="file" />

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [image
(8).png](attachments/2691563521/2691596295.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [image
(10).png](attachments/2691563521/2691596301.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [image
(11).png](attachments/2691563521/2691596307.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Screenshot 2021-05-04
165124.png](attachments/2691563521/2691596313.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ipf_aws_iam_policy.json](attachments/2691563521/2691399704.json)
(application/json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [Snímek
obrazovky 2022-03-02
v 14.54.49.png](attachments/2691563521/2913828865.png) (image/png)  

</div>
