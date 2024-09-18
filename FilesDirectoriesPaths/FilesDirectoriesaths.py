#   ______ _ _               _____  _               _             _                             _               _   _         
#  |  ____(_) |             |  __ \(_)             | |           (_)                           | |             | | | |        
#  | |__   _| | ___  ___    | |  | |_ _ __ ___  ___| |_ ___  _ __ _  ___  ___    __ _ _ __   __| |  _ __   __ _| |_| |__  ___ 
#  |  __| | | |/ _ \/ __|   | |  | | | '__/ _ \/ __| __/ _ \| '__| |/ _ \/ __|  / _` | '_ \ / _` | | '_ \ / _` | __| '_ \/ __|
#  | |    | | |  __/\__ \_  | |__| | | | |  __/ (__| || (_) | |  | |  __/\__ \ | (_| | | | | (_| | | |_) | (_| | |_| | | \__ \
#  |_|    |_|_|\___||___( ) |_____/|_|_|  \___|\___|\__\___/|_|  |_|\___||___/  \__,_|_| |_|\__,_| | .__/ \__,_|\__|_| |_|___/
#                       |/                                                                         | |                        
#                                                                                                  |_|                        

### Files, Directories, and Paths in Python

#### 1. **Working with Files**
# Python provides built-in functions to work with files. You can read from, write to, and manipulate files using these functions.

##### Opening a File
file = open("filename.txt", "mode")

# - **Mode** can be:
#   - `'r'` - Read (default mode, file must exist)
#   - `'w'` - Write (creates a new file or truncates existing)
#   - `'a'` - Append (adds to the end of the file)
#   - `'b'` - Binary mode (e.g., `'rb'`, `'wb'`)

##### Reading from a File
file = open("filename.txt", "r")
content = file.read()  # Reads the entire file
line = file.readline()  # Reads a single line
lines = file.readlines()  # Reads all lines into a list
file.close()

##### Writing to a File
file = open("filename.txt", "w")
file.write("Hello, World!\n")
file.writelines(["Line1\n", "Line2\n"])
file.close()


##### Using `with` Statement
# The `with` statement ensures proper acquisition and release of resources, making it a good practice to use.
with open("filename.txt", "r") as file:
    content = file.read()


#### 2. **Working with Directories**
# The `os` module provides functions to create, remove, and change directories.

##### Importing the `os` Module
import os

##### Creating a Directory
os.mkdir("new_directory")


##### Changing the Current Directory
os.chdir("new_directory")


##### Listing Files in a Directory
files = os.listdir("path_to_directory")


##### Removing a Directory
os.rmdir("new_directory")  # Only works if the directory is empty


#### 3. **Working with Paths**
# The `os.path` module provides functions to work with file paths.

##### Importing the `os.path` Module
import os.path


##### Checking if a Path Exists
exists = os.path.exists("path_to_file_or_directory")


##### Checking if a Path is a File or Directory
is_file = os.path.isfile("path_to_file")
is_dir = os.path.isdir("path_to_directory")


##### Getting the Directory Name and Base Name
dir_name = os.path.dirname("path_to_file")
base_name = os.path.basename("path_to_file")


##### Joining Paths
full_path = os.path.join("directory", "subdirectory", "file.txt")


#### 4. **The `pathlib` Module**
# The `pathlib` module provides an object-oriented approach to working with files and directories.

##### Importing the `pathlib` Module
from pathlib import Path


##### Creating a Path Object
path = Path("filename.txt")

##### Reading from and Writing to a File
content = path.read_text()
path.write_text("Hello, World!")

##### Checking if a Path Exists
exists = path.exists()

##### Iterating Over Directory Contents
for child in path.iterdir():
    print(child)


##### Creating and Removing Directories
path.mkdir()  # Creates the directory
path.rmdir()  # Removes the directory


#### Summary
# - Use the `open` function to read from and write to files.
# - Use the `os` module to manipulate directories and paths.
# - Use the `pathlib` module for an object-oriented approach to file and directory operations.
# - Always handle files and directories using context managers (`with` statement) for better resource management.
