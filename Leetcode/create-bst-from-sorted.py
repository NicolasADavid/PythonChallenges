#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
    
def solution(inputArray):
    
   
    def createLeft(array):

        n = len(array)
        
        if not array:
            return None
        
        if n == 1:
            t = Tree(array[0])
            return t
        
        if n == 2:
            t = Tree(array[0])
            t.right = Tree(array[1])
            return t
        
        if n == 3:
            t = Tree(array[1])
            t.left = Tree(array[0])
            t.right = Tree(array[2])
            return t
            
        midpoint = (len(array) // 2)

        if n % 2 == 0:
            midpoint -= 1
            
        left = array[:midpoint]
        right = array[midpoint+1:]
        
        t = Tree(array[midpoint])
        
        t.left = createLeft(left)
        t.right = createLeft(right)
        
        return t
        
        
    t = createLeft(inputArray)

    return t
    
    
bbst1 = solution([6,9,11,15,19,25])

print(bbst1.value)

bbst2 = solution([-10, -3, 0, 5, 9])

print(bbst2.value)