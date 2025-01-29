# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def longest_path(node: Optional[TreeNode]) -> int:

            if not node:
                return 0

            nonlocal diameter

            left = longest_path(node.left)
            right = longest_path(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)
        
        longest_path(root)
        return diameter