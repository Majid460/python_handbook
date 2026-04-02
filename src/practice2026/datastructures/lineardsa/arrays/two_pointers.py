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
