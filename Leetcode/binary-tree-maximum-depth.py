# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        q = deque()
        q.append(root)
        q.append("level")

        if not root: return 0

        level = 1

        while q:

            e = q.popleft()

            if e == "level":
                if q:
                    level += 1
                    q.append("level")
            else:
                if e.left: q.append(e.left)
                if e.right: q.append(e.right)
        
        return level


# class Solution:
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """ 
#         stack = []
#         if root is not None:
#             stack.append((1, root))
        
#         depth = 0
#         while stack != []:
#             current_depth, root = stack.pop()
#             if root is not None:
#                 depth = max(depth, current_depth)
#                 stack.append((current_depth + 1, root.left))
#                 stack.append((current_depth + 1, root.right))
        
#         return depth

if __name__ == "__main__":
    s = Solution()
    s.maxDepth(TreeNode(0,TreeNode(0, None, None), TreeNode(0, None, None)))