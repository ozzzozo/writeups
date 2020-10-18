

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