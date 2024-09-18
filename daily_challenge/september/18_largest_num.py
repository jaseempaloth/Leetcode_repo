# 179. Largest Number
# Topics: Array, String, Greedy, Sorting

from functools import cmp_to_key

class Solution:
    def largest_number(self, nums: list[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int(''.join(nums)))


s = Solution()
nums = [9,30,34,5,3]
print(s.largest_number(nums))