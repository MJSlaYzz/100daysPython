#    ____  _     _           _         _          ____   ____  _____  
#   / __ \| |   (_)         | |       (_)        / __ \ / __ \|  __ \ 
#  | |  | | |__  _  ___  ___| |_ ___   _ _ __   | |  | | |  | | |__) |
#  | |  | | '_ \| |/ _ \/ __| __/ __| | | '_ \  | |  | | |  | |  ___/ 
#  | |__| | |_) | |  __/ (__| |_\__ \ | | | | | | |__| | |__| | |     
#   \____/|_.__/| |\___|\___|\__|___/ |_|_| |_|  \____/ \____/|_|     
#              _/ |                                                   
#             |__/                                                    

# Classes would be the blueprint (of how to build a ship for example) and Objects are instances of the classes (the different ships we build from that blueprint)
# In OOP, an object is a self-contained unit that contains data and methods to manipulate that data. 
# Objects are instances of classes, which define the structure and behavior of the objects.

# Key Characteristics of Objects
# 1- Attributes (Data)

# - Attributes are variables that belong to an object.
# - They represent the state or properties of the object.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Toyota", "Corolla", 2020)
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.year)  # Output: 2020

# 2- Methods (Functions)

# - Methods are functions that belong to an object.
# - They define the behavior or actions that the object can perform.

class Car2:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The engine of {self.year} {self.make} {self.model} is starting.")

my_car = Car2("Toyota", "Corolla", 2020)
my_car.start_engine()  # Output: The engine of 2020 Toyota Corolla is starting.

# 3- Encapsulation

# - Encapsulation means that the internal state of the object is hidden from the outside.
# - Access to the attributes and methods is controlled through public methods.
class Car3:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = 0  # Private attribute

    def drive(self, miles):
        if miles > 0:
            self._mileage += miles
            print(f"Driven {miles} miles. Total mileage: {self._mileage}")

my_car = Car3("Toyota", "Corolla", 2020)
my_car.drive(150)  # Output: Driven 150 miles. Total mileage: 150
my_car.drive(150)  # Output: Driven 150 miles. Total mileage: 300

# 4- Identity

# - Each object has a unique identity, even if multiple objects have the same attribute values.
# - Identity is typically represented by the object's memory address.
car1 = Car3("Toyota", "Corolla", 2020)
car2 = Car3("Toyota", "Corolla", 2020)
print(car1 == car2)  # Output: False, they are different instances
print(car1 is car2)  # Output: False, they have different memory addresses

# 5- Inheritance

# - Objects can inherit attributes and methods from other classes.
# - This allows for the creation of a hierarchy of classes and promotes code reuse.
class ElectricCar(Car3): # ElectricCar is a subclass of Car. This means ElectricCar inherits all the methods and attributes from the Car class.
    # The __init__ method of ElectricCar is used to initialize its own attributes (battery_size) as well as the inherited attributes (make, model, year).
    def __init__(self, make, model, year, battery_size):
        # super() is called within the __init__ method of the ElectricCar class to invoke the __init__ method of the Car class. 
        # This initializes the make, model, and year attributes in the ElectricCar object.
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def charge_battery(self):
        print(f"Charging the battery of {self.make} {self.model}.")

my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
my_electric_car.charge_battery()  # Output: Charging the battery of Tesla Model S.
my_electric_car.drive(150) # Output: Driven 150 miles. Total mileage: 150

#Example: Objects in a Real-world Context
# Consider a library system where you have different types of books. 
# Each book is an object, and the book's details (title, author, ISBN) are attributes. 
# The book can have methods like borrow and return_book.
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' is now borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' is now returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")

# Creating instances (objects) of the Book class
book1 = Book("1984", "George Orwell", "123456789")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")

# Borrowing and returning books
book1.borrow()  # Output: The book '1984' is now borrowed.
book1.return_book()  # Output: The book '1984' is now returned.
