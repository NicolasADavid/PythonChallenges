from typing import List

class Solution:
    # O(N) S(1)
    # def searchInsert(self, nums: List[int], target: int) -> int:

    #     idx = -1

    #     if(not nums):
    #         return 0

    #     for i in range(len(nums)):
    #         if nums[i] >= target:
    #             idx = i
    #             break
        
    #     if (idx == -1):
    #         return len(nums)
    #     else:
    #         return idx

    # O(logN) S(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        if nums[left] < target:
            return left + 1
        else:
            return left



if __name__ == "__main__":
    solution = Solution()

    # arr1 = [1,2,3,5]
    # arr1 = [1,3,5,6]

    # r = solution.searchInsert(arr1, 2)

    # print(arr1)
    # print(r)

    # Example 1:

    # # Input:
    # nums = [1,3,5,6]
    # target = 5
    # # Output: 2

    # r = solution.searchInsert(nums, target)
    # print("nums: ", nums)
    # print("target: ", target)
    # print("r: ", r)


    # Example 2:

    # Input:
    nums = [1,3,5,6]
    target = 2
    r = solution.searchInsert(nums, target)
    print("nums: ", nums)
    print("target: ", target)
    print("r: ", r)
    # Output: 1

    # # Example 3:

    # # Input:
    # nums = [1,3,5,6]
    # target = 7
    # r = solution.searchInsert(nums, target)
    # print("nums: ", nums)
    # print("target: ", target)
    # print("r: ", r)
    # # Output: 4

