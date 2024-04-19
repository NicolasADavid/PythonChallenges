from typing import List

class Solution:

    def maxDistance(self, arrays: List[List[int]]) -> int:

        minsofar = float("inf")
        maxsofar = float("-inf")
        best = float("-inf")

        for i, a in enumerate(arrays):

            amax = a[-1]
            amin = a[0]


            if i != 0:
                # try best with min of a
                best = max(best, abs(maxsofar - amin))
                # try best with max of a
                best = max(best, abs(amax - minsofar))
            
            minsofar = min(minsofar, a[0])
            maxsofar = max(maxsofar, a[-1])

        return best
            
print(Solution().maxDistance([[1,2,3],[4,5],[1,2,3]])) #4
print(Solution().maxDistance([[1,4],[0,5]])) #4
print(Solution().maxDistance([[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]])) #14

        