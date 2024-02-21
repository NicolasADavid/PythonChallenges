# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        prev = None

        while(head.next):
            next = head.next
            head.next = prev
            prev = head
            head = next

        head.next = prev
        
        return head


        
        