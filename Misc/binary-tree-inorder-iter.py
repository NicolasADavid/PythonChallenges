class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
    
def solution(root):
    
    answer = []
    stack = []
    
    curr = root
    
    while curr or stack:
        
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            popped = stack.pop()
            answer.append(popped.value)
            curr = popped.right
    
    return answer
            

