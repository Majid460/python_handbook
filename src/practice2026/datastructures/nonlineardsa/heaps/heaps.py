"""
A heap is a special type of complete binary tree (every level is filled except maybe the last).

Two properties:
Complete Tree → always filled left-to-right.
Heap Property:
Min-Heap → Parent ≤ Children (smallest element at root).
Max-Heap → Parent ≥ Children (largest element at root).

Because of these properties:
Root = min (min-heap) or max (max-heap).
Efficient for priority-based access.

Feature	            Min-Heap	                                                    Max-Heap
Root	            Smallest element	                                            Largest element
Use Cases	        Priority queues, Dijkstra’s algorithm, event simulation	        Sorting in descending, job schedulers
Insert	            O(log n)	                                                    O(log n)
Extract Root	    O(log n)	                                                    O(log n)
Access Root	        O(1)	                                                        O(1)

--> Detail:
Operation	                            Time Complexity
Build heap (heapify)	                O(n)
Insert (push)	                        O(log n)
Extract root (pop)	                    O(log n)
Peek root	                            O(1)
Search element	                        O(n)
Remove arbitrary item	                O(n) (search) + O(log n) (fix) = O(n)
Insert in middle	                    Not valid (only append + bubble)
"""

import heapq

"""
A regular heap (heapq) guarantees fast access to the root (min or max).

But searching or removing an arbitrary element is O(n).

If your system needs fast arbitrary access + fast min/max, a plain heap is inefficient.
"""


class MinHeap:
    def __init__(self):
        self.arr = []
        heapq.heapify(self.arr)

    # Insert in the heap
    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        heapq.heappush(self.arr, val)
        return True

    # Get min root
    def get_min_root(self):
        if self.arr:
            return self.arr[0]

    # Get max value O(n)
    def get_max(self):
        if self.arr:
            return max(self.arr)

    # Pop min element
    """
    Push item on the heap, then pop and return the smallest item from the heap.
    The combined action runs more efficiently than heappush() followed by a separate call to heappop().
    
    heapq.heappushpop(heap, item)

    Process:
    Push item into the heap.
    Pop & return the smallest element.
    Done in one combined operation (so more efficient than doing heappush + heappop separately).
    Complexity: O(log n).
    
    But note:
    If the pushed item is smaller than the heap’s current min, that pushed item is popped immediately.
    """

    def push_pop(self):
        if self.arr:
            return heapq.heappushpop(self.arr, 100)

    # Pop min element
    def pop(self):
        if self.arr:
            return heapq.heappop(self.arr)

    # Pop and replace
    """
    heapq.heapreplace(heap, item)
    Process:
    Pop & return the smallest element.
    Push item into the heap.
    Complexity: O(log n).
    But Note:
    Requires heap not empty — otherwise throws IndexError.
    """

    def pop_replace(self, item):
        if self.arr:
            return heapq.heapreplace(self.arr, item)


class MaxHeap:
    def __init__(self):
        self.arr = []
        heapq.heapify(self.arr)

    # Insert in the heap
    def insert(self, val: int) -> bool:
        # store negative to simulate max-heap
        if -val in self.arr:
            return False
        heapq.heappush(self.arr, -val)
        return True

    # Get max value O(1)
    def get_max(self):
        if self.arr:
            return -self.arr[0]  # negate back to positive

    # Extract max (O(log n))
    def extract_max(self):
        if self.arr:
            return -heapq.heappop(self.arr)

    # Pop min element
    """
    Push item on the heap, then pop and return the smallest item from the heap.
    The combined action runs more efficiently than heappush() followed by a separate call to heappop().

    heapq.heappushpop(heap, item)

    Process:
    Push item into the heap.
    Pop & return the smallest element.
    Done in one combined operation (so more efficient than doing heappush + heappop separately).
    Complexity: O(log n).

    But note:
    If the pushed item is smaller than the heap’s current min, that pushed item is popped immediately.
    """

    def push_pop(self):
        if self.arr:
            return -heapq.heappushpop(self.arr, 100)

    # Pop min element
    def pop(self):
        if self.arr:
            return -heapq.heappop(self.arr)

    def get_heap(self):
        return [-x for x in self.arr]

    # Pop and replace
    """
    heapq.heapreplace(heap, item)
    Process:
    Pop & return the smallest element.
    Push item into the heap.
    Complexity: O(log n).
    But Note:
    Requires heap not empty — otherwise throws IndexError.
    """

    def pop_replace(self, item):
        if self.arr:
            return -heapq.heapreplace(self.arr, item)


if __name__ == "__main__":
    heap = MinHeap()
    [heap.insert(i) for i in [11, 2, 44, 3, 1, 4, 9]]
    print(heap.arr)
    print("--------------- Get Max Heap ----------------")
    res = heap.get_max()
    print(f"Max number in heap:: {res}")
    print("--------------- Get Min Heap ----------------")
    res = heap.get_min_root()
    print(f"Min number in heap:: {res}")
    print("--------------- Get Min Heap ----------------")
    res = heap.get_min_root()
    print(f"Min number in heap:: {res}")
    print("--------------- Push and Pop in Heap ----------------")
    res = heap.push_pop()
    print(f"Push Pop in heap:: {res}")
    print(heap.arr)
    print("--------------- Pop in Heap ----------------")
    res = heap.pop()
    print(f"Pop in heap:: {res}")
    print(heap.arr)

    print("--------------- Pop and Replace in Heap ----------------")
    res = heap.pop_replace(101)
    print(f"Replace in heap:: {res}")
    print(heap.arr)
    print("--------------- Max Heap ----------------")
    heap = MaxHeap()
    [heap.insert(i) for i in [11, 2, 44, 3, 1, 4, 9]]
    print("Heap internal (negatives):", heap.arr)
    print("Heap as positives:", heap.get_heap())
    print("--------------- Get Max Heap ----------------")
    res = heap.get_max()
    print(f"Max number in heap:: {res}")
    print("--------------- Extract Max ----------------")
    print("Extracted:", heap.extract_max())
    print("Heap now:", heap.get_heap())
