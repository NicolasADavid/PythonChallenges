'''
Given a binary search tree where all nodes have integer values, return the floor and ceiling of a target number.

The floor is the largest element that is smaller than or equal to the target, and the ceil is the smallest element that is greater than or equal to the number.
 

EXAMPLE(S)
  3
1   5

tree = TreeNode(3, 
         TreeNode(1),
         TreeNode(5))

target: 4 returns [3, 5]
target: 2 returns [1, 3]
 

FUNCTION SIGNATURE
function findFloorAndCeil(node, target):
'''


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:


        def floorAndCeil(root, target):

            floor = -1
            ceil = -1
            curr = root
            
            while curr:
                if curr.val == target:
                    floor = curr.val
                    ceil = curr.val
                    break
                elif curr.val > target:
                    ceil = curr.val
                    curr = curr.left
                else:
                    floor = curr.val
                    curr = curr.right
            return [floor, ceil]
        
        output = []

        for target in queries:
            output.append(floorAndCeil(root, target))

        return output