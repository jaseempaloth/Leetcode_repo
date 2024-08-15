# 719. Find K-th Smallest Pair Distance
# Topics: Array, Two Pointers, Binary Search, sorting
class Solution:    
    def smallest_distance_pair(self, nums: list[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            count = self.count_pairs(nums, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low
    
    def count_pairs(self, nums, mid):
        count = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left
        return count