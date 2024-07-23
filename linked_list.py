# Merge Nodes in Between Zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current.next:
            node = current.next
            current = current.next
            while current.next.val != 0:
                node.val += current.next.val
                current = current.next

            current = current.next
            node.next = current.next
        return head.next






