# 198. House Robber

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        t1 = 0
        t2 = 0

        for num in nums:
            temp = t1

            t1 = max(
                t1,      # steal from the previous house
                num+t2 # steal from this house.
            )

            t2 = temp     # Track how much could have been stolen from the previous house
        
        return t1
    


# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         dp = [0] * (len(nums) + 1)
#         dp[1] = nums[0]
#         for i in range(2, len(nums) + 1):
#             dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
#         return dp[-1]

class SolutionDP(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [0] * (len(nums) + 1)

        # Rob the first house
        dp[1] = nums[0]

        # Iterate through the houses
        for i in range(2, len(nums) + 1):
            # Choose the maximum between robbing the current house and not robbing it
            # dp[i - 1] means not robbing the current house
            # dp[i - 2] + nums[i - 1] means robbing the current house
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        
        return dp[-1]
        
        
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    assert Solution().rob(nums) == 4
    assert SolutionDP().rob(nums) == 4

    nums = [2, 7, 9, 3, 1]
    assert Solution().rob(nums) == 12
    assert SolutionDP().rob(nums) == 12

    nums = [0]
    assert Solution().rob(nums) == 0
    assert SolutionDP().rob(nums) == 0
    nums = [1]
    assert Solution().rob(nums) == 1
    assert SolutionDP().rob(nums) == 1
    nums = [2]
    assert Solution().rob(nums) == 2
    assert SolutionDP().rob(nums) == 2
    nums = [1, 2]
    assert Solution().rob(nums) == 2
    assert SolutionDP().rob(nums) == 2
    nums = [2, 1]
    assert Solution().rob(nums) == 2
    assert SolutionDP().rob(nums) == 2
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert Solution().rob(nums) == 5
    assert SolutionDP().rob(nums) == 5