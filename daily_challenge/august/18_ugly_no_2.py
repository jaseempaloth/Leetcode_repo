# 264. Ugly Number II
# Topics: Hash Table, Math, Dynamic Programming, Heap (Priority Queue)

import heapq


class Solution:
    def nth_ugly_number(self, n: int) -> int:
        min_heap = [1]
        visit = set()
        factors = [2, 3, 5]
        for i in range(n):
            num = heapq.heappop(min_heap)

            if i == n - 1:
                return num
            
            for f in factors:
                if num * f not in visit:
                    visit.add(num * f)
                    heapq.heappush(min_heap, num * f)
                    