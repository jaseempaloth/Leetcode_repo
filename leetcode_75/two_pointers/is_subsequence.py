# 392. Is Subsequence
# Topics : Two Pointers, String, Dynamic Programming

class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i = 0 # pointer for s
        j = 0 # pointer for t

        if not s:
            return True
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

sl = Solution()
s = "abc"
t = "ahbgdc"
print(sl.is_subsequence(s, t))
