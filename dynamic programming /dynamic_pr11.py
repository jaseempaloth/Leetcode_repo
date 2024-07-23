# Unique Paths II
from typing import List
class Solutuon:
    def unique_path_with_obstacles(self, obstacleGrid: List[list[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N - 1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]



            

            


        
