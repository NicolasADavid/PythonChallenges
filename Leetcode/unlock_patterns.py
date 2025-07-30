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


Algorithm:


Create a jump matrix that indicates which numbers are jumped over when moving from one number to another.


Start from every number.

If path is of length N, return 1
Consider every possible next number that is not already visted and does not jump over an unused number
Explore that path, incrementing the path length by 1

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
                
            def dfs(src, length, visited, pattern):

                visited.add(src)
                pattern += str(src) + " "
                length += 1

                nonlocal count

                if length >= m:
                    count += 1
                    print("Valid pattern: ", pattern)
                
                if length == n:
                    visited.remove(src)
                    return
                
                for next_key in range(1, self.NUMBER_OF_KEYS + 1):

                    # next_key is not already visited
                    if next_key in visited:
                        continue
                    
                    # src -> next_key does not cover a key that is not visited
                    if cover[(min(src, next_key), max(src, next_key))] != 0 and (cover[(min(src, next_key), max(src, next_key))] not in visited):
                        continue

                    dfs(next_key, length, visited, pattern)

                visited.remove(src)
            
            dfs(target, 0, visited, "")
        
            return count

        total = 0

        # 1, 3, 7, 9 (corners) are symmetric. Only need to calculate possibilities from one of them
        # 2, 4, 6, 8 (edges) are symmetric.
        # 5 is the center and can be used in any pattern.

        corner = helper(1)
        edge = helper(2)
        center = helper(5)

        total += 4 * corner + 4 * edge + center
        return total

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