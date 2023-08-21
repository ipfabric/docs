---
description: This section contains information about how to troubleshoot LDAP-related issues.
---

# How To Troubleshoot LDAP

## Users Are Not Able To Log In

The `ldapsearch` is the best tool to troubleshoot LDAP issues. Sometimes groups or users are not found and LDAP needs to be troubleshot.

To troubleshoot user login/missing group issues, use the following command with similar fields:

```shell
LDAPTLS_REQCERT=ALLOW ldapsearch -W -H "ldap(s)://ldap-server:port" -D "Service account AD path" -b "Base directory path" -s sub sAMAccountName="Username of the user that wants to log in"
```
!!! note

    This command will prompt you to enter service account password.

    Output of this command could be extensive, it shows the information about the user and groups they are part of, check if it matches the group settings in IP Fabric.
    If the user is not part of any required group, you can try to use the next command which will search in nested groups.

To troubleshoot nested groups use the following command to list groups of a specific user:

```shell
LDAPTLS_REQCERT=ALLOW ldapsearch -W -H "ldap(s)://ldap-server:port" -D "Service account AD path" -b "Base directory path" -s sub member:1.2.840.113556.1.4.1941:="Username of the user that wants to log in"
```

## LDAPS Troubleshooting

If you want to use LDAPS, there are certain criteria that need to be met.

1.  Domain name/CN/SAN/hostname of LDAP server needs to be specified as a `ldaps://address`, IP address cannot be present

2.  Root certificate or intermediate certificate by which LDAPS certificate is signed with needs to be uploaded/selected

To verify name/CN/SAN of the LDAP server and root/intermediate certificates by which is the LDAPS certificate signed with, use the following command:

```shell
openssl s_client -connect <ldaps server>:<ldaps port>
```

## Issues With LDAPS After Upgrade To `5.0`

OpenSSL in Debian 11 has significantly improved security, not trusting certificates signed with 2048bit RSA key or lower.

If you are getting `Unexpected Failure` error for LDAP login attempts after upgrade to 5.x, most likely there is an issue with public key length of the certificate.

Check public key length with `openssl s_client -connect <ldaps server>:<ldaps port>`

If it was signed with a low RSA key size, change OpenSSL setting in `/etc/ssl/openssl.cnf` to (located at the end of the configuration file):

```shell
[system_default_sect]
MinProtocol = TLSv1.2
CipherString = DEFAULT@SECLEVEL=1
```

and restart the machine.
