# minimum path sum
from typing import List
class Solution:
    def min_path_sum(self, grid: List[List[int]]) -> int:
        rows, column = len(grid), len(grid[0])

        res = [[float('inf')] * (column + 1) for r in range(rows + 1)]
        res[rows - 1][column] = 0

        for r in range(rows - 1, -1, -1):
            for c in range(column - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        return res[0][0]



