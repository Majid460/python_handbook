"""
A regular heap (heapq) guarantees fast access to the root (min or max).

But searching or removing an arbitrary element is O(n).

If your system needs fast arbitrary access + fast min/max, a plain heap is inefficient.

1. Heap with hashmap for better deletion and searching
"""

