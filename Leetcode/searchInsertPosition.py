from typing import List

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:

        idx = -1

        if(not nums):
            return 0

        for i in range(len(nums)):
            if nums[i] >= target:
                idx = i
                break
        
        if (idx == -1):
            return len(nums)
        else:
            return idx

    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     return len(list(filter(lambda x: x < target, nums)))


if __name__ == "__main__":
    solution = Solution()

    # arr1 = [1,2,3,5]
    arr1 = [1,3,5,6]

    r = solution.searchInsert(arr1, 2)

    print(arr1)
    print(r)
