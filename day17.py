# Day 17 #

# Quiz Project and The benefits of OOP

# to create a Class:
# <class key word> <name of the class><:>
# in class name every first later in every word should be Capital (PascalCase) not camelCase(not used much ion python) nor snake_case(used for everything else)
class User0:
    # if you want to leave a function, class, etc empty and you don't want to get an indentation error you can use the key word pass
    pass

# create a user object from the blueprint/class
# <object name> <=> <class name()>
user_1 = User0()
# Attribute: is a variable that is associated with an object.
# we can use dots (.) to access or create attributes for the classes.
user_1.id = "001"
user_1.username = "Ahmed"
print(f"username is: {user_1.username}, user ID is: {user_1.id}") #Output = username is: Ahmed, user ID is: 001

# But instead of writing attributes for the objects out of the classes and then we will have to do the same process with each  new object,
# we can use Contracting or Initializing : to set (variables, counters, switches, etc.) to their starting values at the beginning of a program or subprogram.

# we create a Constructor by using a special function called (__init__)
class User:
    # The keyword self represents the actual object that being created/initialized.
    # After that we can add as much parameter as we wish and that parameter is going to be passed in when an object gets constructed from this class.

    print("new user being created...")  # every time a construction happens when we create a new user(object) the print statement is going to be triggered.
     # once you receive the data from the parameter, you can use it to set the object's attributes.
    def __init__(self, user_id, username):
        # initialise attributes.
        self.id = user_id
        self.username = username
        # some attributes will have default values, so mostly no need for them to be as a parameter.
        self.followers = 0
        self.following = 0
    # Method : when a Function is attached to an object it's called a Method
    # Methods unlike functions always needs to have a <self> parameter as the first parameter
    # so when this Method is called, it knows the object that called it.
    def follow(self, user):
        user.followers += 1
        self.following += 1

# now when we construct the object we pass in data to the parameters which will be used to set the attributes for that object.
user_1 = User("001", "Ahmed")
user_2 = User("002", "Mohamed")
print(f"user id: {user_1.id}") # Output: user id: 001

print(f"user followers: {user_1.followers}") # Output: user followers: 0
user_1.follow(user_2)
print(f"{user_1.username} following = {user_1.following}") # Output: Ahmed following = 1
print(f"{user_2.username} followers = {user_2.followers}") # Output: Mohamed followers = 1

