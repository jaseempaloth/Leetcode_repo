# 885. Spiral Matrix III
# Topics: Array, Matrix, Simulation

from tables import Cols


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        result = []
        r, c = rStart, cStart
        steps = 1
        i = 0
        while len(result) < rows * cols:
            for _ in range(2):
                dr, dc = directions[i]
                for _ in range(steps):
                    if (0 <= r < rows and 0 <= c < cols):
                        result.append([r, c])
                    r, c = r + dr, c + dc
                i = (i + 1) % 4
            steps += 1                     
        return result

# test cases 
s = Solution()
rows = 5
cols = 6
rStart = 1
cStart = 4

print(s.spiralMatrixIII(rows, cols, rStart, cStart))
# [
#  [1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5],
#  [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2],
#  [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]
# ]