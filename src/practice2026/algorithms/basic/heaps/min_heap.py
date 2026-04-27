import heapq
from typing import List

# Heaps are complete binary trees where nodes are filled level by level from left to right

#  Min Heap - Smallest element on top
#  Max Heap - Largest element on top

# Prob using
"""
Prob - Given an array of integers, return the K largest elements.
nums = [3, 2, 1, 5, 6, 4], k = 2
output = [5, 6]  # order doesn't matter

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
output = [4, 5, 5, 6]
"""


def find_kth_largest_nums(arr, k) -> List[int]:
    # I will use min heap and keep only the size to k
    heap = []
    i = 0
    while i < len(arr):
        if len(heap) < k:
            # Fill the heap until k
            heapq.heappush(heap, arr[i])
        elif arr[i] > heap[0]:
            # num is larger than smallest in heap
            heapq.heapreplace(heap, arr[i])  # remove min, add num
        i += 1
    return heap


# Max Heap
def max_heap(arr):
    heap = []
    # For max heap we use negative numbers
    [heapq.heappush(heap, -x) for x in arr]
    return [-x for x in heap]


# Prob Find the kth smallest numbers
# I will use max heap
# Smallest will left on right side and every time new element comes if it will be smaller than the -heap[0] it should replace with 0th element
def find_kth_smallest(arr, k):
    # heap
    heap = []

    for x in arr:
        if len(heap) < k:
            heapq.heappush(
                heap, -x
            )  # - used becuase to create max heap, large number on right
        elif x < -heap[0]:
            heapq.heapreplace(
                heap, -x
            )  # Pop the smallest from the start which is actually greater and push new element in the end
    return [-x for x in heap]


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3]
    k = 2

    print(find_kth_largest_nums(nums, k))

    print("----- Max Heap ------")
    print(max_heap([2, 4, 1]))

    print(find_kth_smallest(nums, k))
