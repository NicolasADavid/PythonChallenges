from typing import List
import heapq
from collections import Counter, defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # Count number of instances of each integer
        # count = Counter(arr)
        # count unique integers

        # Insert int and counts to a minheap

        # while k, remove items from minheap, decrease count of unique integers for every 
        # item in the heap that appears k or less times, reducing k by the number of times
        # the number appeared

        # uniques = 0
        counts = defaultdict(int)

        # Count appearances of each num
        for num in arr:
            counts[num] = counts[num] + 1

        uniques = len(counts.keys())

        minH = []

        items = counts.items()

        for key, value in items:
            heapq.heappush(minH, (value, key))

        while k > 0:
            item = heapq.heappop(minH)

            if item[0] > k:
                break

            k -= item[0]
            uniques -= 1

        return uniques


if __name__ == "__main__":
    s = Solution()

    v = s.findLeastNumOfUniqueInts([4, 4, 3, 1, 2, 1, 1, 7, 8, 4, 5, 5, 4, 3], 4)
    print(v)
        



