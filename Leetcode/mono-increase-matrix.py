
def solution(matrix):
    
    # every row (left-to-right)
    # every column (top-to-bottom)
    
    # check every row
    for row in matrix:

        prev = float('-inf')
        for num in row:
            if num < prev:
                return False
            
            prev = num
    
    # check every column
    
    # j columns 
    for j in range(len(matrix[0])):
        prev = float('-inf')
        # i rows
        for i in range(len(matrix)):
            num = matrix[i][j]
            if matrix[i][j] < prev:
                return False
            prev = num
    
    return True
            
        
        
print(solution([[1,1,1,2], 
 [1,2,3,3], 
 [3,4,5,6]]))