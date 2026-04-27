# Arrays and traversals

# 1. Defining patterns
arr = []
arr_seq = list(range(0, 10))
arr_1 = [0 for _ in range(10)]
arr_2 = [1, 2, 3, 4, 5]
arr_3 = [0] * 10
# 2D
arr_4 = [[]]
arr_5 = [[0 for _ in range(3)] for _ in range(3)]
arr_6 = [[1, 2, 3], [1, 2, 3]]

print(arr)
print(arr_seq)
print(arr_1)
print(arr_2)
print(arr_3)
print(arr_4)
print(arr_5)
print(arr_6)

# 2. Insert into arrays
arr.append(1)
arr.insert(1, 2)  # index,val
arr.extend(arr_2)
print(arr)

# 2D
arr_4[0].append(1)
arr_4[0].append(2)  # 0 -> first row
arr_4.append([3])
arr_4[1].append(4)
print(arr_4)
# [[1, 2], [3, 4]]

# 3. Loops
print()
for n in arr:
    print(f"{n:<4}", end=" ")
print()
for i, n in enumerate(arr):
    print(f"{i}: {n:<4}", end="\n" if i == len(arr) - 1 else " ")
for i in range(len(arr)):
    print(f"{i}: {arr[i]:<4}", end="\n" if i == len(arr) - 1 else " ")

# 2D
print("---- 2D ----")
rows = len(arr_4)
cols = len(arr_4[0])

# Just rows
for i, n in enumerate(arr_4):
    print(f"Row {i}: {n}", end="\n" if i == len(arr_4) - 1 else " ")

# Just cols
for j, col in enumerate(range(cols)):
    print(f"Column {col}: ", end="")
    for i, row in enumerate(range(rows)):
        print(f"{arr_4[row][col]}", end="\n" if i == len(arr_4) - 1 else " ")

# Using list comprehension
# [col then row]
[
    print(f"{arr_4[row][col]}", end="\n" if i == len(arr_4) - 1 else " ")
    for j, col in enumerate(range(cols))
    for i, row in enumerate(range(rows))
]

# Diagonals
print("---- Diagonals-----")
for i in range(rows):
    print(f"Diagonal At: {(i,i)}: {arr_4[i][i]}")

# Transpose the matrix
# row -> cols and cols -> rows
print("----Transpose----")
for i, n in enumerate(zip(*arr_4)):
    print(f"Row {i}: {list(n)}")

for i in range(rows):
    for j in range(i + 1, cols):
        arr_4[i][j], arr_4[j][i] = arr_4[j][i], arr_4[i][j]
print(arr_4)
