# 1331. Rank Transform of an Array
# Topics: array, hash table, sorting

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr = sorted(set(arr))
        print(sorted_arr)
        rank = {}
        for i in range(len(sorted_arr)):
            if sorted_arr[i] not in rank:
                rank[sorted_arr[i]] = i + 1
        
        print(rank)
        return [rank[x] for x in arr]
        

s = Solution()
arr = [37,12,28,9,100,56,80,5,12]
print(s.arrayRankTransform(arr))
