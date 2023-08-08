# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
from collections import Counter
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        q = []

        bookmark = tail = ListNode()

        # (headValue, tieBreaker, node)

        tb = 0
        
        for list in lists:
            if list:
                tb += 1
                heapq.heappush(q, (list.val, tb, list))

        while q:
           (val, _, node) = heapq.heappop(q)
           tail.next = ListNode(val)
           tail = tail.next
           node = node.next
           if node:
            tb += 1
            heapq.heappush(q, (node.val, tb, node))

        return bookmark.next

# l1 = ListNode(1, ListNode(4, ListNode(5)))
# l2 = ListNode(1, ListNode(3, ListNode(4)))
# l3 = ListNode(2, ListNode(6))

# Solution().mergeKLists(lists = [l1, l2, l3])
# Solution().mergeKLists(lists = [[]])
# Solution().mergeKLists(lists = [])