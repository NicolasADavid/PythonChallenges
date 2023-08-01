from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # n1 + n2 = t

        m = {}

        for idx, n in enumerate(nums):
            if target - n in m:
                return [m[target-n], idx]
            else:
                m[n] = idx
        
        raise Exception("Solution not found")
        

print(Solution().twoSum(nums = [2,7,11,15], target = 9))