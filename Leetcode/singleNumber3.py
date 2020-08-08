from typing import List
from collections import defaultdict

class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:

        numDict = defaultdict(lambda: 0) # O(n)s

        ans = []

        for val in nums: # O(n)c
            numDict[val] += 1

        for i, k in enumerate(numDict): # O(n)c
            val = numDict[k]
            # print("i: %s, k: %s, x: %s" % (i, k, val))
            if(val == 1):
                ans.append(k)

        return ans
            

if __name__ == "__main__":
    s = Solution()

    input = [1, 1, 2, 3, 4, 4] # [2, 3]
    r = s.singleNumber(input)
    
    for x in r:
        print(x)