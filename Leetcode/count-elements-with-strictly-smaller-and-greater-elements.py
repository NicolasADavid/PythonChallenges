class Solution:
    def countElements(self, nums: List[int]) -> int:
        low, high, c = None, None, 0

        for num in nums:
            if low is None:
                low = num
            if high is None:
                high = num
            
            if low > num:
                low = num
            if high < num:
                high = num

        for num in nums:
            if num > low and num < high:
                c = c + 1
        
        return c