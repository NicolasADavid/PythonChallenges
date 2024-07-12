# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)

        # build an equivalent graph of the tree
        def build_graph(cur, parent):
            # parent relationship
            if cur and parent:
                graph[cur.val].append(parent)
                graph[parent.val].append(cur)

            # call on children
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)

        build_graph(root, None)

        results = []
        visited = set([target.val])

        def dfs(cur, distance):
            if distance == k:
                results.append(cur.val)
                return
            for neighbor in graph[cur.val]:
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    dfs(neighbor, distance+1)
        
        dfs(target, 0)

        return results