from typing import List
from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        p1 = p2 = 0
        seen = defaultdict(int)

        # p2 is looking
        # p1 is writing

        for _ in range(len(nums)):
            if seen[nums[p2]] != 2:
                #write nums[p2] to nums[p1]
                seen[nums[p2]] += 1
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return p1
        

# if __name__ == "__main__":
#     print(Solution().removeDuplicates([1,1,1,2,2,3]))