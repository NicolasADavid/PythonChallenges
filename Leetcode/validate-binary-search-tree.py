# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Check if root.left.val < root.val < root.right.val
    def check(self, root: TreeNode) -> bool:
        val = root.val
        left = root.left.val if root.left else val - 1
        right = root.right.val if root.right else val + 1
        return left < val < right

    # As we go left, the largest value we can have gets smaller
    # As we go right, the smallest value we can have gets larger
    def go(self, root: TreeNode, min: int = None, max: int = None) -> bool:

        if not root: return True

        minCheck = min if min else root.val - 1
        maxCheck = max if max else root.val + 1
        if not (minCheck < root.val < maxCheck):
            return False
        
        check = self.check(root)

        left = self.go(root.left, min, root.val)

        right = self.go(root.right, root.val, max)

        return check and left and right

    # nothing in the left subtree can be less than min or larger than root.val
    # nothing in the right subtree can be less than root.val or greater than max
    def isValidBST(self, root: TreeNode) -> bool:

        return self.go(root)