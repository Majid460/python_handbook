from typing import List

# Use two pointers left and right to traverse the array


# Prob - Find a string is a palindrome with case in-sensitivity and only for alpha numeric
# s = "Was it a car or a cat I saw?"
def check_plaindrome(s: str) -> bool:
    n = len(s)
    left, right = 0, n - 1

    # Loop until left less than right
    while left < right:
        # skip non-alphanumeric
        while (
            left < right and not s[left].isalnum()
        ):  # skip if current left is not alpha or number
            left += 1  # move one forward
        while (
            right > left and not s[right].isalnum()
        ):  # skip if current right is not alpha or number
            right -= 1  # move one back

        if s[left].lower() != s[right].lower():
            return False
        left, right = left + 1, right - 1

    return True


# Prob - Two pointers
def two_sum_sorted(arr: List[int], target: int) -> List:
    n = len(arr)
    left, right = 0, n - 1

    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1

    return []


# Prob - Find the duplicate numbers using simple method
def find_duplicate(arr: List[int]):
    arr.sort()
    seen = set()
    duplicates = set()
    for i in arr:
        if i in seen:
            duplicates.add(i)
        seen.add(i)
    return duplicates


# TC -> O(n)
# SC -> O(n) # n is set of number of duplicates if all are duplicates


# Prob - Remove duplicate with two pointers
def remove_duplicate(arr: List[int]):
    # init a slow pointer
    slow = 0
    n = len(arr)
    for fast in range(1, n):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
    print(arr)
    return slow + 1


# Prob - Sliding window - fixed size window
# Problem : Maximum Sum Subarray of Size K
def find_max_sum_sub_arr(arr: List[int]):
    k = 3  # window size
    n = len(arr)
    window_sum = sum(arr[:k])
    max_sum = window_sum
    start = 0

    # slide it
    for right in range(k, n):
        left = right - k  # k = 3, right= 3, left = 0
        window_sum += arr[right]  # add incoming
        window_sum -= arr[left]  # remove outgoing
        if window_sum > max_sum:
            max_sum = window_sum
            start = right - k + 1
    return (max_sum, arr[start : start + k])


# Sliding Window variable size
def length_of_longest_substring(s: str):
    res, left = 0, 0
    seen = set()
    n = len(s)
    best_left = 0  # track where best window started
    best_right = 0  # track where best window ended

    for right in range(n):
        # if s[right] element is in seen means repeating so remove it from left side and move left forward
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        # While runs until unqiue started coming

        # Then add the right in set
        seen.add(s[right])

        # Now find the max length of unique sub string
        if right - left + 1 > res:  # strictly greater only
            res = right - left + 1
            best_left = left
            best_right = right  # old res, right - left + 1 => +1 refers to convert it to elements from range indices
        print(s[best_left : best_right + 1])  # slice to extract substring
        print(f"res::{res}")
    return (res, s[best_left : best_right + 1])


# Prob 167 -  2 sum 2 problem using two pointers
# Rule - array is sorted and in the result array 0 index must be non zero
# arr = [2,7,11,15], target = 9
def two_sum_two(arr: List[int], target: int) -> List[int]:

    # Create two pinters right and left
    left = 0
    right = len(arr) - 1

    while left < right:
        # check the sum of current left and right
        print(f"left:: {left},right:: {right}")
        curr_sum = arr[left] + arr[right]
        print(f"current sum:: {curr_sum}")
        if curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            print(f"left:: {left},right:: {right}")
            # Indices are based on 1 so add one each time
            return [left + 1, right + 1]

    return []
    # TC -> O(n)
    # SC -> O(1)


# Prob 15 - 3 sum problem
# Can have muliple result lists
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# Sum of triplet must be 0
def three_sum(arr: List[int]) -> List[List[int]]:
    arr.sort()  # O(n log n)
    res = []

    for i, a in enumerate(arr):
        if a > 0:  # a should greater than 0
            break
        if (
            i > 0 and a == arr[i - 1]
        ):  # In sorted array if duplicates exist then they are consective
            # To avoid it we need to check it and skip if exist
            continue
        # Use helper to find triplets for this a
        find_triplets(arr, i, a, res)
    return res


def find_triplets(arr: List[int], i: int, a: int, res: List[List[int]]):
    l, r = i + 1, len(arr) - 1  # left always points to one ahead of base pointer i

    while l < r:
        three_sum_val = a + arr[l] + arr[r]
        if (
            three_sum_val > 0
        ):  # Sum of triplet greater than 0, we need to decrease a index of right from right
            r -= 1
        elif three_sum_val < 0:  # sum is less increase left
            l += 1
        else:  # equal to 0
            res.append([a, arr[l], arr[r]])
            # inc and dec the left and right pointer for next slide
            l += 1
            r -= 1
            # Skip duplicates for left
            while l < r and arr[l] == arr[l - 1]:
                l += 1


# TC -> O(n^2)
# SC -> O(1) or O(m) depending on sorting algorithm


# Prob - Container with most amount of water
# TC -> O(n) => linear amount of time
def calculate_container_water(arr: List[int]):

    n = len(arr)
    left, right = 0, n - 1
    max_sum = 0
    temp = 0

    while left < right:
        if arr[left] == 0:
            left += 1
        if arr[right] == 0:
            right -= 1
        # Take min height of bars
        area = min(arr[left], arr[right]) * (right - left)
        if area > max_sum:
            temp = max_sum
            max_sum = area
        print(f"left at:{left} , right at:{right}")
        print(
            f"Sum at {left} at {right}:: {area}, max sum :: {max_sum}, prev max :: {temp}"
        )
        if arr[left] < arr[right]:
            # if height of left less than right inc left to get max result
            left += 1
        else:
            right -= 1
    return max_sum


# Prob - Trapping Rain Water
# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
# Return the maximum area of water that can be trapped between the bars.
# input : height = [0,2,0,3,1,0,1,3,2,1]
# Area = h x w
# TC-> O(n)
def calculate_max_area(height: List[int]):
    if not height:
        return 0
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = height[left], height[right]
    res = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(height[left], left_max)
            res += left_max - height[left]
        else:
            right -= 1
            right_max = max(height[right], right_max)
            res += right_max - height[right]

    return res


# Merge Sort
# Divide array into two and then use two pointer to combine the each sub array into one and sort
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    # get length
    n = len(arr)

    mid = n // 2
    # Make two sub arrays and run it rec for each new array
    left_arr = merge_sort(arr[:mid])  # exclude the mid
    right_arr = merge_sort(arr[mid:])

    return merge_sorting(left_arr, right_arr)


def merge_sorting(left_arr, right_arr) -> List[int]:
    i, j = (
        0,
        0,
    )  # i points to left start index, j points to right start point
    res: List[int] = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            res.append(left_arr[i])
            i += 1
        else:
            res.append(right_arr[j])
            j += 1
    # add remaining elements
    res.extend(left_arr[i:])
    res.extend(right_arr[j:])
    return res


# TC -> O(n log n)
# SC -> O(n) # It uses (extra array for merging)

if __name__ == "__main__":
    print("Two sum")
    print(two_sum_sorted([2, 7, 11, 15], 9))
    print("check palindrome::")
    s = "9 Was it a car or a cat I saw 9?"
    print(f"{s} is palindrome: {check_plaindrome(s)}")
    dup = [1, 2, 2, 4, 5, 5]
    print(f"Find the duplicates::{find_duplicate(dup)}")
    print("Remove duplicates from the array::")
    arr = [1, 2, 2, 3, 3, 4]
    length = remove_duplicate(arr)
    print(f"Remove duplicate :: {arr[:length]}")
    input = [2, 3, 1, 4, 5, 2, 3]
    print(f"Find max sum sub array:: {find_max_sum_sub_arr(input)}")
    sample_str = "abcabcbb"
    print(f"Maximum length sub string:: {length_of_longest_substring(sample_str)}")

    # Two sum two problem
    arr_s = [2, 7, 11, 15]
    target = 9
    print(two_sum_two(arr_s, target))

    # Three sum
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"Three sum:: {three_sum(nums)}")
    # Three sum:: [[-1, -1, 2], [-1, 0, 1]]

    # Trapping water
    print("Trapping water")
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    print(f"max sum is:: {calculate_max_area(height)}")

    # Merge sort
    un_sort_arr = [1, 3, 5, 2, 4, 6]
    print(f"Merge Sort :: {merge_sort(un_sort_arr)}")
