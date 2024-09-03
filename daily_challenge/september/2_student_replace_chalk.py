# 1894. Find the Student that Will Replace the Chalk
# Topics: Array ,Binary, Search ,Simulation, Prefix Sum

class Solution:
    def clalk_replacer(self, chalk: list[int], k: int) -> int:
        k %= sum(chalk)

        for i, chalk_use in enumerate(chalk):
            if k <= chalk_use:
                return i
            k -= chalk_use
        return 0

s = Solution()
chalk = [3,4,1,2]
k = 25
print(s.clalk_replacer(chalk, k))