# -------- Operations on Arrays ------- #
from collections import defaultdict
from typing import List


arr = [1, 2, 4, 5, 3, 6, 9, 0]
arr_2d = [[2, 1, 4], [3, 0, 5], [6, 2, 1]]


def display(*values, sep=" ", end="\n", prefix=""):
    print(prefix + sep.join(str(v) for v in values), end=end)


# 1D


# 1. In array find the max number


def max_element():
    # simple way
    max_n = arr[0]
    for n in arr:
        if n > max_n:
            max_n = n
    display("Max number is:", max_n)
    # Advance
    print("Max Number is:", max(arr, key=lambda x: abs(x)))

    # 2D
    max_num = arr_2d[0][0]
    for n in arr_2d:
        for i in n:
            max_num = max(i, max_num)
    display("Max Number in 2d is:", max_num)
    # another way
    max_val = max(num for row in arr_2d for num in row)
    print(max_val)


def min_element():
    # simple way
    min_n = arr[0]
    for n in arr:
        min_n = min(n, min_n)
    display("Min number is:", min_n)
    # Advance
    # key = how to compare, not what to return
    display("Max Number is:", min(arr, key=lambda x: abs(x)))


def filtering():
    # 1D
    greaterthan4 = list(filter(lambda x: x > 4, arr))
    display(f"Greater than 4: {greaterthan4}")
    smallerthan4 = [x < 4 for x in arr]
    display(f"Smaller than 4: {smallerthan4}")
    eq4 = list(filter(lambda x: x == 4, arr))
    display(f"Eq to 4: {eq4}")

    # Filter on sum
    # sum equal to 10
    sumeq10 = [(x, y) for x in arr for y in arr if x + y == 10]
    display(f"Sum Eq to 10: {sumeq10}")

    # Better O(n) way
    seen = set()
    res = []
    for num in arr:
        if 10 - num in seen:
            res.append((10 - num, num))
        seen.add(num)
    display(f"Sum Eq to 10 using O(n): {res}")

    # 2D
    greaterthan4 = [n for row in arr_2d for n in row if n > 4]
    display(greaterthan4)
    # 2 sum
    flat = [num for row in arr_2d for num in row]

    pairs = [
        (x, y)
        for i, x in enumerate(flat)
        for j, y in enumerate(flat)
        if i < j and x + y == 10
    ]
    display(pairs)
    # Optimal
    seen = set()
    res = set()  # to avoid duplicate
    for i, n in enumerate(arr_2d):
        for j, num in enumerate(n):
            if 10 - num in seen:
                pair = tuple(sorted((num, 10 - num)))
                res.add(pair)
            seen.add(num)
    print(res)


# arr_2d = [
# [2, 1, 4],
# [3, 0, 5],
# [6, 2, 1]]
# Find max in each row and col of 2d matrix


def find_max_in_each_row():

    for row in arr_2d:
        max_n = max(row)
        print(max_n)
    # max in col
    print("Max in each col method 1")
    rows = len(arr_2d)
    cols = len(arr_2d[0])
    for c in range(cols):
        max_n = float("-inf")
        for r in range(rows):
            max_n = max(arr_2d[r][c], max_n)
        print(max_n)

    print("Max in each col method 2")
    for col in zip(*arr_2d):
        max_n = max(col)
        print(max_n)


def search_in_matrix(target: int):
    # 1D
    print("Search in 1D")
    for item in arr:
        if item == target:
            print("Target found")

    # 2D
    print("Search in 2D in Method 1")
    flat = [item for row in arr_2d for item in row]
    for item in flat:
        if item == target:
            print("Target found")
    """
    Issues:
    Uses extra space O(nm)
    Does 2 passes (flatten + search)
    """
    print("Search in 2D in Method 2")
    for row in arr_2d:
        for item in row:
            if item == target:
                print("Target found")
    # Even more cleaner
    if any(target in row for row in arr_2d):
        print("Target found")


# Spiral Order of traversals
def spiral_order():
    print("----- Spiral Order of 2d arr -----")
    res = []

    m = len(arr_2d)  # rows
    n = len(arr_2d[0])  # cols
    top = 0
    bottom = m - 1
    left = 0
    right = n - 1

    while left <= right and top <= bottom:

        # left → right
        for c in range(left, right + 1):
            res.append(arr_2d[top][c])
        top += 1
        # top -> bottom
        for r in range(top, bottom + 1):
            res.append(arr_2d[r][right])
        right -= 1

        if top <= bottom:
            # right → left
            for c in range(right, left - 1, -1):
                res.append(arr_2d[bottom][c])
            bottom -= 1

        if left <= right:
            # bottom → top
            for r in range(bottom, top - 1, -1):
                res.append(arr_2d[r][left])
            left += 1
    print(res)


def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:  # find start
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest


# Count number of 0's and 1's in 2d
"""
1 0 0   
0 1 1       
0 0 1       

"""


def count_zeros_ones(mat: List[List[int]]):
    zeros = 0
    ones = 0

    for row in mat:
        for val in row:
            if val == 1:
                ones += 1
            else:
                zeros += 1

    return zeros, ones


"""
1 0 0       1 0 0
0 1 1       0 1 1
0 0 1       0 0 1

"""


def add_matrix(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])

    # Validate dimensions
    if rows != len(mat2) or cols != len(mat2[0]):
        return -1

    res = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            res[r][c] = mat1[r][c] + mat2[r][c]

    print(res)
    # Using list comprehension
    flat = [
        [mat1[r][c] + mat2[r][c] for c in range(len(mat1[0]))] for r in range(len(mat1))
    ]
    print(flat)


def display(mat):
    print("Just rows")
    for row in mat:
        print(row)
    print(" Just Cols")
    for c in range(len(mat[0])):
        row = []
        for r in range(len(mat)):
            row.append(mat[r][c])
        print(row)


if __name__ == "__main__":
    # max_element()
    # min_element()
    # display("---- Filtering ----")
    # filtering()
    # # Max number
    # print("Max in each row of 2d")
    # find_max_in_each_row()
    # search_in_matrix(6)
    # spiral_order()
    # s = "shshhs"
    # nums = [2, 3, 4, 5]
    # longestConsecutive(nums)
    mat = [[1, 0, 0], [0, 1, 1], [0, 0, 1]]
    # count_zeros_ones(mat)
    # add_matrix(mat, mat)
    display(mat)
