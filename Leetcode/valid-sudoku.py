from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for row in board:
            seen = set()
            for num in row:
                if num != "." and num in seen:
                    return False
                else:
                    seen.add(num)

        #columns
        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                num = board[row][col]
                if num != "." and num in seen:
                    return False
                else:
                    seen.add(num)

        # #3x3 grids
        for row in range(0, len(board), 3):
            # 3 times

            for col in range(0, len(board), 3):
                # 3 times

                seen = set()

                # top left corner board[row][col]

                for i in range(0, 3):
                    for j in range(0, 3):
                        num = board[row + i][col + j]
                        if num != "." and num in seen:
                            return False
                        else:
                            seen.add(num)

        return True

s = Solution().isValidSudoku(
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
)

print(s)