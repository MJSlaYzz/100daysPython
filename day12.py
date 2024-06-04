# Day 12 #

# Scope and number guessing game

# What is Scope?
# Scope refers to the region of a program where a variable is accessible. 
# In Python, the scope of a variable determines where that variable can be used within the code.
# -*-*-*-*-*-*-*-*-*-*-*-*

# Types of Scope:
# Local Scope: Variables created inside a function. These variables are only accessible within that function.
def my_function1():
    x = 10  # Local variable
    print(x)  # Accessible within the function

my_function1()
# print(x)  # Error: x is not defined outside the function
# -*-*-*-*-*-*-*-*-*-*-*-*

# Global Scope: Variables created outside of all functions. These variables are accessible anywhere in the code.
y = 20  # Global variable

def my_function2():
    y = 500
    print(y)  # Accessible inside the function
    # output = 500

my_function2()
print(y)  # Accessible outside the function
# output = 20 but the function can not change the value of the variable outside of the it.
# -*-*-*-*-*-*-*-*-*-*-*-*

# Enclosing Scope: Variables in the local scope of enclosing functions. This applies to nested functions.
def outer_function1():
    z = 'outer'
    
    def inner_function1():
        print(z)  # Accesses 'z' from the outer function's scope

    inner_function1()

outer_function1()
# inner_function1() # Error: name 'inner_function1' is not defined
# you can not call the inner_function1() outside of the outer_function1()
# -*-*-*-*-*-*-*-*-*-*-*-*

# Built-in Scope: Names that are preassigned in Python. This includes functions like print(), len(), etc.
# -*-*-*-*-*-*-*-*-*-*-*-*

# Scope Rules: LEGB
# Python follows the LEGB rule to resolve the scope of a variable:

# L: Local – Names assigned within a function.
# E: Enclosing – Names in the local scope of enclosing functions (nested functions).
# G: Global – Names assigned at the top-level of a module or declared global in a def within the file.
# B: Built-in – Names preassigned in Python.
# -*-*-*-*-*-*-*-*-*-*-*-*

# Global Keyword Example:
g = 20

def my_function3():
    global g
    g = 30  # Modifies the global variable
    print(g)  # 30

my_function3()
print(g)  # 30
# -*-*-*-*-*-*-*-*-*-*-*-*

# It is recommended to (NOT) (modify) global variables using global Keyword, but it's better to use return Keyword to avoid creating bugs. 
# For Example:
r = 60

def my_function4():
    global r
    r += 5  # Modifies the global variable
    return r

print(r)  # 60
r = my_function4()
print(r) # 65
# -*-*-*-*-*-*-*-*-*-*-*-*

# Use upercase letters to define constant variables or variables that you do not want to modify, for example:
PI = 3.14159
URL = "https://google.com"
TWITCH_NAME = "@BunnyFufu"
# -*-*-*-*-*-*-*-*-*-*-*-*

# Nonlocal Keyword Example:
def outer_function2():
    n = 'outer'
    
    def inner_function2():
        nonlocal n
        n = 'inner'  # Modifies the variable in the enclosing scope
        print(n)  # 'inner'

    inner_function2()
    print(n)  # 'inner'

outer_function2()
# -*-*-*-*-*-*-*-*-*-*-*-*

# Block Scope in Python:

# What is Block Scope?
# Block scope refers to the scope of variables declared inside blocks such as loops, if statements, etc. 
# In many programming languages, variables declared within a block (enclosed by {}) are not accessible outside that block. 
# However, Python handles block scope differently.

# Python's Block Scope Behavior
# In Python, block scope does not apply to variables declared within loops, if statements, and other block structures. 
# Instead, Python has function scope, meaning variables declared within a function are local to that function.

# Examples
# No Block Scope in Python:
if True:
    h = 10  # Variable 'h' declared inside an if statement
print(h)  # 'h' is accessible outside the if statement and prints 10

for i in range(5):
    o = i  # Variable 'o' declared inside a for loop
print(o)  # 'o' is accessible outside the for loop and prints 4
# -*-*-*-*-*-*-*-*-*-*-*-*
