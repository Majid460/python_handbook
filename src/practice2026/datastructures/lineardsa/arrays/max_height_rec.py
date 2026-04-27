"""
Maximal Rectangle
Pattern: Height histogram per row
Given a 2D binary matrix filled with 0s and 1s, find the largest rectangle containing only 1s and return its area.
matrix = [
    ["1","0","1","1","1"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Output: 6
Hint: Build the height histogram row by row as we discussed. For each row treat heights as a histogram and find the largest rectangle in it.
"""

from typing import List


def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # flush stack

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop()
    return max_area


def maximal_rectangle(matrix):
    if not matrix:
        return 0

    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for c in range(cols):
            if row[c] == "1":
                heights[c] += 1
            else:
                heights[c] = 0

        max_area = max(max_area, largest_rectangle_area(heights))

    return max_area


# O(rows × cols)
matrix = [
    ["1", "0", "1", "1", "1"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]


print(maximal_rectangle(matrix))
