# 354. Russian Doll Envelopes
# Topics: Array, Binary Search, Dynamic Programming, Sorting 
# Difficulty: Hard


class Solution:
    def max_envelopes(self, envelopes: list[list[int]]) -> int:
        
        
        
        
        
        
        
        
        
        
        
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # dp = []
        # for w, h in envelopes:
        #     l, r = 0, len(dp)
        #     while l < r:
        #         mid = (l + r) // 2
        #         if dp[mid][1] < h:
        #             l = mid + 1
        #         else:
        #             r = mid
        #     if r == len(dp):
        #         dp.append([w, h])
        #     else:
        #         dp[r] = [w, h]
        # return len(dp)
        