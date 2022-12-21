# How to add Custom SSL Certificate

If a custom SSL certificate for HTTPS traffic (IP Fabric main GUI) is required, follow this guide to change the certificate manually:

1.  Make a backup of your previous server certificate and key:

  ```shell
  mv /etc/nginx/ssl/server.crt /etc/nginx/ssl/server.crt.bkp
  mv /etc/nginx/ssl/server.key /etc/nginx/ssl/server.key.bkp
  ```

2.  Upload new certificate chain and private key to the `/etc/nginx/ssl/` folder

  1.  It has to have the same name `server.crt` and `server.key`
  2.  `server.crt` file needs to contain a new SSL certificate and full certificate chain in PEM format
  3.  `server.key` file needs to contain server certificate's private key in decrypted PEM format

3.  The certificate chain in `server.crt` must have the following sequence:

  1.  Server Certificate
  2.  Intermediate Certificate(s)
  3.  Root Certificate

4.  Make sure that files have correct owner and group `root:autoboss`

  1.  Make sure your current working directory is `/etc/nginx/ssl` you can use `pwd` command to be sure, if you're somewhere else then use this command:
  ```shell
  cd /etc/nginx/ssl
  ```
  2.  You can check the owner of the files with `ls -l` command
  3.  If current owner and group are `root:root` then execute following command:
  ```shell
  chown root:autoboss server.crt server.key
  ```
5.  Check if the `MD5` hashes for the `server.crt` and `server.key` files are the same:

  !!! example

      ```shell hl_lines="2 4"
      root@ipfabric:/etc/nginx/ssl# openssl x509 -noout -modulus -in server.crt | openssl md5
      (stdin)= 9dcfd46578b9dffe06ca0146607f6153
      root@ipfabric:/etc/nginx/ssl# openssl rsa -noout -modulus -in server.key | openssl md5
      (stdin)= 9dcfd46578b9dffe06ca0146607f6153
      ```
  !!! danger

      Do not proceed with the next steps if the `MD5` hashes don't match!

6.  Restart `nginx` with the following command:

  ```shell
  systemctl restart nginx
  ```

7.  Check if `nginx` runs correctly with:

  ```shell
  systemctl status nginx
  ```
