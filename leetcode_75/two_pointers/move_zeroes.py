# 283. Move Zeroes
# Arrays, Two Pointers


class Solution:
    def move_zeroes(self, nums: list[int]):
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[right] == 0:
                right -= 1
            else:
                left += 1    

s = Solution()
nums = [0, 2, 0, 3, 12]
print(s.move_zeroes(nums))