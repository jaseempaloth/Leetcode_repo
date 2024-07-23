from typing import List
class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])
        return dp[0]

triangle = [[2],[3,4],[6,5,7],[4,2,8,3]]
s = Solution()
print(s.minimum_total(triangle))

                
        