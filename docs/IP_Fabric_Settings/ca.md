# Certification Authorities

By default, the IP Fabric only trusts certificates issued by CAs listed
in the node.js. Because
internal systems typically use certificates signed by an internal CA,
the root certificate of this certification authority needs to be
uploaded.

For example, establishing a secure connection between IP Fabric and LDAP
server requires a trusted certificate chain.

## Upload root CA certificate

1. Go to **Settings → Advanced → System → Certification Authorities**.
2. Click **Upload CA**.
3. Enter root CA certificate **Name** (it's only your overview)
4. **Choose file**
5. Click **Save**

## Delete root CA certificate

1. Go to **Settings → Advanced → System → Certification Authorities**.
2. Select certificate and click **Delete** on the right.
3. Confirm delete using the **Delete** button.

## Rename root CA certificate

1. Go to **Settings → Advanced → System → Certification Authorities**.
2. Select certificate and click **Edit** on the right.
3. Change **Name**
4. Click **Save**
