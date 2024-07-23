# Find the Winner of the Circular Game
from collections import deque


class Solution:
    def find_the_winner(self, n: int, k: int) -> int:
        cir = deque()

        for i in range(1, n+1):
            cir.append(i)

        while len(cir) > 1:
            # cir.rotate(-k)
            # cir.pop()
            for i in range(k - 1):
                cir.append(cir.popleft())
            cir.popleft()

        return cir[0]




