# 2938. Separate Black and White Balls
# two pointers, string, greedy 

class Solution:
    def minimum_steps(self, s: str) -> int:
        swap, black = 0, 0
        for c in s:
            if c == '0':
                swap += black
            else:
                black += 1
        return swap
      
sn = Solution()
s = "100"
print(sn.minimum_steps(s))
