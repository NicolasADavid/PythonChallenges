from typing import List
import bisect

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        # Binary search to find the closest element
        right = bisect.bisect_left(arr, x)
        left = right - 1

        # Two pointers to find the k closest elements
        while k > 0:
            if right < len(arr) and (left < 0 or abs(arr[right] - x) < abs(arr[left] - x)):
                right += 1
            else:
                left -= 1
            k -= 1

        return arr[left + 1:right]
    
if __name__ == "__main__":
    # arr = [1, 2, 3, 4, 5]
    # k = 4
    # x = 3
    # print(Solution().findClosestElements(arr, k, x))  # Output: [1, 2, 3, 4]
    
    # arr = [1, 2, 3, 4, 5]
    # k = 4
    # x = -1
    # print(Solution().findClosestElements(arr, k, x))  # Output: [1, 2, 3, 4]
    
    # arr = [1, 2, 3, 4, 5]
    # k = 4
    # x = 6
    # print(Solution().findClosestElements(arr, k, x))  # Output: [2, 3, 4, 5]
    
    arr = [1]
    k = 1
    x = 1
    print(Solution().findClosestElements(arr, k, x))  # Output: [1]