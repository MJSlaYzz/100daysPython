# Day 10 #

# Functions with Outputs

# *-*-*-*-*-*-*-*-*-*-*-*-*-* #

# 1- Functions without Outputs

# Definition: Functions without outputs perform tasks but do not return a value.
# These functions can still print, modify variables, or have side effects, 
# but they do not use the `return` statement to send back a result.

# Basic Structure of a Function without Outputs:
def function_name():
    # Code block performing some task
    print("This function does not return a value.")

# Example 1: A function to print a greeting
def greet():
    print("Hello, welcome to the program!")

# Call the function
greet()

# Example 2: A function to update a global variable
counter = 0

def increment_counter():
    global counter #if we did not use the global keyword and just used parameters the value won't be updated.
    counter += 1
    print(f"Counter updated to {counter}")

# Call the function multiple times
increment_counter()
increment_counter()

# Example 3: A function to display information
def display_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

# Call the function with arguments
display_info("Alice", 30)

# Points to Remember:
# 1. Functions without outputs do not use the `return` statement.
# 2. They can still perform actions like printing, modifying variables, etc.
# 3. These functions are useful for tasks that don't require a result to be passed back.

print("*-*-*-*-*-*-*-*-*-*-*-*")

# 2- Functions with Outputs

# Definition: Functions with outputs are designed to perform tasks and return a value to the caller.
# These functions use the `return` statement to send a result back to where the function was called.

# Basic Structure of a Function with Outputs:
def function_name(parameters):
    # Code block performing some task
    result = 5 # some calculation or value
    return result

# Example 1: A function to add two numbers
def add_numbers(a, b):
    return a + b

# Call the function and print the result
sum_result = add_numbers(3, 5)
print(f"Sum: {sum_result}")

# Example 2: A function to square a number
def square_number(x):
    return x * x

# Call the function and print the result
square_result = square_number(4)
print(f"Square: {square_result}")

# Example 3: A function to get the length of a string
def string_length(s):
    return len(s)

# Call the function and print the result
length_result = string_length("Hello, world!")
print(f"Length: {length_result}")

# Example 4: A function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Call the function and print the result
even_check = is_even(7)
print(f"Is the number even? {even_check}")

# Points to Remember:
# 1. Functions with outputs use the `return` statement to send a value back to the caller.
# 2. The returned value can be used directly, stored in a variable, or passed to another function.
# 3. Functions can return any data type, including numbers, strings, lists, dictionaries, and even other functions.

# *-*-*-*-*-*-*-*-*-*-*-*-*-* #

# using the keyword title() to capitalize the first letter in each word.
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    print("This won't be printed, because reutrn keyword tells the computer that this is the end of the function.")

# so what the output does is that it replaces the function itself.
myName = format_name(input("What is your first name?"), input("What is your last name?"))

print("My name is " + myName) # output: My name is Mostafa Ebrahem

#*-*-*-*-*-*--------*-*-*-*-
# Docstrings

# Definition:
# Docstrings are special strings that are used to document a module, function, class, or method in Python. 
# They are placed immediately after the definition of a function, method, class, or module, enclosed in triple quotes """ """ or ''' '''.

# Purpose:
# Docstrings provide a convenient way of associating documentation with Python code. 
# They can be used to explain what a function, class, or module does, its parameters, return values, and other important details.
def add_numbers(num1, num2):
    """This Function takes two numbers as input and returns the sum of them."""
    # now when you hover over the function you will get that Docstring.
    return num1 + num2

# Recursion
# Definition: Recursion is a programming technique where a function calls itself in order to solve a problem. 
# Recursive functions solve complex problems by breaking them down into simpler sub-problems of the same type.

# Structure of a Recursive Function:
# Base Case: The condition under which the recursion ends. It prevents the function from calling itself indefinitely.
# Recursive Case: The part where the function calls itself with a modified argument, gradually moving towards the base case.

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)

# Example of using the recursive function
print(factorial(5))  # It will be 5 * 4 * 3 * 2 * 1 so the Output: 120

# note about converting
# you can not convert a float string directly to an int
# num = "2.5"
# num2 = int(num) # you will get an error here
# print(num2) 
# but you can convert it to float first
num = "2.5"
num2 = int(float(num))
print(num2)