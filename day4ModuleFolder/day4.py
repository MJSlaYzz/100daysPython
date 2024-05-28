# Day 4 #

# Randomisation
import random # we need to import the random module before using it.

random_integer = random.randint(1, 10)
print(random_integer)

# using random.choice() to choose a random element from a non-empty sequence
randomLetters = ['l', 'x', 'g', 'f']
print("The random letter is: " + random.choice(randomLetters))

# using random.shuffle() to randomise the order of elements in a list
print(randomLetters)
random.shuffle(randomLetters)
print(randomLetters)

# What is a module ?
# codes are splited into diffrent modules, with each module responsible for a diffrent bit of functionality.
# so the random module was made to make it easier for the user generate random values,
# without the need to get into the complexities of all the math that's required to generate pseudorandom

# modules in phython are similar to namespaces in C#
# When you import a module in Python, the entire module is executed. 
# This means that any top-level code in the module, including print statements, will be executed when the module is imported.
import day4ModuleTest # importing a module
print(day4ModuleTest.piText) # importing a variable from a module
# module has to be in the same folder.
# This method returns the next random floating point number between [0.0 to 1.0) 1 not included.
random_float = random.random()
print(random_float)

# but it only get a float number between 0 and 1, if we need the number to be between 0 and 5 for example we will have to multiply it by 5
print(random_float * 5)


#Python Lists
# the list is a data structure : a way of organizing and storing data
fruits = ["Mango","Strawberry"]
# items in the list can have diffrent data types
nameAndAge = ["Mostafa", 26]
print(nameAndAge)
# but the syntax is important : name = [iteam1, iteam2]
# you can use lists to store many pieces of related data but also have an order
# the order is determined by the order in the list.

# if you want to get a piece of data according to its position in the list, you can use it:
# remember that the first item is always at position 0.
numbers = [0,1,2,3,4,5,6,7,8,9]
# you can store those data in other variables
numberSeven = numbers[7]
print(numberSeven)

# using minus numbers :
numberMinusOne = numbers[-1] #the output will be: 9 which the last number in the list or first from the other side. 
print(numberMinusOne)

#using .index() : it returns index of the vale
fruitsIndex = fruits.index("Mango") # output = 0
print(f"Fruit index = {fruitsIndex}")

# change items in the list :
numbers[8] = 88
print(numbers[8])

# add items to the list
numbers.append(10)
print(numbers[-1]) #the out put should be 10 now because it's added to the end of the list

# adding a list to our list
numbers.extend([11,12,13,14,15])
print(numbers)

# removing item from the list
numbers.pop(0)
print(numbers)

# challange to chose a random name out of a list

# using The split() function to split the input strings into a list.
# names_string = input("Enter your names please and use a coma to sperate them: ")
# names = names_string.split(", ") # we are using (", ") comma, followed by a space, as a separator.
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
print(names)
# using len() function to get the number of items in the list.
namesAmount = len(names) 
# using -1 because the random starts at 0 so if we had 10 items then the last one should be at position 9 or we will get the index out of range error.
randomNum = random.randint(0, namesAmount - 1) 
theChosenOne = names[randomNum]
print(f"{theChosenOne} is going to buy the meal today!")

# using the list() function. 
# This function takes an iterable (like a string) and converts it into a list of its elements (characters, in the case of a string).
testName = "Mohamed"
testNameChar = list(testName)
print(testNameChar) # output = ['M', 'o', 'h', 'a', 'm', 'e', 'd']

# using the join() function
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator. 
testName2 = ''.join(testNameChar)
print(f"the name {testName2} is back as a string after using the Join() function")

# Nested List

boysNames = ["Ahmed", "Mohamed", "Tarik"]
girlsNames = ["Mayaar", "Mona", "Hala"]

allNames = [boysNames, girlsNames]
print(allNames)
print(allNames[1][1]) # [index of first list][index of second list]

#  triple quotes (''' or """) are used primarily for three purposes:

# 1/ Multi-line Strings: They allow you to create strings that span multiple lines without using newline characters (\n). 
multi_line_string = """This is a multi-line string.
It can span multiple lines.
Here is another line."""
print(multi_line_string)
# 2/ Docstrings: They are used to write documentation for modules, classes, functions, and methods.
# 3/ Commenting Out Blocks of Code: Triple quotes can also be used to temporarily comment out blocks of code during development and debugging.
'''
print("This is a comment and won't be printed!")
'''

# using the sum() Function 
# The sum() function returns a number, the sum of all items in an iterable. 
# It only works with numbers
a = (1, 2, 3, 4, 5)
print(sum(a))
b = (1.3, 2.5, 3.2, 4.1, 5.5)
print(sum(b))

# using the max() Function
# The max() function returns the item with the highest value, or the item with the highest value in an iterable.
c = (25,30,-5,36,15,300)
print(max(c)) # output = 300
# using the min() Function to do the opposite
print(min(c)) # output = -5


# The right way to copy a list :
list1 = ["A", "B", "C"]
list2 = list1
# list1 is assigned directly to list2, meaning both variables refer to the same list. 
# Therefore, any changes made to encryptedLetters will also affect letters.
# To solve this, you need to create a copy of the list1 list when assigning it to list2:

# Slicing ([:]): Creates a shallow copy of the list.
list2 = list1[:]
# list() Constructor: Also creates a shallow copy of the list.
list2 = list(list1)
# copy() Method: Another way to create a shallow copy of the list.
list2 = list1.copy()
