# Day 6 #

# Functions & Karel

# built in functions:
# the print() function or the len() function
print("hello")
print(len("hello"))

# making new functions:
# by using the key word def
# a function can hold a bunch of steps that can be used anywhere in the code.
def my_function(): # what differentiates a function from a variable is the parentheses.
    print("Hello!")
    print("Bye")
# Nothing in the function will be called until it gets executed!!

# calling a function
my_function()

# Indentation
# Unlike C# where you use parentheses () to tell the program where the statement starts and ends, in python we use Indentation to do the same job.
# To indent the selected lines of code (move them right or left) hold CTRL + [ or CTRL + ]
# def my_function():
# ....print("Hello!")

# you can use space or Tab to indent
# 1 tab = 4 spaces
# you don't need to use 1 tab or 4 spaces to make one Indentation, a single space is enoguh but we use 4 to make it more readable


# While Loops

# while something_is_true:
#    Do something repeatedly

numbers = 6
while numbers > 0:
    print(f"numbers = {numbers}")
    numbers -= 1
    # you can use break to get out of the while loop even if the condition isn't met
    if numbers == 3:
        break

# using Negation
# while someting() != True
# while something() == false
# while not somthing() 

# FOR VS WHILE LOOPS

# For Loops
# Use for loops when:
# Iterating over a sequence (list, tuple, string, etc.).
# The number of iterations is known or fixed.

# While Loops
# Use while loops when:
# Iteration depends on a condition.
# The number of iterations is unknown.
# More likely to become infinite loops if the condition is never met.