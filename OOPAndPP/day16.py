# Day 16 #
# OOP: Object Oriented Programming

# Constructing objects and accessing their attributes and methods
# from the 'turtle' module we import the 'Turtle' class 
from turtle import Turtle, Screen

# Constructing object.
timmy = Turtle()
print(timmy)
# Calling methods that are associated to the object.
timmy.shape("turtle")
timmy.color("black", "green")
timmy.forward(100)
timmy.right(20)
timmy.forward(100)

my_screen = Screen()
# identify the Object(my_screen) and get the attribute(canvheight)
print(my_screen.canvheight)

# identify the Object(my_screen) and get the method(exitonclick())
my_screen.exitonclick()

#-*-*-*-*-*-*-*-*-*-*-*-*-*-

# download pages from https://pypi.org
# and Install via pip:
# type in terminal : "python -m pip install <package_name>" to install the package
# you can type "pip list" to see the list of packages you have installed
# you can type "pip show <package_name>" to see the location of the package.
# you can type "pip list -v" to get a List All Installed Packages and Their Locations.
# you can type "pip uninstall <package_name>" to Uninstall a Specific Package

from prettytable import PrettyTable

# create new objects
table = PrettyTable()
# use methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# use attributes / variable
table.align = "l"

print(table)
