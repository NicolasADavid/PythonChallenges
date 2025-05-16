"""
366. Find Leaves of Binary Tree

Companies
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]

"""
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        levels = defaultdict(list)

        # find how far a node is from the leaves
        def helper(node):
            if not node:
                return -1
                     
            distance_to_leaves = max(helper(node.left), helper(node.right)) + 1
            
            levels[distance_to_leaves].append(node.val)

            return distance_to_leaves
        
        helper(root)

        ans = []

        for i in range(len(levels)):
            ans.append(levels[i])

        return ans