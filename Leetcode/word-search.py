from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def helper(row, col, suffix) -> bool:

            nonlocal board
            
            if suffix == "":
                return True

            if row < 0 or row == len(board) or col < 0 or col == len(board[0]):
                return
            
            if suffix[0] != board[row][col]:
                # don't care
                return
            
            dirs = [(-1, 0), (1, 0), (0, 1), (0,-1)]

            # Mark current space
            board[row][col] = "#"

            # Explore UDLR
            for (dr, dc) in dirs:
                if helper(row + dr, col + dc, suffix[1:]):
                    return True

            # Unmark space
            board[row][col] = suffix[0]

        for ri, row in enumerate(board):
            for ci, letter in enumerate(row):
                if helper(ri, ci, word):
                    return True
        
        return False
        