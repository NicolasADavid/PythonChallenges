from typing import List

class Solution:
    # If output should be true if the input can be a Toeplitz matrix left-to-right-diagonally or right-to-left-diagonally
    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

    #     if self.helper(matrix):
    #         return True
    #     else:
    #         flipped = [list(reversed(row)) for row in matrix]
    #         return self.helper(flipped)

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for i, row in enumerate(matrix):

            for j, num in enumerate(row):

                # last row, no check needed. Return True
                if i == len(matrix)-1:
                    return True
                
                # last column, no check needed. Continue
                if j == len(matrix[0])-1:
                    continue
                
                # Numbers diagonally adjacent do not match. Return False
                if not matrix[i+1][j+1] == num:
                    return False
                
        return True

print("True? : ", Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print("False? : ", Solution().isToeplitzMatrix([[1,2],[2,2]]))
print("False? : ", Solution().isToeplitzMatrix(
    [[53,64,90,98,34],
     [91,53,64,90,98],
     [17,91,53,64,0]])
     )


# Row by row solution:
# Take a row, each element, check the next row and one column over for matching number.

#Diagonal traversals:
# All along left side and top side, start a diagonal traversal