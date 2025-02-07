'''
Today, you will be given the problem of the Brick Wall:

Source: https://leetcode.com/problems/brick-wall/description/

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You want to return the least number of bricks that you'll need to cut through.
 

EXAMPLE(S)
[[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]] => 2

[
[1,2,2,1]
[3,1,2]
]

-,--,--,-
---,-,--
 

FUNCTION SIGNATURE
func minBricks(input: [[Int]]) -> Int
'''

from collections import defaultdict
from typing import List
from itertools import accumulate

class Solution:

    def leastBricks(self, wall: List[int]) -> int:

        map, best = defaultdict(int), 0

        for row in wall:

            for idx in accumulate(row[:-1]):
                map[idx] += 1
                best = max(best, map[idx])
                                
        ans = len(wall) - best
        return ans



w1 = [[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]]
a1 = 2

assert Solution().leastBricks(w1) == a1

w2 = [
[1,2,2,1],
[3,1,2]
]
a2 = 0
assert Solution().leastBricks(w2) == a2

