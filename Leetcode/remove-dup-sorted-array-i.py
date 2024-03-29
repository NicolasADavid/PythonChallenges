from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        p1 = p2 = 0
        seen = set()

        # p2 is looking
        # p1 is writing

        for _ in range(len(nums)):
            if nums[p2] not in seen:
                #write nums[p2] to nums[p1]
                seen.add(nums[p2])
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return p1
        

# if __name__ == "__main__":
#     print(Solution().removeDuplicates([1,1,2]))