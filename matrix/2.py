# 1605. Find Valid Matrix Given Row and Column Sums

class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
