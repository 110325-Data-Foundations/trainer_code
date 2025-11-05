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


# Casting
# Type conversion 

# Implicit conversion - happens automatically
num1 = 1
num2 = 3.3
my_sum = num1 + num2

#Explicit conversion - I have to tell the interpreter what I'm intending to do
#In this case - case my_sum as a string 
my_message = "My total is: " + str(my_sum)

print(my_message)

#Another example of explicit conversion - string -> int
my_new_sum = int("124")

#Collections

#Python has a few built in collection types for storing multiple objects/values at once
#Lists, Sets, Dictionaries, Range, etc

#List - Mutable, Allows duplicates, indexable

my_list = [11, 3, 400, 98]

print(my_list[0])

#Append - adds a new object to my list
my_list.append("new thing for my list")

print(my_list)

my_list_extension = [4, 11, 3, 92]

#Extend - adds a collection of objects to the end of my list
my_list.extend(my_list_extension)

print(my_list)

my_list.insert(3, "new position 3")

print(my_list)

# Removes the first instance of the value passed to .remove()
my_list.remove(3)

print(my_list)

# Pop - I can use this to quickly remove the last thing in the list
my_list.pop()

print(my_list)

#If i give pop an index value, it can remove whatever is at that index
my_list.pop(1)

print(my_list)

my_list.reverse()
print(my_list)

#my_list.sort()

print(my_list)

# Sets - Mutable, doesn't allow duplicates, indexable 
my_set = {1, 2, 3}

my_set.add(5)
my_set.add(1)

print(my_set)

#Unlike in a list, pop is FIFO when working with sets
print(my_set.pop())
print(my_set)

#I can use remove() and discard() to remove specific values from my set
#notice we say remove values, not remove the value at an index

#Remove will raise an error if the given value DOESN'T exist in the set
my_set.remove(3)

my_set.discard(342)

print(my_set)
