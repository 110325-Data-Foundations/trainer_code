# Python modules... a module is a just a .py file that has code in it. We can import that code for use in other files!
# I want to work with JSON in this app - I need to import the json module

# Importing the json module
import json
from asciimatics.renderers import Scale
# import classes_objects # I can import my own modules (.py files) for use in other files as needed
# I can get more specific as to what I want to import from a module
from classes_objects import Dog # Only pulling in the class I need for this demo. P.s. put imports before your code.

# File handling in python

# We can interact with files directly from within our app.
# This is useful for things like text files, JSON files, and even things that come in
# as binary streams such as images

# Open takes two arguments, one is optional.
# The first is the name of the file, if you want it to be created in the same directory as your .py file
# I can also give it a relative or even absolute file path. 

# The second thing we can optionally pass, is a mode.
# "r" - read - opens a file for reading. Will raise an exception if the files doesn't exist
# "w" - write - opens the file for writing. If the file exists - this will truncate the data within.
# "a" - append - opens the file for appending. If the file exists, it writes onto the end of the file.
# "x" - create - creates a file that we can work with later. Will raise an exception IF the file does exist. 

# By default, python assumes we are reading a file as text. To work with other kinds of non-text
# files - we can use Binary mode. 
# "rb" - read binary
# "wb" - write binary
# ... and so on. 
# This would be for working with .jpg or .png files or whatever.

# "w" and "a" modes will create a file silently if it doesn't already exist. 

my_file = open('./resources/test-file.txt', "a") 

my_file.write("\nHello... again!")

my_file.close() # Usually a good idea to close your file after you work with it. 


# If we don't want to worry about closing/disposing of resources... we can use a with block

with open("./resources/test-file.txt") as file:
    file_contents = file.read() # Read the contents of my file as a string.
    print(file_contents)
    
# Using the above auto-closes my file - you can use the with statement for any kind
# of disposable connection or resource.

# Working with JSON
# JSON files end in .json - though really they are just strings 
with open("./resources/json-test.json", "w") as jsonfile:
    # By default, the built in JSON module can map certain data types/default objects
    # Lists, Strings, Integers, Floats, Booleans, None.... and Dictionaries
    
    name_list = ["Jonathan", "Richard", "Jasdhir"] # Just a list to test our json.dumps
    
    json_names = json.dumps(name_list) # Converting that list to a json formatted string
    
    print(json_names) # printing it out to test
    
    print(jsonfile.__dict__)
    
    jsonfile.write(json_names)
    
    pancake = Dog("Malchi", 10, "white", "Pancake")
    
    # If we want to serialize anything beyond the aforementioned compatible types
    # we need to turn them into a dictionary first
    jsonfile.write(json.dumps(pancake.__dict__))
    
    
# Reading json from an existing file

with open("./resources/ellie.json", "r") as ellie_json:
    ellie = json.load(ellie_json) # Load vs Loads - json.load() expects things to come from a file
                                    # json.loads() can take any json string and de-serialize it 
    print(ellie)