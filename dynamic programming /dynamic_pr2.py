# Fibonacci Number
class Solution:
    hash_map = {0: 0, 1: 1}
    def fib(self, n: int) -> int:
        # dynamic programming
        
        if n in self.hash_map:
            return self.hash_map[n]
        self.hash_map[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.hash_map[n]
    
    
    
    def fib1(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        
        a, b = 0, 1

        for i in range(n-1):
            c = a + b
            a = b
            b = c
        return c
    

import datetime
start = datetime.datetime.now()
s = Solution()
print(s.fib(10)) # 3
#print(s.fib1(1000)) # 3
print(datetime.datetime.now() - start)