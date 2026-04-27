"""
To create a list from a other collections we can use list()
"""

print("\n----------- Some List Operations-------------\n")
from_tuple_to_list = list(("a", "b", "c"))

"""
Double bracket is used because ("a","b","c") is a tuple so it converts the tuple to list
"""
# From set to list

from_set_to_list = list({"a", "b", "c"})

# From string to list

from_string_to_list = list("abc")
# from string → ['a', 'b', 'c']

# 1. Access Items
thisList = ["a", "b", "c", 1]
print(f"Access Element => {thisList[0]}")
# Prints -> Access Element => a

# 2. Negative Indexing
"""
Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc.
"""

print(f"Negative indexing -> element at -1 index => {thisList[-1]}")
# Negative indexing -> element at -1 index => 1

# 3. Range of Indexes
"""
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
"""
print(
    f"Range of indexing -> element from 0 until 1 index (exclude 2) => {thisList[0:2]}"
)
# Range of indexing -> element from 0 until 2 index (exclude 2) => ['a', 'b']

# From Start to until index-1
print(
    f"Range of indexing -> element from 0 until 2 index (exclude 3) => {thisList[:3]}"
)
# Range of indexing -> element from 0 until 2 index (exclude 3) => ['a', 'b', 'c']

# From specific index to end
print(f"Range of indexing -> element from 2 until end => {thisList[2:]}")
# Range of indexing -> element from 2 until end => ['c', 1]

# 4. Range of Negative Indexes
"""
Specify negative indexes if you want to start the search from the end of the list
"""
# thisList = ["a","b","c",1]
# returns the items from "b" (-3) to, but NOT including "c" (-2):
print(f"Negative Range of indexing -> element from -2 until -3 => {thisList[-3:-2]}")
# Negative Range of indexing -> element from -2 until -3 => ['b']

print("\n----------- Looping Lists-------------\n")
"""
Add Elements in list using Loop
"""
# 1. General Method
# # Add numbers 0 to 5 to the list
emp_list = []
for i in range(6):
    emp_list.append(i)
print(f"Items in list Method 1: => {emp_list}")
# Items in list Method 1: => [0, 1, 2, 3, 4, 5]

# 2. Take input from user
# Commented to just test the other parts of code
# emp_list_two = []
#
# # Take the size of list from user
# size_of = int(input("Enter the size of list: "))
# for i in range(size_of):
#     emp_list_two.append(i)
#
# print(f"Items in list Method 2: => {emp_list_two}")
# """
# Enter the size of list: 4
# Items in list Method 2: => [0, 1, 2, 3]
# """
# # 3. Take size and elements from user
# emp_list_three = []
#
# # Take the size of list from user
# size_of = int(input("Enter the size of list: "))
# for _ in range(size_of):
#     element = input("Enter the element: ")
#     emp_list_three.append(element)
#
# print(f"Items in list Method 3: => {emp_list_three}")

"""
Enter the size of list: 4
Enter the element: 1
Enter the element: 2
Enter the element: 3
Enter the element: 4
Items in list Method 3: => ['1', '2', '3', '4'] 
 All elements are in string because the input function consider every element as string
"""

#  4. List comprehension (Modern)

# Basic
empty_list_comp = [i for i in range(4)]
print(f"Items in list comprehension 1: => {empty_list_comp}")
# Items in list comprehension 1: => [0, 1, 2, 3]

# Moderate

# empty_list_comp_two = [input("Enter an item: ") for _ in range(4)]
# print(f"Items in list comprehension 2: => {empty_list_comp_two}")
"""
Enter an item: 1
Enter an item: 2
Enter an item: 3
Enter an item: 4
Items in list comprehension 2: => ['1', '2', '3', '4']
"""
# Advance
# size = int(input("Enter the size of the list: "))
# items = [input(f"Enter item {_+1}: ") for _ in range(size)]
# print(f"Items in list => {items}")
"""
Enter the size of the list: 3
Enter item 1: 1
Enter item 2: 3
Enter item 3: 4
Items in list => ['1', '3', '4']
"""

# Printing using for loop
thisList = ["apple", "banana", "cherry"]
for i in thisList:
    print(i)
for i in range(len(thisList)):
    print(f"Printing using for loop => {thisList[i]}")

"""
Printing using for loop => apple
Printing using for loop => banana
Printing using for loop => cherry
"""
# Printing using While loop
i = 0
while i < len(thisList):
    print(f"Printing using while loop => {thisList[i]}")
    i += 1
"""
Printing using while loop => apple
Printing using while loop => banana
Printing using while loop => cherry
"""
# Using List Comprehension
[
    print(f"Printing using List comprehension loop => {thisList[i]}")
    for i in range(len(thisList))
]

"""
Printing using List comprehension loop => apple
Printing using List comprehension loop => banana
Printing using List comprehension loop => cherry
"""
print("\n----------- 2D Lists-------------\n")
# 2D Lists

"""
As for now we have explored the 1D lists now we can explore the 2D lists.
A 2D list is a list of lists, often used to represent tables or matrices.
2D List -> [Rows][Columns]
2d_list = [[1,2],[3,4]]

2d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
         Column0 Column1 Column2
Row0  →    1       2       3
Row1  →    4       5       6
Row2  →    7       8       9
"""
# Explore the 2D list in depth
mat = [[0 for _ in range(3)] for _ in range(3)]
print(mat)

# Create a default list
# A metrics with 3x3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Access the elements of 2d_list
print(f"Access the elements of 2d_list at [0][0] => {matrix[0][0]}")

# Print first Row
print(f"Access the elements of first Row of 2d_list => {matrix[0][:]}")
# Access the elements of first Row of 2d_list => [1, 2, 3]

# Print first Column
"""
Matrix will be like :
               Row 0         Row 1           Row 2
2d_list = [  [1, 2, 3],     [4, 5, 6],      [7, 8, 9]   ]

It looped on each row as it has 3 Rows so it like [1,2,3]
1. It will pick the first row and its first element is 1 which is first element of column.
2. After picking first element of first row it will go on second Row and picked first element which is 4.
3. Then on 3rd Row it will pick the first element which is 7.

So think like a 1D array to a 2D array.
"""
for row in matrix:
    print(f"Access the elements of first Column of 2d_list => {row[0]}")

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        print(matrix[row][col])
"""
Access the elements of first Column of 2d_list => 1
Access the elements of first Column of 2d_list => 4
Access the elements of first Column of 2d_list => 7
"""

# Print all elements of 2d_list

for row in matrix:
    for i in row:
        print(f"Access the elements of 2d_list => {i}")

"""
Access the elements of 2d_list => 1
Access the elements of 2d_list => 2
Access the elements of 2d_list => 3
Access the elements of 2d_list => 4
Access the elements of 2d_list => 5
Access the elements of 2d_list => 6
Access the elements of 2d_list => 7
Access the elements of 2d_list => 8
Access the elements of 2d_list => 9
"""
# Customize the output
print(" " * 8 + "Column0 Column1 Column2")
# for row in 2d_list:
#     print(f"Row -> ",sep=" ", end="")
#     for i in row:
#         print(f"{i}",end=" ")
#     print("\n")

for row_index, row in enumerate(matrix):
    print(f"Row {row_index}  →", end="    ")
    for item in row:
        print(f"{item:<7}", end="")  # left-aligned with fixed width
    print()
