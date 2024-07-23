class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        # Initialize the dp array with zeros
        dp = [0] * (n + 1)
        # Base case
        dp[0] = 1
        dp[1] = 1

         # Fill the dp array using the recursive formula
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    # Time complexity: O(n)
    # Space complexity: O(n)

    def climbStairs1(self, n: int) -> int:
        ls, bls = 1, 1
        for i in range(n-2, -1, -1):
            cs = ls + bls
            ls = bls
            bls = cs
        return bls
            



# Test cases
s = Solution()
print(s.climbStairs(4)) # 2

#