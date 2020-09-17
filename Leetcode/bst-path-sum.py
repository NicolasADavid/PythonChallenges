# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #recursive
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     if not root:
    #         return False

    #     # check if sum is reached with this node's value
    #     # check if this is a leaf node
    #     if sum - root.val == 0 and not root.left and not root.right:
    #         return True

    #     # iterate on left and right subtree
    #     return (
    #         self.hasPathSum(root.left, sum - root.val) or 
    #         self.hasPathSum(root.right, sum - root.val)
    #         )

    #iterative
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False

        de = [(root, sum-root.val)]

        while de:
            node, curr_sum = de.pop()

            # check if sum is reached with this node's value
            # check if this is a leaf node
            if curr_sum == 0 and not node.left and not node.right:
                return True

            if node.left:
                de.append((node.left, curr_sum-node.left.val))
            if node.right:
                de.append((node.right, curr_sum-node.right.val))

        return False


if __name__ == "__main__":
    s = Solution()

    bst = TreeNode(1, TreeNode(2), TreeNode(3))

    r = s.hasPathSum(bst, 3)

    print(r)