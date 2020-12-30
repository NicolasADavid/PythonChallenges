from typing import List
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix: return []

        goingUp = True

        def goingDown():
            return not goingUp

        ans = []

        i = 0
        j = 0

        n = len(matrix)
        m = len(matrix[0])

        """
        Loop options
        1: while i < n and j < m
        At edges:
            if goingUp, go right if possible, else go down
            if not, go down if possible, else go right
        At final element, maybe goingUp or goingRight.
        Cannot go right or go down, but i or j will be incremented and equal n or m
        """

        if n == 1:
            return matrix[0]
        if m == 1:
            return [row[0] for row in matrix]

        while i < n and j < m:

            e = matrix[i][j]
            # print(e)

            ans.append(e)

            # Have reached an edge, move right or down and flip

            # Check if we're at an edge.
            # If yes, need to move vertically/horizontally and flip direction
            if goingUp and (i == 0 or j == m - 1):

                # Have to move right or down

                # If can move right
                if j < m - 1:
                    j += 1
                else:
                    i += 1

                goingUp = not goingUp

            elif goingDown() and (i == n - 1 or j == 0):

                # Have to move down or right

                # If can move down
                if i < n - 1:
                    i += 1
                else:
                    j += 1

                goingUp = not goingUp

            else:

                # Proceed diagonally

                if goingUp:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1                

        return ans

if __name__ == "__main__":
    print(Solution().findDiagonalOrder([[2,3]]))
    print(Solution().findDiagonalOrder([[2,5],[8,4],[0,-1]]))