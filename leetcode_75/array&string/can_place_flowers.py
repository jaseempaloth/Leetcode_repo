# 605. Can Place Flowers
# Topics: Array, Greedy

class Solution:
    def can_place_flower(self, flowerbed: list[int], n: int) -> bool:
        flower_arr = [0] + flowerbed + [0]
        for i in range(1, len(flower_arr)-1):
            if flower_arr[i - 1] == 0 and flower_arr[i] == 0 and flower_arr[ i + 1] == 0:
                flower_arr[i] = 1
                n -= 1
        return n <= 0
             
          




s = Solution()
flowerbed =  [1,0,0,0,1,0,0]
n = 3
print(s.can_place_flower(flowerbed, n))

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
