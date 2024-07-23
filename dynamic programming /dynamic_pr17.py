# 712. Minimum ASCII Delete Sum for Two Strings

class Solution:
    def minimum_delete_sum(self, s1: str, s2: str) -> int:
        cache = {}

        def helper(i, j):
            if i >= len(s1):
                return sum([ord(x) for x in s2[j:]])
            if j >= len(s2):
                return sum([ord(x) for x in s1[i:]])
            if (i, j) not in cache:
                if s1[i] == s2[j]:
                    cache[(i, j)] = helper(i + 1, j + 1)
                else:
                    cache[(i, j)] = min(helper(i + 1, j) + ord(s1[i]), helper(i, j + 1) + ord(s2[j]))
            return cache[(i, j)]

        return helper(0, 0)
