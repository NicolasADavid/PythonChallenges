# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return
        
        if root.val == key:
            root = self.replaceNode(root)

        else:
            root.left = self.deleteNode(root.left, key)
            root.right = self.deleteNode(root.right, key)

        return root

    def replaceNode(self, root):

        # Find node to put key node's left subtree under:
        # The smallest valued node in its right subtree.
        if root.right:
            smallestOnRight = root.right

            while smallestOnRight.left:
                smallestOnRight = smallestOnRight.left

            smallestOnRight.left = root.left

            return root.right
                
        # Have no right, but have left, use left.
        elif root.left:
            return root.left        
        
        return None

t1 = TreeNode(0, TreeNode(1), TreeNode(2))

if __name__ == "__main__":
    print(Solution().deleteNode(1221))