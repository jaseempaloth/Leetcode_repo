# 2466. Count Ways To Build Good Strings
# Topics: Dynamic Programming

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (high + 1)  # dp[i] will hold the number of good strings of length i
        dp[0] = 1  # Base case: there's one way to make an empty string

        for length in range(1, high + 1):
            if length >= zero:
                dp[length] += dp[length - zero]  # Add a '0'
            if length >= one:
                dp[length] += dp[length - one]  # Add a '1'
            dp[length] %= mod

        # Sum up all good strings that have length between low and high
        res = 0
        for length in range(low, high + 1):
            res += dp[length]
            res %= mod

        return res