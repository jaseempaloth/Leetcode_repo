# 1431. Kids With the Greatest Number of Candies
# Topics: Array

from numpy import append


class Solution:
    def kids_with_candies(self, candies: list[int], extra_candies: int) -> list[bool]:
        max_candies = max(candies)
        result = [] 

        for candy in candies:
            result.append(candy + extra_candies >= max_candies)
        return result

        





s = Solution()

candies = [2,3,5,1,3]
extra_candies = 3
print(s.kids_with_candies(candies, extra_candies))


# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.