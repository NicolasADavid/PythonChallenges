from typing import List
import math
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
        
#         # Move z to the index of the first number that is not negative, may be last number
#         z = 0
#         while nums[z] < 0 and z < len(nums) - 1:
#             z += 1
        
#         if z == 0:
#             return [int(math.pow(n, 2)) for n in nums]
#         else:
#             # Split array into negative numbers and non-negative numbers
#             a = nums[0:z]
#             b = list(reversed(nums[z:]))
#             r = []
#             while a or b:
#                 if a and b:
#                     if abs(a[-1]) < b[-1]:
#                         r.append(int(math.pow(a.pop(), 2)))
#                     else:
#                         r.append(int(math.pow(b.pop(), 2)))
#                 elif a:
#                     while a:
#                         r.append(int(math.pow(a.pop(), 2)))
#                 elif b:
#                     while b:
#                         r.append(int(math.pow(b.pop(), 2)))
#             return r
class Solution:

    def sortedSquares(self, A):

        N = len(A)
        # i, j: negative, positive parts
        
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans