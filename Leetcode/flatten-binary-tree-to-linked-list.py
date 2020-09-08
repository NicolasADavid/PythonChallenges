# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def flatten(self, root: TreeNode) -> None:

        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        head = root.left

        while head and head.right:
            head = head.right

        if head:
            head.right = root.right
            root.right = root.left
            root.left = None