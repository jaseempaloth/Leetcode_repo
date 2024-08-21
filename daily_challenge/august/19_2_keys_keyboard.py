# 650. 2 Keys Keyboard
# Topics: Math, Dynamic Programming


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        dp = [0] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + (i // j)
                    break
        return dp[n]
    
    def min_steps(self, n: int) -> int:

        cache = {}
        def helper(count, paste):
            if count == n:
                return 0
            if count > n:
                return 1000
            if (count, paste) in cache:
                return cache[count, paste]
            
            # paste
            result_1 = 1 + helper(count + paste, paste)
            # copy & paste
            result_2 = 2 + helper(count + count, count)
            cache[(count, paste)] = min(result_1, result_2)
            return cache[((count, paste))]
        if n == 1:
            return 0  
        return 1 + helper(1, 1)
            