# Day 7 #

# Flowchart programming:

# Flowchart programming involves using flowcharts to represent the logic and flow of a program or algorithm visually. 
# Flowcharts use different symbols to denote different types of actions or steps, 
# making it easier to understand and plan out the structure of a program. 
# They help in illustrating the sequence of operations, decisions, and loops in a program.

# Key Symbols in Flowcharts:
# - Oval: Start/End
# - Rectangle: Process/Action
# - Diamond: Decision/Branching
# - Parallelogram: Input/Output
# - Arrow: Flow of Control

# Benefits of Flowchart Programming :
# Clarity: Provides a clear visual representation of the logic.
# Communication: Helps in explaining the program to others.
# Problem-Solving: Makes it easier to identify logical errors and inefficiencies.
# Planning: Assists in planning the structure before coding.

# HANGMAN Game

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
import hangmanStages
# first way to import a variable by using import then assigning the variables to another variable in this module.
import hangmanWords
word_list = hangmanWords.word_list
hints_list = hangmanWords.hints_list
stages = hangmanStages.stages
# second way to import a variable by using from [name of the module] and then use import [name of the variable].
from hangmanStages import logo
lives = 6
index = 0
letterExisted = False
hintGotPrinted = False
chosen_word = random.choice(word_list)
blanks = "-" * len(chosen_word)
blanksList = list(blanks)
print(logo + "\n")
print("You can type \'@\' to see the Hint!")
print(blanksList)
#print(f"The Choosen word is: {chosen_word}")
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while lives > 0:
    guess = input("Please guess a letter: ").lower()
    guess_was_right = False
    index = 0
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
    for letter in chosen_word:
      if guess == '@' and not hintGotPrinted:
         # getting the index of the chosen_word in the word list.
         wordIndex = word_list.index(chosen_word)
         # use that index to get the hint for the word.
         print(f"The Hint is: {hints_list[wordIndex]}")
         hintGotPrinted = True
      elif guess == letter:
        if blanksList[index] != letter:
          blanksList[index] = letter
          blanks = ''.join(blanksList)
          guess_was_right = True
          letterExisted = False
        else:
           guess_was_right = True
           letterExisted = True
      index += 1
    if letterExisted:
      print("Letter Already used, please type another letter.")
    else:
      if guess != '@':
        print("You guessed it right!")
    print(stages[lives])
    print(blanksList)
    if not guess_was_right and guess != '@':
        lives -= 1
        if lives > 0:
            print(f"Wrong guess, {lives} lives left")
        else:
            print(f"{lives} lives left, You Lost!")
            print(f"The Choosen word is: {chosen_word}")
    if blanks == chosen_word:
        print("You Win!")
        break
  
# Another way of doing the for loop
'''
for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    blanksList[position] = letter 
'''