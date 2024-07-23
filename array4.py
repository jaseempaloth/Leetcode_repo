# contains Duplicate
# topic array, hash table, sorting
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
            else:
                return True
        return False
    
s = Solution()
nums = [1,2,3,1]
print(s.containsDuplicate(nums)) # True


