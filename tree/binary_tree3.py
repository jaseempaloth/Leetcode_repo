# 1530. Number of Good Leaf Nodes Pairs
# Definition for a binary tree node.
from collections import defaultdict, deque

from sympy.abc import q


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.pairs = None

    def count_pairs(self, root: TreeNode, distance: int) -> int:
        adj = defaultdict(list)
        leaf_set = set()

        def build_graph(node):
            if not node:
                return
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
            if not node.left and not node.right:
                leaf_set.add(node)
            build_graph(node.left)
            build_graph(node.right)

        def bfs(node):
            visit = set([node])
            q = deque([(node, 0)])

            while q:
                cur, dist = q.popleft()
    
                if cur != node and cur in leaf_set and dist <= distance:
                    self.pairs += 1
    
                for neighbor in adj[cur]:
                    if neighbor not in visit and dist + 1 <= distance:
                        q.append((neighbor, dist + 1))
                        visit.add(neighbor)

        build_graph(root)
        self.pairs = 0
        for node in leaf_set:
            bfs(node)
        return self.pairs // 2





