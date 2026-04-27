from collections import Counter
import copy
from functools import reduce
from typing import List
from collections import defaultdict

# Lists are a collection of items that are ordered and changeable. They are defined by using square brackets [].
list_1 = [1, 2, 3, 2, 2, 4, 5]
c = Counter(list_1)
print(c)


def sum_elements():
    sum_of_elements = sum(list_1)
    print(sum_of_elements)


# Two sum problem
def two_sum_prob(list: list[int], target: int) -> list[int]:
    # Create a hashmap
    hash_map = {}  # num -> index
    for i, n in enumerate(list):
        diff = target - n  # Cal diff btw target and current element
        if diff in hash_map:  # if diff in hashmap
            return [hash_map[diff], i]
        hash_map[n] = i

    return []


# TC -> O(n)
# SC -> O(n)


# duplicate in array - return true else false
def check_dpl(list: list[int]):
    v_set = set()
    for i in list:
        if i in v_set:
            return True
        v_set.add(i)
    return False


# Worked Example — Number of Islands
# Classic problem: count groups of connected 1s in a grid.
# def num_islands(grid):
#     if not grid:
#         return 0
#     # Find rows and cols
#     rows, cols = len(grid), len(grid[0])
#     dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down,left, right
#     count = 0

#     def dfs(r, c):
#         # Handle bounds and base case, out of bounds not a land
#         if (
#             0 > r >= rows or 0 > c >= cols or grid[r][c] != "1"
#         ):  # if r less than 0 or greater than rows | c less than 0 or greater than cols | [r][c] is not equal to 1
#             return
#         grid[r][c] = "0"
#         for dr, dc in dirs:  # loop on directions array
#             dfs(r + dr, c + dc)  # dr -> delta row, dc -> delta col :: dr
#             # dr -> how many rows to move
#             # dc -> how many cols to move

#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == "1":
#                 dfs(i, j)
#                 count += 1
#     return count


def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    count = 0

    def dfs(r, c):
        # base case: out of bounds or not land
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return

        grid[r][c] = "0"  # mark visited by sinking the land

        for dr, dc in dirs:
            dfs(r + dr, c + dc)  # explore all 4 neighbours

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)  # sink the whole island
                count += 1  # one dfs call = one island

    return count


# Find the elements those are duplicate
def get_dpl(list: list[int]):
    # advance
    return {k: v for k, v in Counter(list).items() if v > 1}  # O(n) + O(k) = O(n)
    # Basic
    # freq = {}
    # for n in list:
    #     freq[n] = freq.get(n, 0) + 1
    # freq = {k: v for k, v in freq.items() if v > 1}
    # return freq

    # dup = []
    # for k, v in dpl_map.items():
    #     if v > 1:
    #         dup.append((k, v))
    # return dup


# Array concat
def array_concat(arr):
    new_arr = arr + copy.deepcopy(arr)
    print(new_arr)

    # Another approach using another list of 0s
    n = len(arr)
    emp = [0] * (2 * n)
    for i, num in enumerate(arr):
        emp[i] = emp[i + n] = num
    return emp


# Check two strings are anagrams => Anangram means two strings have exact same characters but order may differ
def check_anagram(s1: str, s2: str) -> bool:
    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False
    # 1st Approach
    # new_s1 = sorted(s1.lower())
    # new_s2 = sorted(s2.lower())
    # if new_s1 == new_s2:
    #     return True

    # TC -> O(n log n + m log m)
    # SC -> O(1) or O(m + n) # depend on sorting algo

    # 2nd Approach

    count_s, count_t = (
        {},
        {},
    )  # store the count of numbers in each string :: char -> count
    for i in range(len(s1)):
        count_s[s1[i]] = 1 + count_s.get(s1[i], 0)
        count_t[s2[i]] = 1 + count_t.get(s2[i], 0)
    # TC -> O(n+m)
    # SC -> O(1) # since we have less chars
    return count_s == count_t


# 238. Product of Array Except self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
def product_array(arr: List[int]):
    # arr = [1,2,4,6]
    output_arr = []
    temp_arr = copy.deepcopy(arr)
    for i in range(len(arr)):
        temp_element = arr[i]
        temp_arr.pop(i)  # Remove indexed value from temp arr
        prod = reduce(lambda x, y: x * y, temp_arr)
        output_arr.insert(i, prod)
        temp_arr.insert(i, temp_element)
    return output_arr


# TC -> O(n^2) -> because of shifting of elements every time on pop and insert
# SC -> O(n)


# Optimized solution for the product array
def product_array_opt(arr: List[int]):
    # arr = [1,2,4,6]
    n = len(arr)
    res = [1] * n

    prefix = 1  # Left side product of arr
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]
    # res = [1, 1, 2, 8]
    suffix = 1  # Right side of array
    for i in range(n - 1, -1, -1):  # Start from end, go backwards till index 0
        res[i] *= suffix
        suffix *= arr[i]
    # [48, 24, 12, 8]
    return res


# Single pass left + right → O(n)
# No extra arrays → O(1) space


if __name__ == "__main__":
    list_ = [3, 4, 5, 6]
    target = 7

    res = two_sum_prob(list_, target)
    print(res)
    print(check_dpl([1, 2, 4, 5, 2]))
    print("Get Duplicate values")
    print(get_dpl([1, 2, 2, 3, 4, 3]))

    print("Find the number of islands")
    grid = [["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]]
    print(num_islands(grid))
    print("Concate array")
    print(array_concat([1, 2, 3]))

    # product of array
    print("Product")
    print(product_array([1, 2, 4, 6]))
    print(product_array_opt([1, 2, 4, 6]))
