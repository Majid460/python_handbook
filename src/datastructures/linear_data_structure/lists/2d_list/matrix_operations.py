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
"""
Examples of Matrices 
"""
print("\n----------- Examples of Matrices -------------\n")
print("\n----------- 1. Count Number of occurrence of a number in 2d_list -------------\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Example 1
# 1. Count Number of occurrence of a number in 2d_list
matrix_two = [
    [1, 2, 3],
    [4, 5, 2],
    [5, 8, 3]
]

# So we will loop through each row and column of 2d_list and will check

# Solution 1
"""
We will create a empty dictionary (We will explore more to dictionaries. For now just think them like key value pair.

dict = {"a":1, "b":2, "c":3, "d":4}
"""
# Empty dictionary
count = {}

for row in matrix_two:
    for element in row:
        if element not in count:
            count[element] = 1
        else :
            count[element] += 1

print("Occurrences of elements in 2d_list:")
for key, val in count.items():
    print(f"{key} → {val}")
"""
Occurrences of elements in 2d_list:
1 → 1
2 → 2
3 → 2
4 → 1
5 → 2
8 → 1
"""
# Solution 2

# Using List Comprehension
# [expression for outer in outer_list for inner in outer]   Template for the list comprehension
list_comp = [item for row in matrix_two for item in row]
count = {}
for element in list_comp:
    count[element] = count.get(element, 0) + 1

print("Occurrences of elements in 2d_list using List comprehension:")
for key, val in count.items():
    print(f"{key} → {val}")

"""
Occurrences of elements in 2d_list using List comprehension:
1 → 1
2 → 2
3 → 2
4 → 1
5 → 2
8 → 1
"""

# Example 2
print("\n----------- 2. Write a program to calculate the sum of all numbers in a 2D array. -------------\n")

"""
To calculate the sum of all elements of 2d_list we have to go through the all elements and add them
"""
sum_of_elements = 0
for row in matrix:
    for element in row:
        sum_of_elements += element

print(f"The sum of all elements of 2d_list is =>: {sum_of_elements}")

# Using Comprehension
sum_of_elements = sum([item for row in matrix for item in row])
print(f"The sum of all elements of 2d_list using comprehension =>: {sum_of_elements}")
"""
The sum of all elements of 2d_list is =>: 45
The sum of all elements of 2d_list using comprehension =>: 45
"""

# Example 3
print("\n----------- 3. Print the sum of elements in each row. -------------\n")

sum_of_elements_of_row = {}
for i,row in enumerate(matrix):
    row_sum = sum(row)
    print(f"Sum of Row {i} = {row_sum}")

"""
Sum of Row 0 = 6
Sum of Row 1 = 15
Sum of Row 2 = 24
"""

"""
matrix_two = [
    [1, 2, 3],
    [4, 5, 2],
    [5, 8, 3]
]
"""

# Example 4
print("\n----------- 4. Print the sum of elements in each column. -------------\n")
num_col = len(matrix_two[0])

for col in range(num_col):
    total_sum = 0
    for row in matrix_two:
        total_sum += row[col]
    print(f"Sum of Column {col} = {total_sum}")
"""
Sum of Column 0 = 10
Sum of Column 1 = 15
Sum of Column 2 = 8
"""
# Example 5
print("\n----------- 5. Print the max and min element in 2d_list. -------------\n")
max_element = matrix_two[0][0]
min_element = matrix_two[0][0]

for row in matrix_two:
    for element in row:
        if element > max_element:
            max_element = element
        if element < min_element:
            min_element = element

print(f"Max element of the 2d_list is =>: {max_element}")
print(f"Min element of the 2d_list is =>: {min_element}")

"""
Max element of the 2d_list is =>: 8
Min element of the 2d_list is =>: 1
"""

# Example 6
print("\n----------- 6. Count even and odd number. -------------\n")

even_odd_dict = {"even": 0, "odd": 0}
even_numbers = []
odd_numbers = []
for row in matrix_two:
    for element in row:
        if element % 2 == 0:
            even_odd_dict["even"] += 1
            even_numbers.append(element)
        elif element % 2 == 1:
            even_odd_dict["odd"] += 1
            odd_numbers.append(element)

print(f"Number of Even element of the 2d_list is =>: {even_odd_dict['even']}")
print(f"Number of Odd element of the 2d_list is =>: {even_odd_dict['odd']}")
print(f"Even elements of the 2d_list is =>: {even_numbers}")
print(f"Even elements of the 2d_list is =>: {odd_numbers}")

# Example 7
print("\n----------- Advance  -------------\n")
print("\n----------- 7. Transpose a 2d_list like convert rows to columns and vice versa -------------\n")

"""
matrix_two = [
    [1, 2, 3], Row 1
    [4, 5, 2], Row 2
    [5, 8, 3]  Row 3
]
"""
"""
1. Create a empty array
2. Find no. of rows and cols in original 2d_list
3. Add outer loop on cols because we will flip the 2d_list so original's 2d_list cols will be rows
4. Add inner loop on rows because we will flip the 2d_list so original's 2d_list rows will be columns
5. Append the rows in the transpose empty list
"""
# Solution 1 using loops

transpose_matrix = []
rows = len(matrix_two)
cols = len(matrix_two[0])

for col in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix_two[i][col])
    transpose_matrix.append(new_row)

print("Transpose of 2d_list:")
for row in transpose_matrix:
    print(row)
"""
Transpose of 2d_list:
[1, 4, 5]
[2, 5, 8]
[3, 2, 3]
"""
# Solution 2 using List comprehension
li = [[]]

transpose_matrix = [[matrix_two[i][j] for i in range(rows)] for j in range(len(matrix_two[0]))]
print("Transpose of 2d_list:")
for row in transpose_matrix:
    print(row)
"""
Transpose of 2d_list:
[1, 4, 5]
[2, 5, 8]
[3, 2, 3]
"""