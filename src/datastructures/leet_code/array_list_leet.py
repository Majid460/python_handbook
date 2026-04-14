# Find target from list indices
"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""
arr1 = [1, 3, 4, 5]
arr2 = [4, 6]


def two_sum(target):
    input_list = [2, 7, 11, 15]
    hash_map = {}

    # With two loops
    # for i in range(len(input_list)):
    #     for j in range(i+1, len(input_list)):
    #         if input_list[i] + input_list[j] == target:
    #             return [i,j]

    for i, num in enumerate(input_list):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i


# Find median of two arrays
def find_median():
    # merge both
    arr3 = arr1 + arr2
    arr4 = sorted(arr3)
    start, end = 0, len(arr4) - 1
    mid = (start + end) // 2
    print(arr4)
    median = arr4[mid]
    print(median)


# Find the longest prefix in the array
def find_the_longest_prefix():
    list_str = ["flow", "flower", "floor"]
    prefix = list_str[0]
    for i in list_str[1:]:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    print(f"Longest prefix is: {prefix}")


# Find the max area of container
def max_area():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_a = 0

    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            h = min(height[i], height[j])
            area = h * width
            max_a = max(max_a, area)

    return max_a


res = two_sum(9)
print(res)
find_median()
# Find prefix
find_the_longest_prefix()

print(f"Max Area is = {max_area()}")
# Max Area is = 49
