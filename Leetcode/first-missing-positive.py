from typing import List

class Solution:

    # Unsorted int array
    # Find the smallest missing positive integer
    # Strive for O(n) time and constant space
    # 1 is the smallest possible positive integer

    # discard numbers that are less than 1 or greater than len(nums)
    # put numbers to keep where they would go in sorted order
    # find first number missing from the array after processing

    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1

        # discard numbers x < 1 or x > len(nums)
        # put the number where it would go if the array was filled perfectly
        # Take the number there and try to put it as well
        def putWell(put: int):
            # Discard
            if not put or put < 1 or put > len(nums):
                return

            # Already in place
            if nums[put-1] == put:
                return

            # Put in place, handle displaced
            take = nums[put-1]
            nums[put-1] = put
            putWell(take)


        for i in range(len(nums)):
            take = nums[i]
            nums[i] = None
            putWell(take)

        for i in range(len(nums)):
            if nums[i] is None:
                return i+1

        return len(nums) + 1