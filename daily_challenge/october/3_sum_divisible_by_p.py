# 1590. Make Sum Divisible by P
# Topics: array, hash table, prefix sum


class Solution:
    def min_subarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0
        
        result = len(nums)
        curr_sum = 0
        remain_hash = {0: -1}

        for i, n in enumerate(nums):
            curr_sum = (curr_sum + n) % p
            prefix = (curr_sum - remain + p) % p
            if prefix in remain_hash:
                length = i - remain_hash[prefix]
                result = min(result, length)
            remain_hash[curr_sum] = i
        
        return -1 if result == len(nums) else result

s = Solution()
nums = [6,3,5,2] 
p = 9
print(s.min_subarray(nums, p))
