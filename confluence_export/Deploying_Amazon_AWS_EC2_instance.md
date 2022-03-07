# Deploying Amazon AWS EC2 instance

## **Deploying IP Fabric AWS EC2 instance**

In order to deploy IP Fabric into your AWS VPC, you will need the AMI to
be shared with the AWS account in question. Contact the [IP Fabric
support team](mailto:support@ipfabric.io) with your AWS account details
and the region in which you want to deploy instance, and the team will
ensure the AMI is available to you to install.  

<div>

<div>

Access to AWS AMI instance is restricted to registered customers only.
Please contact our [sales representative](mailto:sales@ipfabric.io) if
you are interested in a trial of IP Fabric

</div>

</div>

## **Deployment And Configuration Of The AMI**

### Pre-requisites

Before you are begin the deployment, please note the following:

1.  IP Fabric uses SSH, telnet and REST API over http/https in order to
    access network devices and controllers and carry out its discovery.
    Please ensure that the VPC subnet chosen for the deployment has the
    appropriate level of access and routing in order to complete the
    discovery.

2.  The IP Fabric AMI uses SSH for CLI console access, and HTTPS on
    ports 443 and 8443 for Web UI and system console access
    respectively. Security groups will need the appropriate
    configuration to allow inbound access to the AMI.

### Deployment Steps

1.  Login to the AWS console for the account provided to the IP Fabric
    support team.

2.  Select the region for the VPC where you want to deploy IP Fabric:  

    <img src="attachments/2330853377/2331344897.png?width=136" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2331344897.png" data-height="875" data-width="412" data-unresolved-comment-count="0" data-linked-resource-id="2331344897" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210503-155557.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="e84e3b80-5ae6-4027-a5e4-c3e020206e91" data-media-type="file" width="136" />

3.  From the “Services” menu at the top left, select “EC2”

4.  Then choose “Instances” in the left hand menu, and hit the “Launch
    Instances” button on the right:

5.  <img src="attachments/2330853377/2330263561.png" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2330263561.png" data-height="348" data-width="1720" data-unresolved-comment-count="0" data-linked-resource-id="2330263561" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210503-155335.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="675e423e-41eb-4aa0-a5b9-d3aed2c98275" data-media-type="file" />

    Select “My AMIs”, then under “Ownership”, select “Shared with me”.
    The IP Fabric AMI should show up here. “Select” it.

    <img src="attachments/2330853377/2330853393.png?width=646" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2330853393.png" data-height="594" data-width="1702" data-unresolved-comment-count="0" data-linked-resource-id="2330853393" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210503-155929.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="92de7ca5-ecb9-488f-8c27-c697e4999d93" data-media-type="file" width="646" />

6.  Choose the most appropriate instance type:

<div class="table-wrap">

|         |     |        |                                      |                           |
|---------|-----|--------|--------------------------------------|---------------------------|
| Devices | CPU | RAM    | HDD (will need to be set in step #8) | Example EC2 Instance Type |
| 500     | 4   | 16 GB  | 90 GB                                | c5.2xlarge                |
| 1 000   | 4   | 32 GB  | 100 GB                               | r5.xlarge                 |
| 2 000   | 8   | 64 GB  | 200 GB                               | r5.2xlarge                |
| 5 000   | 12  | 64 GB  | 300 GB                               | r5.2xlarge or r5.4xlarge  |
| 10 000  | 16  | 128 GB | 550 GB                               | r5.4xlarge                |
| 20 000  | 18  | 256 GB | 1000 GB                              | r5.8xlarge                |

</div>

<div>

<div>

Since AWS is often changing/adding instance types and their resources,
please follow this table when determining correct EC2 instace type [Host
Hardware Requirements](Host_Hardware_Requirements)

</div>

</div>

<div>

<div>

Selecting an appropriate instance type is necessary to achieve a stable
and reliable system! Please double-check if your Instance settings are
proper for your environment size.

</div>

</div>

7\. Select “Configure Instance Details”, then ensure the correct VPC and
subnet are selected for the IP Fabric instance. (Create a new VPC and
subnet if required):

<img src="attachments/2330853377/2329477143.png" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2329477143.png" data-height="1243" data-width="1715" data-unresolved-comment-count="0" data-linked-resource-id="2329477143" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210503-164356.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="67a19fe9-74b5-4a55-b514-93d58cd3dc58" data-media-type="file" />

8\. Then select “Add Storage”, add 80G to the additional amount from the
table above for the root volume:

For example, the instance **c5.4xlarge** should have 200G in total.

<img src="attachments/2330853377/2384429057.png" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2384429057.png" data-height="239" data-width="1447" data-unresolved-comment-count="0" data-linked-resource-id="2384429057" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210512-113147.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="6831a984-7ea7-487c-8249-ff048ab73cf2" data-media-type="file" />

9\. Select “Edit Security Groups” to make sure that IP Fabric will have
the connectivity it requires to function:

<img src="attachments/2330853377/2329477151.png" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2329477151.png" data-height="211" data-width="1545" data-unresolved-comment-count="0" data-linked-resource-id="2329477151" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210503-164622.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="00d7f011-26b1-4828-a890-563a1464475c" data-media-type="file" />

10\. Confirm the details with the [IP Fabric Connectivity
Requirements](Network_Connectivity_Requirements). The security group
rules should look something like:

<img src="attachments/2330853377/2331475973.png" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2331475973.png" data-height="448" data-width="1710" data-unresolved-comment-count="0" data-linked-resource-id="2331475973" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210503-165522.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="ee5f935f-0f87-46ef-9166-ff6b06ca182e" data-media-type="file" />

<div>

<div>

Note that you can only select incoming rules at this point! By default
the security group allows access to everything over any protocol and
port: you will need to revisit once the instance has launched if you
need to restrict access at source.

</div>

</div>

11\. Click “Review and Launch”

12\. At this point, if you never used Debian in AWS before, subscription
alert can appear. If requires, please follow instruction and open
hyperlink in Error message: “In order to user this AWS Marketplace
product….“

<img src="attachments/2330853377/2331475983.png" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2331475983.png" data-height="256" data-width="1865" data-unresolved-comment-count="0" data-linked-resource-id="2331475983" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200424-090801.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="fbf24844-c2d2-4125-afce-1207905c0f6e" data-media-type="file" />

13\. On new page, please click “Continue to Subscribe”

<img src="attachments/2330853377/2331475989.png?width=306" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2331475989.png" data-height="694" data-width="839" data-unresolved-comment-count="0" data-linked-resource-id="2331475989" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200424-090959.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="d4885ed0-daf2-4c78-af75-3cd5b7580013" data-media-type="file" width="306" />

14\. When done, please click “Launch” button once again.

15\. Please confirm “Key pair” information and click “Launch
Instance”*.*

<img src="attachments/2330853377/2331475995.png?width=306" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2331475995.png" data-height="436" data-width="702" data-unresolved-comment-count="0" data-linked-resource-id="2331475995" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200424-091325.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="c115a774-b1b4-4555-b6ea-12c8c57228fe" data-media-type="file" width="306" />

16\. Your Instance will appear in the instances list, and it will be
started automatically by AWS:

<img src="attachments/2330853377/2330820622.png" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2330820622.png" data-height="1061" data-width="1450" data-unresolved-comment-count="0" data-linked-resource-id="2330820622" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210503-170900.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="4fc71edf-b16f-4d3e-bc99-46eada6eace2" data-media-type="file" />

17\. You can now [access the Web UI, install the license
file](Access_User_Interface_and_Install_License) and login to the
instance to run the Configuration Wizard.

18\. There is a bug in the latest version and you will need to setup
traceroute in the IPFabric in order to run Discovery. Traceroute must be
setup to - [127.0.0.1/32](http://127.0.0.1/32)

This is going to be fixed in the future.

<img src="attachments/2330853377/2390327358.png" class="image-center" loading="lazy" data-image-src="attachments/2330853377/2390327358.png" data-height="261" data-width="1884" data-unresolved-comment-count="0" data-linked-resource-id="2390327358" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210513-133152.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2330853377" data-linked-resource-container-version="10" data-media-id="e10927d9-9e26-4581-92f0-56e9013148c6" data-media-type="file" />

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200424-084219.png](attachments/2330853377/2329772052.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210503-155335.png](attachments/2330853377/2330263561.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210503-155557.png](attachments/2330853377/2331344897.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210503-155929.png](attachments/2330853377/2330853393.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210503-164356.png](attachments/2330853377/2329477143.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210503-164622.png](attachments/2330853377/2329477151.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210503-165522.png](attachments/2330853377/2331475973.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200424-090801.png](attachments/2330853377/2331475983.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200424-090959.png](attachments/2330853377/2331475989.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200424-091325.png](attachments/2330853377/2331475995.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210503-170900.png](attachments/2330853377/2330820622.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210503-175503.png](attachments/2330853377/2330820636.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210512-113147.png](attachments/2330853377/2384429057.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210513-133152.png](attachments/2330853377/2390327358.png)
(image/png)  

</div>
