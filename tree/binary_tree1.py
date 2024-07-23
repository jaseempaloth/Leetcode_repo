# 2096. Step-By-Step Directions From a Binary Tree Node to Another
# String Tree Depth-First Search Binary Tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_direction(self, root: Optional[TreeNode], start_value: int, dest_value: int) -> str:
        def dfs(node, path, target):
            if not node:
                return ""
            if node.val == target:
                return path
            path.append("L")
            res = dfs(node.left, path, target)
            if res: return res

            path.pop()
            path.append("R")
            res = dfs(node.right, path, target)
            if res: return res

            path.pop()
            return ""
        start_path = dfs(root, [], start_value)
        destination_path = dfs(root, [], dest_value)
        i = 0
        while i < min(len(start_path), len(destination_path)):
            if start_path[i] != destination_path[i]:
                break
            i += 1

        res = ["U"] * len(start_path[i:]) + destination_path[i:]
        return "".join(res)

