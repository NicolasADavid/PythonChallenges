class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        n = len(arr)

        current = 1
        index = 0

        # Until we find k of missing numbers
        while k > 0:

            # If index is valid and current is equal to arr[index]
            if index < n and arr[index] == current:
                # Not a missing number
                index += 1
            else:
                # Missing number found
                k -= 1

            current += 1

        return current - 1