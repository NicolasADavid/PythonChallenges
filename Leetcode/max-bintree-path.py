class Tree(object):
  def __init__(self, x, left = None, right = None):
    self.value = x
    self.left = left
    self.right = right
    
    
def solution(root):
    
    best = 0
    
    def help(tree):

        nonlocal best
        
        if not tree:
            return 0
        
        leftSum = help(tree.left)
        rightSum = help(tree.right)
        
        selfWithLeft = tree.value + max(0, leftSum)
        selfWithRight = tree.value + max(0, rightSum)

        selfWithBoth = tree.value + leftSum + rightSum
        
        # Can include both self.value and sums of left and right subtrees, but cannot pass that value upwards
        localBest = max(selfWithLeft, selfWithRight, selfWithBoth)
        best = max(best, localBest)

        # Pass self + left or self + right upwards
        return max(selfWithLeft, selfWithRight)
    
    help(root)
        
    return best

tree = Tree(1, Tree(2, Tree(-1)), Tree(3))
print(solution(tree))