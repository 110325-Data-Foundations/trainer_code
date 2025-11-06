
#Flow Control in Python

# For
# While
# Do-while 
# If-else
# Switch 
# Try-except... can also function as flow control, more exception handling

#For Loops

class_pets = ["pancake", "ellie", "eddie", "ollie", "ketchup", "tripod"]

# The main use of the for loop in Python is iterating through a collection
# For x in collection... execute some code.
for pet in class_pets:
    print(pet)
    
# If you want the behavior of a c-style For-Loop, you can use range()
for i in range(0, 10):
    print(i)
    
# Adding an else statement to a for loop
# Can be used to confirm that the for loop executed successfully
for i in range(0,7):
    if i == 6:
        break
else:
    print("If completed")
    
# While

count = 0

while(count < 5):
    print("From the while loop")
    count += 1 # += is a shorthand for count = count + 1
    
# If we need to, we can nest loops, and mix and match them 
# If you find yourself 3 or more loops deep... there's probably a better way.

# If-else
# We check a condition, and if it's true - run the if block code
# Otherwise, run the else block code

condition = True

if condition:
    print("From the if-block")
else:
    print("From the else block")

# You can check multiple conditions sequentially using elif
# Chain as many as you want or need - optionally ending with an else
# in case none of the conditions are met.
if condition:
    print(1)
elif (4 > 9):
    print("How'd we get here?")
else:
    print("Hmmmm?")
    

# Match-case (In other languages, this is called Switch). New to 3.10.

print("Please enter a selection (1-3): ")
choice = input()

match choice:
    case "1":
        print("Selected option 1")
    case "2":
        print("Selected option 2")
    case "3":
        print("Selected option 3")
    case _: # Default case - if none above are matched
        print("You failed to select 1-3 somehow")

