'''
Given an array of 0s and 1s, what is the minimum number of moves needed to group all 0s on one side and 1s on the other side. A "move" is a swap between any adjacent positions.
 

EXAMPLE(S)
[0, 1] => 0, no swaps are needed since they are already grouped.
[0, 1, 0] => 1, swap 1 with either 0 to group them.


[1, 1, 1, 0, 0] => 2, swap 0 with 1 then swap it again with the next 1.
 

FUNCTION SIGNATURE
function minSwaps(input: Array<number>): number

constant space, do not modify array

[0, 1 1, 1, 0]
1 -> 2
0 -> 3
return minimum?
4 moves 0s to the left
2 moves 1s to the left




[1, 0, 1, 0, 1, 1, 1]
 5  C  4  C  3  2  1 R->L -> 3 + 4 = 7
 1. C  2. C. 3. 4. 5 L->R -> 1 + 2 = 3 -> return 3


   L
       R
[0,0,1,1,1]

move = 1 + 2 = 3

Plan:
2 passes
  1: consider move all 0s to right
  2: consider move all 0s to left

  init count of 1s
  init count of moves required
  iterate through array from right to left
    if 1, increment count of 1s
    if 0, increment moves required by 1s count
  
  repeat from left to right
  iterate through array from left to right
    if 1, increment count of 1s
    if 0, increment moves required by 1s count

  return minimum of leftToRightMoves and rightToLeftMoves
'''

def minSwaps(nums) -> int:

  ltr = 0
  ones = 0

  for num in nums:
    if num == 1:
      ones += 1
    else:
      ltr += ones
  
  rtl = 0
  ones = 0
  
  for num in list(reversed(nums)):
    if num == 1:
      ones += 1
    else:
      rtl += ones
  
  return min(rtl, ltr)
    



test1_swaps = minSwaps([0, 1])
assert test1_swaps == 0, test1_swaps

test2_swaps = minSwaps([0, 1, 0])
assert test2_swaps == 1, test2_swaps

test3_swaps = minSwaps([1, 0, 1, 1, 0])
assert test3_swaps == 2, test3_swaps

test4_swaps = minSwaps([1, 0, 0, 1, 1, 1])
assert test4_swaps == 2, test4_swaps

test5_swaps = minSwaps([1, 0, 1, 1, 0, 1, 0, 1, 0])
assert test5_swaps == 7, test5_swaps

test6_swaps = minSwaps([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
assert test6_swaps == 10, test6_swaps