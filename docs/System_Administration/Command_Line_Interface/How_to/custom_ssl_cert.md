---
description: This section contains information on how to implement your own custom TLS certificate for the web GUI.
---

# How to add Custom SSL Certificate

If a custom SSL certificate for HTTPS traffic (IP Fabric main GUI) is required, follow this guide to change the certificate manually.

!!! important

    Please ensure that the FQDN (DNS name) of the IP Fabric appliance is set as your custom certificate's `Subject Alternative Name`. Having the FQDN as the certificate's `Subject` or `Common Name` is not sufficient.

1. Log in to the IP Fabric appliance's CLI as `osadmin` and change to `root`:

  ```shell
  sudo su
  ```

2.  Backup the previous server certificate and its private key:

  ```shell
  mv /etc/nginx/ssl/server.crt /etc/nginx/ssl/server.crt.bkp
  mv /etc/nginx/ssl/server.key /etc/nginx/ssl/server.key.bkp
  ```

3.  Upload the new certificate chain and private key to the `/etc/nginx/ssl/` directory

  1.  They have to have the same names as those previous ones -- `server.crt` and `server.key`
  2.  `server.crt` needs to contain the new SSL certificate and full certificate chain in PEM format
  3.  `server.key` needs to contain the new SSL certificate's private key in decrypted PEM format

4.  The certificate chain in `server.crt` must have the following sequence:

  1.  Server Certificate
  2.  Intermediate Certificate(s)
  3.  Root Certificate

5.  Make sure that the new `server.key` has the same owner and group (`root:autoboss`) and permissions (`-rw-r-----`) as the old one:

  ```shell
  chown root:autoboss /etc/nginx/ssl/server.key
  chmod 0640 /etc/nginx/ssl/server.key
  ```

6.  Check if the `MD5` hashes for `server.crt` and `server.key` are identical:

  !!! example

      ```shell hl_lines="2 4"
      root@ipfabric:~# openssl x509 -noout -modulus -in /etc/nginx/ssl/server.crt | openssl md5
      (stdin)= 9dcfd46578b9dffe06ca0146607f6153
      root@ipfabric:~# openssl rsa -noout -modulus -in /etc/nginx/ssl/server.key | openssl md5
      (stdin)= 9dcfd46578b9dffe06ca0146607f6153
      ```
  !!! danger

      Do not proceed with the next step if the `MD5` hashes don't match!

      If `MD5` hashes do not match, check if the certificate chain is in the correct order, or if the server private key corresponds to the server certificate. 

7.  Restart `nginx` with the following command:

  ```shell
  systemctl restart nginx
  ```

8.  Check if `nginx` is running:

  ```shell
  systemctl status nginx
  ```

9. Verify that the new certificate works correctly by visiting the IP Fabric main GUI in the browser.
