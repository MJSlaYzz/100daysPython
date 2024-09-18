# Day 24 #

### Definitions with Examples

def files():
    #### 1. Files
    # **Definition:** A file is a container in a computer system for storing information.
    # Files can contain text, images, audio, video, and other types of data. In Python, files are used to store and retrieve data.

    # you should always remember to use ".close()" to close the files you have already opened because it takes recourses or simply use "with"
    # if you open a file in "w" write mode and that file doesn't exist. then it will create that file for you.
    # **Example:**
    # Writing to a file
    with open("example.txt", "w") as file: # This will open the file, replace everything inside with the next argument inside the write() method.
        file.write("Hello, World!")

    # Reading from a file
    with open("example.txt", "r") as file:
        content = file.read()
        print(content) # output: Hello, World!
    
    # add a Writing to a file
    with open("example.txt", "a") as file: # This will open the file, add what in the next argument inside the write() method.
        file.write("\nBye bye, World!")
    
    # Reading from a file using a path to find the file
    with open("100daysPython/example.txt", "r") as file:
        content = file.read()
        print(content) # output: Hello, World! Bye bye, World!
    
    
    # In this example, we create a file named `example.txt`, write "Hello, World!" to it, and then read the content back from the file.

def directories():
    #### 2. Directories
    # **Definition:** A directory (also known as a folder) is a collection of files and other directories.
    # Directories are used to organize files on a computer.
    # They can contain other directories, forming a hierarchy.

    # **Example:**
    
    import os

    # Creating a directory
    os.mkdir("example_directory")

    # Changing the current directory
    os.chdir("example_directory")

    # Creating a file inside the directory
    with open("example_file.txt", "w") as file:
        file.write("Hello from the directory!")

    # Listing files in the directory
    print(os.listdir("."))
    
    # In this example, we create a directory named `example_directory`, change the current directory to `example_directory`, 
    #   create a file inside it, and list the files in the directory.

def paths():
    #### 3. Paths
    # **Definition:** A path is a string that specifies the location of a file or directory within the filesystem.
    # Paths can be absolute (providing the complete path from the root of the filesystem) or relative (providing the path relative to the current directory).

    # **Example:**
    
    import os

    # Step 1: Get the absolute path
    # Absolute path
    # Absolute paths starts from the root which is the hard drive D, C, etc...
    absolute_path = os.path.abspath("day19.py")
    print(f"Absolute path: {absolute_path}") # output: D:\road_to_programming\GitHub\100daysPython\example.txt
    
    # Step 2: Convert the absolute path to a relative path
    # Assuming the current directory is the base path (working directory)
    current_dir = os.getcwd()
    print(f"current_dir = {current_dir}") # current_dir = D:\road_to_programming\GitHub\100daysPython

    # Calculate the relative path
    relative_path = os.path.relpath(absolute_path, current_dir)
    print(f"Relative path: {relative_path}") # output: Relative path: example.txt

    # Relative path
    # in relative path you can use ./ to get the path ("./" is optional.)
    # or we can use two dots to get to a parent file or folder ../
    # relative file starts from base path because we are at 'D:\road_to_programming\GitHub\100daysPython' (which is the Absolute path)
    # the relative path would start from 100daysPython so it won't use it. example:
    # relative_path = os.path.join("example_directory", "example_file.txt")
    relative_path = os.path.join("snakeGame", "day20.py") # the folder snakeGame is inside the base so our relative path is snakeGame\day20.py
    print(f"Relative path: {relative_path}")

    # Checking if a path exists
    if os.path.exists(relative_path):
        print(f"The file {relative_path} exists.")
    else:
        print(f"The file {relative_path} does not exist.")
    
    # trying to get a file from a parent file in a relative path using "../".
    #  we want to start from here which is the (working directory) D:\road_to_programming\GitHub\100daysPython
    # to go here which is where the file is located, using relative path D:\road_to_programming\Visual Studio Code Python classes
    # so we first need to get out of 100daysPython by using "../" then get out of GitHub using another ../ and now we are working from road_to_programming directory.
    relative_path2 = "../../Visual Studio Code Python classes/test_file_for_paths_day24.txt"

    if os.path.exists(relative_path2):
        print(f"The file {relative_path2} exists.")
    else:
        print(f"The file {relative_path2} does not exist.")
    with open(relative_path2) as test:
        content = test.read()
        print(f"test = {content}")
    
    # Absolute file path is always relative to the root of your computer.
    # Relative file path is relative to your current working directory.

    # In this example, we obtain the absolute path of `example.txt`, create a relative path to `example_file.txt` inside `example_directory`, 
    #   and check if the file exists at the specified relative path.

### Summary
# - **Files** are containers for storing data and can be manipulated using file operations like read and write.
# - **Directories** are used to organize files and can contain other directories, creating a hierarchical structure.
# - **Paths** specify the location of files and directories and can be either absolute or relative.


### Notes on Absolute and Relative Paths
def Absolute_Relative_paths():
    

    #### Absolute Paths

    # - **Definition**: An absolute path is a complete path that specifies the location of a file or directory from the drive letter (for Windows systems).

    # - **Characteristics**:
    # - Starts from the root directory or drive letter.
    # - Always points to the same location, regardless of the current working directory.
    # - Example (Windows): `C:\Users\Username\Documents\file.txt`


    #### Relative Paths

    # - **Definition**: A relative path specifies the location of a file or directory relative to the current working directory.
    # - **Characteristics**:
    # - Does not start from the root directory or drive letter.
    # - The location it points to can change depending on the current working directory.
    # - Uses special symbols like `.` (current directory) and `..` (parent directory) to navigate.
    # - Example: `Documents/file.txt` (if the current working directory is `/home/username`)
    # - Example: `../file.txt` (refers to a file one directory up from the current directory)

    #### Examples

    ##### Absolute Path

    # - **Windows**: `C:\Users\John\Pictures\image.jpg`
    # - Starts from the `C:` drive.
    # - Points to the same file regardless of where the script is executed.

    ##### Relative Path

    # - **Windows/Unix/Linux**: `data/info.txt`
    # - If the current directory is `C:\Users\John` (Windows), this path refers to `C:\Users\John\data\info.txt`.
    # - **Windows/Unix/Linux**: `../config/settings.cfg`
    # - Refers to `settings.cfg` in the parent directory of the current working directory.

    #### Usage in Python

    # To work with absolute and relative paths in Python, you can use the `os` and `os.path` modules or the `pathlib` module.

    ##### Using `os` and `os.path`

    
    import os

    # Absolute path
    absolute_path = "/Users/John/Documents/file.txt"
    print(os.path.isabs(absolute_path))  # True

    # Relative path
    relative_path = "Documents/file.txt"
    print(os.path.isabs(relative_path))  # False

    # Converting relative path to absolute path
    base_path = os.getcwd()  # Get current working directory
    full_path = os.path.join(base_path, relative_path)
    print(full_path)
    

    ##### Using `pathlib`

    
    from pathlib import Path

    # Absolute path
    absolute_path = Path("C:/Users/John/Documents/file.txt")
    print(absolute_path.is_absolute())  # True

    # Relative path
    relative_path = Path("Documents/file.txt")
    print(relative_path.is_absolute())  # False

    # Converting relative path to absolute path
    full_path = relative_path.resolve()
    print(full_path)
    

    #### Summary

    # - **Absolute Paths**: Start from the root directory or drive letter, always point to the same location.
    # - **Relative Paths**: Start from the current working directory, can change location depending on where the script is run.
    # - Use `os` and `os.path` or `pathlib` in Python to work with file paths effectively.

def working_directory():
    ### Working Directory in Windows using VSCode

    #### Definition:
    # The working directory is the directory in which a program is currently running. 
    # It is the default location for file operations when a specific path is not provided.

    ### Finding the Working Directory in Visual Studio Code (VSCode)

    #### Using the Terminal in VSCode:

    # 1. **Open the Terminal in VSCode**:
    # - Open the terminal by going to the top menu and selecting `Terminal` -> `New Terminal`, or use the shortcut `Ctrl + ` (backtick).

    # 2. **Find the Current Working Directory**:
    # - In the terminal, you can use the `cd` command to print the current directory, or use `pwd`.

    
    # Using Command Prompt
    # cd

    # Using PowerShell in VSCode
    # pwd
    

    # **Example Output**:
    
    # Path
    # ----
    # C:\Users\yourusername\projects\myproject
    

    # 3. **Changing the Working Directory**:
    # - To change the working directory, use the `cd` command followed by the path to the desired directory.

    
    # Change to a specific directory
    # cd C:\path\to\your\directory
    

    ### Finding and Changing Working Directory in Python:

    #### Find Current Working Directory in Python:

    # You can also find the current working directory from within a Python script using the `os` module.

    
    import os

    current_working_directory = os.getcwd()
    print("Current Working Directory:", current_working_directory)
    

    #### Change Working Directory in Python:

    # To change the working directory in a Python script, use the `os.chdir()` method.
    import os

    new_directory = "C:\\path\\to\\your\\directory"
    os.chdir(new_directory)
    print("Changed Working Directory:", os.getcwd())
    

    ### Summary

    # - **Working Directory**: The default directory where a program operates.
    # - **Finding the Path in Terminal (VSCode)**: Use `Get-Location` for PowerShell and `cd` for Command Prompt, or `pwd` in PowerShell.
    # - **Finding and Changing Working Directory in Python**: Use `os.getcwd()` to find and `os.chdir()` to change the working directory.

    # Understanding and managing the working directory is crucial for correct file operations in your programs.

# Changes were made to day 20 (Snake Game)
paths()

