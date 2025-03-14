# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        counts = defaultdict(int)

        l = 0
        r = -1

        while r < len(nums) - 1:

            if r - l < k:

                # Increment right pointer
                r += 1

                new = nums[r]

                # Check if new number has match in window
                counts[new] += 1
                if counts[new] > 1:
                    return True

            else:

                # Increment left pointer
                old = nums[l]
                counts[old] -= 1
                l += 1

        return False

        