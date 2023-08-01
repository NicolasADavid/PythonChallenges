from typing import List
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None
        
        q = deque()
        q.append(root)
        nextlevel = []
        
        answer = []
        level = []

        while q:

            next = q.popleft()
            level.append(next.val)
            if next.left: nextlevel.append(next.left)
            if next.right: nextlevel.append(next.right)
            if not q:
                answer.append(level)
                level = []
                q = deque(nextlevel)
                nextlevel.clear()

        answer.reverse()
        return answer
    
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
r = Solution().levelOrderBottom(root)

print("")
