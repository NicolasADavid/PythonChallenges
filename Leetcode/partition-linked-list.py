from typing import List
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x = None, next = None):
    self.value = x
    self.next = next

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
        print('{',n.value,'}')
        n = n.next
    print("____")
    print("Len: ", c)


def solution(head, k):

    # For returning
    dummy = ListNode()
    dummy.next = head

    # For constructing new list with elements >= k
    newDummy = ListNode()
    newLast = newDummy

    # For traversing/operating on the list
    curr = head
    prev = dummy

    while curr:

        next = curr.next

        
        if curr.value >= k:

            # remove from list
            prev.next = next

            # add to new list
            newLast.next = curr
            newLast = curr
            curr.next = None
        else:
            prev = curr
       
        curr = next

    # join lists
    if prev:
        prev.next = newDummy.next
    
    return dummy.next

# l1 = makeLL([1,2])
# o1 = solution(l1, 2)
# printL(o1)
# l1 = makeLL([1])
# o1 = solution(l1, 2)
# printL(o1)
l1 = makeLL([2])
o1 = solution(l1, 2)
printL(o1)


# l1 = makeLL([1,2,3,4,5])
# o1 = solution(l1, 2)
# printL(o1)

# l2 = makeLL([3,3,3,1,1,1,1,2])
# o2 = solution(l2, 2)
# printL(o2)