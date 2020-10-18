# Null And Void (25 points)

`flag format = flag{column-name, command}`

## Problem
```
Using the Shallow Grave SQL dump, which field(s) in the users table accepts NULL values? Submit the field name followed by the single command used to show the information (separated by a comma).
```

## Solution
```
The ctf gives us a .sql file to download.

in order to view it like its supposed to we need to import it into a mysql database.

lets first create a database to import that file into.

#mysql -u root -p#
#create database NullAndVoid;#

now we need to import the sql file.

#mysql -u root -p NullAndVoid < shallowgraveu.sql#

after the sql file is imported we can start to view the tables.

#mysql -u root -p NullAndVoid#

now to check which field allows null value.

we can do that by using #describe users;# to view the tables properties;

flag{middle, describe}
```