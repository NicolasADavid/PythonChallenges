from typing import List
from collections import deque
class Solution:
    # def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

    #     # Edge cases:
    #     if nums and lower == upper and nums[0] == lower:
    #         return []

    #     ranges = deque([(lower, upper)])

    #     def getFirst():
    #         return ranges[0]
        
    #     def getLower(range):
    #         return range[0]

    #     def getUpper(range):
    #         return range[1]

    #     for num in nums:


    #         firstRange = getFirst()

    #         if num == getLower(firstRange) and num == getUpper(firstRange):
    #             #remove range
    #             _ = ranges.popleft()
    #         elif num == getLower(firstRange):
    #             ranges[0] = (getLower(firstRange) + 1, getUpper(firstRange))

    #         elif num == upper:
    #             ranges[0] = (getLower(firstRange), getUpper(firstRange) - 1)

    #         else:
    #             # Split the first range in dq
    #             range = ranges.popleft()
    #             range1, range2 = (getLower(range), num - 1), (num+1, getUpper(range))
    #             ranges.append(range1)
    #             ranges.appendleft(range2)

    #     # Move first range to end
    #     if len(ranges) > 1 and getLower(getFirst()) > getLower(ranges[-1]):
    #         r = ranges.popleft()
    #         ranges.append(r)

    #     return ranges
        
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        missing_ranges = []

        if n == 0:
            missing_ranges.append([lower, upper])
            return missing_ranges
        
        # Check for missing numers between the lower bound and nums[0]
        if lower < nums[0]:
            missing_ranges.append([lower, nums[0]-1])

        # Check for missing numbers between successive elements of num.
        for i in range(n-1):
            if nums[i+1] - nums[i] > 1:
                missing_ranges.append([nums[i] + 1, nums[i+1] -1])

        # Check for missing numbers bewtween last element of nums and the upper bound
        if upper > nums[-1]:
            missing_ranges.append([nums[-1] + 1, upper])
        
        return missing_ranges

if __name__ == "__main__":
    print(Solution().findMissingRanges(nums = [0,1,3,50,75], lower = 0, upper = 99))
    # Output: [[2,2],[4,49],[51,74],[76,99]]

    print(Solution().findMissingRanges(nums = [0,1], lower = 0, upper = 1))
    # []

    print(Solution().findMissingRanges(nums = [8,9], lower = 0, upper = 9))
    # [[0, 7]]

    print(Solution().findMissingRanges(nums = [6,8,9], lower = 0, upper = 9))
    # [[0, 5], [7, 7]]