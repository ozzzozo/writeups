# Fall Classes (100 points)

`flag format = flag{#}`

## Problem
```
Without counting duplicates, how many courses are being offered in the FALL2020 term at Shallow Grave University?
```

## Solution
```
The ctf gives us a .sql file to download.

in order to view it like its supposed to we need to import it into a mysql database.

lets first create a database to import that file into.

#mysql -u root -p#
#create database FallClasses;#

now we need to import the sql file.

#mysql -u root -p FallClasses < shallowgraveu.sql#

after the sql file is imported we can start to view the tables.

#mysql -u root -p FallClasses#
```
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/FallClasses/0.png)
```
if we look inside table `terms` we can see the term_id of FALL2020 which will help us later filter out what we don't need.

#select * from terms;#
```
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/FallClasses/1.png)
```
to view all the courses offered we need to look into `term_courses`

we can use #describe term_courses# to get more info about that table.
```
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/FallClasses/4.png)
```
for this I wanted to write a simple script(for fun).

lets first output all the term_courses into a file.

#select * from term_courses INTO OUTFILE '/var/lib/mysql-files/terms.txt';#
```
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/FallClasses/2.png)
![alt text](https://raw.githubusercontent.com/ozzzozo/writeups/main/ctfs/hacktober/sql/FallClasses/5.png)
```
flag{401}
```

```
file1 = open('terms.txt', 'r') # Opens File
Lines = file1.readlines() # Reads file contents
  
count = 0 # initialization count var
was_checked = [] # initialization was_checked array

for line in Lines: # Looping through each line in Lines variable

	current_line = line.strip().split("	") # Splits line into array

	if current_line[2] == '2' and current_line[1] not in was_checked: # Checks if term_id is '2'(FALL2020) and if course_id was not checked already
		count = count + 1 # Increment count by 1
		was_checked.append(current_line[1]) # Append to was_checked array the course_id

print(count) # Prints amount of terms counted
```
