
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        last = head = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                last.next = ListNode(list1.val)
                list1 = list1.next
            else:
                last.next = ListNode(list2.val)
                list2 = list2.next
            last = last.next
        
        while list1:
            last.next = ListNode(list1.val)
            last = last.next
            list1 = list1.next
        while list2:
            last.next = ListNode(list2.val)
            last = last.next
            list2 = list2.next

        return head.next
    
s = Solution()
l1 = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 4, next = None)))
l2 = ListNode(val = 1, next = ListNode(val = 3, next = ListNode(val = 4, next = None)))
r1 = s.mergeTwoLists(l1, l2)

while r1:
    print(r1.val)
    r1 = r1.next