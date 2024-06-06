---
description: This section contains information on how to troubleshoot LDAP-related issues.
---

# How To Troubleshoot LDAP

## Users Cannot Log In

The `ldapsearch` is the best tool to troubleshoot LDAP issues. Sometimes, groups
or users are not found, and LDAP needs to be troubleshot.

To troubleshoot user login or missing group issues, use the following command
with similar fields:

```shell
LDAPTLS_REQCERT=ALLOW ldapsearch -W -H "ldap(s)://ldap-server:port" -D "Service account AD path" -b "Base directory path" -s sub sAMAccountName="Username of the user who wants to log in"
```

!!! note

    This command will prompt you to enter the service account password.

    The output of this command could be extensive. It shows the information
    about the user and the groups they are part of and checks if they match the
    group settings in IP Fabric.

    If the user is not part of any required group, you can try to use the next
    command, which will search in nested groups.

To troubleshoot nested groups, use the following command to list the groups of a
specific user:

```shell
LDAPTLS_REQCERT=ALLOW ldapsearch -W -H "ldap(s)://ldap-server:port" -D "Service account AD path" -b "Base directory path" -s sub member:1.2.840.113556.1.4.1941:="Username of the user that wants to log in"
```

## LDAPS Troubleshooting

If you want to use LDAPS, these criteria need to be met:

1. The domain name/CN/SAN/hostname of the LDAP server needs to be specified as
   `ldaps://address`; an IP address cannot be present.

2. The root/intermediate certificates by which the LDAPS certificate is signed
   needs to be uploaded/selected.

To verify the name/CN/SAN of the LDAP server and the root/intermediate
certificates by which is the LDAPS certificate signed, use the following
command:

```shell
openssl s_client -connect <ldaps server>:<ldaps port>
```

## Issues With LDAPS After Upgrade to `5.0`

OpenSSL in Debian 11 has significantly improved security, not trusting
certificates signed with a 2048-bit (or lower) RSA key.

If you are getting an `Unexpected Failure` error for LDAP login attempts after
upgrading to `5.0`, there is most likely an issue with the certificate's public
key length.

Check the public key length with:

```shell
openssl s_client -connect <ldaps server>:<ldaps port>
```

If it was signed with a low RSA key size:

1. Change the OpenSSL settings in `/etc/ssl/openssl.cnf` to:

   ```shell
   [system_default_sect]
   MinProtocol = TLSv1.2
   CipherString = DEFAULT@SECLEVEL=1
   ```

   (located at the end of the configuration file)

2. Restart the machine.
