# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Return minimum node
    # Points next smallest node.right to root
    # Points root.right next largest node
    # Points root.left to None 
    def increasingBST(self, root: TreeNode) -> TreeNode:

        if root is None: return None

        minNode = None
        prevNode = None
        nextNode = None

        # Find prevNode
        if root.left:
            prevNode = root.left
            while prevNode.right:
                prevNode = prevNode.right
        
        # Find minNode + process left
        minNode = self.increasingBST(root.left)

        # find nextNode +  process right
        nextNode = self.increasingBST(root.right)

        # If prevNode exists, make prevNode.next = self
        if prevNode:
            prevNode.right = root

        root.right = nextNode
        root.left = None

        return minNode if minNode else root

if __name__ == "__main__":
    r = TreeNode(
        5,
        TreeNode(
            3,
            TreeNode(
                2,
                TreeNode(
                    1,
                    None,
                    None
                ),
                None
            ),
            TreeNode(
                4,
                None,
                None
            )
        ),
        TreeNode(
            6,
            None,
            TreeNode(
                8,
                TreeNode(
                    7,
                    None,
                    None
                ),
                TreeNode(
                    9,
                    None,
                    None
                )
            )
        )
    )

    s = Solution()

    n = s.increasingBST(r)

    while(n):
        print(n.val)
        n = n.right