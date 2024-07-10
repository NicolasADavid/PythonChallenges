# // Given an array of 0s, 1s, and 2s, return a sorted array.
from typing import List
from collections import Counter

# O(N)
class Solution:
    def dutchNationalFlag(self, input: List[int]) -> List[int]:
        c = Counter(input)

        ones = [1] * c[1]
        twos = [2] * c[2]
        zeroes = [0] * c[0]

        return zeroes+ones+twos

print(Solution().dutchNationalFlag([ 2, 1, 1, 0, 0, 0, 2 ]))