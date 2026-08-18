class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        positive_diagonals = set()  # r + c
        negative_diagonals = set()  # r - c

        def backtrack(row):
            # All queens are placed
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                # Check column and diagonals
                if col in cols:
                    continue

                if row + col in positive_diagonals:
                    continue

                if row - col in negative_diagonals:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)

                # Move to next row
                backtrack(row + 1)

                # Remove queen
                board[row][col] = "."
                cols.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)

        backtrack(0)

        return result