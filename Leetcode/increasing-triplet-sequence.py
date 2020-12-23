from typing import List
class Solution:

    #T O(N) S O(N)
    # def increasingTriplet(self, nums: List[int]) -> bool:
        
    #     mins = []
    #     maxs = []

    #     low = nums[0]
    #     for n in nums:
    #         low = min(low, n)
    #         mins.append(low)

    #     high = nums[len(nums)-1]
    #     for n in reversed(nums):
    #         high = max(high, n)
    #         maxs.append(high)
        
    #     maxs = list(reversed(maxs))

    #     for idx, i in enumerate(nums):
    #         if mins[idx] < i < maxs[idx]:
    #             return True

    #     return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False

    # """
    # Idea: iterate over nums
    # Keep track of the first min and second min and basically just look for the third min
    # so basically keep 1 & 2 and look for 3
    # never update two before 1 if both 1 & 2 are less than the current value
    # TC: O(n) where n is the # of elements in nums
    # Space: O(1) we only keep two int variables at once
    # """
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     one, two = None, None

    #     for n in nums:
    #         print(n)
    #         if one is None or n <= one:
    #             one = n
    #         elif two is None or n <= two:
    #             two = n
    #         elif n > two:
    #             return True
            
    #     return False

if __name__ == "__main__":
    print(Solution().increasingTriplet([2,1,5,0,3,4]))