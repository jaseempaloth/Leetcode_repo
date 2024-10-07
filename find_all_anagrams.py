# 438. Find All Anagrams in a String
# Topics: Hash Table, String, Sliding Window


class Solution:
    def find_anagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        count_idx = []
        s_count = [0] * 26
        p_count = [0] * 26 

        for i in range(len(p)):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1
        
        for i in range(len(s) - len(p)):
            if s_count == p_count:
                count_idx.append(i)
            s_count[ord(s[i]) - ord('a')] -= 1
            s_count[ord(s[i + len(p)]) - ord('a')] += 1
        if s_count == p_count:
            count_idx.append(len(s) - len(p))
        
        return count_idx
        


sl = Solution()
s = "cbaebabacd"
p = "abc"
# Output: [0,6]
print(sl.find_anagrams(s, p))

