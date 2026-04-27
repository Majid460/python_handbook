"""
Problem 2 — Medium
Rotate Image 90° Clockwise
Pattern: In-place matrix manipulation
You are given an n×n 2D matrix. Rotate it 90° clockwise in place — you cannot use another matrix.
Input:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Output:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Hint: Two steps — transpose first, then reverse each row.

"""

from typing import List


def rotate_mat(mat: List[List[int]]):
    n = len(mat)

    # Step 1 — Transpose (swap upper triangle with lower)
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Step 2 — Reverse each row
    for row in mat:
        row.reverse()


input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_mat(input)
