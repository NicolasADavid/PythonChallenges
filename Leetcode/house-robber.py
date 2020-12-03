
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        t1 = 0
        t2 = 0

        for num in nums:
            temp = t1

            t1 = max(
                t1,         # steal from the previous house
                num+t2      # steal from this house.
            )

            t2 = temp     # Track how much could have been stolen from the previous house
        
        return t1

        