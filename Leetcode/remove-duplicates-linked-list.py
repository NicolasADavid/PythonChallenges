# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        last = None
        n = head

        while n and n.next:

            if n.val == n.next.val:

                end = n.next

                while end and end.next and end.val == end.next.val:
                    end = end.next
                
                if last:
                    last.next = end.next
                else:
                    head = end.next

                n = end.next

            else:
                last = n
                n = n.next


        return head
            
        