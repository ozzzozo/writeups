# Talking To The Dead 1-4

`ssh server = hacktober@env.hacktober.io`
`ssh password = hacktober-Underdog-Truth-Glimpse`

## Problem
```
We've obtained access to a server maintained by spookyboi. There are four flag files that we need you to read and submit (flag1.txt, flag2.txt, etc).
```

## Solution
```
we need to obtain 4 files.

flag1.txt flag2.txt flag3.txt and flag4.txt

lets get searching!

for this we can use the find command.

#find / -iname *flag* 2>/dev/null | grep .txt#

here we are searching for files that have `flag` in their name and grepping the ones that are .txt files.

and we got the flags location!

we can read the first 2 flags but the others give us permission denied.

cat /home/luciafer/Documents/flag1.txt
cat /home/luciafer/Documents/.flag2.txt

flag{cb07e9d6086d50ee11c0d968f1e5c4bf1c89418c} - flag 1
flag{728ec98bfaa302b2dfc2f716d3de7869f3eadcbf} - flag 2

lets priv esc!

runing `sudo -l` gives us `bash: sudo: command not found`

I will not try to upload linpeas here.

lets search for suid.

we find /usr/local/bin/ouija

which looks weird.

lets try to run it.

looks like its for file reading in the root directory.

lets try to read flag4 on the root directory.

we can see the that file puts `/root/` at the start for us.

so we just need to enter the file name in the root directory.

#/usr/local/bin/ouija flag4.txt#

and we have flag4!

flag{4781cbffd13df6622565d45e790b4aac2a4054dc} - flag 4

now to read flag3 on spookyboi Documents directory.

#/usr/local/bin/ouija ../home/spookyboi/Documents/flag3.txt#

we need to escape the default `/root/` directory so we add `../` at the start

and we have flag 3!

flag{445b987b5b80e445c3147314dbfa71acd79c2b67} - flag 3
```