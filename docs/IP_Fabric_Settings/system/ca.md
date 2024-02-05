---
description: This section contains information how to add CA certificates to IP Fabric.
---

# Certification Authorities

Before version `6.0`, IP Fabric used the CA bundle shipped with `node.js`. This
led to confusion as system utilities were not aware of new certificates.

Since version `6.0`, we have switched to global cert store trusted by `openssl`.
Internally, this is achieved by passing `--use-openssl-ca` to `node.js`.

## Adding a custom certificate

You can add a certificate by placing its `.crt` file in the
`/usr/local/share/ca-certificates` directory and running the following command:

```shell
update-ca-certificates
```

We recommend creating a subdirectory in case you are going to add multiple
certificates:

```shell
mkdir /usr/local/share/ca-certificates/my_custom_ca
```

!!! Info

    The certificate has to be in PEM format with `.crt` extension. Files with
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

`.crt` is nothing more than a PEM certificate with a custom extension.
If you need to convert your certificate, you can use the `openssl` command-line
tool to do so:

```shell
openssl x509 -in my_custom_ca.der -out /usr/local/share/ca-certificates/my_custom_ca.crt
```

`openssl` is typically pretty good at guessing the input format.

## Deleting a custom certificate

1. Remove relevant files/subdirectories from `/usr/local/share/ca-certificates`.
2. Run `update-ca-certificates`.
