from typing import List
import heapq
from collections import defaultdict

class Solution:
    # Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        h = []

        # O(n)
        for num in nums:
            counts[num] = counts[num] + 1
        
        # O(n)
        for key, value in counts.items():
            # O(logn)
            heapq.heappush(h, (-value, key))
            
        ans = []
        while len(ans) < k and h:
            ans.append(heapq.heappop(h)[1])

        return ans
    

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))

