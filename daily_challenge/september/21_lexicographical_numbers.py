# 386. Lexicographical Numbers
# Depth-First Search, Trie


class Solution:
    def lexical_order(self, n:int) -> list[int]:
        res = []
        cur = 1
        while len(res) < n:
            res.append(cur)

            if cur * 10 <= n:
                cur *= 10
            else:
                while cur == n or cur % 10 == 9:
                    cur = cur // 10
                cur += 1
        
        return res

s = Solution()
n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
print(s.lexical_order(n))














