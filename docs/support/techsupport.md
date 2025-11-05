---
description: This page explains how to generate and upload a techsupport file for troubleshooting your IP Fabric appliance by our teams. The page also describes the contents of such a file.
---

# Techsupport File

!!! note "Techsupport Data Handling"

    A techsupport file uploaded to the `upload.ipfabric.io` server is stored
    there only temporarily. The file is eventually moved to a permanent location
    on Microsoft SharePoint. The `upload.ipfabric.io` server is accessible only
    to the IP Fabric Ops team, who facilitate the transfer to the permanent
    location. The file in the permanent location has strict RBAC rules
    configured, allowing access only to those at IP Fabric who need it for their
    work (such as the Support team, Network Automation engineers, etc.).

!!! info "Video Tutorial"

    A techsupport file from the IP Fabric appliance is one of the ways you can
    share discovered data with our Support team and engineers. This quick
    tutorial demonstrates how to generate the file and share it with us. The
    techsupport file is encrypted, and only IP Fabric support staff can decrypt
    the data.

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/SJZAzYAuXrE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Generating Techsupport File

### WEB / GUI

1. In the IP Fabric GUI, go to **Support --> Generate Techsupport**:

   ![Generate techsupport file](../images/support/techsupport/support-techsupport-images_techsupport_generation-20250307.webp)

2. Select the data to be included in the techsupport file (when in doubt, keep
   the defaults):

   ![Configure what to include in techsupport file](../images/support/techsupport/support-techsupport-images_techsupport_generation_settings-20250307.webp)

!!! note "Possible error when generating Techsupport file"

    If you encounter an error while generating the Techsupport file, try again,
    but first uncheck the **General environment information** option and then retry.

### CLI

1. Connect to the IP Fabric appliance via SSH with the `osadmin` user:

   ```shell
   ssh osadmin@<IP_or_FQDN>
   ```

2. Switch to `root`:

   ```shell
   sudo su -
   ```

3. Run the `ipf-techsupport-exporter.sh` script as the `autoboss` user to
   generate an encrypted techsupport file with the recommended default contents 
   (system and service logs, usage data, and a specific snapshot `SNAPSHOT_ID` 
   with its database records).

   ```shell
   sudo -u autoboss /opt/ipf-techsupport-exporter/bin/ipf-techsupport-exporter.sh \
   -e -1 -2 \
   -3 <SNAPSHOT_ID> \
   -4 <SNAPSHOT_ID> \ 
   -6
   ```

   If needed, you can use the following options to select what to include in the
   techsupport file:

   ```
   Techsupport content (default if not specified is the first four):
	-1	System logs
	-2	Discovery logs
	-3	Snapshots (specify snapshot number)
	-4	DB dump (specify snapshot number or use "full" keyword for complete dump)
	-5	Exclude CLI logs from snapshot
	-6	Usage data
   ```

4. By default, the file will be named `techsupport-<JOB_ID>.tar` and stored in
   the `/home/autoboss/files` directory. You can copy it to another computer or 
   upload it directly to us using the [`curl`](#curl) command if your IP Fabric 
   appliance has access to the internet.

### API

Please refer to the [Techsupport](../IP_Fabric_API/techsupport.md) section of
our API documentation.

## Uploading Techsupport File

### WEB / HTTPS

Please visit <https://upload.ipfabric.io> in your browser to upload the
generated techsupport file for us. Depending on your location, you will be
redirected to `upload.EU.ipfabric.io` or `upload.US.ipfabric.io` (this can be
switched on the page). The username and password are provided by IP Fabric
Support.

![Upload techsupport file](../images/support/techsupport/support-techsupport-images_upload.webp)

### `curl`

If your IP Fabric appliance has direct internet access, you can upload the
techsupport file directly from it using the following `curl` command:

```shell
curl --user username:password \
-T "/home/autoboss/files/techsupport-<JOB_ID>.tar" \
-X POST https://upload.EU.ipfabric.io/upload \
-f
```

Generated techsupport files are located in the `/home/autoboss/files` directory
on the IP Fabric appliance.

In the command, you may change `https://upload.EU.ipfabric.io/upload` to
`https://upload.US.ipfabric.io/upload`. The username and password are provided by
IP Fabric Support.

## What Techsupport File Includes

1. **System logs** -- Includes `syslog`, `dmesg`, RabbitMQ, NGINX, PostgreSQL, Redis,
   and IP Fabric API service logs. Customer data are **not** included.

2. **Service logs** -- Includes IP Fabric discovery service logs without CLI.
   Included customer data is limited to IP addresses used during discovery and
   serial numbers of devices.

3. **Current Snapshot** -- Includes the currently selected snapshot.

   - **Remove CLI logs from snapshot** -- Removes devices' CLI logs from the
     currently selected snapshot.
   - **Database dump** -- Includes the database dump of the currently selected
     snapshot.

4. **Complete database dump** -- Includes the database dump of all snapshots
   currently loaded in memory.

5. **Database dump without devices data** -- Removes all collected data from
   devices. The dump contains only error and service tables.

6. **Usage data** -- Includes
   [usage data](../IP_Fabric_GUI/usage_data_collection.md). Providing this data
   helps us improve the product.

!!! info

    Snapshot and database dumps do not include any customer credentials
    (passwords, keys, etc.)
