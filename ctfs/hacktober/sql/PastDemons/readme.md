# Past Demons (30 points)

`format = flag{password}`

## Problem
```
We've had a hard time finding anything on spookyboi. But finally, with some search engine finessing, an analyst found an old, vulnerable server spookyboi used to run. We extracted a database, now we need your help finding the password.
```

## Solution
```
The ctf gives us a .db file to download.

in order to view it like its supposed to we need to import it into a sqlite3 database.

to open it with sqlite3 we need to run #sqlite3 out.db#
```
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/PastDemons/0.png)
```
to view all the tables we need to run #.tables# inside the sqlite db.

we need to found spookyboi password.

before we run any sql commands we need to set the header on and mode to column in order for the sql commands to be run like we want them to.

#.header on#
#.mode column#

now to view `passwd` and `users` table contents.

#SELECT * FROM passwd;#
#SELECT * FROM users;#

we can see that spookyboi's uid is 8 so we need to crack the password with the uid of 8.
```
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/PastDemons/2.png)
```
doing this with john or hashcat will be a waste of time because we can do it with online tools like crackstation.net

we can see that crackstation.net was able to find that hash contents in their database and also find the type of hash.
```
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/PastDemons/3.png)
```
flag{zxcvbnm}
```
