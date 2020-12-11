from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False

        
        goingUp = True

        if arr[0] > arr[1]:
            return False

        for i in range(0, len(arr)):

            curr = arr[i]
            next = arr[i+1] if i < len(arr) - 1 else -1

            if curr == next:
                return False

            if goingUp:
                if next < curr:
                    goingUp = False
            else:
                if next > curr:
                    return False

        if arr[-2] < arr[-1]:
            return False

        return True

# class Solution(object):
#     def validMountainArray(self, A):
#         N = len(A)
#         i = 0

#         # walk up
#         while i+1 < N and A[i] < A[i+1]:
#             i += 1

#         # peak can't be first or last
#         if i == 0 or i == N-1:
#             return False

#         # walk down
#         while i+1 < N and A[i] > A[i+1]:
#             i += 1

#         return i == N-1

if __name__ == "__main__":
    # print(Solution().validMountainArray([0,3,2,1])) # True
    print(Solution().validMountainArray([0,1,2,3,4,5,6,7,8,9])) # False