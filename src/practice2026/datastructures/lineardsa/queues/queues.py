from collections import deque
from dataclasses import dataclass, field
from typing import List
import heapq

# Insert elements in queue from back
# Remove elements from queue from the front
# First person in line gets served first

# This is called FIFO — First In, First Out.
# Opposite of stack which was LIFO.

# Python has built-in queues  - deque


def basic_queue():
    queue = deque()  # Double ended queue
    # Insert at end
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    print(queue)
    # deque([1, 2, 3, 4])

    # Remove elements from the start of the queue
    queue.popleft()
    print(queue)
    # Peek front
    front = queue[0]  # 2
    print(front)

    # Peek back
    back = queue[-1]  # 3
    print(back)
    # Check empty
    if not queue:
        print("empty")

    # Size
    print(len(queue))  # 2


## Chapter 2: Heap — Priority Queue
### The Mental Model

# Queue serves people in order of **arrival.**
# Heap serves people in order of **priority.**

# Think of a **hospital emergency room:**
#
# Patient A — broken finger  (low priority)
# Patient B — heart attack   (HIGH priority)  ← treated first
# Patient C — sprained ankle (low priority)
#

# Patient B arrived last but gets seen first. Order of arrival doesn't matter — **urgency does.**

# That's a heap. Always gives you the most important element first.

### Two Types of Heap

# **Min Heap** — smallest element always at top (most common in interviews)
# **Max Heap** — largest element always at top


# Python's heapq is a min heap by default.
def heap():
    nums = [5, 3, 8, 1, 9, 2]

    # Heapify — What Does It Mean?
    # Heapify = take an unordered list and rearrange it into heap order.
    heapq.heapify(nums)  # rearranges IN PLACE
    print(nums)  # [1, 3, 2, 5, 9, 8]
    # Cost: O(n) — faster than sorting which is O(n log n).

    # Heap operations
    heap = []

    # Push — add element
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 3)
    # heap = [1, 5, 3]  ← 1 always at top
    heapq.heappush(heap, -1)
    # Pop — remove and return smallest
    val = heapq.heappop(heap)  # val = 1
    # heap = [3, 5]

    # Peek — look at smallest without removing
    smallest = heap[0]  # 3

    # Push and pop in one step (more efficient)
    val = heapq.heappushpop(heap, 2)

    # Heapify existing list
    nums = [5, 3, 8, 1]
    heapq.heapify(nums)  # [1, 3, 8, 5]

    # Max Heap in Python — The Trick
    # Python only has min heap. To simulate max heap, negate the values:
    heap = []

    # Push negated
    heapq.heappush(heap, -5)
    heapq.heappush(heap, -1)
    heapq.heappush(heap, -3)

    # Pop and negate back
    val = -heapq.heappop(heap)  # val = 5  ← largest

    print(val)  # 5 ✓


# Negating flips the order. Smallest negative = largest original number.


# Heap problems
# Prob 1 - Kth Largest Element
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# maintain a min heap of size k. The top is always the kth largest.
def kth_largest(arr, k):
    heap = []
    # heapq is by default min heap
    if not arr:
        return
    for v in arr:
        heapq.heappush(heap, v)

        if len(heap) > k:
            heapq.heappop(heap)  # pop the smallest item which is on index 0

    # Top of heap = kth largest
    return heap[0]  # evantually second last number is min of k largest


# Problem: Given a list of tasks where each task has a priority number, always process (print) the highest priority task first.
# tasks = [(3, "wash dishes"), (1, "check email"), (5, "fix bug"), (2, "eat lunch")]


# Expected output (highest priority first):
# fix bug
# wash dishes
# eat lunch
# check email
@dataclass(order=True)
class Task:
    priority: int
    task_name: str = field(compare=False)


class TasksCl:
    def __init__(self) -> None:
        self.heap: List = []

    def insert_task(self, task: Task):
        # Negate priority inside the Task itself
        negated = Task(-task.priority, task.task_name)
        heapq.heappush(self.heap, negated)

    def check_task_priorities(self):
        if not self.heap:
            return None
        while self.heap:
            task: Task = heapq.heappop(self.heap)
            print(f"Task Name: {task.task_name:<20}, Priority:{-task.priority:>2}")


## Stack vs Queue vs Heap — When to Use What
#
# STACK
# → You need the most RECENT thing
# → Matching pairs, undo, backtracking
# → LIFO

# QUEUE
# → You need the OLDEST thing
# → Level by level processing, BFS
# → FIFO

# HEAP
# → You need the SMALLEST or LARGEST thing
# → Priority processing, top K problems
# → Priority order

if __name__ == "__main__":
    basic_queue()
    heap()
    print("--- Kth largest number ---")
    arr = [3, 2, 1, 5, 6, 4]
    print(kth_largest(arr, 2))

    print("--- Check the priority---")
    tasks = TasksCl()
    task_list = [
        Task(3, "wash dishes"),
        Task(1, "check email"),
        Task(5, "fix bug"),
        Task(2, "eat lunch"),
    ]
    [tasks.insert_task(task) for task in task_list]
    tasks.check_task_priorities()
