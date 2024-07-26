# Longest Arithmetic Subsequence of Given Difference

class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = {}
        max_length = 1
        # for a in arr:
        #     dp[a] = dp.get(a - difference, 0) + 1
        # return max(dp.values())

        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
            max_length = max(max_length, dp[num])
        return max_length
    
    

        