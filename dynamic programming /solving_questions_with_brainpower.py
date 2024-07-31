# 2140. Solving Questions With Brainpower
# Topics: Array, Dynamic Programming
# zero-one knapsack dynamic programming
class Solution:
    def most_points(self, questions: list[list[int]]) -> int:
        dp = {}
        for i in range(len(questions) - 1, -1, -1):
            dp[i] = max(
                questions[i][0] + dp.get(i + 1 + questions[i][1], 0),
                dp.get(i + 1, 0)
            )
        return dp[0]


