from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sentence in sentences:
            words_count = len(sentence.split())
            if words_count > max_words:
                max_words = words_count
        return max_words
    
    def mostWordsFound1(self, sentences: List[str]) -> int:
        return max([len(sentence.split()) for sentence in sentences])
    
    def mostWordsFound2(self, sentences: List[str]) -> int:
        return max(map(lambda sentence: len(sentence.split()), sentences))
    
    def mostWordsFound3(self, sentences: List[str]) -> int:
        return max(map(len, map(str.split, sentences)))
    
    def mostWordsFound4(self, sentences: List[str]) -> int:
        max_words = 0
        for sentence in sentences:
            words_count = sentence.count(" ") + 1
            if words_count > max_words:
                max_words = words_count
        return max_words

# Time complexity: O(n) where n is the number of sentences
# Space complexity: O(1)

# Test cases
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
solution = Solution()
print(solution.mostWordsFound(sentences))

# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6