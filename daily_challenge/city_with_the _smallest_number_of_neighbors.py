# Find the City With the Smallest Number of Neighbors at a Threshold Distance
from collections import defaultdict
import heapq
class Solution:
    def find_the_city(self, n: int, edges: list[list[int]], distance_threshold: int) -> int:
        adj = defaultdict(list)
        for v1, v2, dist in edges:
            adj[v1].append((v2, dist))
            adj[v2].append((v1, dist))

        def dijkstra(src):
            heap = [(0, src)]
            visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei, dist2 in adj[node]:
                    nei_dist = dist + dist2
                    if nei_dist <= distance_threshold:
                        heapq.heappush(heap, (nei_dist, nei))
            return len(visit) - 1
        res, min_count = -1, float('inf')    
        for src in range(n):
            count = dijkstra(src)
            if count <= min_count:
                res, min_count = src, count
        return res
    
# test cases
s = Solution() 
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distance_threshold = 4
print(s.find_the_city(n, edges, distance_threshold)) 







        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dp = [[float('inf') for j in range(n)] for i in range(n)]
        
        # for i in range(n):
        #     dp[i][i] = 0
        
        # for u, v, w in edges:
        #     dp[u][v] = w
        #     dp[v][u] = w
        
        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
        # min_count = float('inf')
        # min_city = -1
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if dp[i][j] <= distance_threshold:
        #             count += 1
        #     if count <= min_count:
        #         min_count = count
        #         min_city = i
        
        # return min_city


