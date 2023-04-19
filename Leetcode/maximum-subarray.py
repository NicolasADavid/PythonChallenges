from typing import List, Set

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        s, bs = None, None

        for num in nums:

            if s is None:
                s = bs = num
            else:
                if num > s and s < 0:
                    # reset
                    s = num
                else:
                    # add num to sum
                    s = s + num

            if s > bs:
                bs = s

        return bs
    
if __name__ == "__main__":
    solution = Solution()
    # r = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    # print(r)
    # r = solution.maxSubArray([5,4,-1,7,8])
    # print(r)
    # r = solution.maxSubArray([-1,0,-2])
    # print(r)
    r = solution.maxSubArray([1,2])
    print(r)