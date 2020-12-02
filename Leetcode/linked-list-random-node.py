# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import random

# class Solution:
#     O(N)t
#     O(N)s
#     def __init__(self, head: ListNode):
#         """
#         @param head The linked list's head.
#         Note that the head is guaranteed to be not null, so it contains at least one node.
#         """

#         elements = []

#         while head:
#             elements.append(head.val)
#             head = head.next

#         n = len(elements)

#         self.elements = elements
#         self.n = n
#         self.r = lambda: elements[random.randint(0, n-1)]
#
#     O(1)t
#     O(1)s
#     def getRandom(self) -> int:
#         """
#         Returns a random node's value.
#         """
#         return self.r()
        

class Solution:
    # O(1)t
    # O(1)s
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    # O(N)t
    # O(1)s
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value
if __name__ == "__main__":
    input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution(input)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)
    r = s.getRandom()
    print(r)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()