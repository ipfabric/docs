---
description: This page describes how to generate and download a techsupport file via the API.
---

# Generate and Download Techsupport File via API

To generate and download a [techsupport](../support/techsupport.md) file via the
API, follow these steps:

1. Send a POST request to `/os/techsupport`. The information to include in the
   techsupport file is specified in the request body. In the example below, the
   default options from the GUI (system and service logs, usage data, and a
   specific snapshot `SNAPSHOT_ID` with its database records) are shown.

   ```json
   {
     "databases": false,
     "discoveryServicesLogs": true,
     "snapshot": {
       "backupDb": true,
       "id": "SNAPSHOT_ID",
       "removeCli": false
     },
     "systemLogs": true,
     "usageData": true
   }
   ```

2. Obtain the list of jobs by sending a POST request to `/tables/jobs`. It is
   necessary to include an array that specifies the desired columns.

   ```json
   {
     "columns": [
       "downloadFile",
       "id",
       "isDone",
       "status"
     ]
   }
   ```

   While the techsupport file is being generated, there will be a job with
   `running` status:

   ```json
   {
     "data": [
       {
         "downloadFile": null,
         "id": "YOUR_JOB_ID",
         "isDone": false,
         "status": "running"
       },
     ],
   }
   ```

   Once it is generated, the `downloadFile` key will have the file location as
   its value.

   ```json
   {
     "data": [
       {
         "downloadFile": "/home/autoboss/files/techsupport-YOUR_JOB_ID.tar",
         "id": "YOUR_JOB_ID",
         "isDone": true,
         "status": "done"
       }
     ]
   }
   ```

3. Download the techsupport file by sending a GET request to
   `/jobs/YOUR_JOB_ID/download`.
