# 1768. Merge Strings Alternately
# Topics: Two Pointers, String

class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        result.append(word1[i:])
        result.append(word2[2:])
        return "".join(result)

# test cases
s = Solution()
word1 = "abc"
word2 = "pqr"
print(s.merge_alternately(word1, word2))
# Output: "apbqcr"
