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