class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        best = float('-inf')
        current = 0

        for num in nums:
            if current < 0:
                current = 0
            current += num
            best = max(best, current)
            
        return best