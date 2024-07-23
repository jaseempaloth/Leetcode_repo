# Longest palindromic substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0

        for i in range(len(s)):
            # Odd length palindrome
            len1 = self.expand_around_center(s, i, i)
            # Even length palindrome
            len2 = self.expand_around_center(s, i, i + 1)

            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]



    def expand_around_center(self, s: str, left: int, right: int) -> int:
        # Expand outwards while the characters match and are within bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1
    
# Time complexity: O(n^2)
# Space complexity: O(1)

# Test cases

s = Solution()
print(s.longestPalindrome("babad")) # "bab"       
