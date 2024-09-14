# Count the Number of Consistent Strings
# Topics: Array, Hash, Table, String, Bit, Manipulation, Counting

class Solution:
    def count_consistent_strings(self, allowed: str, words: list[int]) -> int:
        allowed = set(allowed)
        count = len(words)
        for word in words:
            for char in word:
                if char not in allowed:
                    count -= 1
                    break      
        return count 

s = Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(s.count_consistent_strings(allowed, words))