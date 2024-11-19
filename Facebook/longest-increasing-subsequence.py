'''
Longest Increasing Subsequence

Given an array of integers, return an integer representing the length of the longest increasing subsequence.
 

EXAMPLE(S)
[1, 2, 3] => 3 (whole array)
[5, 1, 4, 2, 3] => 3 ([1, 2, 3] is the longest increasing subsequence)
 

FUNCTION SIGNATURE
function longestIncreasingSubSequenceLength(sequence: [Int]) -> Int:
'''

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        b = 1

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    b = max(b, dp[i])

        return b

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(Solution().lengthOfLIS([0,1,0,3,2,3])) # 4
print(Solution().lengthOfLIS([7,7,7,7,7,7,7])) # 1

    


