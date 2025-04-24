"""
1. Square Matrix

Given a m x n matrix of integers, determine if it is a square matrix (i.e. m equals n).

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] boolean


What?? m == n?

"""


def is_square_matrix(m):
    if not m:
        return False
    
    rows = len(m)
    cols = len(m[0])

    return rows == cols


"""
2. Square Matrix Zigzag

Q. Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in horizontal zigzag order (see examples below) starting from the top left element

Examples:
Input1:
[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
Output1:
[1, 2, 3, 6, 5, 4, 7, 8, 9]
Input2:
[
[1, 2, 3],
[4, 5, 6]
]
Output2: [1, 2, 3, 6, 5, 4]"""

def zigzag(matrix):
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # Traverse the matrix in zigzag order
    for i in range(rows):
        if i % 2 == 0:
            # Traverse left to right
            for j in range(cols):
                result.append(matrix[i][j])
        else:
            # Traverse right to left
            for j in range(cols - 1, -1, -1):
                result.append(matrix[i][j])
    
    return result

assert zigzag([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 5, 4, 7, 8, 9]


"""
Given a matrix of integers m, rotate it by 90 degrees clockwise
"""

def rotate(matrix):
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    if not cols:
        return [[]]
        
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][rows - 1 - i] = matrix[i][j]
    
    return result

assert rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
assert rotate([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
assert rotate([[1]]) == [[1]]
assert rotate([]) == []
assert rotate([[]]) == [[]]
assert rotate([[1, 2, 3, 4], [5, 6, 7, 8]]) == [[5, 1], [6, 2], [7, 3], [8, 4]]

"""
Q. Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order (counter-clockwise) starting from the top left element

Examples:
Input1:
[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
Output1:
[1, 4, 7, 8, 9, 6, 3, 2, 5]
Input2:
[
[1, 2, 3],
[4, 5, 6]
]
"""

def spiral(matrix):
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:


        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][left])
        left += 1

        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[bottom][i])
        bottom -= 1

        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][right])
            right -= 1

        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[top][i])
            top += 1
    
    return result

assert spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 4, 7, 8, 9, 6, 3, 2, 5]
assert spiral([[1, 2, 3], [4, 5, 6]]) == [1, 4, 5, 6, 3, 2]


"""
Q. Given a square matrix of integers, return the sum of all edges. Do not count the same element more than once.

Example:
Input:
[[1,2,3],
[4,5,6],
[7,8,9]]
"""

def sum_edges(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    if not cols:
        return 0
        
    total_sum = 0

    # Sum the top row
    total_sum += sum(matrix[0])

    # Sum the right column, excluding the first and last elements
    for i in range(1, rows - 1):
        total_sum += matrix[i][cols - 1]

    # Sum the bottom row
    if rows > 1:
        total_sum += sum(matrix[rows - 1])

    # Sum the left column
    for i in range(rows - 2, 0, -1):
        total_sum += matrix[i][0]
    
    return total_sum

assert sum_edges([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 40
assert sum_edges([[1, 2, 3], [4, 5, 6]]) == 21
assert sum_edges([[1, 2], [3, 4]]) == 10
assert sum_edges([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 10
assert sum_edges([[1]]) == 1
assert sum_edges([]) == 0
assert sum_edges([[]]) == 0

"""
You are given a rectangular matrix m. Your goal is to write a program that,
if an element of m is equal to 0, sets that element's entire row and column to 0.
"""

def set_zeroes(matrix):
    if not matrix:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    zero_rows = set()
    zero_cols = set()

    # First pass to find all zero positions
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Second pass to set rows and columns to zero
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

    return matrix