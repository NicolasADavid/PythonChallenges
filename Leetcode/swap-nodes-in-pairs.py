# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Input: head = [1,2,3,4]
    # Output: [2,1,4,3]
    # Iterative
    def swapPairs(self, head: ListNode) -> ListNode:
        # b points to head, b.next will be changed if head is swapped. Return b.next.
        # p points to node that points to the node being processed (head)
        b = ListNode(None, head)
        p = b

        while head:

            if head.next:                
                p.next = head.next
                t = head.next.next
                head.next.next = head
                head.next = t

            p = head
            head = head.next

        return b.next

    # # Recursive
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     return self.swap(head)

    # """
    # Swap node and node.next
    # Call swap on node.next.next
    # Return node.next for pointing to from prev node (known to caller)
    # """
    # def swap(self, node: ListNode) -> ListNode:

    #     if not node or not node.next: return node

    #     # New head to return
    #     nh = node.next

    #     # Remaining list to recurse on
    #     t = node.next.next

    #     # Swap second node.next
    #     node.next.next = node

    #     # Swap first node.next
    #     node.next = self.swap(t)

    #     return nh

# LC Solution
# class Solution():
#     def swapPairs(self, head: ListNode) -> ListNode:
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """

#         # If the list has no node or has only one node left.
#         if not head or not head.next:
#             return head

#         # Nodes to be swapped
#         first_node = head
#         second_node = head.next

#         # Swapping
#         first_node.next  = self.swapPairs(second_node.next)
#         second_node.next = first_node

#         # Now the head is the second node
#         return second_node