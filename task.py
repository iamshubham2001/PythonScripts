# Task 1
'''
cpu_list = [30,55,85,90,60] # List of CPU usage percentages
for cpu in cpu_list: # for loop to iterate through the list
    if cpu <80:
        print ('OK')
    else:
        print('Alert')

def count(cpu_list):
    count = 0
    for cpu in cpu_list:
        if cpu >= 80:
            count += 1
    return count
print(count(cpu_list)) # count() - to count the number of occurrences of a substring in a string
'''


# Task 2

'''
Write a Python script (log_analyzer.py) that:

1. Reads the file
2. Prints only ERROR lines
3. Counts total errors
'''

with open ('log.txt', 'r')as file: # open() - to open a file in read mode
    errors_count = 0 
    warnings_count = 0
    info_count = 0
    for line in file: # for loop to iterate through the lines in the file
        if "ERROR" in line: # if statement to check if the line contains the word "ERROR"
            print (line) # print() - to print the line
            errors_count += 1 # count() - to count the number of occurrences of a substring in a string
        elif "WARNING" in line: # if statement to check if the line contains the word "WARNING"
            print (line) # print() - to print the line
            warnings_count += 1 # count() - to count the number of occurrences of a substring in a string
        elif "INFO" in line: # if statement to check if the line contains the word "INFO"
            print (line) # print() - to print the line
            info_count += 1 # count() - to count the number of occurrences of a substring in a string
print (f"Total errors: {errors_count}") # Using f-string to print the value of the variable in a string
print (f"Total warnings: {warnings_count}") # Using f-string to print the value of the variable in a string
print (f"Total info: {info_count}") # Using f-string to print the value of the variable in a string





