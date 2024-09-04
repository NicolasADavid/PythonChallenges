'''
Given an array where each number is located less than k places away from its sorted position, fully sort the array.
 

EXAMPLE(S)
[1, 3, 4, 2, 6, 5], k = 3
returns [1, 2, 3, 4, 5, 6]
 

FUNCTION SIGNATURE
def k_sort(input, k)
'''

from typing import List
import heapq

def k_sort(arr: List[int], k: int) -> List[int]:

    mh = []
    ans = []

    for element in arr:

        if len(mh) == k:
            # Pops minimum element added so far to mh
            ans.append(heapq.heappop(mh)) 
        
        heapq.heappush(mh, element)

    while mh:
        ans.append(heapq.heappop(mh))

    return ans

assert k_sort([1, 3, 4, 2, 6, 5], k = 3) == [1, 2, 3, 4, 5, 6]

assert k_sort([6, 5, 4, 3, 2, 1], k = 6) == [1, 2, 3, 4, 5, 6]

assert k_sort([1, 2, 1, 2, 1, 2, 1, 2, 1, 2], k = 6) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]