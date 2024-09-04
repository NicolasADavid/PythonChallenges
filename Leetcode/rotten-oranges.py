
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

# https://leetcode.com/problems/rotting-oranges/description/

from typing import List

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        if not grid[0]:
            return 0
        
        n = len(grid)
        m = len(grid[0])

        freshOranges = []
        newlyRotten = []
        visited = set()

        # Collect rotten and fresh orange coordinates
        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == 2:
                    newlyRotten.append((r, c))
                if orange == 1:
                    freshOranges.append((r, c))

        ans = 0

        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]


        while newlyRotten:
            rottenOranges = newlyRotten.copy()
            newlyRotten.clear()

            for ro in rottenOranges:

                for dir in directions:

                    nr, nc = ro[0] + dir[0], ro[1] + dir[1]

                    # Validate coordinates
                    if nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1:
                        continue

                    # Check if visited before
                    if (nr, nc) in visited:
                        continue

                    visited.add((nr, nc))

                    # If fresh orange, 'rot' and collect
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 3
                        newlyRotten.append((nr, nc))   
            
            # If turn/minute 'rotted' a fresh orange, increase number of minutes needed to rot all oranges
            if newlyRotten:
                ans += 1

        # Check that all fresh oranges were visited/rotted
        for fo in freshOranges:
            if fo not in visited:
                return -1
        
        return ans

assert Solution().orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]) == 4
assert Solution().orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]) ==  4
assert Solution().orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]) == -1
assert Solution().orangesRotting(grid = [[0,2]]) ==  0

# https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/