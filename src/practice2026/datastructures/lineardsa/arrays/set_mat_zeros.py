"""
Set Matrix Zeroes
Pattern: In-place flagging
Given an m×n matrix, if an element is 0, set its entire row and column to 0. Do it in place with O(1) extra space.
Input:
[[1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]]

Output:
[[1, 0, 1],
 [0, 0, 0],
 [1, 0, 1]]
Constraint: O(1) space — you cannot use a separate matrix or sets.
Hint: Use the first row and first column of the matrix itself as your flags.
"""


def set_mat_zeros(mat):
    rows, cols = len(mat), len(mat[0])
    col0 = 1

    # Step 1: mark
    for i in range(rows):
        if mat[i][0] == 0:
            col0 = 0
        for j in range(1, cols):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    # Step 2: fill (reverse)
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, 0, -1):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
        if col0 == 0:
            mat[i][0] = 0

    return mat


input = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(set_mat_zeros(input))
