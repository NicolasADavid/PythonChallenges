from sortedcontainers import SortedList

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """


from sortedcontainers import SortedList


class SolutionSortedContainers(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        set_ = SortedList()
        for i in range(len(nums)):
            # Find the successor of current element
            idx = set_.bisect_left(nums[i])
            if idx != len(set_) and set_[idx] <= nums[i] + t:
                return True

            # Find the predecessor of current element
            if idx > 0 and nums[i] <= set_[idx - 1] + t:
                return True

            set_.add(nums[i])
            if len(set_) > k:
                set_.remove(nums[i - k])

        return False
    
import bisect
class SolutionSortedContainers2(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        s = SortedList()

        for i, n in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])

                pos1 = bisect.bisect_left(s, n-t)

            if s and (s[-1] - n <= t or n - s[0] <= t):
                return True

            s.add(n)



class SolutionBucket(object):
    # Get the ID of the bucket from element value x and bucket width w
    # Division '/' in Python with '//' performs floor division, which is necessary for correct bucketing.
    def getID(self, x, w):
        return (
            x // w
        )  # Floor division to handle both positive and negative integers correctly

    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):

        k = indexDiff
        t = valueDiff
        
        if t < 0:
            return False
        buckets = {}
        w = t + 1  # Increment by 1 to handle the range correctly
        for i in range(len(nums)):
            bucket = self.getID(nums[i], w)
            # Check if current bucket is empty, each bucket may contain at most one element
            if bucket in buckets:
                return True
            # Check the neighbor buckets for almost duplicates
            if bucket - 1 in buckets and abs(nums[i] - buckets[bucket - 1]) < w:
                return True
            if bucket + 1 in buckets and abs(nums[i] - buckets[bucket + 1]) < w:
                return True
            # Now bucket is empty and no almost duplicates in neighbor buckets
            buckets[bucket] = nums[i]
            if i >= k:
                del buckets[self.getID(nums[i - k], w)]
        return False
    
# assert SolutionBucket().containsNearbyAlmostDuplicate(nums = [1,2,3,1], indexDiff = 3, valueDiff = 0) == True
# assert SolutionBucket().containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 0) == False




"""
Initialize a hashmap of buckets, where the key is the bucket ID and the value is the element in that bucket.
An elements bucket ID is calculated by dividing the elements value by the bucket width.

TODO: Why??? The bucket width is set to t + 1 to ensure that the range of values in each bucket is t.

For each element in the array, calcuate its bucket ID and check if the bucket is already occupied.
If the bucket is occupied, return True.
If the bucket is not occupied, check the neighboring buckets (bucket - 1 and bucket + 1) to see if they are occupied.
If either of the neighboring buckets is occupied, check if the absolute difference between the current element and the element in the neighboring bucket is less than or equal to t.
If so, return True.
If none of the conditions are met, add the current element to its bucket.
If the number of elements in the hashmap exceeds k, remove the oldest element from the hashmap. Remove nums[current index - k] from the hashmap.
If conditions are not met once all elements have been checked, return False.
"""
class MySolutionBucket():
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):

        def getID(x, w):
            return x // w
        
        buckets = {}

        w = valueDiff + 1

        for i in range(len(nums)):
            element = nums[i]
            id = getID(element, w)

            # Check if the current bucket is already occupied
            if id in buckets:
                return True
            # Check the neighboring buckets
            if id - 1 in buckets and abs(element - buckets[id - 1]) <= valueDiff:
                return True
            if id + 1 in buckets and abs(element - buckets[id + 1]) <= valueDiff:
                return True
            # Add the current element to its bucket
            buckets[id] = element
            # Remove the oldest element from the hashmap if it exceeds indexDiff
            if i >= indexDiff:
                del buckets[getID(nums[i - indexDiff], w)]

        return False
    
assert MySolutionBucket().containsNearbyAlmostDuplicate(nums = [1,2,3,1], indexDiff = 3, valueDiff = 0) == True
assert MySolutionBucket().containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3) == False
assert MySolutionBucket().containsNearbyAlmostDuplicate(nums = [1,3,5,9,1,5,9], indexDiff = 2, valueDiff = 3) == True

        