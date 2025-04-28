"""
Given a square matrix of integers, return the sum of the elements along the two major diagonals, top left to bottom right and top right to bottom left. Do not count the same index more than once.

Example:
Input:
[[1,2,3],
[4,5,6],
[7,8,9]]

Output: 25
Explanation: 1 + 5 + 9 + 3 + 7 = 25 (note that 5 is not counted twice).
"""

def diagonalSum(matrix):

    
    if not matrix:
        return 0
    if not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    answer = 0
    
    # TL->BR
    c = 0
    r = 0
    while r < rows:
        answer += matrix[r][c]
        r += 1
        c += 1
        
    r = 0
    c = cols - 1
    
    # TR->BL
    while r < rows:
        if r != c:
            answer += matrix[r][c]
        
        r += 1
        c -= 1
    
    return answer   

assert diagonalSum([[1,2,3],[4,5,6],[7,8,9]]) == 25

"""
Given a square matrix of integers, sort it in ascending order.

Example:

Given:
[  [6, 4, 7],
   [1, 3, 2],
   [8, 9, 5]  ]
returns:
[  [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]  ]
"""

def matrixSort(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    flattened = []
    
    for i in range(rows):
        for j in range(cols):
            flattened.append(matrix[i][j])
            
    flattened.sort()
    idx = 0
    
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = flattened[idx] 
            idx += 1
    
    return matrix

assert matrixSort([[6, 4, 7],[1, 3, 2],[8, 9, 5]]) == [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

"""
Q. Given a square matrix with a minimum length of 2 on each side, sum top right triangular portion.

Example 1:

Given:
[  [6, 4, 7],
   [1, 3, 2],
   [8, 9, 5]  ]
returns: 27 (6+4+7+3+2+5)

Explanation: The top right triangular portion is:

[  [6, 4, 7],
   [   3, 2],
   [      5]  ]
Example 2:

Given:
[  [6, 4, 7, 1],
   [1, 3, 2, 2],
   [0, 0, 5, 2],
   [8, 9, 5, 3]  ]
returns: 35

Explanation: The top right triangular portion is:

[  [6, 4, 7, 1],
   [   3, 2, 2],
   [      5, 2],
   [         3]  ]
"""

def topRightTriangularSum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    cStart = 0
    
    ans = 0
    
    for row in range(rows):
        for col in range(cStart, cols):
           ans += matrix[row][col]
        cStart += 1
    
    return ans

assert topRightTriangularSum([[6, 4, 7],[1, 3, 2],[8, 9, 5]]) == 27
assert topRightTriangularSum([[6, 4, 7, 1],[1, 3, 2, 2],[0, 0, 5, 2],[8, 9, 5, 3]]) == 35


"""
Q. Given a square matrix with each row sorted and consist of either 0 or 1, return the index of the first row
 from the top with the minimum positive number of 1s. If no rows have even a single 1, return -1.

"""

# for each row, binary search for the first 1. Count of 1s for the row is cols - index of first 1.
def binarySearchFirst1(row):
    left = 0
    right = len(row) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if row[mid] == 1:
            right = mid - 1
        else:
            left = mid + 1
            
    return left

def minRowWith1s(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    minRow = -1
    minCount = float('inf')
    
    for i in range(rows):
        index = binarySearchFirst1(matrix[i])
        count = cols - index
        if count < minCount and count > 0:
            minCount = count
            minRow = i
    
    return minRow

assert minRowWith1s([[0, 0, 0],[0, 1, 1],[0, 1, 1],[0, 1, 1]]) == 1

"""
You are given a rectangular matrix m. Your goal is to write a program that, if an element of m is equal to 0, sets that element's entire row and column to 0.

"""

def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    rowSet = set()
    colSet = set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rowSet.add(i)
                colSet.add(j)
    
    for i in range(rows):
        for j in range(cols):
            if i in rowSet or j in colSet:
                matrix[i][j] = 0
    
    return matrix