from typing import List

class Solution:
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # start with an empty list in the output
        output = [[]]
        seen = set()
        
        # for each num, add num to every element in output
        # O(n)t
        for num in nums:

            # add to output
            for curr in output.copy():

                #O(n)t O(n)s
                new = curr.copy() + [num]

                #O(nlgn)t -> n^2 ??
                new.sort()
                
                #O(n)t
                t = tuple(new)

                #O(1)t
                if t in seen:
                    continue

                #O(1)t
                seen.add(t)

                output += [new]
        
        return output
        
s = Solution()
print(s.subsetsWithDup([1,2,3,3]))