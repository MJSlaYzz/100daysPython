#    _____ _                 _____       _               _ _                       
#   / ____| |               |_   _|     | |             (_) |                      
#  | |    | | __ _ ___ ___    | |  _ __ | |__   ___ _ __ _| |_ __ _ _ __   ___ ___ 
#  | |    | |/ _` / __/ __|   | | | '_ \| '_ \ / _ \ '__| | __/ _` | '_ \ / __/ _ \
#  | |____| | (_| \__ \__ \  _| |_| | | | | | |  __/ |  | | || (_| | | | | (_|  __/
#   \_____|_|\__,_|___/___/ |_____|_| |_|_| |_|\___|_|  |_|\__\__,_|_| |_|\___\___|


### Class Inheritance in Python

# **Class inheritance** allows a class (called a child or subclass) to inherit attributes and methods from another class (called a parent or superclass). 
# This promotes code reuse and logical structure in your programs.

#### Key Concepts

# 1. **Parent Class (Superclass)**: The class whose attributes and methods are inherited.
# 2. **Child Class (Subclass)**: The class that inherits attributes and methods from the parent class.

#### Basic Syntax

class Parent:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr

    def parent_method(self):
        print("This is a method in the Parent class")

class Child(Parent):
    def __init__(self, parent_attr, child_attr):
        super().__init__(parent_attr)
        self.child_attr = child_attr

    def child_method(self):
        print("This is a method in the Child class")

# Creating an instance of the Child class
child_instance = Child("Parent Attribute", "Child Attribute")

# Accessing methods from both Parent and Child classes
child_instance.parent_method()  # Inherited method
child_instance.child_method()   # Child's own method


#### `super()` Function
# - The `super()` function is used to call the `__init__` method or other methods from the parent class.
# - Ensures that the child class inherits all the properties of the parent class.

#### Example

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

# Creating an instance of Dog
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)   # Output: Buddy
print(dog.breed)  # Output: Golden Retriever
print(dog.speak())  # Output: Buddy says Woof!


#### Benefits of Inheritance
# - **Code Reusability**: Reduces redundancy by reusing existing code.
# - **Logical Structure**: Creates a logical hierarchy and relationship between classes.
# - **Ease of Maintenance**: Easier to maintain and update code.

#### Notes
# - The child class can override methods from the parent class.
# - Multiple inheritance (a class inheriting from more than one parent class) is also possible, though it should be used with caution due to increased complexity.

### Summary

# - **Inheritance**: Allows one class to inherit attributes and methods from another.
# - **`super()`**: Calls the parent class's methods and constructors.
# - **Benefits**: Promotes code reuse, logical structure, and ease of maintenance.