from typing import List
from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # reduce matrix to list of first elements.
        # O(M)
        firstElements = [row[0] for row in matrix]

        # Search. Unless the element is found, idx returned is that of the row succeeding the row that the value would exist in
        # O(log M)
        searchRowIdx = bisect_left(firstElements, target)

        if (searchRowIdx < len(matrix) and matrix[searchRowIdx][0] == target):
            return True

        searchRowIdx -= 1

        if searchRowIdx == -1:
            return False

        # Search the row.
        # O(log N)
        searchRow = matrix[searchRowIdx]
        elementIdx = bisect_left(searchRow, target)

        if elementIdx < len(searchRow) and searchRow[elementIdx] == target:
            return True

        return False


if __name__ == "__main__":
    s = Solution()
    r = s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [
        23, 30, 34, 60]], target=13)
    print(r)
    r = s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [
        23, 30, 34, 60]], target=7)
    print(r)
    r = s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [
        23, 30, 34, 60]], target=61)
    print(r)
