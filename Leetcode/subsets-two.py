from typing import List

class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # start with an empty list in the output
        output = [[]]
        
        # for each num, add num to every element in output
        for num in nums:
            # add to output
            for curr in output.copy():
                new = curr.copy() + [num]
                output += [new]
        
        return output
        
s = Solution()
print(s.subsets([1,2,3]))