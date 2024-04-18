from typing import List
class Solution:

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     k %= len(nums)
    #     for _ in range(k):
            
    #         prev = nums[-1]
    #         for i in range(n):
    #             take = nums[i]
    #             nums[i] = prev
    #             prev = take

    # def rotate(self, nums: List[int], k: int) -> None:
    #     n = len(nums)
    #     a = [0] * n
    #     for i in range(n):
    #         a[(i + k) % n] = nums[i]
            
    #     nums[:] = a

    # def rotate(self, nums: List[int], k: int) -> None:
    #     # speed up the rotation
    #     k %= len(nums)

    #     for i in range(k):
    #         previous = nums[-1]
    #         for j in range(len(nums)):
    #             nums[j], previous = previous, nums[j]

    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k %= n # mod n because rotating n times has no impact

        # start at 0, track how many placements have been made.
        # when n placements have been made, the array has been rotated completely
        start = count = 0
        
        while count < n:

            current, prev = start, nums[start]

            while True:
                nextIdx = ( current + k ) % n
                
                nums[nextIdx], prev = prev, nums[nextIdx]
                current = nextIdx
                count += 1

                if start == current:
                    break
            start += 1
            
# nums = [i for i in range(1, 8)]
# print(nums)
# Solution().rotate(nums, 3)
# print(nums)

nums = [-1,-100,3,99]
k = 2
print(nums)
Solution().rotate(nums, k)
print(nums)

