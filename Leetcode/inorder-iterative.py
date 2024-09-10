# Definition for a binary tree node.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inorder:
# # Traverse left subtree
# # Visit root
# # Traverse right subtree

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            
        ans = []
        stack = []

        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                node = stack.pop()
                ans.append(node.val)
                curr = node.right
        
        return ans
        
