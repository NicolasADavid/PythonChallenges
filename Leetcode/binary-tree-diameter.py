class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
    
def solution(t):
    
    answer = 0
    
    # int is length of longest path (left or right) including the node 
    def process(node) -> int:
        
        nonlocal answer
        
        if not node:
            return 0
        
        left = process(node.left)
        right = process(node.right)
        
        answer = max(answer, left + right + 1)
        
        return max(left + 1, right + 1)
    
    process(t)
    return answer
    