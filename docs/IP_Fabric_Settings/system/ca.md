---
description: This section contains information on how to add CA certificates to IP Fabric.
---

# Certificate Authorities

Before version `6.0`, IP Fabric used the CA bundle shipped with Node.js. This
led to confusion as system utilities were not aware of new certificates.

Since version `6.0`, we have switched to global cert store trusted by OpenSSL.
Internally, this is achieved by passing `--use-openssl-ca` to Node.js.

## Adding a Custom Certificate

You can add a certificate by placing its `.crt` file in the
`/usr/local/share/ca-certificates` directory and running the following command:

```shell
update-ca-certificates
```

If you are going to add multiple certificates, we recommend creating a
subdirectory:

```shell
mkdir /usr/local/share/ca-certificates/my_custom_ca
```

!!! info

    The certificate must be in PEM format with a `.crt` extension. Files with
    other extensions are omitted.

After placing the certificate in the directory, you will need to run the
`update-ca-certificates` command to link the certificate to the `Trusted Root
Certificate Store`. Running it should give you an output like the following:

```shell
Updating certificates in /etc/ssl/certs...
1 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
```

### Converting to `.crt`

`.crt` is nothing more than a PEM certificate with a custom extension. If you
need to convert your certificate, you can use the `openssl` command-line tool to
do so:

```shell
openssl x509 -in my_custom_ca.der -out /usr/local/share/ca-certificates/my_custom_ca.crt
```

`openssl` is typically pretty good at guessing the input format.

## Deleting a Custom Certificate

1. Remove the relevant files/subdirectories from
   `/usr/local/share/ca-certificates`.
2. Run `update-ca-certificates`.
