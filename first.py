# print ("Hello!")

# # a python module is a file containing python code which can be imported and used in other python files. A module can contain functions, classes, and variables. A module can also include runnable code.   
# # piu is a python module which contains functions and classes for performing various mathematical operations. It is a built-in module in python and can be imported using the import statement.
# import math

# print ('shubh' + 'am') # String concatenation - joining two strings together
# print (2**2) # Exponentiation - raising a number to the power of another number
# print (math.sqrt(16)) # Square root - finding the square root of a number using the math module

'''
my_name = input('>') # Taking input from the user and storing it in a variable
print (f"Hello {my_name}!") # Using f-string to print the value of the variable in a string 
print(f'it is good to meet you,' + my_name) # String concatenation - joining a string and a variable together 
print(len(my_name)) # len() - to find the length of the string stored in the variable
print(my_name.upper()) # upper() - to convert the string stored in the variable to uppercase
print(my_name.lower()) # lower() - to convert the string stored in the variable to lowercase
print(my_name.title()) # title() - to convert the string stored in the variable to title
print(my_name.strip()) # strip() - to remove any leading or trailing whitespace from the string stored in the variable
print('what is your age?') # print() - to print a string to the console
my_age = input('How old are you? ') # Taking input from the user and storing it in a variable
print('you will be ' + str(int(my_age) + 1) + ' years old next year') # str() - to convert a number to a string, int() - to convert a string to a number
'''

'''
type (43)
<class 'int'>
type (3.14)
<class 'float'>
type ("Hello")
<class 'str'>
type (True)
<class 'bool'>
'''

'''
print(round (3.14159, 2)) # round() - to round a number to a specified number of decimal places
print(abs (-5)) # abs() - to find the absolute value of a number
print(max (1, 2, 3)) # max() - to find the maximum value among the given numbers
print(min (1, 2, 3)) # min() - to find the minimum value among the given numbers
'''


'''
# Variables are used to store data in a program. A variable is a name that refers to a value. The value can be of any data type such as int, float, str, bool, etc. Variables can be assigned values using the assignment operator (=).   

name = "Shubham" # String variable
cpu_usage = 75.5 # Float variable
is_active = True # Boolean variable 
disk_space = 50 # Integer variable

# list is a collection of items which is ordered and changeable. It is defined using square brackets [] and items are separated by commas. A list can contain items of different data types.
my_list = [1, 2, 3, "Hello", True] # List variable

servers = ["server1", "server2", "server3"] # List variable
for server in servers: # for loop to iterate through the list
    print (f"Checking {server}...") # Using f-string to print the value of the variable in a string 
    print (f"{server} is up and running!") # Using f-string to print the value of the variable in a string
    print(server)
'''

'''
# Dictionaries are used to store data in key-value pairs. A dictionary is defined using curly braces {} and each key is separated from its value by a colon (:). The items in a dictionary are separated by commas. A dictionary can contain items of different data types.

my_dict = {"name": "Shubham", "age": 25, "is_active": True} # Dictionary variable
print (my_dict["name"]) # Accessing the value of a key in the dictionary using the key
print (my_dict["age"]) # Accessing the value of a key in the dictionary using the key
print (my_dict["is_active"]) # Accessing the value of a key in the dictionary using the key    
'''

server = {
    "name": "server1",
    "ip": "192.168.1.10",
    "status": "running"
}

print(server["ip"]) # Accessing the value of a key in the dictionary using the key
