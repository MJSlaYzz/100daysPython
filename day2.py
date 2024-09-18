# DAY 2 #

# Data Types

# String
# Subscripting: we can put a the index inside square brackets to get the letter at the index position.
# remember that index start at 0 not 1
string1 = "Hello"[3]
print(string1) # the output will be  = l
# numbers will not be treated as numbers if written as a String.
print("123" + "456") # the output will be = l23456

# Integer : numbers without any decimal places
int1 = 5
# you can replace commas in numbers such as: 123,254,368 with "_" to make it more readable
int2 = print(123_456_36) # the output will be = 12345636 # python will ignore the underscores 
# Float : numbers with decimal at one point point and they can hold a bigger number than int
float1 = 3.14159

# Boolean
# Booleans in Python should start with a capital letter : True or False
bool1 = True

# type checking
# type() is a method that shows the type of the data inside the brackets
print(type(bool1)) # the output will be = <class 'bool'>

# type conversion / type casting
num_char = len(input("what is your name?"))
new_num_char = str(num_char)
# without the conversion we would have got an error for using an integer
print("Your name has " + new_num_char + " characters.")

#If you want to comment multiple lines you can select all of them then press : Ctrl + /

# Mathematical operations
# addition
3 + 5
# subtraction
7 - 3
# multiplication
3 * 2
# division
# note division will always has a float as outcome even if the result of the division was a whole number such as 4 / 2
6 / 3
# power
2 ** 3 # which is 2 * 2 * 2

# operations priority :.
# PEMDAS :
# Parentheses ()
# Exponentiation 2 ** 3
# Multiplication 2 * 43
# Division 10 / 4
# Addition 8 + 3
# Subtraction 6 - 4

# (Multiplication and Division) (Addition and Subtraction) are equally important, 
# but the calculation that's most to the left is the one that will be prioritized.
print (3 * 3 + 3 / 3 - 3)
# so the order will be: 3 * 3 => 3 / 3 => 9 + 1 => 10 - 3 = 7

print(3 * (3 + 3) / 3 - 3)
# when using Parentheses the priority will change and the out put will change as well 
# so the order will be: (3 + 3) => 3 * 6 => 18 + / 3 => 6 - 3 = 3

# Number Manipulation
print(8 / 3) # output : 2.6666666666666665
# method 1 : using int() to chop off the rest of the numbers after the comma
print(int(8 / 3)) # output : 2
# method 2: using round() to round the number we have into a whole number
print(round(8 / 3)) # output : 3 because 2.6 is closer to become 3 than 2.
# you can specify the number of digits of precision you want to round the number to.
print (round(8 / 3, 2)) # output : 3.67 because we rounded it to 2 decimal places
# method 3: use the floor division //
print (8 // 3) # output : 2 just so it converts it to an Integer just like using the int() 

# shorthands
# From
score = 0
score = score + 2
score = score - 1
score = score * 1
score = score / 1
# To
score += 2
score -= 1
score *= 1
score /= 1

# F string : it makes mixing strings and different data types easy.
height = 1.8
isWinning = True
# From
print("your score is " + str(score) + " your height is " + str(height) + " your winning is " + str(isWinning))
# To
print(f"your score is {score}, your height is {height}, your winning is {isWinning}")

# sometimes when using round(),2 you will get result like 33.6 because there's nothing behind the .6 so we can use another format to get 2 digits after comma.
# using "{:.2f}".format()
# From
print(round(3360 / 100),2)        # output = 34.2
# To
print("{:.2f}".format(3360 / 100))  # output = 33.60

# using math.ceil() Method
# The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result.
import math
print(math.ceil(6.1)) # output = 7

# using math.floor() Method
# The math.ceil() method rounds a number Down to the nearest integer, if necessary, and returns the result.
print(math.floor(6.9)) # output = 6