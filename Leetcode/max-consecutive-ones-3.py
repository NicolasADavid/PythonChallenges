class Solution(object):

    # Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

    def longestOnes(self, nums, k):

        """
        :type nums: List[int]
        :rtype: int
        """

        best = 0
        replaced = 0

        left = 0
        right = -1

        while right < len(nums) - 1:

            if replaced <= k:
                right += 1

                if nums[right] == 0:
                    replaced += 1

                if replaced <= k:
                    best = max(best, right - left + 1)
            else:
                if nums[left] == 0:
                    replaced -= 1
                left += 1

        return best