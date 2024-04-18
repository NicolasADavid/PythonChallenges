from typing import List

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max(c.keys(), key=c.get)

print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))