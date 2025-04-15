
# # https://leetcode.com/problems/sort-colors/
# Input: nums = [2,0,2,1,1,0]

'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Plan:

Left pointer    (where 0 should go)
Mid pointer     (where 1 should go)
Right pointer   (where 2 should go)

while mid less than right:
    If 1, increment mid
    If 0, swap left and mid, increment left
    If 2, swap right and mid, decrement right


Input: nums = [0,1,2,1,1,0]
Input: nums = [0,1,0,1,1,2]
Input: nums = [2,0,2,1,1,0]
Input: nums = [2,0,2,1,1,2]
               ^       ^
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
            
        left = 0
        mid = 0
        right = len(nums) - 1

        while mid <= right:

            if nums[mid] == 0:
                # swap left and mid
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1

                # If left exceeded mid (first swap), increment mid
                if left > mid:
                    mid += 1

            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                # swap right and mid
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        
        return nums

# assert Solution().sortColors([2,0,2,1,1,2]) == [0, 1, 1, 2, 2, 2]
# assert Solution().sortColors([0,1,2,1,1,0]) == [0, 0, 1, 1, 1, 2]
assert Solution().sortColors([2,0,1]) == [0, 1, 2]