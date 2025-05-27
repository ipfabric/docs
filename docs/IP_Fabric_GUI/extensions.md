---
description: Complete guide to IP Fabric Extensions - create, deploy, and manage custom applications within your IP Fabric instance.
---

# Extensions

Extensions allow you to add and customize your IP Fabric instance with tailored functionality. Transform your network management experience by deploying custom applications that integrate seamlessly with your IP Fabric environment.

## What Extensions Can Do

Extensions enable you to:

- **Generate custom reports** (e.g., DORA metrics)
- **Transform data in real time** (custom tables and views)
- **Enrich data through external integration** (CVE information for devices)
- **Implement business-specific processing logic** (global search functionality)
- **Create specialized dashboards** and analytical tools
- **Integrate with third-party services** and APIs

Extensions are managed through the standard IP Fabric UI under **Extensions** in the main menu.

## Prerequisites

Before creating extensions, ensure you have:

- **Required permissions**: Extension management permissions assigned through security policies
- **Platform compatibility**: Applications must be compatible with `linux/amd64` architecture
- **Network requirements**: Extensions with web interfaces must listen on port `80/tcp` for incoming traffic
- **IP Fabric version**: Release 7.0 or later with Extensions feature flag enabled

## Feature Availability

| Feature | Version | Description |
|---------|---------|-------------|
| Basic Extensions | 7.0+ | Core extension functionality, Docker deployment |
| Resource Allocation | 7.2+ | CPU and memory limits, security enhancements |
| Access Control | 7.2+ | User-based access permissions |

## Feature Activation

Starting with version 7.0, enable Extensions with the `ENABLE_EXTENSIONS=true` [feature flag](../System_Administration/Command_Line_Interface/Feature_Flags.md) in `/etc/default/ipf-appliance-local`.

⚠️ Docker Default Subnet Configuration Required

**Important**: As of version `7.0.14`, the Docker service is **disabled by default** to prevent subnet conflicts with your network infrastructure.

The default Docker subnet (`172.17.0.0/16`) may conflict with existing network ranges in your environment.

### Configuration Options

**Option 1: Customize Docker Subnet** (Recommended)

Edit `/etc/docker/daemon.json` to use a non-conflicting subnet range.

📖 [See detailed configuration guide](../support/known_issues/IP_Fabric/unable_to_discover_devices_in_172_17_0_0_16_subnet.md)

**Option 2: Get Support**

Contact our support team for assistance via the [support portal](https://support.ipfabric.io)

**Option 3: Use Default Subnet** (Only if safe)

If `172.17.0.0/16` is completely unused in your environment:

```bash
sudo systemctl enable docker && sudo systemctl start docker
```

⚠️ **Before proceeding**: Verify that `172.17.0.0/16` does not conflict with your network infrastructure.

## Creating Extensions

### Step 1: Access the Extension Setup

1. Navigate to **Extensions** in the main IP Fabric menu
2. Click the **Add** button to open the Extension Setup form

### Step 2: Configure Basic Information

**Name** (Required)

- Human-readable identifier for your extension
- Does not need to be unique across the platform
- Example: "Network Security Dashboard"

**Slug** (Required)  

- Unique identifier automatically generated from your extension name
- Uses dash-separated format (e.g., "network-security-dashboard")
- Cannot be duplicated across the platform
- Used in URLs: `https://<host>/extensions-apps/<slug>`

**Type** (Required)
Choose your deployment method:

- **Docker Zip**: Upload source code and `Dockerfile` in a ZIP archive
  - System builds the image on the host machine
  - Automatically ensures correct `linux/amd64` architecture
  - Best for custom applications built from source

- **Docker Image**: Upload a pre-built Docker image file
  - Must be built for `linux/amd64` architecture
  - Supports `.tar` and `.tar.gz` formats
  - Created using `docker save` command
  - **Important**: Wrong architecture will cause constant restart loops

**Description** (Required)

- Describe your extension's purpose and functionality
- Visible to users who have access to your extension

### Step 3: Configure Application Settings

**Environment Variables**
Define environment variables your application needs:

- Format: Enter each variable as `KEY=VALUE` on separate lines
- Example:

```bash
API_KEY=your-secret-key
DATABASE_URL=postgresql://localhost:5432/mydb
DEBUG=true
```

**Import File** (Required)

- **For Docker Zip**: Upload ZIP file containing Dockerfile and source code
- **For Docker Image**: Upload `.tar` or `.tar.gz` Docker image file
- No file size limits, but larger files will take significantly longer to process

### Step 4: Resource Allocation (Release 7.2+)

#### CPU Allocation

- Minimum: 0.01 units
- Increment: 0.01 units  
- Example: 1.00 units = 1 CPU core
- Note: CPU allocation is not guaranteed (soft limit)

#### Memory Allocation

- Minimum: 6 MB
- Specify in megabytes (MB)
- Example: 512 MB
- Note: Memory is subtracted from total available system memory (hard limit)

> **Resource Management**: You can overprovision resources beyond what's physically available. Monitor actual usage to ensure optimal performance.

### Step 5: Access Control (Release 7.2+)

**Access Permissions**
Control who can access your extension:

- **Anyone**: All authenticated users can access the extension
- **Only me**: Restricted to you and platform administrators
- **Selected users**: You, administrators, and specified users

## Managing Extensions

### Extension Lifecycle

Once created, extensions appear in the Extensions dashboard with the following information:

- **Name**: Extension identifier
- **Description**: Purpose and functionality
- **Status**: Current operational state
- **URL**: Direct link to access the extension
- **Resource Limits**: Current CPU and memory allocation
- **Actions**: Management options

### Available Operations

#### Start Extension

- Makes the extension accessible via its URL
- Creates internal routing to the container
- Status changes to "running"

#### Stop Extension

- Makes the extension inaccessible (URL returns error)
- Removes internal routing but keeps container
- Status changes to "stopped"

#### Remove Extension

- Completely removes the extension and all associated resources
- Deletes container, image, and routing configuration
- **Warning**: This action cannot be undone

### Access Extension

Access your running extensions at:

```bash
https://<your-ip-fabric-host>/extensions-apps/<extension-slug>
```

Extensions integrate seamlessly with IP Fabric's authentication system - users must be logged in to IP Fabric and have appropriate permissions.

### Updating Extensions

Currently, extensions cannot be updated in place. To update an extension:

1. Note the current configuration settings
2. Remove the existing extension
3. Create a new extension with updated code/image
4. Reconfigure settings as needed

> **Future Enhancement**: In-place updates will be available in future releases.

## Access Control and Permissions

### Management Permissions

Extensions are governed by atomic permissions assigned through security policies. Administrative accounts have full access by default.

Required permissions for different operations:

- **Viewing Extensions dashboard**: Basic extension permissions
- **Register new Extensions**: Extension creation permissions  
- **Starting/Stopping Extensions**: Extension management permissions
- **Remove Extensions**: Extension deletion permissions

**Release 7.2+**: Additional policy required: `POST /tables/users` for viewing/editing extensions.

### User Access Control

Extension creators can control who accesses their extensions through the Access Control settings. This is separate from management permissions and controls end-user access to the extension's functionality.

## Technical Requirements

### Network Communication

- **Container → Host**: Port 443 (for IP Fabric API requests)
- **Host → Container**: Port 80 (for extension web interfaces, if applicable)
- **External Access**: Full network access for third-party service integration

### Platform Requirements

- **Architecture**: `linux/amd64` only
- **Port**: Applications with web interfaces must listen on port `80/tcp`
- **Container Runtime**: Standard Docker container support

### Storage Considerations

Please note that Extensions utilize temporary storage in the `/tmp` folder for:

- Uploaded source code archives
- Docker image files

### Docker Image Considerations

- Use `docker save` to create `.tar` files for upload
- Consider `.tar.gz` compression for large images
- Ensure images target `linux/amd64` platform
- Base images should be compatible with the target architecture

## Troubleshooting

### Common Issues

#### Extension Stuck in Restarting State

- **Cause**: Wrong platform architecture (not `linux/amd64`)
- **Solution**: Rebuild Docker image for correct architecture
- **Note**: Automatic detection will be available in future releases

#### Environment Variable Format Errors

- **Cause**: Incorrect format in environment variables field
- **Solution**: Ensure each variable is on a separate line using `KEY=VALUE` format
- **Example**:

  ```bash
  ✓ Correct:
  API_KEY=secret123
  DEBUG=true
  
  ✗ Incorrect:
  API_KEY=secret123, DEBUG=true
  ```

#### Extension Not Accessible

- **Cause**: Extension stopped or insufficient permissions
- **Solution**: Check extension status and access permissions

#### Resource Allocation Issues

- **Cause**: Insufficient system resources
- **Solution**: Monitor system resources and adjust allocation accordingly
- **Note**: Overprovisioning is allowed but may impact performance

### Getting Help

If you encounter issues not covered in this guide:

1. Check the Extensions dashboard for status information
2. Verify your permissions with system administrators
3. Consult system logs for detailed error information
4. Contact your IP Fabric support for advanced troubleshooting
