'''
for i in range (5):
    env =input("Enter the environment:") # Taking input from the user
    print ("The user input is:",env)
    if env == "dev":
        print ("Don't deploy on Friday")
    elif env == "staging":
        print ("testing")
    elif env == "prod":
        print ("if all good then deploy")
    else:
        print ("Invalid environment")
'''

'''
num = int(input("Enter the number:")) # Taking input from the user
for i in range (10):
    print (f"{num} * {i} = {num*i}")
'''

'''
while True:
    num = int(input("Enter the number:")) # Taking input from the user
    for i in range (10):
        print (f"{num} * {i} = {num*i}")
    cont = input("Do you want to continue? (yes/no):") # Taking input from the user
    if cont.lower() != "yes":
        break
'''

choice = input("Enter the choice (Pressq to quit):") # Taking input from the user
while choice != "q":
    num = int(input("Enter the number:")) # Taking input from the user
    for i in range (10):
        print (f"{num} * {i} = {num*i}")
    choice = input("Enter the choice (Press q to quit):") # Taking input from the user