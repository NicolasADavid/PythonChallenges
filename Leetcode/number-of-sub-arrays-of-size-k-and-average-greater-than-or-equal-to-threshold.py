# number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
from typing import List

# Every element is added and subtracted from average at most twice: O(n)t
# Create a constant number of variables: O(1)s
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        n = len(arr)

        # If cannot reach window of size k, return 0
        if k > n:
            return 0

        avg = 0 # average of elements in window
        res = 0 # number of solutions

        # Expand window to size k, accumulating average
        for i in range(k):
            avg += arr[i]
        avg = avg/k

        left = 0
        while left + k <= n:

            # Check average
            if avg >= threshold:
                res += 1

            if left + k >= n:
                break

            # Slide window by subtracting (expunged number / k) and adding (inserted number / k)
            avg += ( -(arr[left]) + arr[left+k]) / k

            left += 1
        
        return res

if __name__ == "__main__":
    s = Solution()

    s.numOfSubarrays([1,1,1,1,1], 1, 0)