import math
from math import *


# Separate Numbers
# Reverse Numbers
# To count digits introduce a variable
def print_numbers(n: int):
    count = 0
    while n > 0:
        last_digit = n % 10
        count += 1
        print(f"{last_digit}", end=" ")
        n = n // 10
    print()
    print(f"digit counts:: {count}")


# Count Numbers using log
def count_integers(n: int):
    res = math.pow(2, 2)
    print(res)
    print(int(math.log10(n) + 1))


# Remove minimum parenthesis from string like (a(b)))
def remove_parenthesis(s: str):
    stack = []
    remove = set()

    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        elif ch == ")":
            if stack:
                stack.pop()
            else:
                remove.add(i)

    remove.update(stack)

    result = "".join(ch for i, ch in enumerate(s) if i not in remove)
    print(result)


# Prob - Binary Search using two pointers
# nums = [-1, 0, 3, 5, 9, 12] ,search element
def binary_search(arr, n):
    if not arr:
        return
    size = len(arr)
    left, right = 0, size - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == n:
            return mid
        if n > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Sorted Rotated array find a num
# I will use bst and find whether the left half is sorted or right
# Then i will check the element in the given half
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0  # returns 4
# target = 3  # returns -1
def rotated_bs(arr, target):
    if not arr:
        return -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        # Check which half is sorted
        if arr[left] <= arr[mid]:
            # Left half is sorted
            # Check if target is in left..mid
            if arr[left] <= target < arr[mid]:  # yes → go left
                right = mid - 1
            else:  # no -> go right
                left = mid + 1

        else:
            # Step 4: is target in this sorted right half?
            # Right half is sorted
            if arr[mid] < target <= arr[right]:  # yes go -> right
                left = mid + 1
            else:
                # Go left
                right = mid - 1
    return -1
    # Time:  O(log n) — halving search space each iteration
    # Space: O(1)     — no extra space used


if __name__ == "__main__":
    n1 = 4393
    # print_numbers(n1)
    count_integers(n1)
    print("-------- Remove parenthesis----------")
    # remove_parenthesis("()())()")
    print("----- Binary Search -------")
    nums = [-1, 0, 3, 5, 9, 12]
    print(binary_search(nums, 3))

    arr = [4, 5, 6, 7, 0, 1, 2]
    target = 0  # returns 4
    # target = 3  # returns -1
    print(rotated_bs(arr, target))
