#   _____      _            _                         _   _____           _            _           _  __      __        _       _     _           
#  |  __ \    (_)          | |                       | | |  __ \         | |          | |         | | \ \    / /       (_)     | |   | |          
#  | |__) | __ ___   ____ _| |_ ___    __ _ _ __   __| | | |__) | __ ___ | |_ ___  ___| |_ ___  __| |  \ \  / /_ _ _ __ _  __ _| |__ | | ___  ___ 
#  |  ___/ '__| \ \ / / _` | __/ _ \  / _` | '_ \ / _` | |  ___/ '__/ _ \| __/ _ \/ __| __/ _ \/ _` |   \ \/ / _` | '__| |/ _` | '_ \| |/ _ \/ __|
#  | |   | |  | |\ V / (_| | ||  __/ | (_| | | | | (_| | | |   | | | (_) | ||  __/ (__| ||  __/ (_| |    \  / (_| | |  | | (_| | |_) | |  __/\__ \
#  |_|   |_|  |_| \_/ \__,_|\__\___|  \__,_|_| |_|\__,_| |_|   |_|  \___/ \__\___|\___|\__\___|\__,_|     \/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/

# In Python, the concept of private and protected variables is different from languages like C#. 
# Python does not have true private variables like some other object-oriented languages. 
# Instead, it relies on a convention and name mangling to indicate that a variable is intended to be private.

### Name Mangling for Private Variables

# In Python, if you want to make a variable "private" and not easily accessible from outside the class, 
# you can use name mangling by prefixing the variable name with `__` (double underscores). 
# This changes the name of the variable in a way that makes it harder (but not impossible) to access it from outside the class.

### Example with Name Mangling

# Here’s an example demonstrating name mangling:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private variable using name mangling
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age


# Creating an instance of Person
my_friend = Person("Ahmed", 21)

# Accessing public attribute
print(my_friend.name)  # Output: Ahmed

# Accessing private attribute directly (not recommended)
# This will raise an AttributeError
#print(my_friend.__age)

# Correct way to access private attribute via getter method
print(my_friend.get_age())  # Output: 21

# You can still access the mangled name directly, but it's not recommended
print(my_friend._Person__age)  # Output: 21 (not recommended)


### Explanation

# - **`__age`**: When you define `self.__age`, Python uses name mangling to change the name of the attribute to `_Person__age` internally. 
# This makes it harder to access the variable directly, indicating that it is intended to be private.

# - **Access via Getter and Setter**: The `get_age` and `set_age` methods provide a way to access and modify the private variable. 
# This is the recommended way to interact with private attributes.

# - **Direct Access**: While you can technically access the mangled variable name directly using `my_friend._Person__age`, 
# this is not recommended. It breaks the encapsulation and goes against the intended use of private variables.

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #

### Protected Variables

# If you want to indicate that a variable is intended to be protected (accessible within the class and its subclasses, but not from outside), 
# you can use a single underscore `_` prefix. However, this is still just a convention and does not enforce access control:

class Person1:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected variable
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age

# Creating an instance of Person
my_friend = Person1("Ahmed", 20)


# Correct way to access private attribute via getter method
print(my_friend.get_age())  # Output: 20

# Accessing protected attribute directly
print(my_friend._age)  # Output: 20 (possible but not recommended)


### Conclusion

# - **Name Mangling (`__var`)**: Use double underscores for private variables. 
# This makes it harder to access the variable directly and indicates that it is intended to be private.
# - **Convention (`_var`)**: Use a single underscore for protected variables. 
# This is a convention to indicate that the variable is intended for internal use within the class and its subclasses.

# Unlike C#, Python relies on these conventions and name mangling for encapsulation rather than strict access control.