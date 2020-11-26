# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
from typing import List
from collections import defaultdict
import heapq

class Solution:

    def isPossible(self, nums: List[int]) -> bool:

        # O(n)s, potentially one list for every input num
        map = defaultdict(list)
        tb = 0 # tiebreaker

        # O(n)t
        
        for num in nums:

            # If len(map[num]), pop target from map[num], insert num to target, append to map[num+1]
            # If not len(map[num]), create new list, append to map[num+1]
            # Maintain map target lists sorted by length of targets. Want to insert nums into shortest lists.

            if not len(map[num]):
                # TargetSet is empty
                # insert new target to TargetSet of map[num+1].
                nt = (1, tb, [num])
                tb += 1
                heapq.heappush(map[num+1], nt)
            else:
                # pop target of min length from TargetSet
                # O(n) * O(lgn) t
                t = heapq.heappop(map[num])
                nt = (
                    t[0] + 1,               # inc size
                    t[1],                   # tiebreaker
                    t[2] + [num]            # add num
                )
                # O(n) * O(lgn) t
                heapq.heappush(map[num+1], nt)

        # Check accumulated target lists' lengths
        # O(n)t
        for targetSet in map.values():
            for target in targetSet:
                if target[0] < 3:
                    return False

        return True

if __name__ == "__main__":
    s = Solution()
    s.isPossible([1,2,3,3,4,5]) # true