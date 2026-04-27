# Sliding Window problem

# Maximum Average Subarrayax
"""
Find the contiguous subarray of length k with maximum average.
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75  # subarray [12,-5,-6,50]
"""
import copy
from typing import List


def max_sub_arr(arr, k) -> tuple[List, float]:
    n = len(arr) - 1
    sub_arr = arr[:k]
    window_sum = sum(sub_arr)
    max_sum = window_sum
    max_start = 0

    for i in range(k, n):
        window_sum += arr[i]  # Add next element
        window_sum -= arr[i - k]  # Remove prev

        if window_sum > max_sum:
            max_sum = window_sum
            max_start = i - k + 1  # start = i - (k - 1)
    max_sub = arr[max_start : max_start + k]
    return (max_sub, max_sum / k)


# Longest Substring Without Repeating Characters
"""Already done — resolve it from scratch without looking at previous solution.
Input: "abcabcbb"
Output: 3
"""


def longest_sub(s):
    seen = set()
    l = 0
    max_len = 0
    l_start = 0
    l_end = 0

    for r in range(len(s)):
        while s[r] in seen:  # If seen, remove from left
            seen.remove(s[l])
            l += 1
        # Add new element from right
        seen.add(s[r])

        if r - l + 1 > max_len:
            max_len = r - l + 1
            l_start = l
            l_end = r + 1
    return (max_len, s[l_start:l_end])


# Minimum Size Subarray Sum
"""Find the minimum length subarray whose sum is greater than or equal to target.
Input: target=7, nums=[2,3,1,2,4,3]
Output: 2  # [4,3]

def min_subarray_len(target, nums):
    left = 0
    curr_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len
"""


def min_sub_arr(arr, target):
    n = len(arr)
    window_sum = 0
    l = 0
    min_len = float("inf")
    start = 0  # to track best window

    for right in range(n):
        window_sum += arr[right]

        while window_sum >= target:
            if right - l + 1 < min_len:
                min_len = right - l + 1
                start = l  # save best start

            window_sum -= arr[l]
            l += 1

    if min_len == float("inf"):
        return ([], 0)

    return (arr[start : start + min_len], min_len)


# nums = [1, 12, -5, -6, 50, 3]
# k = 4
# print(max_sub_arr(nums, k))

print("-- Longest Sub string ---")
input = "abcabcbb"
print(longest_sub(input))

print("-- Min Size Sub array -- ")
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(min_sub_arr(nums, target))
