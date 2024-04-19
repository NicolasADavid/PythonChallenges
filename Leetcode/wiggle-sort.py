from typing import List
from collections import deque
class Solution:
    # def wiggleSort(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     nums.sort()
    #     dq = deque(nums)

    #     ans = deque()


    #     # start with min
    #     ans.append(dq.popleft())

    #     # start added max
    #     maxdir = True
    #     first = True

    #     while dq:
    #         if maxdir:
    #             if first:
    #                 ans.append(dq.pop())
    #                 first = False
    #             else:
    #                 ans.appendleft(dq.pop())
    #                 first = True
    #                 maxdir = False
    #         else:
    #             if first:
    #                 ans.append(dq.popleft())
    #                 first = False
    #             else:
    #                 ans.appendleft(dq.popleft())
    #                 first = True
    #                 maxdir = True
    #     nums = list(dq)
    #     return
    
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)

        def swap(i):
            nums[i], nums[i+1] = nums[i+1], nums[i]

        for i in range(n-1):
            if i % 2 == 0 and nums[i] > nums[i+1]:
                swap(i)
            elif i % 2 == 1 and nums[i] < nums[i+1]:
                swap(i)
        
        return







Solution().wiggleSort([3,5,2,1,6,4])
Solution().wiggleSort([6,6,5,6,3,8])