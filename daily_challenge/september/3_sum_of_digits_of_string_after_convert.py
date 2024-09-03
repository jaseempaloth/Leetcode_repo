class Solution:
    def get_lucky(self, s: str, k: int) -> int:
        result = []
        s = s.lower()
        for char in s:
            index = ord(char) - ord('a') + 1
            result.append(str(index))
              
        num_str = ''.join(result)
        for _ in range(k):
            total = 0
            for digit in num_str:
                total += int(digit)
            num_str = str(total)
        return int(num_str)
            

sln = Solution()
s = "leetcode"
k = 2
print(sln.get_lucky(s, k)) # 6
