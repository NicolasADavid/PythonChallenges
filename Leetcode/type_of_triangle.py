class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        total = sum(nums)
        m = max(nums)

        if total - m <= m:
            return "none"

        eq = total / 3
        
        if eq == nums[0] and eq == nums[1] and eq == nums[2]:
            return "equilateral"
        
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"
        
        return "scalene"