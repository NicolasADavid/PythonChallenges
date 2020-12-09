# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def inorderTraversalList(self, root: TreeNode) -> TreeNode:

        # self.ops += 1
        # print("ops: " + str(self.ops))

        if not root: return None

        # Prepare to process self

        # find minNode
        minNode = root.left
        while minNode and minNode.left:
            minNode = minNode.left

        # find prevNode
        prevNode = root.left
        while prevNode and prevNode.right:
            prevNode = prevNode.right

        # Process left
        minNode = self.inorderTraversalList(root.left)

        # Process right
        nextNode = self.inorderTraversalList(root.right)

        # Process self
        if prevNode:
            prevNode.right = root
        if nextNode:
            root.right = nextNode

        # Return minNode or self
        return minNode if minNode else root

    def __init__(self, root1: TreeNode):

        # self.ops = 0

        ll = self.inorderTraversalList(root1)

        nums = []

        while ll:
            nums.append(ll.val)
            ll = ll.right

        self.nums = nums
        self.idx = 0

        
    def next(self) -> int:
        num = self.nums[self.idx]
        self.idx += 1
        return num

    def hasNext(self) -> bool:
        return self.idx < len(self.nums)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.nextNode()
# param_2 = obj.hasnextNode()

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