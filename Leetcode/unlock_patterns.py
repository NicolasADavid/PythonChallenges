"""
Given a 3x3 lock screen in the following arrangement:

1 2 3
4 5 6
7 8 9

count the total number of unlock patterns that use N numbers.

A pattern is valid if the following criteria are met:
- no number is used more than once
- a path from one number to another does not directly pass through an unused number. eg:
  - 2 -> 1 -> 3 is valid, but 1 -> 3 is not valid because it directly passes through the unused number 2

NOTE: It is possible to go from 2 to 9 (or 3 to 4) because the pattern may move between rows and colunns on diagonals.


Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" by connecting 
the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two 
consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:

All the dots in the sequence are distinct.
If the line segment connecting two consecutive dots in the sequence passes through the center of any other dot, 
the other dot must have previously appeared in the sequence. No jumps through the center non-selected dots are allowed.
For example, connecting dots 2 and 9 without dots 5 or 6 appearing beforehand is valid because the line 
from dot 2 to dot 9 does not pass through the center of either dot 5 or 6.

However, connecting dots 1 and 3 without dot 2 appearing beforehand is invalid because the line from dot 1 to dot 3 passes through the center of dot 2.

Here are some example valid and invalid unlock patterns:

The 1st pattern [4,1,3,6] is invalid because the line connecting dots 1 and 3 pass through dot 2, but dot 2 did not previously appear in the sequence.
The 2nd pattern [4,1,9,2] is invalid because the line connecting dots 1 and 9 pass through dot 5, but dot 5 did not previously appear in the sequence.
The 3rd pattern [2,4,1,3,6] is valid because it follows the conditions. The line connecting dots 1 and 3 meets the condition because dot 2 previously appeared in the sequence.
The 4th pattern [6,5,4,1,9,2] is valid because it follows the conditions. The line connecting dots 1 and 9 meets the condition because dot 5 previously appeared in the sequence.

Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid lock screen that consist of at least m keys and at most n keys.

Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, or the order of the dots is different.

"""

from collections import defaultdict

class Solution(object):

    NUMBER_OF_KEYS = 9

    def numberOfPatterns(self, m, n):
  
        """
        1 2 3
        4 5 6
        7 8 9
        """

        visited = set()
        cover = defaultdict(int)
        
        # cover[min(src, dest), max(src, dest)] = covered
        cover[(1,3)] = 2
        cover[(1,7)] = 4
        cover[(1,9)] = 5
        cover[(2,8)] = 5
        cover[(3,9)] = 6
        cover[(3,7)] = 5
        cover[(4,6)] = 5
        cover[(7,9)] = 8

        def helper(target):

            count = 0
                
            def dfs(src, length, visited, pattern = ""):

                visited.add(src)
                pattern += str(src) + " "
                length += 1

                nonlocal count

                if length >= m:
                    count += 1
                    print(pattern)
                
                if length < n:

                    for next_key in range(1, self.NUMBER_OF_KEYS + 1):

                        # next_key is not already visited
                        if next_key in visited:
                            continue
                        
                        # src -> next_key does not cover a key that is not visited
                        covered = cover[(min(src, next_key), max(src, next_key))]
                        if covered != 0 and covered not in visited:
                            continue

                        # continue the search
                        dfs(next_key, length, visited, pattern)

                visited.remove(src)
            
            dfs(target, 0, visited)
        
            return count

        # 1, 3, 7, 9 (corners) are symmetric. Only need to calculate possibilities from one of them
        # 2, 4, 6, 8 (edges) are symmetric.
        # 5 (center) is unique

        corner = helper(1) * 4
        edge = helper(2) * 4
        center = helper(5)

        return corner + edge + center

if __name__ == "__main__":

    assert Solution().numberOfPatterns(m = 1, n = 1) == 9
    assert Solution().numberOfPatterns(m = 1, n = 2) == 65
    assert Solution().numberOfPatterns(m = 1, n = 3) == 385

    assert Solution().numberOfPatterns(1, 1) == 9
    assert Solution().numberOfPatterns(2, 2) == 56
    assert Solution().numberOfPatterns(3, 3) == 320
    assert Solution().numberOfPatterns(4, 4) == 1624
    assert Solution().numberOfPatterns(5, 5) == 7152
    assert Solution().numberOfPatterns(6, 6) == 26016
    assert Solution().numberOfPatterns(7, 7) == 72912
    assert Solution().numberOfPatterns(8, 8) == 140704
    assert Solution().numberOfPatterns(9, 9) == 140704