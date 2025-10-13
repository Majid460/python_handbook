class TwoDList:
    def __init__(self):
        self.arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def print_using_join(self):
        in_single_line = ' '.join(map(lambda row: ' '.join(map(str, row)), self.arr))
        print(f"Array is single line: {in_single_line} ")  # 1 2 3 4 5 6 7 8 9
        res = '\n'.join(map(lambda row: ' '.join(map(str, row)), self.arr))
        print(res)

    # Sum of each row and column
    def sum_of(self):
        # Each row
        res = list(map(sum, self.arr))
        print(f"rows sum: {res} ")
        # Each column
        # Columns are not directly iterable so we use zip(*matrix) to transpose the matrix

        transpose = zip(*self.arr)
        print([list(row) for row in transpose])
        col_sums = list(map(sum, zip(*self.arr)))
        print("Column sums:", col_sums)
        # columns sum: [12, 15, 18]
        # Without zip transpose
        rows_s = len(self.arr)
        col_s = len(self.arr[0])
        transposed_mat = [[0 for _ in range(rows_s)] for _ in range(col_s)]
        print(transposed_mat)

        for i in range(rows_s):
            for j in range(col_s):
                transposed_mat[j][i] = self.arr[i][j]
        print(f"Transposed: {transposed_mat} ")
        # To declare a empty 2d list
        _d = [[0] * col_s] * rows_s
        __d = [[0 for _ in range(col_s)] for _ in range(rows_s)]
        print(_d)
        print(__d)

        # Transpose with empty:
        trans = []
        for i in range(rows_s):
            row = []
            for j in range(col_s):
                row.append(self.arr[j][i])
            trans.append(row)
        print(trans)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

        # Print Main Diagonal (top-left → bottom-right)
        diag = [self.arr[i][i] for i in range(rows_s)]
        print(diag)  # [1, 5, 9]
        # Secondary Diagonal (top-right → bottom-left)
        # rows_s -> size of 2d array
        # rows_s-1 -> points to last index
        # rows_s-1-i -> decrement i index every time from last
        sec_diag = [self.arr[i][rows_s - 1 - i] for i in range(rows_s)]
        print(sec_diag)  # [3, 5, 7]

    # Maximum at each row
    def max_at_row(self):
        rows = len(self.arr)
        cols = len(self.arr[0])

        # Using map
        max_n = list(map(lambda row: max(row), self.arr))
        print(max_n)
        # sum of main diagonals
        sum_main_diag = sum(self.arr[i][i] for i in range(rows))
        print(sum_main_diag)
        # sum of secondary diagonals
        sum_sec_diag = sum(self.arr[i][rows - 1 - i] for i in range(rows))
        print(sum_sec_diag)

        # For rectangular matrix:
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]

        rows = len(matrix)
        cols = len(matrix[0])

        main_diag = [matrix[i][i] for i in range(min(rows, cols))]
        sec_diag = [matrix[i][cols - 1 - i] for i in range(min(rows, cols))]

        print("Main diagonal:", main_diag)  # [1, 6, 11]
        print("Secondary diagonal:", sec_diag)  # [4, 7, 10]

    # Searching and counting
    def search_counting(self, number: int = None):
        count_dict = {}
        for i, row in enumerate(self.arr):
            for j, num in enumerate(row):
                if num not in count_dict:
                    count_dict[num] = {"count": 1, "indexes": [(i, j)]}
                else:
                    count_dict[num]["count"] += 1
                    count_dict[num]["indexes"].append((i, j))
        print(count_dict)

        # Search a number from list
        if number:
            i = count_dict[number]["indexes"]
            if len(i) == 1:
                v,u = i[0]
                # Find number on that index
                number = self.arr[v][u]
                print(f"Number at {(v,u)} is {number}")




if __name__ == '__main__':
    print(f"\n -------- 2D List--------")
    two_d = TwoDList()
    two_d.print_using_join()
    print(f"\n -------- Sum of row and column--------")
    two_d.sum_of()
    print(f"\n -------- Max at Each row -------")
    two_d.max_at_row()
    print(f"\n -------- Search and Count -------")
    two_d.search_counting(5)

