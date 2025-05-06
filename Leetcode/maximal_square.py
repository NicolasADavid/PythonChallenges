class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        
        dp_up = [[0] * cols for _ in range(rows)]
        dp_left = [[0] * cols for _ in range(rows)]
        dp = [[0] * cols for _ in range(rows)]
        best = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp_up[i][j] = 1
                        dp_left[i][j] = 1
                        dp[i][j] = 1
                    else:
                        dp_up[i][j] = dp_up[i-1][j] +1
                        dp_left[i][j] = dp_left[i][j-1] +1
                        dp[i][j] = min(dp_up[i][j], dp_left[i][j], dp[i-1][j-1] + 1)
                        
                    best = max(best, dp[i][j])
        
        return best * best
    
if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(Solution().maximalSquare(matrix))  # Output: 4
    matrix = [
        ["0", "1"],
        ["1", "0"]
    ]
    print(Solution().maximalSquare(matrix))  # Output: 1
    matrix = [
        ["0"]
    ]
    print(Solution().maximalSquare(matrix))  # Output: 0
    matrix = [
        ["1"]
    ]
    print(Solution().maximalSquare(matrix))  # Output: 1
    matrix = [
        ["1", "1"],
        ["1", "1"]
    ]
    print(Solution().maximalSquare(matrix))  # Output: 4
    matrix = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    print(Solution().maximalSquare(matrix))  # Output: 9

    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print(Solution().maximalSquare(matrix))  # Output: 4