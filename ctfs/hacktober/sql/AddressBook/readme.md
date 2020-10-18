# Address Book (50 points)

`flag format = flag{username@email.com}`

## Problem
```
Shallow Grave University has provided us with a dump of their database. Find luciafer's email address.
```

## Solution
```
The ctf gives us a .sql file to download.

in order to view it like its supposed to we need to import it into a mysql database.

lets first create a database to import that file into.

#mysql -u root -p#
#create database AddressBook;#

now we need to import the sql file.

#mysql -u root -p AddressBook < shallowgraveu.sql#

after the sql file is imported we can start to view the tables.

#mysql -u root -p AddressBook#
```
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/AddressBook/0.png)
```
we need to check the users table content.

we know that lucifer is studies at Shallow Grave University so we can check for that domain in the emails.

#select * from users where email LIKE '%@shallowgrave%';#

which gives us only one row which is lucifer's row.
```
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/AddressBook/1.png)
```
flag{luc1afer.h4vr0n@shallowgraveu.com}
```
