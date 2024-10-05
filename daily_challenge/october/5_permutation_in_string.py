# 567. Permutation in String
# hash table, two pointers, sliding window, array

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[i]) - ord('a')] -= 1
            s2_count[ord(s2[i + len(s1)]) - ord('a')] += 1
        
        return s1_count == s2_count
        
    
s = Solution()
s1 = "ab" 
s2 = "eidbaooo"
print(s.check_inclusion(s1, s2))