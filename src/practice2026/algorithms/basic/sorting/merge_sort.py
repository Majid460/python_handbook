from typing import List, Tuple

# Divide first using recursion
# Pick each level from stack and perform merge


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right) -> List[int]:
    # Declare two pointers i and j
    # i points to the start index of left
    # j points to the start index of right
    i, j = (0, 0)
    res = []
    while i < len(left) and j < len(right):
        # No check the comparison for index to index of left and right
        if left[i] <= right[j]:
            # left element is small
            res.append(left[i])
            # inc i to compare each element of left to right
            i += 1
        else:
            res.append(right[j])
            j += 1
    # add remaining elements
    # extend → adds elements individually
    res.extend(left[i:])
    res.extend(right[j:])
    return res


"""
Complexity — Know This Cold
Time: O(n log n)
log n levels of splitting
n work at each level (merging)
total = n × log n
Level 0:  [3,1,4,1,5,2]           → n=6 work
Level 1:  [3,1,4]  [1,5,2]        → n=6 work
Level 2:  [3,1][4] [1,5][2]       → n=6 work
Level 3:  [3][1][4][1][5][2]      → n=6 work

log₂(6) ≈ 3 levels × 6 work = O(n log n)
Space: O(n)
Each merge creates a new array. Total extra space across all levels = O(n).
"""

if __name__ == "__main__":

    arr = [4, 5, 6, 7, 0, 1, 2]
    print(merge_sort(arr))
