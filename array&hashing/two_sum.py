# 1. Two Sum
class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        prev_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [i, prev_map[diff]]
            prev_map[num] = i
        return -1

s = Solution()
nums = [2,7,11,15]
target = 9
print(s.two_sum(nums, target))



