# 283. Move Zeroes
# Arrays, Two Pointers


class Solution:
    def move_zeroes(self, nums: list[int]):
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums   

s = Solution()
nums = [0, 2, 0, 3, 12]
print(s.move_zeroes(nums))

for r in range(len(nums)):
    if nums[r]:
        print(f'nums[{r}] is non-zero', nums[r])
    else:
        print(f'nums[{r}] is zero', nums[r])