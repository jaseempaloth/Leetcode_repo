# 1395. Count Number of Teams
# Topics: Array, Dynamic Programming, Binary Indexed Tree, Segment Tree
class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        dp = [[0, 0] for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                if rating[i] > rating[j]:
                    dp[i][0] += 1
                    res += dp[j][0]
                else:
                    dp[i][1] += 1
                    res += dp[j][1]
        return res
    
rating = [2,5,3,4,1]
sol = Solution()
print(sol.numTeams(rating)) # 3