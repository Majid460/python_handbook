"""
Problem 3 — Medium
Submatrix Sum Equals K
Pattern: 2D prefix sum
Given a 2D matrix of integers and a target k, return the number of submatrices whose elements sum to k.
matrix = [
    [1,  -1],
    [-1,  1]
]
k = 0
Output: 4

matrix = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]
k = 0
Output: 4
Hint: Fix two rows, compress columns into 1D, then use hashmap to find subarrays summing to k — same as subarray sum equals k in 1D.
"""

from typing import List


def sum_of_sub_mat(mat, k):
    rows, cols = len(mat), len(mat[0])
    result = 0

    for r1 in range(rows):
        col_sum = [0] * cols

        for r2 in range(r1, rows):
            for c in range(cols):
                col_sum[c] += mat[r2][c]

            prefix_sum = 0
            count = {0: 1}

            for num in col_sum:
                prefix_sum += num
                result += count.get(prefix_sum - k, 0)
                count[prefix_sum] = count.get(prefix_sum, 0) + 1

    return result


matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
k = 0
print(sum_of_sub_mat(matrix, k))
