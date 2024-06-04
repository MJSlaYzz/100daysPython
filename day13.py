# Day 13 #

# Debugging

# Debugging is the process of identifying, analyzing, and removing errors or bugs in your code. 
# Effective debugging is crucial for writing reliable and efficient programs.

# Common Debugging Techniques

# 1-Print Statements:
# Use print() statements to output variable values and program states at different points in your code.
# Helps to quickly identify where things are going wrong.
def add(a, b):
    print(f"a: {a}, b: {b}")  # Debugging line
    return a + b

result = add(3, 4)
print(f"Result: {result}")
# -*-*-*-*-*-*-*-*-*-*-*-*

# 2-Using a Debugger:

# Use an integrated development environment (IDE) with a built-in debugger like PyCharm, VS Code, or PDB (Python Debugger).
# Set breakpoints, step through the code, inspect variables, and evaluate expressions.
# debuggers that i use: Python Tutor, Thonny
# -*-*-*-*-*-*-*-*-*-*-*-*

# 3-Exception Handling:

# Use try and except blocks to catch and handle exceptions.
# This prevents your program from crashing and allows you to log error messages.
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
# -*-*-*-*-*-*-*-*-*-*-*-*

# 4-Logging:

# Use the logging module for more advanced and configurable logging compared to print statements.
# Helps to keep track of different levels of severity (e.g., debug, info, warning, error, critical).
import logging

logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f"a: {a}, b: {b}")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    logging.error(f"Error occurred: {e}")
# -*-*-*-*-*-*-*-*-*-*-*-*

# Tips for Effective Debugging

# Reproduce the Bug:
# Ensure you can consistently reproduce the bug. 
# This makes it easier to isolate and fix the issue.

# Simplify the Problem:
# Reduce the problem to a simpler version. 
# Remove unnecessary parts of the code to focus on the core issue.

# Check Assumptions:
# Verify that your assumptions about how the code should work are correct. 
# Often, bugs arise from incorrect assumptions.

# Divide and Conquer:
# Isolate sections of the code to find the problematic area. 
# Use a binary search approach: comment out half the code to see if the bug persists.

# Read Error Messages Carefully:
# Error messages often provide valuable information about what went wrong and where to look.

# Understand the Code:
# Ensure you fully understand the code you're debugging. 
# Read documentation, and comments, and understand the logic before making changes.

# Keep a Debugging Log:
# Maintain a log of what changes you make and what you observe. 
# This helps track your debugging process and avoid repeated mistakes.

# Stay Calm and Take Breaks:

# Debugging can be frustrating. 
# If you're stuck, take a break and return with a fresh perspective.
