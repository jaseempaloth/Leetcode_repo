class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        return [original[i*n:(i+1)*n] for i in range(m)]
            
            
                

s = Solution()
print(s.construct2DArray([1,2,3,4], 2, 2))