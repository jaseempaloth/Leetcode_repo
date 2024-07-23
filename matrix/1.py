# 1380. Lucky Numbers in a Matrix
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = [min(row) for row in matrix]
        max_col = [max(col) for col in zip(*matrix)]
        return [cell for row in matrix for cell in row if cell in min_row and cell in max_col]  