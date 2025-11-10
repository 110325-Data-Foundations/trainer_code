# This will be a simple module with arithmetic math methods
# to write tests against. 

def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
    
def multiply(x,y):
    return x * y
    
def divide(x, y):
    if y == 0: # Checking for zero division
        raise ValueError("Cannot divide by zero") # manually raising exception
    return x / y