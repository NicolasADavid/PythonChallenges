'''
Reverse Linked List in Groups of K

Given a linked list and an integer k, reverse the list in groups of k.
 

EXAMPLE(S)
Input:
1→2→3→4→5→6
K=2

Output:
2→1→4→3→6→5
 

FUNCTION SIGNATURE
def reverseKGroup(head: ListNode, k: int) -> ListNode
'''


# Explore

    # Linked List
# 1→2→3→4→5→6
# K = 3
# 3→2→1→6→5→4


# 1→2→3→4→5→6-7-8
# K = 3
# 3→2→1→6→5→4 - 7 - 8
# 1→2→3→4→5→6-8-7

# Brainstorm

# 1→2→3→4→5→6
# 1, 2, 3. // 4, 5, 6

# 3→2→1→6→5→4

# Plan

# represent a segment: head node + K
# Helper function: L times, iterate K times, reversing list


# Iterative:

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

# # FUNCTION SIGNATURE
# def reverseKGroup(head: ListNode, k: int) -> ListNode:

#     # Reverse a segment of the linked list
#     # Reverse k times
#     def helper(nextSegmentHead):
#         c = 0
#         prev = None
#         curr = nextSegmentHead

#         while curr and c < k:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#             c += 1

#         return [prev, nextSegmentHead, curr]

#     dummy = ListNode(0)

#     prevSegmentEnd = None
#     while head:
#         # reverse a segment of the list
#         [segHead, segTail, nextSegHead] = helper(head)

#         if prevSegmentEnd:
#             prevSegmentEnd.next = segHead
#         else:
#             dummy.next = segHead

#         prevSegmentEnd = segTail
#         head = nextSegHead

#     return dummy.next

def reverseKGroup(head: ListNode, k: int) -> ListNode:

    # Reverse a segment of the linked list
    # Reverse k times
    def helper(nextSegmentHead):
        c = 0
        prev = None
        curr = nextSegmentHead

        while curr and c < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            c += 1

        return [prev, nextSegmentHead, curr]

    dummy = ListNode(0)
    prevSegmentEnd = None

    while head:
        # reverse a segment of the list
        [segHead, segTail, nextSegHead] = helper(head)

        if prevSegmentEnd:
            prevSegmentEnd.next = segHead
        else:
            dummy.next = segHead

        prevSegmentEnd = segTail
        head = nextSegHead

    return dummy.next


from typing import List
def makeLL(vals: List[int]) -> ListNode:

    x = None
    last = None

    for n in vals:
        node = ListNode(n)
        if last:
            last.next = node
        last = node
        if not x:
            x = ListNode(0, node)

    return x.next if x else None

def printL(n):
    c = 0
    while n:
        c += 1
        print(n.val)
        n = n.next
    print("____")
    print("Len: ", c)

# l1 = makeLL([1,2,3,4,5,6,7,8])
# # printL(l1)

# output = reverseKGroup(l1, 3)
# printL(output)

# Input: 
# 1→2→3→4→5
# K=3
# Output:
# 3→2→1→5→4
# l1 = makeLL([1,2,3,4,5])
# o1 = reverseKGroup(l1, 3)
# printL(o1)



# # Input: 
# # 1→2→3→4→5
# # K=5
# # Output:
# # 5→4→3→2→1
# l2 = makeLL([1,2,3,4,5])
# o2 = reverseKGroup(l2, 5)
# printL(o2)

# # Input: 
# # 1→2→3
# # K=5
# # Output:
# # 3→2→1
# l3 = makeLL([1,2,3])
# o3 = reverseKGroup(l3, 5)
# printL(o3)

# No next node
l4 = ListNode(1)
o4 = reverseKGroup(l4, 2)
printL(o4)


def recursivelyReverseKGroup(head, k: int) -> ListNode:
    curr = head
    prev = None

    for _ in range(k):
        if not curr:
            return prev
        next_head = curr.next
        curr.next = prev
        prev = curr
        curr = next_head

    next_segment_head = recursivelyReverseKGroup(curr, k)
    head.next = next_segment_head
    return prev


l3 = makeLL([1,2,3])
o3 = recursivelyReverseKGroup(l3, 5)
printL(o3)

