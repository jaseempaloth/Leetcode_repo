from typing import Optional
# 2196. Create Binary Tree From Descriptions
# Array, Hash Table, Tree, Binary Tree
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def create_binary_tree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for parent, child, is_left in descriptions:
            children.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for p, c, l in descriptions:
            if p not in children:
                return nodes[p]


