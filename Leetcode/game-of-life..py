from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])

        live = []
        die = []

        def isLive(row, col) -> bool:
            if 0 <= row < m and 0 <= col < n:
                return board[row][col]

        def liveOrDie(row, col, cell) -> bool:

            # Determine how many living neighbors the cell has

            liveNeighbors = 0

            for neighborRow in [row - 1, row, row + 1]:
                for neighborCol in [col - 1, col, col + 1]:
                    if neighborRow == row and neighborCol == col:
                        continue

                    if isLive(neighborRow, neighborCol):
                        liveNeighbors += 1

            if not cell:
                return True if liveNeighbors == 3 else False
            else:
                return True if 1 < liveNeighbors < 4 else False

        for rowIdx, col in enumerate(board):
            for colIdx, cell in enumerate(col):

                if liveOrDie(rowIdx, colIdx, cell):
                    live.append((rowIdx, colIdx))
                else:
                    die.append((rowIdx, colIdx))

        # Live all live
        while live:
            row, col = live.pop()
            board[row][col] = 1

        # Die all die
        while die:
            row, col = die.pop()
            board[row][col] = 0

if __name__ == "__main__":
    [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
    Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])