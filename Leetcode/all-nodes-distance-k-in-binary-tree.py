from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        # Annotate each node with its parent O(N)
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        # Begin dfs from root
        dfs(root)

        # Target node is an arg, can begin queue with it
        # Target is 0 distance from itself.
        # (node, distanceFromTarget) 
        queue = deque([(target, 0)])

        seen = {target}

        # For each node in the queue, enqueue its parent, left, right with
        # d+1.
        while queue:

            # If queue's front is K distance from target, all the nodes that 
            # are K-1 distance from target have been processed and the queue
            # contains all of the nodes that are K distance from target. 
            # Return the contents of the queue.
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            
            node, d = queue.popleft()

            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        # If queue never contains a node that is K distance from target,
        # return an empty list
        return []