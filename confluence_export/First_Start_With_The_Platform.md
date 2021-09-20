# First Start With The Platform

# Overview

IP Fabric is distributed as a single self-contained virtual machine.
Distribution links contain current versions of the VM image files for
the initial deployments and also update files offline for existing IP
Fabric deployments (only versions 2.2.0 onward). The image files and the
license file (distributed via a separate channel) are necessary to
successfully complete the first start. Read-only network credentials are
necessary to complete the first network discovery and analysis.

## Deploy and configure VM

<div>

Supported hypervisors

<div>

**VMware vSphere**, **Hyper-V**, **Nutanix** and **KVM** are the only
supported platforms.  
For vShpere, please follow these instructions [Deploying VMware OVA
Virtual
Machine](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/901808145/Deploying+VMware+OVA+Virtual+Machine)  
For HyperV, please follow these instructions [Deploying Hyper-V Virtual
Machine](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/899285029/Deploying+Hyper-V+Virtual+Machine)  
For Nutanix, please follow these instructions [Deploying Nutanix Virtual
Machine](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/899317804/Deploying+Nutanix+Virtual+Machine)  
For KVM, please follow these instructions [Deploying KVM Virtual
Machine](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/1879081063/Deploying+KVM+Virtual+Machine)  
For AWS EC2 Instance, please follow these instructions [Deploying Amazon
AWS EC2
instance](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/2330853377/Deploying+Amazon+AWS+EC2+instance)

</div>

</div>

Please follow the instructions available above as separate sub-topics
regarding VM's deployment. Instructions cover deployment and the First
Boot Wizard Configuration

## Access User Interface and Install License

Type IP Fabric VM's address into a web browser and allow HTTPS
exceptions in case of a warning.

<div>

<div>

### Trusted certificate

A trusted certificate can replace a self-signed SSL certificate using a
web UI.

</div>

</div>

The system requires a license file that uniquely identifies the system
and links it to the dedicated support channels. Keep the license file
safe, as the license file is also used as part of the key to encrypt
sensitive information. Drag the license.key file into the web interface,
or click “Select file” and browse to the license file. If the license
installation fails, contact the IP Fabric support team.

<img src="attachments/79036476/2393505983.png?width=272" class="image-left" loading="lazy" data-image-src="attachments/79036476/2393505983.png" data-height="430" data-width="843" data-unresolved-comment-count="0" data-linked-resource-id="2393505983" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210420-104930.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79036476" data-linked-resource-container-version="15" data-media-id="866f1b0d-e2fa-4ce1-be31-4e0e05e448db" data-media-type="file" width="272" />

Once the license is valid, the system will present a login screen. The
default system username is **admin** and the password is
**netHero!123**. The admin account can be used as a regular account to
run the system or to create and manage other users.

<img src="attachments/79036476/2393505990.png?width=170" class="image-left" loading="lazy" data-image-src="attachments/79036476/2393505990.png" data-height="422" data-width="779" data-unresolved-comment-count="0" data-linked-resource-id="2393505990" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210420-105220.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79036476" data-linked-resource-container-version="15" data-media-id="5dd62855-39fd-41c6-b486-88943db7e2f0" data-media-type="file" width="170" />

<div>

<div>

### Invalid default admin credentials

For an unknown reason, it might happen that on the first start-up
default system username and password are not working. To fix this issue,
please login to the System administration on an
address [https://ipfabric.example.com:8443](https://ipfabric.company.com:8443) and
after login as **osadmin** user go to ***Create admin*** and create a
new local administrator account. With this new account, you can login to
the main IP Fabric user interface and change a password to the default
admin account or delete him. See [Create Local
Administrator](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/1899790374/Create+Local+Administrator)
page.

</div>

</div>

## Setup Wizard

After login in for the first time, you will be presented with the
Configuration Wizard. This will guide you throughout the initial setup,
in order to start the first discovery.

<img src="attachments/2390130689/2390130696.png" class="image-center" loading="lazy" data-image-src="attachments/2390130689/2390130696.png" data-height="326" data-width="899" data-unresolved-comment-count="0" data-linked-resource-id="2390130696" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210513-101646.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2390130689" data-linked-resource-container-version="8" data-media-id="12e97fa3-a699-4a24-b69f-e218d214c1c4" data-media-type="file" />

## Run initial discovery

<div>

<div>

Now that you have entered the essential details, you can start the
discovery!

</div>

</div>

### Option 1 - via the Setup Wizard

If you haven’t yet, you can click on **Start Discovery** from [Step 11
of the Setup
Wizard](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/2396389388/11+-+Configuration+Complete).

### Option 2 - via the Discovery Snapshot page

From the “Discovery Snapshot” page, click on ***+ New snapshot*** and
start the discovery:

<img src="attachments/79167531/2393506082.png?width=340" class="image-center" loading="lazy" data-image-src="attachments/79167531/2393506082.png" data-height="263" data-width="1095" data-unresolved-comment-count="0" data-linked-resource-id="2393506082" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210421-080636.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79167531" data-linked-resource-container-version="11" data-media-id="36645449-9b04-4738-b988-b832a7fc5fdb" data-media-type="file" width="340" />

IP Fabric will attempt to connect to the default gateway of the VM and
any provided Seed IP Addresses. Once connected to a device, IP Fabric
will fingerprint the vendor, model, and version, and adjust accordingly
to run the necessary commands as per the [Used
Commands](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/80019486/Used+CLI+commands+for+Discovery)
list.

After the discovery is completed, all of the state data is available in
structured [Technology
tables](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/79069282/Technology+Tables),
[Diagrams](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/78872710),
a [MS Word Document
Reports](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/79265870/Reports),
or through API. Technology tables can be colored for specific
[verification or
reporting](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/79102058/Technology+verification+and+analysis)
using the ![Colorize
columns](plugins/servlet/confluence/placeholder/unknown-attachment "image2018-7-27_14-39-31.png") button
on the table heading row, which can then be displayed in a
[dashboard](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/79233065/Dashboard). At
least two discovery runs are required to compare changes or to see rates
and the delta counter data.

**Enjoy using IP Fabric!**

If [no devices are
discovered](https://ipfabric.atlassian.net/wiki/spaces/NK/pages/79986690/No+devices+discovered),
or something is missing, check the [knowledge
base](https://kb.ipfabric.io) for known cases or [contact
support](https://ipfabric.atlassian.net/servicedesk/customer/portals).
