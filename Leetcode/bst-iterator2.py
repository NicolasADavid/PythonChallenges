# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.nums = []
        self.idx = 0

        self.inorder(root)

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.nums.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        num = self.nums[self.idx]
        self.idx += 1
        return num

    def hasNext(self) -> bool:
        return self.idx < len(self.nums)
        

if __name__ == "__main__":

    root = TreeNode(7, 
        TreeNode(3), 
        TreeNode(15, 
            TreeNode(9),
            TreeNode(20)
        )
    )

    obj = BSTIterator(root)

    while obj.hasNext():
        print(obj.next())