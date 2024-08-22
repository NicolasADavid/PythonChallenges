'''
You are given a binary tree that is represented by a string. Nodes have no value. A 0 represents null and a (00) represents a node with no children, a leaf node.
((00)0) would represent a tree where the root has one left node and no right node. ((00)(00)) represents a tree with one left and one right node.

Given this representation of the tree, return the maximum depth of the tree.

EXAMPLE(S)
(((00)0)0) represents this tree with a max depth of 2
    0
   /
  0
 /
0
           r
((0(0(00)))(00)) represents this tree with a max depth of 3
    0
   /  \
  0    0
   \
    0
      \
       0


FUNCTION SIGNATURE
def maxDepth(tree: str) -> int:
'''
def maxDepthStacked(tree: str) -> int:

    ans = 0
    lbracks = []

    for s in tree:
        if s == "(":
            lbracks.append(s)
            ans = max(ans, len(lbracks))
        if s == ")":
            lbracks.pop()
    
    return ans - 1

def maxDepth(tree: str) -> int:
    ans = 0
    count = 0

    for s in tree:
        if s == "(":
            count += 1
            ans = max(ans, count)
        if s == ")":
            count -= 1
    
    return ans - 1

# assert calculate_tax(100000, [(0, 10000, 0.10), (10000, 30000, 0.15), (30000, 60000, 0.25), (60000, float('inf'), 0.35)]) == 25500

print(maxDepth("((0(0(00)))(00))"))
print(maxDepth("(((00)0)0)"))

print(maxDepthStacked("((0(0(00)))(00))"))
print(maxDepthStacked("(((00)0)0)"))
# EXPLORE

# BRAINSTORM

# PLAN

# IMPLEMENT

# VERIFY
# */