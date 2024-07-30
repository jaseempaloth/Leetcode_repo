# 1653. Minimum Deletions to Make String Balanced
# Topics: String, Dynamic Programming, Stack

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_right = [0] * len(s)
        for i in range(len(s) -2, -1, -1):
            a_count_right[i] = a_count_right[i + 1]
            a_count_right[i] += 1 if s[i + 1] == 'a' else 0
        
        b_count_left = 0
        result = len(s)
        for i, c in enumerate(s):
            result = min(result, b_count_left + a_count_right[i])
            if c == 'b':
                b_count_left += 1
        return result
             
        






        # a = 0
        # b = 0
        # for i in s:
        #     if i == 'a':
        #         a += 1
        #     else:
        #         b = max(a, b) + 1
        # return len(s) - max(a, b)