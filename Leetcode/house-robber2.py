from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        # No houses
        if nums is None or len(nums) == 0:
            return 0

        # One house
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[1:]), self.rob_simple(nums[:-1]))

    def rob_simple(self, nums: List[int]) -> int:
        
        t1 = 0
        t2 = 0

        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp
        
        return t1
        