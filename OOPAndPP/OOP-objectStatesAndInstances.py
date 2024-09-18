#    ____  _     _           _      _____ _        _                              _   _____           _                            
#   / __ \| |   (_)         | |    / ____| |      | |                            | | |_   _|         | |                           
#  | |  | | |__  _  ___  ___| |_  | (___ | |_ __ _| |_ ___  ___    __ _ _ __   __| |   | |  _ __  ___| |_ __ _ _ __   ___ ___  ___ 
#  | |  | | '_ \| |/ _ \/ __| __|  \___ \| __/ _` | __/ _ \/ __|  / _` | '_ \ / _` |   | | | '_ \/ __| __/ _` | '_ \ / __/ _ \/ __|
#  | |__| | |_) | |  __/ (__| |_   ____) | || (_| | ||  __/\__ \ | (_| | | | | (_| |  _| |_| | | \__ \ || (_| | | | | (_|  __/\__ \
#   \____/|_.__/| |\___|\___|\__| |_____/ \__\__,_|\__\___||___/  \__,_|_| |_|\__,_| |_____|_| |_|___/\__\__,_|_| |_|\___\___||___/
#              _/ |                                                                                                                
#             |__/                                                                                                                 

### Object-Oriented Programming (OOP) Notes: Object States and Instances

#### Objects
# - **Definition**: An object is an instance of a class. It represents a real-world entity with attributes and behaviors.
# - **Attributes**: These are variables contained in an object that store information about the object.
# - **Methods**: These are functions defined within a class that describe the behaviors of the object.

#### States
# - **Definition**: The state of an object is defined by the values of its attributes at a particular moment.
# - **Changing State**: The state of an object can change when its attributes are modified, typically through methods.
# - **Example**:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age
        self.age += 1

my_dog = Dog("Rex", 5)
print(my_dog.age)  # Output: 5
my_dog.birthday()
print(my_dog.age)  # Output: 6

# In this example, the state of `my_dog` changes when the `birthday()` method is called, increasing its age.

#### Instances
# - **Definition**: An instance is a concrete occurrence of any object, created based on the blueprint provided by the class.
# - **Creating Instances**: Instances are created by calling the class itself as if it were a function.
# - **Example**:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)

# Here, `car1` and `car2` are instances of the `Car` class, each with its own state (attributes).

#### Differences Between Class and Instance
# - **Class**: A blueprint or template for creating objects. Defines a type of object according to the attributes and methods.
# - **Instance**: A single, unique object created from a class, with its own specific data.

#### Example to Illustrate States and Instances
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Creating instances
account1 = BankAccount("Alice")
account2 = BankAccount("Bob", 100)

# Checking initial states
print(account1.balance)  # Output: 0
print(account2.balance)  # Output: 100

# Changing states
account1.deposit(50)
account2.withdraw(30)

# Checking updated states
print(account1.balance)  # Output: 50
print(account2.balance)  # Output: 70

# In this example, `account1` and `account2` are instances of the `BankAccount` class, and their states change when `deposit` and `withdraw` methods are called.

### Summary
# - **Objects**: Instances of classes representing entities with attributes and methods.
# - **States**: Defined by the values of an object's attributes at any given time.
# - **Instances**: Concrete occurrences of objects created from classes, each with its own state.