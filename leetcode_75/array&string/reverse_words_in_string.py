# 151. Reverse Words in a String
# Topics: 

class Solution:
    def reverse_words(self, s: str) -> str:
        s = s.strip().split()
        new_s = s[::-1]
        return " ".join(new_s)



sl = Solution()
s = "  hello world  "

print(sl.reverse_words(s))