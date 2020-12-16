# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        # Track where a val can be increased by 1 without requiring a carry
        carryNode = None

        def carry(node: ListNode):
            node.val += 1
            node = node.next
            while node:
                node.val = 0
                node = node.next

        # Find end of the list, where 1 will be added
        last = head
        while last.next:
            if last.val < 9:
                carryNode = last
            last = last.next

        if last.val == 9:
            # Have to carry
            if carryNode:
                carry(carryNode)
            else:
            # If carryNode not found, create new head
            # Carry from the head
                tmp = ListNode(0, head)
                head = tmp
                carry(head)
        else:
            last.val = last.val + 1

        return head

        