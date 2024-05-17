---
description: This section contains information on how to set up API discovery for GCP.
---

# Google Cloud Platform (GCP)

## Generate a Private Key for Your GCP Service Account

1. Select a project for which you want to create a service account:

   ![Select a project](gcp/selectAProject.png)

2. Navigate to **IAM & Admin --> Service Accounts**:

   ![Navigate to Service Accounts](gcp/gcpSideBarServiceAccount.png)

3. Click **+ CREATE SERVICE ACCOUNT**:

   ![Create a service account](gcp/createAServiceAccount.png)

4. Give it a name and click **CREATE AND CONTINUE**:

   ![Service account details](gcp/giveAServiceAccountName.png)

5. Select a role for the account. We recommend using the `Viewer` role as it
   provides only read access to the project. Then, click **CONTINUE**.

   ![Grant this service account access to project](gcp/selectAViewRole.png)

6. In the last step, simply click **DONE**:

   ![Grant users access to this service account](gcp/finishAccountCreation.png)

7. Search for the account that was just created and select it:

   ![Select the account](gcp/selectTheCreateAccount.png)

8. Navigate to the **KEYS** tab, click **ADD KEY**, and select `Create new key`.
   (You can use your own key, but the properties must be the same as when you
   generate it. Therefore, it is highly recommended to use the `Create new key` option.)

   ![Create a new private key](gcp/selectToCreateANewKey.png)

9. The key type we support is `JSON`. Click **CREATE**, and the private key will
   be downloaded to your computer.

   ![Generate a JSON key](gcp/selectJsonKey.png)

## Load the `JSON` Key to IP Fabric

1. In the IP Fabric GUI, navigate to **Settings --> Discovery & Snapshots -->
   Discovery Settings --> Vendors API**, and click **+ Add**:

   ![Vendors API - Add](gcp/addingNewVendor.png)

2. Select `Google Cloud Platform` from the list.

3. Move your key to the Drag&Drop area or select it from your computer, and
   enter the other required information:

   ![Add Connection - Google Cloud Platform](gcp/loadingKeyFile.png)
