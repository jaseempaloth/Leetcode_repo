# 242. Valid Anagram
# Hash table, string, sorting


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        s_count = [0] * 26
        t_count = [0] * 26

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            t_count[ord(t[i]) - ord('a')] += 1

        return s_count == t_count

sn = Solution()
s = "anagram"
t = "nagaram"
print(sn.is_anagram(s, t))