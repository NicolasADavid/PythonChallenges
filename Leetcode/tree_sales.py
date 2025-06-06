'''
A garden store notices an interesting pattern in their tree sales.  When the trees are all lined up in a row, some of the trees are taller than their two immediate neighbors. Let's call these trees taller than their neighbors, stand out trees. They stand above the rest!

Customers tend to buy these stand out trees before others, but here's where it gets more interesting: the manager has noticed that the **shortest of the stand out trees** often get sold first!

The store manager wants to test this hypothesis. Write a function that takes these tree heights in an array as input and returns a new array with the height in the order that we predict they will be purchased.

The heights will all be positive and greater than zero. The output should include all values in the input.
 

EXAMPLE(S)
Tree heights: [2, 7, 8, 5, 1, 6, 3, 9, 4]
Output: [6, 8, 7, 5, 2, 9, 4, 3, 1]
Explanation:
[2, 7, 8, 5, 1, 6, 3, 9, 4] -> 6 (stand outs are 8, 6, 9)
[2, 7, 8, 5, 1, 3, 9, 4] -> 8 (stand outs are 8, 9)
[2, 7, 5, 1, 3, 9, 4] -> 7 (stand outs are 7, 9)
[2, 5, 1, 3, 9, 4] -> 5 (stand outs are 5, 9)
[2, 1, 3, 9, 4] -> 2 (stand outs are 2, 9)
[1, 3, 9, 4] -> 9 (only one stand out)
[1, 3, 4] -> 4 (only one stand out)
[1, 3] -> 3 (only one stand out)
[1] -> 1 (only stand out)
 
Tree heights: [1, 2, 3, 4]
Output: [4,3,2,1]
Explantation
[1,2,3,4] -> standouts: (4)
[1,2,3] -> standouts: (3)
[1,2] -> standouts: (2)
[1] -> standouts: (1)


Tree heights: [2, 7, 8, 5, 1, 6, 3, 9, 4]
Output: [6,8,7,5,2,9,4,3,1]
Explantation: 
[2, 7, 8, 5, 1, 6, 3, 9, 4] -> standouts (8,6,9)
[2, 7, 8, 5, 1, 3, 9, 4] -> standouts (8,9)
[2, 7, 5, 1, 3, 9, 4] -> standouts (7,9)
[2, 5, 1, 3, 9, 4] -> standouts (5,9)
[2, 1, 3, 9, 4] -> standouts (2,9)
[1, 3, 9, 4] -> standouts (9)
[1, 3, 4] -> standouts (4)
[1, 3] -> standouts (3)
[1] -> standouts (1)


Stand out tree: 

- bigger than its neighbors ( )
FUNCTION SIGNATURE
function standoutTreeSales(heights)
def standoutTreeSales(heights):


Brainstorming: 

Idea #1: 
results = []
- Loop through the tree heights

  current_standout = small < max
  determine if current elm is a stand out 
    if stand out -> add to current_standout

  push the current_standout to results 


Idea #2: [1, 2, 3, 4]


1: L(N) R(2)
2: L(1) R(3)
3: L(2) R(4)
4: L(3) R(N)
MH: [4]

Output: [4]
1: L(N) R(2)
2: L(1) R(3)
3: L(2) R(N)
MH: [3]

Output: [4, 3]
1: L(N) R(2)
2: L(1) R(N)
MH: [2]


Output: [4, 3, 2]
1: L(N) R(N)
MH: [1]

Output: [4, 3, 2, 1]

MH: []

Return output



turn tree heights into a double linked list
identify stand out tree nodes, add to min heap by height, add to seen set
while elements in min heap
  pop element
  add to output
  update left node's right node
  check if left is now an SOT, add to min heap, add to seen set
  update right node's left node
  check if right is now an SOT, add to min heap, add to seen set


Idea #3: 
If the list is empty:
  return an empty list

loop through the tree height (index 1 - second to last)
  determine if the curr elemt is a stand out 
  if it is -> store the index

if we found any stand out:
  find the with smallest heigh
  remove from the list
  return that element recursive call on the new list 

if there no stand outs
  remove the first element 
  return [element] + recursive call 
'''


'''
turn tree heights into a double linked list
identify stand out tree nodes, add to min heap by height, add to seen set
while elements in min heap
  pop element
  add to output
  update left node's right node
  check if left is now an SOT, add to min heap, add to seen set
  update right node's left node
  check if right is now an SOT, add to min heap, add to seen set
'''

import heapq

class Node:
    def __init__(self, height, left=None, right=None):
        self.height = height
        self.left = left
        self.right = right


def standout_tree_sales(heights):

  left_dummmy = Node(0)
  right_dummy = Node(0)
  left_dummmy.right = right_dummy
  right_dummy.left = left_dummmy
  tail = right_dummy

  for idx, height in enumerate(heights):
    node = Node(height)
    prev = tail.left
    node.left = prev
    node.right = tail
    prev.right = node 
    tail.left = node
  
  heap = []
  seen = set()

  curr = left_dummmy
  while curr:
    if curr.height == 0:
      curr = curr.right
      continue
    
    if curr.height > curr.left.height and curr.height > curr.right.height:
      heapq.heappush(heap, (curr.height, curr))
      seen.add(curr.height)

    curr = curr.right

  def is_stand_out(node):
    return node.height > node.left.height and node.height > node.right.height
  
  result = []
  while heap:
    _, node = heapq.heappop(heap)
    result.append(node.height)

    left = node.left
    right = node.right

    left.right = right 
    right.left = left

    if left.height != 0 and is_stand_out(left) and left.height not in seen:
      heapq.heappush(heap, (left.height, left))
      seen.add(left.height)

    if right.height != 0 and is_stand_out(right) and right.height not in seen:
      heapq.heappush(heap, (right.height, right))
      seen.add(left.right)

  return result


assert standout_tree_sales([1,2,3,4]) == [4, 3, 2, 1]
assert standout_tree_sales([2, 7, 8, 5, 1, 6, 3, 9, 4]) == [6, 8, 7, 5, 2, 9, 4, 3, 1]