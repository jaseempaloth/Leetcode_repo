# Find the Minimum and Maximum Number of Nodes Between Critical Points
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode, List
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def criticalPoints(prev, cur, nxt):
            return (
                prev.val < cur.val > nxt.val or
                prev.val > cur.val < nxt.val
            )
        prev, cur = head, head.next
        nxt = cur.next
        min_dist, max_dist = float('inf'), -1
        prev_critical_idx = 0
        first_critical_idx = 0
        i = 1
        while nxt:
            if criticalPoints(prev, cur, nxt):
                if first_critical_idx:
                    max_dist = i - first_critical_idx
                    min_dist = min(
                        min_dist,
                        i - prev_critical_idx
                    )
                else:
                    first_critical_idx = i
                prev_critical_idx = i

            prev, cur, nxt = cur, nxt, nxt.next
            i += 1

        if min_dist == float('inf'):
            min_dist = -1
        return [min_dist, max_dist]



            
