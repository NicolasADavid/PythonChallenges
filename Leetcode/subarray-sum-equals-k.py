from typing import List
from collections import defaultdict

# class Solution:
    # recursive solution. Gets TLE
    # def subarraySum(self, nums: List[int], k: int) -> int:

    #     def help(nums: List[int], t: int, left: int, right: int, seen: set) -> int:

    #         if (left, right) in seen:
    #             return 0

    #         seen.add((left, right))

    #         # Don't check empty sets
    #         if not nums:
    #             return 0

    #         # Number of subarrays with sums equal to k
    #         r = 0

    #         # If total equals k, this array is a solution
    #         if t == k:
    #             r += 1

    #         # Run help on subarray with leftmost item removed and rightmost item removed
    #         # Adjust total by subtracting the number removed from the array
    #         return (
    #             r + 
    #             help(nums[1:], t - nums[0], left+1, right, seen) + 
    #             help(nums[:-1], t - nums[-1], left, right+1, seen)
    #         )

    #     # Get total sum of all numbers in the input
    #     total = sum(nums)

    #     return help(nums, total, 0, 0, set())

class Solution:

    # nums [ 3, 4, 7, 2,  -3, 1,  4,  2 ]
    # cSum [ 0, 3, 7, 14, 16, 13, 14, 18, 20]
    # Sum of elements between i and j is cumulativesum[j+1] - cumulativesum[i]
    def subarraySum(self, nums: List[int], k: int) -> int:

        count, summ = 0, 0
        sums = defaultdict(int)
        sums[0] = 1

        for num in nums:
            summ += num
            if sums[summ - k] > 0:
                count += sums[summ-k]
            sums[summ] = sums[summ] + 1

        return count

# if __name__ == "__main__":
    # s = Solution()
    # v = s.subarraySum([1,1,1], 2)
    # print(v)

    # v = s.subarraySum([1,2,1,2,1], 3)
    # print(v)

    # v = s.subarraySum([1], 0)
    # print(v)

    # v = s.subarraySum([1,2,3], 3)
    # print(v)

    # v = s.subarraySum([-1,-1,-1], 0)
    # print(v)

