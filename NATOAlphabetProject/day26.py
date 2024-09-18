# Day 26 #

# List and dictionary comprehensions

# Definition: it's a case where you create a new list from a previous list.
# so far we have been doing this using for loops

def list_comprehension():
    # for loop
    numbers = [1, 2, 3]
    new_list = []
    for n in numbers:
        add_1 = n + 1
        new_list.append(add_1)

    # **list comprehension**

    # new_list = [new_item for item in list]
    numbers1 = [1, 2, 3]
    new_list1 = [n + 1 for n in numbers1]

    # we are using python interactive terminal here!!


    # what happens here is that it takes this sequence (name) (the string).
    # and it goes through each of the letters in that string and it adds each of the letters into this new list.
    name = "Mostafa"
    letters_list = [letter for letter in name]

    #python sequences:
    # example: List - string - range - tuple
    # they are called sequences because they have a specific order.
    # when you preform a list comprehension it's going to take that sequence and it's going to go through it in oder
    # either be it the letters in the string or the items in a list.
    # and then it's going to take each of those items iun that correct order and do something with it.

    # Challenge: double the sequence of range:
    new_range = [r * 2 for r in range(1,5)]

    # conditional list comprehension
    # new_list = [new_item for item in list if test]

    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
    short_names = [name for name in names if len(name) < 5]

    # Challenge: change each long name in names to all CAPS.
    upper_case_names = [name.upper() for name in names if len(name) >= 5]

def dictionary_Comprehension():
    # **Dictionary Comprehension**
    # new_dict = {new_key: new_value for item, in list}
    # new_dict = {new_key: new_value for (key,value), in dict.items()}
    # new_dict = {new_key: new_value for (key,value), in dict.items() if test}

    # Challenge: take the values in names list and add them to a new dictionary with randomly generated scores.
    import random
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
    students_scores = {student: random.randint(1,100) for student in names}
    passed_students = {passed_student: score for (passed_student, score) in students_scores.items() if score >= 60}
    #print(passed_students)

def iterate_over_dataFrame():
    # How to iterate over a pandas dataFrame
    import pandas
    student_dict = {
        "student": ["Angela", "James", "Lily"],
        "score": [56, 76, 98]
    }
    # looping through dictionaries
    for (key, value) in student_dict.items():
        print(key)

    # looping through a dataFrame
    student_data_frame = pandas.DataFrame(student_dict)
    for (key, value) in student_data_frame.items():
        print(value)

    # or using .iterrows() to loop through rows of data frame
    for (index, row) in student_data_frame.iterrows():
        #print(row) # this will print us each row that means we can tab into the values of each row
        if row.student =="Angela":
            print(row.student)
            print(row.score)
    # {new_key: new_value for (index, row) in df.iterrows()}
    
def nato_alphabet_project():
    #TODO 1. Create a dictionary inm this format:
    # {"A": "Alfa", "B": "Bravo"}
    import pandas
    data = pandas.read_csv("NATOAlphabetProject/nato_phonetic_alphabet.csv")
    data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    
    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    user_input = input("Enter a word: ").upper()
    list_of_words = [data_dict[letter] for letter in user_input]
    print(list_of_words)

        

nato_alphabet_project()
    