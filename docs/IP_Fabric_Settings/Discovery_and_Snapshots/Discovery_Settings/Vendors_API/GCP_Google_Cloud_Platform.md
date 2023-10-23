---
description: In order to add GCP to discovery, you will need an access to private key for your GCP service account.
---

# Google Cloud Platform (GCP)

## Generate a private key for your GCP service account

1. Select a project that you want to create a service account for:

   ![Select a project](gcp/selectAProject.png)

2. Navigate to **IAM & Admin --> Service Accounts**:

   ![Navigate to Service Accounts](gcp/gcpSideBarServiceAccount.png)

3. Click **+ CREATE SERVICE ACCOUNT**:

   ![Create a service account](gcp/createAServiceAccount.png)

4. Give it a name and click **CREATE AND CONTINUE**:

   ![Service account details](gcp/giveAServiceAccountName.png)

5. Select a role for the account. We recommend to use the `Viewer` role as it
   gives only read access to the project. Afterwards, click **CONTINUE**.

   ![Grant this service account access to project](gcp/selectAViewRole.png)

6. In the last step, just click **DONE**:

   ![Grant users access to this service account](gcp/finishAccountCreation.png)

7. Search for the account that was just created and select it:

   ![Select the account](gcp/selectTheCreateAccount.png)

8. Navigate to the **KEYS** tab, click **ADD KEY** and select `Create new key`.
   (You can use your own key, but the properties have to be the same as when you
   generate it. So it is highly recommended to use the `Create new key` option.)

   ![Create a new private key](gcp/selectToCreateANewKey.png)

9. The key type we support is `JSON`. Click **CREATE** and the private key will
   be downloaded to your computer.

   ![Generate a JSON key](gcp/selectJsonKey.png)

## Load the `JSON` key to IP Fabric

1. In the IP Fabric GUI, navigate to **Settings --> Discovery & Snapshots -->
   Discovery Settings --> Vendors API** and click **+ Add**:

   ![Vendors API](gcp/addingNewVendor.png)

2. Select `Google Cloud Platform` from the list.

3. Move your key to the Drag&Drop area or select it from your computer. And
   enter the other required information.

   ![Add Connection](gcp/loadingKeyFile.png)
