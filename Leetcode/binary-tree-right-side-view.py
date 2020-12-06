# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root: return None

        q = deque([])

        q.append(root)
        q.append(None)

        last = None

        ans = []

        while q:

            curr = q.popleft()

            if curr:
                last = curr
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

            else:

                ans.append(last.val)

                if q:
                    q.append(None)

        return ans


# class Solution:
#     # dfs
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []
        
#         rightside = []
        
#         def helper(node: TreeNode, level: int) -> None:
#             if level == len(rightside):
#                 rightside.append(node.val)
#             for child in [node.right, node.left]:
#                 if child:
#                     helper(child, level + 1)
                
#         helper(root, 0)
#         return rightside