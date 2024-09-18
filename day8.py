# Day 8 #

# Functions Parameters & Caesar Cipher
'''
# Simple Functions
def greet():
    print("Hello Ali")
    print("How are you doing?")
    print("Isn't the weather great today?")
greet()
print("------------------")
# Functions that allows input
# The parameter is the name of the data that is being passed in (name)
# The Argument is the actual value of that data
def greet_with_name(name):
    print(f"Hello, {name}")
    print("How are you doing?")
    print("Isn't the weather great today?")
myName = input("What is your name?\n")
greet_with_name(myName)
print("------------------")
# Functions with more than 1 input
def greet_with_two_parameters(name, location):
    print(f"Hello, {name}")
    print("How are you doing?")
    print(f"What is it like in {location}?")
# Positional Arguments is very important, Arguments position should match the position of the parameters
greet_with_two_parameters("Mostafa ", "Egypt")
print("------------------")
# we can avoid this issue by using keyword Arguments
# no the order doesn't matter.
greet_with_two_parameters(location = "Oman", name = "Ahmed")
print("------------------")
'''
# Caesar cipher is an ancient type of encryption
# he would encode his message so that each letter would be shifted by a predetermined amount.
# so if we want to encode the letter "A" and we shift it by three, them A becomes D, B becomes E and so on and so forth.
# before encoding. shift = 0
# A B C D E
# 0 1 2 3 4
# after encoding. shift = 3
# A B C D E
# D E F G H
# 3 4 5 6 7

def reducing_shift_number(shiftNumber, letters):
    numberOfLetters = len(letters)
    # to avoid having extra compiling time we are keeping the shift number <= 26
    # because any sequence made with a shift number above 26 was already made with a shift number less than 26
    # for example the shift numbers 26, 52, 780 all have the sequence of [a, b, c]
    # and the shift numbers 18, 44, 70 all have the sequence of [s, t, u]
    if shiftNumber > numberOfLetters:
        if shiftNumber % numberOfLetters == 0: # if the number is a Multiple of 26.
            print("Warning, you have chosen a shift number which is a multiple of 26, so the message won't be encrypted!")
        shiftNumber = shiftNumber % numberOfLetters # shiftNumber will be equal to the remainder of dividing shiftNumber on numberOfLetters
        print(f"new shift number = {shiftNumber}")

def take_inputs():
    while True:
        userInput = input("Type 'encode' to encrypt, type 'decode' to decrypt or type 'break' to exit the program: ").lower()
        if userInput != "encode" and userInput != "decode":
            print("Wrong Input!")
        else:
            break
    encodededMessage = input("Type your message:\n").lower()
    shiftNumber = int(input("Type shift number:\n"))
    return userInput, encodededMessage, shiftNumber

def ceaser(alphabet, text, shiftNumber, direction):
    while True:
        encrypted_alphabet = alphabet.copy()
        index = 0
        new_text_list = []
        reducing_shift_number(shiftNumber, alphabet)
        for i in range(shiftNumber):
            removedLetter = encrypted_alphabet[0]
            encrypted_alphabet.pop(0)
            encrypted_alphabet.append(removedLetter)
        new_text_list = list(text)
        if(direction == "encode"):
            for letter in text:
                if(letter in alphabet):
                    new_text_list[index] = encrypted_alphabet[alphabet.index(letter)]
                index += 1
            result = "".join(new_text_list)
            print(f"The Result of your encode is: {result}")
        elif(direction == "decode"):
            for letter in text:
                if(letter in alphabet):
                    new_text_list[index] = alphabet[encrypted_alphabet.index(letter)]
                index += 1
            result = "".join(new_text_list)
            print(f"The Result of your decode is: {result}")
        elif(direction == "break"):
            break
        direction, text, shiftNumber = take_inputs()
        
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
userInput = ""
encodededMessage = ""
shiftNumber = 0
userInput, encodededMessage, shiftNumber = take_inputs()
ceaser(letters, encodededMessage, shiftNumber, userInput)