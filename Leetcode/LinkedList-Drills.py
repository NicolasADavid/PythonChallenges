from typing import List

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

# Given a target k, create a linked list with values starting at 0 and incrementing by 1 until k.
def createLLUpToK(k):

    if k == 0:
        return ListNode(0)
    
    ans = ListNode()
    last = ans

    for i in range(k+1):
        n = ListNode(i)
        last.next = n
        last = n

    return ans.next

# Given a linked list and a sorted array of indices, return the sum of nodes at the indices.
def sumLinkedListNodesAtIndices(head: ListNode, indices: List[int]) -> int:

    if not indices:
        return 0
    
    indicesIdx = 0
    listIdx = 0
    sum = 0

    while head:
        if listIdx == indices[indicesIdx]:
            sum += head.val
            indicesIdx += 1
            if indicesIdx == len(indices):
                break

        head = head.next
        listIdx += 1

    return sum

# Given a linked list and a value k, return the number of nodes that have the value k.
def countLLNodesValueK(head: ListNode, k: int) -> int:
    count = 0
    while head:
        if head.val == k:
            count +=1
        head = head.next

    return count

# Given a linked list, return true if all its values are unique and false otherwise.
def isLLAllUnique(head: ListNode) -> bool:
    seen = set()

    while head:
        if head.val in seen:
            return False
        seen.add(head.val)
        head = head.next
    
    return True

# Given a linked list, insert a node with the value 0 after each existing node. This should double the length of the original list and every other value should be 0.
def insertZerosInLL(head: ListNode) -> ListNode:

    insert = True
    x = ListNode(0, head)

    while head:
        # insert a zero node
        # advance twice

        zNode = ListNode(0, head.next)
        head.next = zNode
        head = zNode.next

    return x.next

# Given a linked list, a target and a replacement, replace all nodes with the target value with the replacement value.
def replaceNodeValuesLL(head: ListNode, target: int, replacement: int) -> ListNode:

    x = ListNode(0, head)

    while head:
        if head.val == target:
            head.val = replacement
        head = head.next

    return x.next

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

# printL(createLLUpToK(0))
# printL(createLLUpToK(1))
# printL(createLLUpToK(3))

# l1 = ListNode(5,
# ListNode(6,
# ListNode(7,
# ListNode(8,
# ListNode(9,)))))

# print(sumLinkedListNodesAtIndices(l1, [0, 2, 4])) #  returns 21 (5 + 7 + 9)

# l1 = ListNode(1,
# ListNode( 2,
# ListNode( 3,
# ListNode( 1,
# ListNode(1)))))
# print(countLLNodesValueK(l1, 1))

# l1 = ListNode(1,
# ListNode(3,
# ListNode(2))) #returns true

# l2 = ListNode(1,
# ListNode(6,
# ListNode(7,
# ListNode(1,
# ListNode(9))))) #returns false

# #True
# print(isLLAllUnique(l1))
# #False
# print(isLLAllUnique(l2))

# l1 = createLLUpToK(10)
# printL(l1)
# printL(insertZerosInLL(l1))

# l1 = makeLL([1,2,3,1,5])
# printL(replaceNodeValuesLL(l1, 1, 7))