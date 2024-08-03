# 1105. Filling Bookcase Shelves
# Topics: Array, Dynamic Programming, Memoization


class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        dp = [0] * (len(books) + 1)
        for i in range(len(books) - 1, -1, -1):
            current_width = shelfWidth
            max_height = 0
            dp[i] = float('inf')
            for j in range(i, len(books)):
                width, height = books[j]
                if current_width < width:
                    break
                current_width -= width
                max_height = max(max_height, height)
                dp[i] = min(
                    dp[i],
                    max_height + dp[j + 1]
                )
        return dp[0]


# test cases to validate the solution
s = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
print(s.minHeightShelves(books, shelfWidth)) # 6
# ex        
        
        # n = len(books)
        # dp = [float('inf')] * (n + 1)
        # dp[0] = 0
        # for i in range(1, n + 1):
        #     width = 0
        #     height = 0
        #     for j in range(i - 1, -1, -1):
        #         width += books[j][0]
        #         if width > shelfWidth:
        #             break
        #         height = max(height, books[j][1])
        #         dp[i] = min(dp[i], dp[j] + height)
        # return dp[n]
        