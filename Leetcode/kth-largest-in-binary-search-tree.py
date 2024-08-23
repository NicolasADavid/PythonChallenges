class Tree(object):
  def __init__(self, x, left = None, right = None):
    self.value = x
    self.left = left
    self.right = right

def solution(root, k):
    

    answer = None
    
    def help(node, seenSoFar):

        nonlocal answer
        
        if not node:
            return seenSoFar
        
        leftCount = help(node.left, seenSoFar)

        seenSoFar = leftCount + 1

        if seenSoFar == k:
            answer = node.value
            print("val found")
            raise Exception("Value found")
        
        seenSoFar = help(node.right, seenSoFar)
        
        return seenSoFar
            
    try:
        help(root, 0)
    except:
        return answer
    return -1

t = Tree(3, Tree(1), Tree(5, Tree(4), Tree(6)))

print(solution(t, 4))