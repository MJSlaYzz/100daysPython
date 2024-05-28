# Day 3 #

# If Statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
# else should be written at the same indentation level as the if statement.    
else:
    print("Sorry, you have to grow taller before you can ride.")

# Comparison Operators
# Operator: >  || Meaning: Greater than
# Operator: <  || Meaning: Less than
# Operator: >= || Meaning: Greater than or equal to
# Operator: <= || Meaning: Less than or equal to
# Operator: == || Meaning: Equal to
# Operator: != || Meaning: Not equal to

# when using one equal sign it means that you are assigning a value to a variable
# but when using two equal signs it means that you are checking if the value on the left is equal to the value on the right

# the way to define even numbers from odd numbers by using %.
# 4 / 2 = 2 and nothing remains so 4 % 2 = 0 so it's an even number.
# 4 / 3 = 1.333333333 and there's a remaining number so 4 % 3 = 1 so it's an odd number.

# Nested If Statement: and If statement within another If statement
height1 = int(input("What is your height in cm? "))
if height1 >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 5$")
    elif age <= 18:
        print("Please pay 7$")
    else:
        print("Please pay 12$")
# else should be written at the same indentation level as the if statement.    
else:
    print("Sorry, you have to grow taller before you can ride.")

#Check Leap year challange.
year = int(input("What year is it? "))
if year % 4 == 0: # on every year that is divisible by 4 with no remainder.
  if year % 100 == 0: # except every year that is evenly divisible by 100 with no remainder.
    if year % 400 == 0: # unless the year is also divisible by 400 with no remainder.
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

# Multiple If Statements
# used to check an answer, no matter what the previous answer was, without having to check the for the same answer in each age if statement.
# so no matter what your age was you will be asked the photo question.
bill = 0
height2 = int(input("What is your height in cm? "))
if height2 >= 120:
    print("You can ride the rollercoaster!")
    age1 = int(input("What is your age? "))
    if age1 < 12:
        bill = 5
        print("Child tickets cost 5$")
    elif age1 <= 18:
        bill = 7
        print("Youth tickets cost 7$")
    else:
        bill = 12
        print("Adult tickets cost 12$")
    # the Multiple If Statement has to be at the same indentation level as the age if block.
    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
       bill += 3
       print(f"Your final bill is {bill}$")
    elif wants_photo == "N":
       print("You missed a good memory")
    else:
       print("Invalid input.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Logical Operators
# A And B
# if A and B are true or A and B are false then it's true, else it's false
# C Or D
# if A or B is true or A and B are true then it's true, else it's false
#  Not E
# if E is not true then it's true, else it's false
bill1 = 0
isElder = False
height3 = int(input("What is your height in cm? "))
if height3 >= 120:
    print("You can ride the rollercoaster!")
    age2 = int(input("What is your age? "))
    if age2 < 12:
        bill1 = 5
        print("Child tickets cost 5$")
    elif age2 <= 18:
        bill1 = 7
        print("Youth tickets cost 7$")
    elif age2 > 18 and age2 < 45:
        bill1 = 12
        print("Adult tickets cost 12$")   
    elif age2 >= 45 and age2 <= 55:
        isElder = True
        print("Elder tickets are free!")
    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        if not isElder:
            bill1 += 3
            print(f"Your final bill is {bill1}$")
        else:
          print(f"Your Photo is on us ^^") 
    elif wants_photo == "N":
       print("You missed a good memory")
    else:
       print("Invalid input.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Love Story Challange: To work out the love score between two people:

# 1- Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2- Then check for the number of times the letters in the word LOVE occurs.
# 3- Then combine these numbers to make a 2 digit number.

print("Welcome to The Love Calculator")
name1 = input("Please enter your name? ") # What is your name?
name2 = input("Please enter their name? ") # What is their name?
print("The Love Calculator is calculating your score...")
combineNames = name1 + name2
# using lower() to lower case the string, because for the computer Y and y are not the same.
lowerCaseNames = combineNames.lower()
totalScore = 0
trueScore = 0
loveScore = 0
letters = ['t','r','u','e','l','o','v']
# using count() to return the number of times the value in brackets appears in a list.
trueScore += lowerCaseNames.count("t")
trueScore += lowerCaseNames.count("r")
trueScore += lowerCaseNames.count("u")
trueScore += lowerCaseNames.count("e")
loveScore += lowerCaseNames.count("l")
loveScore += lowerCaseNames.count("o")
loveScore += lowerCaseNames.count("v")
loveScore += lowerCaseNames.count("e")
totalScore = (trueScore *10) + loveScore
# another way to calculate totalScore:
#totalScore = int(str(trueScore) + str(loveScore))
if totalScore < 10 or totalScore > 90:
  print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif totalScore >= 40 and totalScore <= 50:
  print(f"Your score is {totalScore}, you are alright together.")
else:
  print(f"Your score is {totalScore}.")
