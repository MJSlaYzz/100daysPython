# Day 18 #

# Turtle & the Graphical User interface (GUI)

from turtle import Turtle, Screen
import random
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("black","green")

#creating a square 
# for n in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# ways of importing modules:

# 1- import...
# import Turtle
# timmy_the_turtle = turtle.Turtle()

# 2- from...import...
# from turtle import Turtle
# timmy_the_turtle = Turtle()

# 3- from...import *  # by using asterisks you import everything from that module, but then it will make it hard to check where every class, method, etc came from.
# from turtle import *
# timmy_the_turtle = Turtle()
# forward(300)

# 4- import...as.... # Aliases modules (assigning names to the modules)
import turtle as t
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("black","green")

# 5- Installing Modules packages.
# from pypi.org by example you can get the installation code to write in the terminal
# like <$ pip install heroes> for example
# import heros
# and those packages are going to be installed in the venv/virtual environment folder
# you can setup a virtual environment by typing <python -m venv venv> in the terminal (<python -m venv <name of the venv>)
# to resolve the Execution Policies issue:
# run in the terminal the following script: <Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser>
# then type in terminal <name of the venv>\Scripts\activate

# and you can use CTRL + Shit + P to select the interpreter then select the (ven ven)
# but the reason to have a virtual environment is when you are dealing with code from python 2 and you add code from python 3 to it, it won't work


#creating a dashed line 
# for n in range(10):
#     timmy_the_turtle.pencolor("Black")
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pencolor("White")
#     timmy_the_turtle.forward(10)
# timmy_the_turtle.pencolor("Black")

# (OR)

# timmy_the_turtle.left
# for n in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#*-*-*-*-*-*-*-*-
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# angle = 360
colors = ["medium spring green", "spring green", "lime green", "green", "forest green", "dark green", "green yellow", "chartreuse"]
# for i in range(8):
#     timmy_the_turtle.color(random.choice(colors))
#     number_of_sides = i + 3
#     new_angle = angle/number_of_sides
#     for a in range(number_of_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(new_angle)
#     timmy_the_turtle.color(random.choice(colors))

# Draw a random walk
# def chose_direction(steps):
#     randNum = random.randint(0, 2)
#     if randNum == 0:
#         return timmy_the_turtle.forward(steps)
#     elif randNum == 1:
#         return timmy_the_turtle.right(90), timmy_the_turtle.forward(steps)
#     else:
#         return timmy_the_turtle.left(90), timmy_the_turtle.forward(steps)

# timmy_the_turtle.speed(7)
# timmy_the_turtle.pensize(7)
# for i in range(100):
#     timmy_the_turtle.color(random.choice(colors))
#     chose_direction(30)

# Or

# direction = [0, 90 ,180, 270]
# def chose_direction(steps):
#     return timmy_the_turtle.forward(steps), timmy_the_turtle.setheading(random.choice(direction))

# timmy_the_turtle.speed(7)
# timmy_the_turtle.pensize(7)
# for i in range(100):
#     timmy_the_turtle.color(random.choice(colors))
#     chose_direction(30)


# Tuples: 
# my_tuple = (1, 3, 8)
# print(my_tuple[1]) # Output = 3
# so the tuple is just like a list, the only difference is that you can not change the items inside of it.


# change color mode to RGB:
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# direction = [0, 90 ,180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(direction))


# make a spirograph
timmy_the_turtle.speed("fastest")
# for n in range(50):
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.right(n)
#     timmy_the_turtle.color(random_color())

# OR
def draw_spirograph(size_of_gap):
    for n in range(int(360/size_of_gap)): # to have the starting point = ending point
        direction = timmy_the_turtle.heading()
        timmy_the_turtle.setheading(direction + size_of_gap)
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
draw_spirograph(10)
















screen = Screen()
screen.exitonclick()