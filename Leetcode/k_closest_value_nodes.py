"""

LinkedIn 2025

Given the following Binary Search Tree:
 
                10
               /  \
              5    20
             /\    /\
            1  6  15 30
                \
                 7


                100
               /  \
              5    102
             /\    /  \
            1  99  101 103
t = 99                
k = 7                

Maintain priority queue O(log depth)
0: 99, -- 1
1: 100, -- 1

3: 102, -- 1
94: 5



Given target=8, and k=3, it should return 6,7,10


What if nodes < k, return everything
If target not in tree, return k closest.
Values are not duplicated in tree


Approach 1
Pre-order traversal O(N)-> sorted list
Find target index O(ln)-> index
Build list of k closest values O(k) -> answer
T O(N)
S O(N)

Approach 2


"""
from typing import List
import bisect

class TreeNode():

    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



def get_k_closest_nodes(root: TreeNode, target: int, k: int) -> List[TreeNode]:

    sorted_list = []

    # Create sorted list with pre-order traversal
    def pre_order_helper(node):
        if not node:
            return

        pre_order_helper(node.left)
        sorted_list.append(node)
        pre_order_helper(node.right)

    pre_order_helper(root)

    # Find index of target value
    idx = bisect.bisect_left(sorted_list, target)

    answer = []

    left = idx - 1
    right = idx

    # Scan left and right, building answer
    while len(answer) < min(k, len(sorted_list)):

        # If right OOB, make impossible
        if right == len(sorted_list):
            right_difference = float("inf")
        else:
            # Difference between right candidate and target
            right_difference = sorted_list[right].value - target

        # If left OOB, make impossible
        if left == -1:
            left_difference = float("inf")
        else:
            # Difference between left candidate and target
            left_difference = target - sorted_list[left].value

        # Compare
        if left_difference <= right_difference:
            next_idx = left
            left -= 1
        else:
            next_idx = right
            right += 1

        answer.append(sorted_list[next_idx])
        
    return answer
    


