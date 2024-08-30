# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def solution(root, val1, val2):
  
  # left and right have to return true

  answer = None

  def checkNode(node):

    nonlocal answer

    if not node:
      return False
    
    selfHas = False
    rightHas = False
    leftHas = False
    
    if node.value in [val1, val2]:
      selfHas = True

    leftHas = checkNode(node.left)
    rightHas = checkNode(node.right)

    if sum([selfHas, rightHas, leftHas]) == 2:
      answer = node
      return False

    return selfHas or rightHas or leftHas
  
  checkNode(root)
  
  if answer:
    return answer.value
  else:
    return -1
    

