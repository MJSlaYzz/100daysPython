#    _____ _ _      _             
#   / ____| (_)    (_)            
#  | (___ | |_  ___ _ _ __   __ _ 
#   \___ \| | |/ __| | '_ \ / _` |
#   ____) | | | (__| | | | | (_| |
#  |_____/|_|_|\___|_|_| |_|\__, |
#                            __/ |
#                           |___/ 

### Slicing in Python
# Slicing is a technique used to access a portion of sequences like strings, lists, or tuples in Python. 
# It allows you to retrieve specific parts of a sequence by specifying a start, stop, and step.

#### Basic Syntax
# sequence[start:stop:step]

# - **start**: The index where the slice starts (inclusive).
# - **stop**: The index where the slice ends (exclusive).
# - **step**: The step or stride between each element in the slice.

#### Examples

# 1. **String Slicing**
text = "Hello, World!"
print(text[0:5])  # Output: Hello
print(text[7:12]) # Output: World
print(text[::2])  # Output: Hlo ol!


# 2. **List Slicing**
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  # Output: [2, 3, 4]
print(numbers[:3])   # Output: [0, 1, 2]
print(numbers[7:])   # Output: [7, 8, 9]
print(numbers[::-1]) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed list)


# 3. **Tuple Slicing**

tuple_data = (10, 20, 30, 40, 50)
print(tuple_data[1:4]) # Output: (20, 30, 40)
print(tuple_data[:3])  # Output: (10, 20, 30)
print(tuple_data[::2]) # Output: (10, 30, 50)


#### Negative Indices
# - Negative indices can be used to slice from the end of a sequence.

text = "Python"
print(text[-6:-1])  # Output: Pytho
print(text[-3:])    # Output: hon


#### Omitting Indices
# - If the **start** index is omitted, slicing starts from the beginning of the sequence.
# - If the **stop** index is omitted, slicing continues to the end of the sequence.
# - If the **step** is omitted, the default step is 1.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:5])   # Output: [0, 1, 2, 3, 4]
print(numbers[5:])   # Output: [5, 6, 7, 8, 9]
print(numbers[:])    # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#### Step Argument
# - The **step** argument specifies the interval between elements in the slice.
# - A negative **step** can be used to reverse the sequence.


text = "abcdefg"
print(text[::2])   # Output: aceg
print(text[::-1])  # Output: gfedcba (reversed string)


### Summary
# - **Slicing**: Accesses a portion of a sequence.
# - **Syntax**: `sequence[start:stop:step]`.
# - **Default values**: `start`=0, `stop`=length of the sequence, `step`=1.
# - **Negative indices**: Count from the end of the sequence.
# - **Omitting indices**: Uses default start or stop values.

# Slicing is a powerful and flexible tool for working with sequences in Python, enabling efficient and concise data manipulation.