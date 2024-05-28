# Day 5 #

# Loops

# For Loops : used to do something to each item
# for item in list_of_items:

fruites = ["Apple", "Peach", "Pear"]
for fruit in fruites:
    print(fruit)
    print(fruit + " Pie")

# using the range() Function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
x = range(6) # it will stop before reaching 6 so it will stop at 5
for n in x:
  print(n)
for n in range(0,6): # n is the number that will happen 6 times from 0 to 5 and each time will increase by one.
  print(str(n) + " wow")

# using range() Function with steps
# the steps number indicates how much of a difference we made with each loop.
# we will increase the number each time by [steps] amount.
for n in range(0,6,2): # the output will be 0, 2, 4
  print(str(n))

import random
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

target = nr_letters + nr_symbols + nr_numbers
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easyPassword = ""
for x in range(1, nr_letters + 1):
  easyPassword += letters[random.randint(0,len(letters) - 1)]
for y in range(1, nr_numbers + 1):
  easyPassword += numbers[random.randint(0,len(numbers) - 1)]
for z in range(1, nr_symbols + 1):
  easyPassword += symbols[random.randint(0,len(symbols) - 1)]
print(easyPassword)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hardPassword = ""
tempEasyPassword = list(easyPassword)
randomNum = 0
for p in range(0, target):
  randomNum = random.randint(0, len(tempEasyPassword) - 1)
  hardPassword += tempEasyPassword[randomNum]
  tempEasyPassword.pop(randomNum)
print(hardPassword)


