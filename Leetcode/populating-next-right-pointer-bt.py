class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:

        
    # def connect(self, root: 'Node') -> 'Node':

    #     if not root: return None

    #     def leftMostChild(node: 'Node') -> 'Node':
    #         if not node: return None
    #         if node.left: return node.left
    #         if node.right: return node.right
    #         return None

    #     def rightMostChild(node: 'Node') -> 'Node':
    #         if not node: return None
    #         if node.right: return node.right
    #         if node.left: return node.left
    #         return None

    #     def findFirstLeft(node: 'Node') -> 'Node':
    #         lm = leftMostChild(node)

    #         if lm:
    #             return lm
    #         elif node.next:
    #             return findFirstLeft(node.next)
    #         else:
    #             return None

    #     # If left and right, left.next = right
    #     if root.left and root.right:
    #         root.left.next = root.right

    #     if root.next:

    #         # Find rightmost of root
    #         rm = rightMostChild(root)

    #         # Find leftmost child of a node at root's level
    #         lm = findFirstLeft(root.next)

    #         if rm and lm:
    #             rm.next = lm

    #     self.connect(root.right)
    #     self.connect(root.left)

    #     return root

    
    def connectChild(self, child, prev, leftMost):

        if child:
            if prev:
                prev.next = child
            else:
                leftMost = child
            prev = child

        return prev, leftMost

    def connect(self, root: 'Node') -> 'Node':

        if not root: return None

        leftMost = root

        while leftMost:

            prev, curr = None, leftMost
            leftMost = None

            while curr:

                prev, leftMost = self.connectChild(curr.left, prev, leftMost)
                prev, leftMost = self.connectChild(curr.right, prev, leftMost)

                curr = curr.next
        
        return root
