# 27. Remove Element
# Topics: Array, Two Pointers
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# test cases
s = Solution()
nums = [3, 2, 2, 3]
val = 3
print(s.removeElement(nums, val)) # 2
