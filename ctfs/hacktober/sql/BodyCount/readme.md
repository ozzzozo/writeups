# Body Count (25 Points)

`format = flag{#}`

## Problem
```
How many users exist in the Shallow Grave University database?
```

## Solution
```
The ctf gives us a .sql file to download.

in order to view it like its supposed to we need to import it into a mysql database.

lets first create a database to import that file into.

#mysql -u root -p#
#create database BodyCount;#

now we need to import the sql file.

#mysql -u root -p BodyCount < shallowgraveu.sql#

after the sql file is imported we can start to view the tables.

#mysql -u root -p BodyCount#

to view all the tables we imported into the mysql database we can use #show tables;#

we can see that there is a `users` table.

by counting how many users there is in that table we can answer the question.

one way of doing that is by using #select * from users;#


flag{900}
```