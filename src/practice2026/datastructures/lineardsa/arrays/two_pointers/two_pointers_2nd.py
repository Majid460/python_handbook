# Two pointer probs


# Sum of two numbers in 1d to target
from enum import Enum


def sum_of_numbers(arr, target):
    arr.sort()
    n = len(arr)
    l, r = 0, n - 1
    while l < r:
        sum_ = arr[l] + arr[r]
        if sum_ == target:
            return (l, r)
        if sum_ > target:
            r = r - 1  # move left
        else:
            l = l + 1


# Palindrome
def valid_palindrome(s: str):
    s = s.lower()
    n = len(s)

    l, r = 0, n - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def max_area_water_container(heights):
    n = len(heights)
    max_area = 0
    l, r = 0, n - 1
    while l < r:
        width = r - l
        height = min(heights[l], heights[r])
        area = width * height
        max_area = max(area, max_area)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1


def three_sum(arr, target):
    arr.sort()
    n = len(arr)
    res = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            # duplicate
            continue
        inner_sum(arr, i, n, target, res)

    return res


def four_sum(arr, target):
    arr.sort()
    n = len(arr)
    res = []

    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            # duplicate
            continue
        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j - 1]:
                # duplicate
                continue
            inner_sum(arr, i, n, target, res, j)
    return res


def inner_sum(arr, i, n, target, res, j=-1):
    l, r = i + 1 if j == -1 else j + 1, n - 1
    while l < r:
        elem_j = arr[j] if j != -1 else 0
        sum_ = arr[i] + elem_j + arr[l] + arr[r]
        if sum_ == target:
            if j != -1:
                res.append([arr[i], arr[j], arr[l], arr[r]])
            else:
                res.append([arr[i], arr[l], arr[r]])
            # check duplicate pairs
            while l < r and arr[l] == arr[l + 1]:
                l += 1
            while l < r and arr[r] == arr[r - 1]:
                r -= 1
            l += 1
            r -= 1
        elif sum_ > target:
            r -= 1
        else:
            l += 1


# Max Trap Water
# height = [0,2,0,3,1,0,1,3,2,1]
"""
Water at any position depends on the shorter wall between the left and right sides.
So if the left wall is shorter, the right wall can't help us—water is limited by the left side.
That means we safely move the left pointer inward and calculate how much water can be trapped there.
Similarly, if the right wall is shorter, we move the right pointer left.

As we move the pointers, we keep track of the highest wall seen so far on each side (leftMax and rightMax).
The water at each position is simply:

max wall on that side – height at that position
"""


def trap_water(height):
    if not height:
        return 0
    res = 0
    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]

    while l < r:
        # We are calc the l-1 and l water storage
        # left wall is shorter move
        if left_max <= right_max:  # Move right
            l += 1
            left_max = max(left_max, height[l])
            res += (
                left_max - height[l]
            )  # max wall on left side - height at that position
        else:
            r -= 1
            right_max = max(right_max, height[r])
            res += right_max - height[r]
    return res


s = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(valid_palindrome(s2))

print(" ------- Sum Probs. -------- ")

print("---- Two sum -----")
arr = [3, 1, 7]
print(sum_of_numbers(arr, 4))
print("---- Three sum -----")
arr = [2, 3, 1, 7, 9, 3, 8]
target = 16
print(three_sum(arr, target))


print("---- Four sum -----")
arr = [2, 3, 1, 7, 9, 3, 8]
target = 21
print(four_sum(arr, target))

print("---- Trap water -----")
height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
print(trap_water(height))
