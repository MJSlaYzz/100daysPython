# DAY 2 #

# writing a message:
print("Hello World!")

# Print Modifiers:
#error# print("She said: "Hello" and then left.")
# that line will cause an error because it includes "double quotes", and the way to deal with that is :
# 1st way: use single Quotes.
print('She said: "Hello" and then left.')
# 2st way: use excape backslash (\)
print("She said: \"Hello\" and then left.")

# A way to start a new line by using \n.
print("Hello World!\n")

# Concatenation.
print("Hello" + " " + "World!")

# errors to avoid:  you will get an error if you had a space before the line of code.


#enter data in the terminal / console
#input("A prompt for the user")
print("Hello " + input("What is your name ?\n"))

# the data type in input() is always a string so if you need to use it in mathematical equations you will have to convert it.
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second  number: "))
# and you will have to convert the int to string using str() because the print method can't have more than one different data type.
print("Your sum of your numbers is = " + str(num1 + num2))
# so you can print it right away like this:
print(num1 + num2)

#You can use len(" ") in order to get the length of the text inside the double quotes.
numOfLetters = len("Mostafa")
print("the length of the name Mostaafa is: " + str(numOfLetters) + " Letters.")

#len() only works with strings.
print(len(input("Write any word to get the length of it: ")))

# python variables
name = input("What is your name?")
print(name)
# you can cahgne the same variable data in the code
name = "Saif"
print("the new name is: " + name)
# make the code readable (give variables valid and reliable)
# do not use spaces in the variable name.
# you cannot use variable at the beginning of a variable name 
# you can't name variable with methods names such as print, input, etc.