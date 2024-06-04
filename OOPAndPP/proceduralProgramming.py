#   _____                        _                 _   _____                                               _             
#  |  __ \                      | |               | | |  __ \                                             (_)            
#  | |__) | __ ___   ___ ___  __| |_   _ _ __ __ _| | | |__) | __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___  _ _ __   __ _ 
#  |  ___/ '__/ _ \ / __/ _ \/ _` | | | | '__/ _` | | |  ___/ '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
#  | |   | | | (_) | (_|  __/ (_| | |_| | | | (_| | | | |   | | | (_) | (_| | | | (_| | | | | | | | | | | | | | | | (_| |
#  |_|   |_|  \___/ \___\___|\__,_|\__,_|_|  \__,_|_| |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
#                                                                       __/ |                                       __/ |
#                                                                      |___/                                       |___/ 

### Procedural Programming

# Procedural Programming is a programming paradigm that uses a sequence of well-structured procedures (functions) and steps to compose a program. 
# It focuses on a linear top-down approach and the concept of procedure calls, where functions are used to perform operations.

#### Key Concepts

# 1. **Procedures (Functions)**:
#    - Blocks of code that perform a specific task.
#    - Can be called (invoked) to execute the task whenever needed.
   

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!


# 2. **Linear Execution**:
#    - The program is executed in a sequential manner from top to bottom.
   

def step_one():
    print("Step one executed")

def step_two():
    print("Step two executed")

step_one()
step_two()
# Output:
# Step one executed
# Step two executed


# 3. **Modularity**:
#    - Code is divided into smaller, manageable functions or procedures.
#    - Enhances readability, maintainability, and reusability.

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result = add(2, 3)
print(result)  # Output: 5
result = multiply(2, 3)
print(result)  # Output: 6

# 4. **Local and Global Variables**:
#    - Local variables are defined inside functions and are not accessible outside.
#    - Global variables are defined outside functions and can be accessed globally.


global_var = "I am global"

def func():
    local_var = "I am local"
    print(global_var)
    print(local_var)

func()
# Output:
# I am global
# I am local


# 5. **Parameter Passing**:
#    - Functions can take parameters (arguments) to operate on different values.
   

def subtract(a, b):
    return a - b

result = subtract(5, 3)
print(result)  # Output: 2

# 6. **State Management**:
#    - Functions operate on data and modify states through parameters or global variables.

count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
increment()
print(count)  # Output: 2

#### Advantages
# - **Simplicity**: Easy to understand and implement.
# - **Modularity**: Functions allow code reuse and better organization.
# - **Ease of Debugging**: Functions can be tested individually.

#### Disadvantages
# - **Scalability Issues**: As programs grow, managing and maintaining the code becomes challenging.
# - **Global State Management**: Extensive use of global variables can lead to unintended side effects.

### Example

# Here’s a simple example of procedural programming to calculate the factorial of a number:

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
print(f"The factorial of {number} is {factorial(number)}")
# Output: The factorial of 5 is 120


# Function And Procedures:
# In Python, the distinction between functions and procedures is not explicit. Python uses functions to achieve both behaviors.

# Function-like Behavior:

# When a Python function returns a value, it behaves like a traditional function.
# Example:
def multiply1(a, b):
    return a * b

product = multiply(4, 5)
print(product)  # Output: 20


# Procedure-like Behavior:

# When a Python function does not return a value, it can be thought of as a procedure.
# Example:

def greet1(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!


### Summary

# - **Procedural Programming** is a paradigm that relies on functions and procedures to operate on data.
# - **Functions** are the building blocks, performing specific tasks and promoting code reuse.
# - It follows a **linear execution** model, with a focus on breaking down tasks into smaller procedures.

# This paradigm is widely used in programming, especially for simple and small-scale applications where a straightforward approach is sufficient.