"""
A farmer wants to farm their land with the maximum area where good land is present.
The land is represented as a matrix with 1s and 0s, where 1s mean "good land" and 0s mean "bad land."
The farmer only wants to farm in a square of good land with the maximum area.
Please help the farmer to find the maximum area of the land they can farm in good land.

Example:
0 1 1 0 1
1 1 0 1 0
0 1 1 1 0
1 1 1 1 0
1 1 1 1 1
0 0 0 0 0

hint:
- I have to check every possible squares we can make and also count diagonals
"""


def square_max_area(dp_array: list[list[int]]) -> tuple[int,int]:
    n = len(dp_array)  # Num of rows
    m = len(dp_array[0])  # Col length
    dp = [[0] * m for _ in range(n)]
    max_size = -1
    for i in range(n):
        for j in range(m):
            if dp_array[i][j] == 0:
                continue
            if dp_array[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else :
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])+1  # take min of left, top, top-left (+1) counts the current cell
                    max_size = max(max_size,dp[i][j])
            print(dp_array[i][j], end=" ")
        print()
    return max_size,max_size * max_size


if __name__ == '__main__':
    l = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
    max_s = square_max_area(l)
    print(f"Max square can be:: {max_s}")
    # Max square can be:: (3, 9)
    # 3 represents max size of square
    # 9 represents max area

