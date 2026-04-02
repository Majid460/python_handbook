"""
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)


"""

# 1. To open a file use open()
file = open(
    "test.txt", "rt"
)  # Because "r" for read, and "t" for text are the default values, you do not need to specify them.
print(file.read())
file.close()

# 2. Open with "with"
"""
Then you do not have to worry about closing your files, the with statement takes care of that.
"""
with open("test.txt", "rt") as f:
    print(f.read())

# 3. Read Only Parts of the File
"""

By default the read() method returns the whole text, but you can also specify how many characters you want to return:
"""
with open("test.txt", "rt") as f:
    print(f.read(5))
    # Reads first 5 characters
# Q. Wh

# 4. Read lines
with open("test.txt", "rt") as f:
    print(f.readline())  # Reads first line

# By calling readline() two times, you can read the two first lines:

"""Example
Read two lines of the file:
"""

with open("test.txt") as f:
    print(f.readline())
    print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line:

"""Example
Loop through the file line by line:"""

with open("test.txt") as f:
    for x in f:
        print(x)

# Read second line
with open("test.txt") as f:
    lines = f.readlines()
    if len(lines) >= 2:
        print(f"second line:: {lines[1]}")
# second line:: A. Life is temporary environment to execute certain tasks.

# Read last line
with open("test.txt") as f:
    lines = f.readlines()
    print(f"last line:: {lines[len(lines)-1]}")
# second line:: Q. How?

### Write to file
print("-------------------Write in file------------------")
"""
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""
# with open("test.txt","w") as f:
#     f.write("Because life is harsh")
# #open and read the file after the appending:
# with open("test.txt") as f:
#   print(f.read())

# with open("test.txt","a") as f:
#     f.write("A. Because life is harsh.\n")
# #open and read the file after the appending:
# with open("test.txt") as f:
#   print(f.read())


print("-------------------Create a new file------------------")

# with open("newfile.txt","x") as f:
#     f.write("Hey new file is created \n")

# Remove a file
import os

# os.remove("newfile.txt")

# if os.path.exists("newfile.txt"):
#   os.remove("newfile.txt")
# else:
#   print("The file does not exist")

print("------------------- Json Handling ------------------")
"""
JSON (JavaScript Object Notation)

- A standard data interchange format supported in Python via the json module.
- Serialization = converting Python objects → JSON string.
- Deserialization = converting JSON string → Python object.
- JSON is widely used for data exchange and is interoperable across languages.
"""

import json

# To convert a dict to json use dumps

x = {"name": "Test", "age": 20}
"""The json.dumps() method has parameters to order the keys in the result:

Example
Use the sort_keys parameter to specify if the result should be sorted or not:"""

y = json.dumps(x, indent=4, sort_keys=True)
print(y)
"""
{
    "age": 20,
    "name": "Test"
}
"""

# Convert json to dict
js = json.loads(y)
print(js)
