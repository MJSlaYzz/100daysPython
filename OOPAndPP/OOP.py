#    ____  _     _           _           ____       _            _           _   _____                                               _             
#   / __ \| |   (_)         | |         / __ \     (_)          | |         | | |  __ \                                             (_)            
#  | |  | | |__  _  ___  ___| |_ ______| |  | |_ __ _  ___ _ __ | |_ ___  __| | | |__) | __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___  _ _ __   __ _ 
#  | |  | | '_ \| |/ _ \/ __| __|______| |  | | '__| |/ _ \ '_ \| __/ _ \/ _` | |  ___/ '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
#  | |__| | |_) | |  __/ (__| |_       | |__| | |  | |  __/ | | | ||  __/ (_| | | |   | | | (_) | (_| | | | (_| | | | | | | | | | | | | | | | (_| |
#   \____/|_.__/| |\___|\___|\__|       \____/|_|  |_|\___|_| |_|\__\___|\__,_| |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
#              _/ |                                                                               __/ |                                       __/ |
#             |__/                                                                               |___/                                       |___/ 

# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes 
# to organize and structure code in a way that models real-world entities and relationships.

#### Key Concepts

# 1. **Class**:
#    - A blueprint for creating objects.
#    - Defines attributes (data) and methods (functions) that the objects will have.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking.")

# 2. **Object**:
#    - An instance of a class.
#    - Represents a specific example of the class with actual values.
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
my_dog.bark()  # Output: Buddy is barking.


# 3. **Attributes**:
#    - Variables that belong to an object.
#    - Defined in the class using the `__init__` method.
#    - The __init__ method initializes the instance attributes make, model and year. 
# The self keyword is used to refer to the instance being created.
# self.make = make assigns the value of the make parameter to the instance attribute make.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


# 4. **Methods**:
#    - Functions that belong to a class.
#    - Used to define behaviors of the objects.
class Car1:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f"The engine of the {self.make} {self.model} is now running.")

# 5. **Inheritance**:
#    - A way to create a new class from an existing class.
#    - The new class (child) inherits attributes and methods from the existing class (parent).
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog2(Animal):
    def speak(self):
        print(f"{self.name} barks.")

my_dog = Dog2("Buddy")
my_dog.speak()  # Output: Buddy barks.


# 6. **Encapsulation**:
# - Bundling data (attributes) and methods that operate on the data into a single unit (class).
# - Use of private variables (with a single underscore `_`) to restrict access.
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Private variable
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age
my_friend = Person("Ahmed", 20)
# my_friend.set_age(20)
print(my_friend.get_age())

# 7. **Polymorphism**:
#    - Ability of different classes to be treated as instances of the same class through inheritance.
#    - Different classes can define the same method, which can be called in the same way.
class Bird:
    def fly(self):
        print("Bird is flying.")

class Airplane:
    def fly(self):
        print("Airplane is flying.")

def let_it_fly(flying_object):
    flying_object.fly()

bird = Bird()
airplane = Airplane()

let_it_fly(bird)  # Output: Bird is flying.
let_it_fly(airplane)  # Output: Airplane is flying.

### Summary
# - **Class**: Blueprint for objects.
# - **Object**: Instance of a class.
# - **Attributes**: Variables within a class.
# - **Methods**: Functions within a class.
# - **Inheritance**: Derive new classes from existing ones.
# - **Encapsulation**: Restrict access to methods and variables.
# - **Polymorphism**: Methods with the same name in different classes. 

# These concepts are fundamental to organizing and managing code in an object-oriented manner, making it more modular, reusable, and easier to maintain.