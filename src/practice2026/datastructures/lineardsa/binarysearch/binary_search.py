from typing import List, Optional, Tuple, Union


# Chapter 1: The Core Idea
# The Mental Model
# Think of a dictionary book. You want to find the word "Mango."
# Brute force: Start from page 1, read every word until you find it. O(n).
# Binary search: Open the book in the middle. See "P" words.

# "Mango" comes before "P" → throw away the right half
# Open the middle of the left half. See "G" words.
# "Mango" comes after "G" → throw away the left half
# Keep halving until you find it.

# Every single step eliminates half the remaining search space.
# Time Complexity: O(log n)
# Because it drop half every time for the search
# One hard requirement: Binary search only work for the sorted array


def binary_search(arr: List[int], target: int):
    # define left and right
    left, right = 0, len(arr) - 1

    while (
        left <= right
    ):  # Always use <= becuase otherwise it will leave the middle element
        # calculate the mid on each iteration
        mid = (left + right) // 2  # // for integer division

        # Step 1: Check if mid is the target number
        if arr[mid] == target:
            return mid
        # Step 2: check if target is greater than the mid -> add one in left to move more right
        if arr[mid] < target:
            left = (
                mid + 1
            )  # Note why mid + 1, becuase mid is already have seen so we need to look after it
            # If we don't use +1 then it would end up as infinite loop
        else:
            right = mid - 1  # if target less then mid move right to left by 1

    return -1  # if not found return -1


# Prob - Given a sorted array that has been rotated, find the target.
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4  (index of 0)


def binary_search_for_rotated(arr: List[int], target):
    # define the pointers
    left, right = 0, len(arr) - 1

    # Steps:

    while left <= right:
        # Step 1: Divide array into two halfs
        mid = (left + right) // 2
        # Mid =    3
        # Left Half =  [4, 5, 6, 7]
        # Right Half = [0, 1, 2]
        if arr[mid] == target:
            return mid
        # Step 2: Check if left half or right sorted
        if arr[left] <= arr[mid]:
            # left half is sorted

            # Step 3: is target in this sorted left half?
            if arr[left] <= target < arr[mid]:  # yes → go left
                right = mid - 1
            else:
                # no -> go right
                left = mid + 1

        else:
            # Step 4: is target in this sorted right half?
            # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1  # yes → go right
            else:
                right = mid - 1  # no → go left

    return -1


# Prob - Find the number in 2D array where every row is in sorted order and every rows ending number is less then the starting number of the next row
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10


def find_num_in_2d(matrix: List[List[int]], target: int) -> Optional[Tuple[int, int]]:
    # Using brute force
    cols = len(matrix[0]) - 1
    for i, row in enumerate(matrix):
        if row[0] <= target <= row[cols]:
            res = binary_search(row, target)
            if res >= 0:
                print(matrix[i][res])
                return (i, res)
    # Total: O(rows + log cols)
    return None


def find_num_in_2d_opt(
    matrix: List[List[int]], target: int
) -> Optional[Tuple[int, int]]:
    # Using optimized solution
    # Steps
    # 1. In upper solution we already ran binary search on the columns to find the exact number in every row
    # 2. But the issue with that is we were still filtering out the rows in sequential order
    # 3. So new approach is we will scan best row same way using binary search as we did for the cols
    rows = len(matrix)
    cols = len(matrix[0])
    target_row = -1

    # define top and bottom pointers for the rows
    top, bot = 0, rows - 1  # point top row and bottom row

    # loop
    while top <= bot:
        row = (top + bot) // 2  # [row][x]

        # check the target is greater then largest value in this row
        if target > matrix[row][-1]:  # -1 -> last value in this row
            # yes -> move row to next
            top = row + 1
        elif target < matrix[row][0]:  # if target less then smallest value in this row
            # Move bottom row pointer up
            # now -> dec row
            bot = row - 1
        else:
            target_row = row  # explicitly save found row
            break
    if target_row == -1:
        return None
    # Run binary search on found row
    left, right = 0, cols - 1

    while (
        left <= right
    ):  # Always use <= becuase otherwise it will leave the middle element
        # calculate the mid on each iteration
        mid = (left + right) // 2  # // for integer division

        # Step 1: Check if mid is the target number
        if matrix[target_row][mid] == target:
            return (target_row, mid)
        # Step 2: check if target is greater than the mid -> add one in left to move more right
        if matrix[target_row][mid] < target:
            left = (
                mid + 1
            )  # Note why mid + 1, becuase mid is already have seen so we need to look after it
            # If we don't use +1 then it would end up as infinite loop
        else:
            right = mid - 1  # if target less then mid move right to left by 1

    return None


# Phase 1 — Binary search on rows:    O(log rows)
# Phase 2 — Binary search on columns: O(log cols)

# Total Time:  O(log rows + log cols) = log(rows × cols)
# Total Space: O(1) — no extra memory used


def print_ext(result):
    if isinstance(result, tuple):
        row, col = result
        print(
            f"Target {target} is present in matrix at: {[row][col]} value is: {input[row][col]}"
        )
    else:
        print(f"Target {target} is not in range")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    target = 5
    res = binary_search(arr, target)
    if res < 0:
        print(f" Target, {target} is not present in list")
    else:
        print(f" Target, {target} is present at position: {res}")
    arr_rot = [4, 5, 6, 7, 0, 1, 2]
    print("---- Rotated Binary Search ----")
    arr_rot = [4, 5, 6, 7, 0, 1, 2]
    target_two = 0
    res = binary_search_for_rotated(arr_rot, target_two)
    if res < 0:
        print(f" Target, {target_two} is not present in list")
    else:
        print(f" Target, {target_two} is present at position: {res}")

    print("---- Find number in 2d array ----")
    input = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    target = 10
    result = find_num_in_2d(input, target)
    print_ext(result)

    print("---Optimized solution for 2d binary search----")
    print_ext(find_num_in_2d_opt(input, target))
