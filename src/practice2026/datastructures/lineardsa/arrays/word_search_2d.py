"""
Problem 1 — Medium
Word Search
Pattern: DFS + Backtracking on 2D grid
Given a 2D board of characters and a string word, return True if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells — horizontally or vertically adjacent. The same cell cannot be used more than once.
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCCED"  → True
word = "SEE"     → True
word = "ABCB"    → False  # can't reuse B
Hint: At each cell try all 4 directions. Mark cell as visited before going deeper, unmark when backtracking.
"""

from typing import List


def search_word(mat: List[List[str]], word: str) -> bool:
    rows = len(mat)
    cols = len(mat[0])
    seen = set()
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(i, j, k):
        if k == len(word):
            return True
        # out of bounds OR mismatch OR already used
        if (
            i < 0
            or i >= rows
            or j < 0
            or j >= cols
            or (i, j) in seen
            or mat[i][j] != word[k]
        ):
            return False
        seen.add((i, j))  # mark seen
        for dr, dc in dirs:
            if dfs(i + dr, j + dc, k + 1):
                return True

        # backtrack
        seen.remove((i, j))

        return False

    # try starting from every cell
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False


# Opt approach with inplace mark as visited:

# def dfs(i, j, k):
#     if k == len(word):
#         return True
#     if (
#         i < 0 or i >= rows
#         or j < 0 or j >= cols
#         or mat[i][j] != word[k]   # '#' won't match any letter
#     ):
#         return False

#     temp = mat[i][j]
#     mat[i][j] = '#'           # mark visited in place

#     for dr, dc in dirs:
#         if dfs(i + dr, j + dc, k + 1):
#             mat[i][j] = temp  # restore before returning
#             return True

#     mat[i][j] = temp          # restore on backtrack
#     return False


"""
Trade-off:
seen            set.              In-place #
Space           O(n×m)extra       O(1)extra
Modifiesinput   No.               Yes
Interview       preferenceSafe.   Slightly more impressive
"""
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(search_word(board, word))
