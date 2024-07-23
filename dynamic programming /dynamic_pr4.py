# N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]

        if n < 3:
            return arr[n]
        
        for i in range(3, n + 1):
            arr[0], arr[1], arr[2] = arr[1], arr[2], sum(arr)
        return arr[2]
    


        