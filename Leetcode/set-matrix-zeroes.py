from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        debug = True

        if debug:
            print("before marking: ")
            for row in matrix:
                print(row)
            print("----")
            
        markFirstCol = False

        # O(mn)
        # find zeroes, set corresponding top cell in matrix[0] and leftmost cell in same row to zero
        for idxr, row in enumerate(matrix):
            for idxc, val in enumerate(row):
                if val == 0:
                    # left cell
                    matrix[idxr][0] = 0
                        
                    # top cell
                    if idxc == 0:
                        markFirstCol = True
                    else:
                        matrix[0][idxc] = 0

        if debug:
            print("after marking: ")
            for row in matrix:
                print(row)
            print("----")

        # O(mn)
        for idxr, row in enumerate(matrix):
            if idxr == 0:
                continue
            for idxc, val in enumerate(row):
                if idxc == 0:
                    continue

                # if top cell or left cell are zero, change to zero
                if matrix[0][idxc] == 0 or matrix[idxr][0] == 0:
                    matrix[idxr][idxc] = 0
                    
        # O(m)
        # process row 0
        if matrix[0][0] == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        # O(n)
        #process column 0
        if markFirstCol:
            for row in matrix:
                row[0] = 0

        if debug:
            print("after processing")
            for row in matrix:
                print(row)
            print("----")

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)

matrix = [[1],[0],[3]]
Solution().setZeroes(matrix)

matrix = [[1, 2, 3, 4],
[5, 0, 7, 8],
[0, 10, 11, 12],
[13, 14, 15, 0]]
Solution().setZeroes(matrix)