class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        # Find first decreasing element, from right
        i = n - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        # first decreasing element at i or i == -1
        if i >= 0:

            # Find first element larger than first decreasing element, from right
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Swap
            self.swap(nums, i, j)

        # reverse everything following index of left swapped index
        self.reverse(nums, i + 1)

    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

if __name__ == "__main__":
    nums = [1, 2, 3]
    s = Solution()
    s.nextPermutation(nums)
    print(nums)  # Output: [1, 3, 2]