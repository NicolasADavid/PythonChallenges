import heapq
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def getDepth(n: Node, currDepth: int):
            if n.children:
                return currDepth + max([getDepth(c, 1) for c in n.children])
            else:
                return currDepth

        def process(n: Node):

            straight = 0
            bend = 0
            below = 0

            if not n.children:
                return 0
            elif len(n.children) == 1:
                straight = getDepth(n.children[0], 1)
            else:
                h = []
                for c in n.children:
                    heapq.heappush(h, -getDepth(c, 1))
                bend = -heapq.heappop(h) + -heapq.heappop(h)

            below = max([process(c) for c in n.children])

            return max([straight, bend, below])

        return process(root)

if __name__ == "__main__":
    root = Node(1, 
         [
            Node(3, [
                Node(5),
                Node(6)
            ]),
            Node(2),
            Node(4),
         ]
    )
    print(Solution().diameter(root))

    root = Node(3, [Node(1, [Node(5)])])
    print(Solution().diameter(root))