# 1568. Minimum Number of Days to Disconnect Island
# Topics: array, depth first search, breadth first search, matrix, strong connected components : hard

class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if self.count_islands(grid) != 1:
            return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self.count_islands(grid) != 1:
                        return 1
                    grid[i][j] = 1
        return 2

    def count_islands(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.dfs(grid, visited, i, j)
                    count += 1
        return count

    def dfs(self, grid, visited, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True
        self.dfs(grid, visited, i + 1, j)
        self.dfs(grid, visited, i - 1, j)
        self.dfs(grid, visited, i, j + 1)
        self.dfs(grid, visited, i, j - 1)