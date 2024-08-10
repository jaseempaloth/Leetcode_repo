# 151. Reverse Words in a String
# Topics: Two Pointers, String 

from hmac import new


class Solution:
    def reverse_words(self, s: str) -> str:
        s = s.strip().split()
        s = s[::-1]
        #s = list(reversed(s.strip().split())) 
        return " ".join(s)



sl = Solution()
s = "  hello world  "

print(sl.reverse_words(s))