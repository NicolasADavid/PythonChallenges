from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        # In-place, set visited spots to 0

        n = len(grid)
        m = len(grid[0])

        # When turf is found, count. Search and empty all connected turf.

        count = 0

        def empty(row, col):
            if 0 <= row < n and 0 <= col < m and grid[row][col] == '1':
                grid[row][col] = 0
                goWays(row, col)
                

        def goWays(row, col):

            dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]

            for rowOff, colOff in dirs:
                empty(row+rowOff, col+colOff)


        for rowIdx, row in enumerate(grid):
            for colIdx, turf in enumerate(row):
                if turf == '1':
                    count+=1
                    empty(rowIdx, colIdx)

        return count



if __name__ == "__main__":
    s = Solution()

    input = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    print(s.numIslands(input)) #1