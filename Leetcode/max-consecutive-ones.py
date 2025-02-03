class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        run = 0
        best = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                run += 1
                best = max(best, run)
            else:
                run = 0
        
        return best
