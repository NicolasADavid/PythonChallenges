from typing import List

import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        leftMost = bisect.bisect_left(nums, target)
        
        if(leftMost == len(nums) or nums[leftMost] != target):
            return [-1,-1]
        
        rightMost = leftMost

        while(rightMost < len(nums)-1 and nums[rightMost+1] == target):
            rightMost += 1

        return [leftMost, rightMost]

if __name__ == "__main__":

    s = Solution()

    i1 = [1,1,3,5,7,8,8,8,8,8,8,8,8,8,8,8,9]

    # print(s.searchRange(i1, 1))
    # print(s.searchRange(i1, 5))
    # print(s.searchRange(i1, 6))
    # print(s.searchRange(i1, 8))
    
    def index(a, x):
        'Locate the leftmost value exactly equal to x'
        i = bisect.bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        raise ValueError

    # print(bisect.bisect_left(i1, -1)) #0
    # print(bisect.bisect_left(i1, 1)) #0
    # print(bisect.bisect_left(i1, 2)) #2
    # print(bisect.bisect_left(i1, 8)) #5


    i2 = [2,2]
    print(s.searchRange(i2, 3))

    millionOnes = [1] * 100000
    print(s.searchRange(millionOnes, 1))