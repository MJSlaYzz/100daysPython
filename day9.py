# Day 9 #

# Dictionaries, Nesting and the Secret Auction

# Dictionaries
# A dictionary is a collection of key-value pairs, where each key is unique and is used to retrieve its corresponding value.
# {Key: Value}
programming_dictinary = {
    "Bug": "An error in a program that prevents the progtram from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Retrieving items from the Dictionary:
# you need to right the key in it's right data type
print(programming_dictinary["Bug"]) # and you will get the value for that Key

# Adding new items to the Dictionary.
programming_dictinary["Loop"] = "The action of doing something over and over again."
print(programming_dictinary)

# Creating an empty dictionary
empty_dictionary = {}

# Wipe and existing dictionary
#programming_dictinary = {}
#print(programming_dictinary)

# Edit an item in a dictionary
programming_dictinary["Bug"] = "A moth in your computer."

# Loop through a dictionary
# in loops you don't get key and the value printed but you only get the key
for key in programming_dictinary:
    print(key + ": "+ programming_dictinary[key])


# Nesting
# Nesting refers to having dictionaries within dictionaries.
students_scores = {
    "Alice": {"Math": 90, "Science": 85, "English": 88},
    "Bob": {"Math": 78, "Science": 80, "English": 75},
    "Charlie": {"Math": 95, "Science": 92, "English": 90},
}

# Accessing nested dictionary items
# Retrieve the Science score of Bob
bob_science_score = students_scores["Bob"]["Science"]
print(bob_science_score)  # Output: 80

# Adding a new nested dictionary for a new student
students_scores["David"] = {"Math": 85, "Science": 88, "English": 82}
print(students_scores)

# Modifying a value in a nested dictionary
students_scores["Alice"]["Math"] = 95
print(students_scores["Alice"])  # Output: {'Math': 95, 'Science': 85, 'English': 88}

# Looping through a nested dictionary
for student, scores in students_scores.items():
    print(f"{student}'s scores:")
    for subject, score in scores.items():
        print(f"  {subject}: {score}")

# Another example for having a [list] and/or a {dictionary} inside another dictionary:
# test_dict = { Key: [List], Key2:{Dictionary},}
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgard"], "total_visits": 42}
}
# Retrieving items from that Dictionary:
print(travel_log["France"]["cities_visited"][0]) # to get date of a specifc item in the list inside the dictionary.
print(travel_log["France"]["total_visits"])
# you can nest a list in another list but it's not useful because the way the data is structured.
["A", "B",["C", "D"]]

# Nesting a dictionary in a list
travel_log_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited":["Berlin", "Hamburg", "Stuttgard"], 
        "total_visits": 42
    }
]
# Retrieving items from that List:
print(travel_log_list[0]["cities_visited"][2]) # to get date of a specifc item in the list inside a dictionary inside a list.

## Adding a new nested dictionary in a list by using the key word append.
travel_log_list.append({"country": "Egypt", 
                        "cities_visited": ["Cairo", "Alexandria", "Sinai"],
                        "total_visits": 66
                    })
# Loop through each dictionary in the list
for log in travel_log_list:
    # Extract and print the country
    country = log["country"]
    print(f"Country: {country}")
    
    # Extract and print the cities visited
    cities = log["cities_visited"]
    print("Cities visited:")
    for city in cities:
        print(f"  - {city}")
    
    # Extract and print the total visits
    total_visits = log["total_visits"]
    print(f"Total visits: {total_visits}\n")

#Another way of doing it:

# Loop through each dictionary in the list
for log in travel_log_list:
    # Loop through each key-value pair in the dictionary
    for key, value in log.items():
        if key == "country":
            print(f"Country: {value}")
        elif key == "cities_visited":
            # Join the list of cities into a single string
            cities = ", ".join(value)
            print(f"Cities visited: {cities}")
        elif key == "total_visits":
            print(f"Total visits: {value}")
    print()  # Print a blank line between entries
