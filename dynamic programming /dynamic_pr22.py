class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp = {}
        max_length = 2
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if (i, diff) in dp:
                    dp[(j, diff)] = dp[(i, diff)] + 1
                else:
                    dp[(j, diff)] = 2
                max_length = max(max_length, dp[(j, diff)])
        return max_length

# test cases to validate the solution
sol = Solution()

print(sol.longestArithSeqLength([9,4,7,2,10])) 