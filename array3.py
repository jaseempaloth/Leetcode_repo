# Best Time to Buy and Sell Stock
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointers
        left, right = 0, 1
        max_profit = 0
        
        while right < len(prices):
            # profitable 
            if prices[right] > prices[left]:
               max_profit = max(max_profit ,prices[right] - prices[left])
            else:
                # not profitable
                left = right
            right += 1
        return max_profit
    # Time complexity: O(n)
    # Space complexity: O(1)

# Test cases
prices = [7,1,5,3,6,4]
s = Solution()

print(s.maxProfit(prices)) # 5