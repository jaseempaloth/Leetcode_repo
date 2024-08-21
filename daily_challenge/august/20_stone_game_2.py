# 1140. Stone Game II
# Topics: Array, Math, Dynamic Programming, Prefix Sum, Game Theory

import itertools


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n)]
        prefix_sum = [0] + list(itertools.accumulate(piles))
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                for x in range(1, 2 * m + 1):
                    if i + x > n:
                        break
                    dp[i][m] = max(dp[i][m], prefix_sum[n] - prefix_sum[i] - dp[i + x][max(m, x)])
        return dp[0][1]
        



       