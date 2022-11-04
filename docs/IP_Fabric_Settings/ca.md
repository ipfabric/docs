# Certification Authorities

Prior version `6.0` IP Fabric used the CA bundle shipped with `node.js`. This led to confusion as the system utilities were not aware of the new certificates. Starting with release `6.0` we have switched to global cert store as trusted by `openssl`.

Internally this is achieved with passing `--use-openssl-ca` to `node.js`.

## Adding a custom certificate

You add certificate by placing `.crt` file to `/usr/local/share/ca-certificates` and running `update-ca-certificates`. We recommend creating a subdirectory in case you are planning to have multiple certificates added.

```shell
mkdir /usr/local/share/ca-certificates/my_custom_ca
```

!!! Info

	Certificate has to be in PEM format with `.crt` extension, files with other extensions are omitted.

After placing the certificate there, you will need to run `update-ca-certificates` command to link the certificate to the Trusted Root Certificate Store. Running it should give you output similar to the following:

```shell
Updating certificates in /etc/ssl/certs...
1 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
```

### Converting to `.crt`

`.crt` is nothing more than a PEM certificate with a custom extension. If you need to convert you certificate, you can use `openssl` command line tool to do so. It is typically pretty clever in guessing input format:

```shell
openssl x509 -in my_custom_ca.der -out /usr/local/share/ca-certificates/my_custom_ca.crt
```

## Deleting a custom certificate

1. Delete appropriate files / directories from `/usr/local/share/ca-certificates/`.
2. Run `update-ca-certificates`.
