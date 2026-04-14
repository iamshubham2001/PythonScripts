# Get the environment from user and print it

env =input("Enter the environment:") # Taking input from the user
print (env)

if env == "dev":
    print ("Don't deploy on Friday")
elif env == "staging":
    print ("testing")
elif env == "prod":
    print ("if all good then deploy")
else:
    print ("Invalid environment")

# Type Casting - converting one data type to another data type

a = input("Enter the value of a:") # Taking input from the user
b = input("Enter the value of b:")

c = int(a)*int(b) # Multiplication of a and b
print ("Multiplication of a and b is:", c)

print (type(c)) # type() - to check the data type of the variable a

