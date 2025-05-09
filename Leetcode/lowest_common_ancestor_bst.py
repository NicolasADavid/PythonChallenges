"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

"""

"""
Algorithm:

1. Start at the root node.
2. If both p and q are less than the root, then LCA lies in the left subtree.
3. If both p and q are greater than the root, then LCA lies in the right subtree.
4. If one of p or q is less than the root and the other is greater, then the root is the LCA.
5. If either p or q is equal to the root, then the root is the LCA.
6. Recursively call the function on the left or right subtree based on the values of p and q.
7. Return the LCA node when found.
8. The time complexity is O(h), where h is the height of the tree.
9. The space complexity is O(h) for the recursion stack.
10. This algorithm works for both balanced and unbalanced trees.
11. The algorithm assumes that both p and q are present in the tree.
12. If either p or q is not present, the algorithm will still return the LCA of the nodes that are present.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """

#         if not root:
#             return None
        
#         if root.val > p.val and root.val > q.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif root.val < p.val and root.val < q.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node