# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # number of nodes is between 0 and 10^4
    # goal is O(1) memory. Can't add things for each node.
    # slow and fast
    # move slow 1 and move fast 2
    # worst case cycle is 10000 nodes where last node points to first node
    # fast would reach slow after slow traveled 10000 and fast traveled 20000
    # iterate at least 10000 times
    # if fast reaches tail, false
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False

        slow = ListNode(None)
        slow.next = fast = head

        while fast.next:

            slow = slow.next

            for j in range(2):

                if not fast.next:
                    return False

                fast = fast.next

                if fast == slow:
                    return fast

        return False
        