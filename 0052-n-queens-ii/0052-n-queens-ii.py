class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set()  # row + col
        negDiag = set()  # row - col

        count = 0

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                    continue

                # Place queen
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)

                backtrack(row + 1)

                # Remove queen
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)

        backtrack(0)
        return count