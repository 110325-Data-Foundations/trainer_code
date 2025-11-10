# Last week we saw inheritance between two "concrete" classes
# Both these classes provided for object instantiation as well as method implementation

# In order to use Abstract classes, I need to import ABC (Abstract Base Class)
from abc import ABC, abstractmethod

# What if, I wanted a class to enforce developer behavior BUT not allow for implementation? 

class Vehicle(ABC):
    
    # Abstract method: A method that needs to be implemented by any child classes. We don't provide for implementatio
    # within our abstract class
    @abstractmethod # This decorator lets the interpreter know that this method is abstract
    def move():
        pass # This is just a placeholder for a null operation - essentially telling the interpreter nothing happens
            # here ON PURPOSE
    
    # Unlike the abstract method above, this method is concrete - any children will inherit this default implementation
    # They can override it if they want to. 
    def breakdown(): 
        print("Something's gone wrong")
        
    # Since we don't have an __init__ we can't create abstract properties the way we'd probably expect to.
    # We have to make use of decorators. 
    @property
    @abstractmethod # things are getting a little weird...
    def vin(self): # This is how I would create an abstract property
        pass # It looks like an abstract method but with the property decorator layered on top
    

class Car(Vehicle):
    
    def __init__(self, make, model, year, value, vin):
        self.make = make
        self.model = model
        self.year = year
        self.value = value
        self._vin = vin # Notice, no super() call here - Vehicle never overrode __init__()

    # Providing implementation for move()
    def move():
        print("We start driving down the road. Good luck!")
        
    # Providing implementation for abstract properties is a little less straightforward - which is why you probably
    # want to keep them to a minimum. 
    @property # We need the @property decorator - because this is going to look like a method.
    def vin(self):
        self._vin # Kind of ugly IMO - but this is how Python provides for Abstract Properties
        # Take it in from the __init__, set it like normal, then define what appears to be a getter method

my_car = Car("Toyota", "Prius", 2020, 500000, "123FDS3FDS54DF")

print(my_car.__dict__)

my_car._vin # Despite the fact that the underscore technically means internal or protected: python doesn't care. 


class Animal:
    
    def __init__(self, name, age, species, protected_secret, private_secret):
        self.name = name
        self.age = age
        self.species = species # This is just public - the default 
        self._protected_secret = protected_secret # This underscore is a convention. It is not enforced by the interpreter. Its for us.
        self.__private_secret = private_secret # This double underscore is python's version of "private" - this is actually
        # enforced by the interpreter as best it can. 
        
        # Under the hood, the __field uses name mangling. It just automatically alters the name of this property
        # my_animal.__super_secret - NOT VALID
        # my_animal._Animal__super_secret - this is the post name-mangling name of the property 