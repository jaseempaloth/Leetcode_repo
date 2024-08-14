# 959. Regions Cut By Slashes
# Topics: Array, Hash Table, Depth First Search, Breadth First Search, Union Find, Matrix

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        m = 3 * n
        new_grid = [[0] * m for _ in range(m)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    new_grid[i * 3][j * 3 + 2] = 1
                    new_grid[i * 3 + 1][j * 3 + 1] = 1
                    new_grid[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    new_grid[i * 3][j * 3] = 1
                    new_grid[i * 3 + 1][j * 3 + 1] = 1
                    new_grid[i * 3 + 2][j * 3 + 2] = 1
        count = 0
        for i in range(m):
            for j in range(m):
                if new_grid[i][j] == 0:
                    self.dfs(new_grid, i, j)
                    count += 1
        return count
        
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] == 1:
            return
        grid[i][j] = 1
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)