# Errors vs Exceptions

# Error
# my_string = str ing

# Exception - is raised during run time. 
user_number = int(input())

print(user_number)

# We can handle exceptions that arise during runtime with try-except blocks

# Place the potentially offending code, inside our try block
try:
    user_number = int(input()) # This code could raise an exception based on user input.
except: # This code only runs if an exception is raised.
    print("Please enter an integer.")
    
# I can have as many except blocks as I need, if I want to catch different specific types
# of exceptions

try:
    user_number = int(input())
    result = 6 / user_number
    print(result)
except ValueError: # Example of catching a specific Exception type
    print("Please enter an integer.")
except ZeroDivisionError: # We can catch multiple exception types in one try-except-except... block
    print("Can't divide by zero!")
except: # Always a good idea to end with a generic except block
    print("How did you even get here?")
    

# If we need to, we can create custom exceptions based on business rules.
# Not related to python or arithmetic rules.
class MyException(Exception): # A custom exception is just a class that inherits from the Exception class
    # Like any other class, we need to override __init__ to create this object
    def __init__(self, message="Time to lock in buddy. Number's too small"):
        self.message = message

try:
    print("Please enter an integer")
    user_num = input()
    
    # If this condition is NOT true....
    if int(user_num)>0: #Checking if the user entered an integer
        raise MyException() # If we get here, manually raise this exception
    
    print(user_num)
except MyException as e:
    print(e.message)
except: 
    print("Caught.....something else")