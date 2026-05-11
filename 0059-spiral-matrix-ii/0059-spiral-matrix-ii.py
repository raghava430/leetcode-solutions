class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while left <= right and top <= bottom:
            # move left to right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # move top to bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # move right to left
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

            # move bottom to top
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

        return matrix