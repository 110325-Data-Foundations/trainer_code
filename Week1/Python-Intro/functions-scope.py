# Functions - great way to package useful/discrete functionality so you can reuse it when needed

# Creating a function - we use the "def" keyword, name the function, give it a parameter list with ()
# then write the function's code below

# I've annotated my addition_function to make it more self-documenting
# I can even add a return type... the interpreter doesn't really care though
def addition_function(x:int, y:int) -> int:
    return x + y

#This function takes no parameters and doesn't return anything
def bark():
    print("bork")

# Calling my functions
sum = addition_function(10, 5)
print(sum)
bark()

print(addition_function("First ", "Second")) # If I call my add function on strings, I get string concat

# Scopes...
# Scope: Area of the code where some object/variable/function can be called upon and used

# Local
# Enclosed
# Global
# Built-in

# Built-in: Default python methods and all the keywords live here. Can be accessed 
# from anywhere in your code, in any Python file - this is where print() lives


# Global: Accessed anywhere within the file they are declared in - as well as in other files/modules
# if brought in via import

# This variable is global. I can reference it inside any functions or code blocks in this file
my_dog = "pancake"


# Local: If I have a block of code (i.e. function or flow control block) and I declare
# a variable/function/etc in it - that object has local scope. 

# This function has its own code block - anything underneath it that is indented until I break out of it
def local_and_enclosed():
    # This variable is locally scoped to this function local_and_enclosed()
    # Available within the function, not outside of it.
    dog = "tripod"
    print(my_dog) # Because my_dog is globally scoped, I can use it within this function
    
    # Enclosed
    def enclosed(): # This function is enclosed within the outer function local_and_enclosed()
        # This function can access variables from the outer function
        dog = "ollie"
        print(dog)
    
    enclosed()
    print(dog)
    

other_dog = "ellie"

local_and_enclosed()