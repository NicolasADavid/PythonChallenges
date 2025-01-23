'''
Given a chess board with a set of bishops, return the number of pairs of bishops that are attacking each other. Bishops will be given as an array of tuples.
 

EXAMPLE(S)
Bishops: [(0, 0), (2, 2), (1, 2), (3, 0)]
This would look like this:

  0 1 2 3 4
0 x . . . .
1 . . x . .
2 . . x . .
3 x . . . .
4 . . . . .


  0 1 2 3 4
0 x . . . .
1 . . . . .
2 . . x . .
3 . . . . .
4 x . . . .
output = 2

  0 1 2
0 x . .
1 . x .
2 . . x

2,2 can attact 0,0
output = 3

[0,0][1,1][2,2]


In this case, there are 2 pairs of bishops attacking each other.
 

FUNCTION SIGNATURE
def numberOfBishops(bishops): Int
function pairsOfAttackingBishops(bishops)


Brainstorming;

-------------------
[0,0] [1,1]
row1 row2   col1 col2
|0 - 1| === |0 - 1|

sort our bishops array in asc order
iterate over array, checking to see if another bishop is in the line of sight for the bishop being checked 

NlogN + N




----------
  0 1 2 3
0 x . . .
1 . x . .
2 X . x .
3 . . . x

[(0,0), (1,1),(2,2), (0,2), (3, 3)]

x+y dict : {0:1, 2:2, 6:1}
x-y dict : {0:4, -2:1}
no of pair = 0+1+2+1+ (1 * count at diagonal = 3)

left diagonals
 x-y
 0-0 = 0
 1-1 = 0
 2-2 = 0

[(0, 0), (2, 2), (1, 2), (3, 0)]


right diagonals
x+y

1+2 = 3
3+0 = 3


| 1 - 3 | === | 2 - 0 | true


'''

from collections import defaultdict
def pairsOfAttackingBishops(bishops) -> int:

  ans = 0

  # dict of diagonals and counts of bishops for each diagonal
  ld = defaultdict(int)
  rd = defaultdict(int)

  for bishop in bishops:
    ans += ld[bishop[0] - bishop[1]]
    ld[bishop[0] - bishop[1]] += 1

    ans += rd[bishop[0] + bishop[1]]
    rd[bishop[0] + bishop[1]] += 1 

  return ans

print("main.py")
print(pairsOfAttackingBishops([(0,0), (1,1),(2,2), (0,2)]))



# Test case: Bishops form two attacking pairs
bishops = [(0, 0), (2, 2), (1, 2), (3, 0)]
print(pairsOfAttackingBishops(bishops) == 2)

# Test case: Bishops form no attacking pairs
bishops = [(0, 0), (1, 3), (3, 4), (9, 6)]
print(pairsOfAttackingBishops(bishops) == 0) # should be 0

# Test case: Bishops form multiple attacking pairs
bishops = [(1, 1), (2, 2), (5, 3), (6, 2), (5, 0), (0, 5)]
print(pairsOfAttackingBishops(bishops) == 3) ## should be 3

# Test case: Bishops form attacking pairs on both diagonals
bishops = [(0, 0), (3, 3), (6, 6), (0, 6), (6, 0)]
print(pairsOfAttackingBishops(bishops) == 6) # should be 6

# Test case: Bishops form attacking pairs on a single diagonal
bishops = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
print(pairsOfAttackingBishops(bishops) == 10) # should be 10

# Test case: Single bishop, no attacking pairs
bishops = [(0, 0)]
print(pairsOfAttackingBishops(bishops) == 0) # Defaults to 0 

# Test case: Empty list, no attacking pairs
bishops = []
print(pairsOfAttackingBishops(bishops) == 0) # Defaults to 0
  
