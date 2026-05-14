from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue

                top = grid[r - 1][c] if r > 0 else float("inf")
                left = grid[r][c - 1] if c > 0 else float("inf")

                grid[r][c] += min(top, left)

        return grid[rows - 1][cols - 1]