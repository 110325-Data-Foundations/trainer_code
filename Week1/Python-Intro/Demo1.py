#This is a comment, even if there's valid code in here the interpreter will ignore it.

# Datatypes

#String - Strings of characters 

#Num
    #Int - Integer whole numbers
    #Float - Floating point numbers
    
#Boolean - True/False values

#None 

#If I want to declare a variable...

#Notice no type is given... python will intuit the type during runtime
myNum1 = 10

# This :int is a type hint - its more for us the humans reading/writing the code
# It doesn't change the behavior of the interpreter
myNum2:int = 11

#Numeric types: Int and Float 
my_integer = 1 #no decimals
my_float = 1.1 #Has a decimal

# String is used for words and text
my_String = "here are some words!"

# booleans true/false
true_boolean = True
false_boolean = False

# None - just telling the interpreter we intentionally have an empty variable
#Cant use a keyword as a variable name
# None = 3
my_none = None
# print(my_none)

# We can use arithmetic operators with numerical types

sum = my_integer + my_float
print(sum)

# We can use the + operator to do string concatenation 
name = "Jonathan"
greeting = "Hello " + name

print(greeting)

#It can be cleaner to use formatted strings for this purpose
formatted_greeting = f"Hello {name}"
print(formatted_greeting)

# Operators 
# +  addition
# - subtraction
# * multiplication
# / division
# ** power 
# % modulus
# // floor division
# == comparison/equality operator 

# Console input and output

# Output to the console is easy in python, there's a built in method called "print()"

print("Here is my console output")
my_input = input() # Taking in console input is just as easy!
print(f"User typed {my_input} \n This will be on a new line")

#Truthy vs falsy 

#We can evaluate anything in a boolean context
#Certain things will be considered "falsy"

#Falsy values
#False
#None 
#0, 0.0, 0j
# ""
# empty collections (lists, tuple,dictionary, etc)

# Truthy values
# ... everything else

#Some new change