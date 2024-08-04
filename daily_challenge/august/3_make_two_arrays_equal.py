# 1460. Make Two Arrays Equal by Reversing Subarrays
# Topics: Array, Hash Table, Sorting

from collections import defaultdict


class Solution:
    def can_be_equal(self, target: list[int], arr: list[int]) -> bool:
        count_1, count_2 = defaultdict(int), defaultdict(int)
        for n1, n2 in zip(target, arr):
            count_1[n1] += 1
            count_2[n2] += 1

        if len(count_1) != len(count_2):
            return False
        for n in count_1:
            if count_1[n] != count_2[n]:
                return False
        return True

# test cases  



s = Solution()
target = [3, 2, 1, 4, 7]
arr = [2, 7, 4, 1, 3]
print(s.can_be_equal(target, arr))