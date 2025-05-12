class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            for di, dj in directions:
                dfs(i + di, j + dj)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
                    
        return count
