# Unique Paths
class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1, ):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
        return row[0]

# Test Cases


solution = Solution()
# Example 1
m = 3
n = 7
# Output: 28
print(solution.unique_paths(m, n))



