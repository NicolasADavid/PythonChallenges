from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = [1] * len(nums)
        r = [1] * len(nums)

        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]

        for i in reversed(range(0, len(nums)-1)):
            r[i] = r[i+1] * nums[i+1]

        ans = [0] * len(nums)
        for i in range(len(ans)):
            ans[i] = l[i] * r[i]

        return ans

# Input: 
nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

print(Solution().productExceptSelf(nums))