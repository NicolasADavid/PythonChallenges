# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Advance fast n times
# Advance both fast and slow until hare reaches tail
# Slow points to node to be removed

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # Start out of bounds
        slow = fast = ListNode(None, head)

        # Move fast n spaces up the list
        for i in range(n):
            fast = fast.next

        # Move fast to tail of list
        while fast.next:
            slow = slow.next
            fast = fast.next

        # If slow is pointing to head, return head.next to remove it
        if slow.next == head:
            return head.next

        # slow is n spaces behind fast
        # node to remove is 1-indexed from tail
        slow.next = slow.next.next

        return head

    # Move to end of list, annotating every node with prev, move backwards n-1 times, remove
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

    #     if not head:
    #         return head

    #     curr = head
    #     prev = None
    #     curr.prev = None

    #     # Move curr to the end of the list
    #     while curr.next:
    #         prev = curr
    #         curr = curr.next
    #         # Add reference to previous node
    #         curr.prev = prev

    #     # curr is at the end of the list
    #     # n = 1 means remove the last node. So decrement n by 1 to start and move curr backwards until n = 0
    #     while n-1 > 0:
    #         curr = curr.prev
    #         n -= 1

    #     prev = None

    #     # curr is the target node
    #     if curr.prev:
    #         prev = curr.prev
    #         prev.next = curr.next

    #     if prev:
    #         return head
    #     else:
    #         return curr.next
