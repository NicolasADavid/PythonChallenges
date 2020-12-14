from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Numbers can appear at most twice

        lastNum = None
        lastNumUsedTwice = False
        placeAt = 0

        for num in nums:

            # Num is brand new
            if num != lastNum:
                lastNumUsedTwice = False

            # Num has been seen before
            else:

                # Twice
                if not lastNumUsedTwice:
                    lastNumUsedTwice = True

                # Thrice +
                else:
                    continue
            
            lastNum = num
            nums[placeAt] = num
            placeAt += 1

        return placeAt

if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,1,2,2,3]))
