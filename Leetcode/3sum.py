from typing import List, Set, Tuple

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        threeSolsSet, dupes = set(), set()

        def twoSum(target) -> Set[Tuple[int, int]]:

            twoSolsSet = set()

            numMap = {}

            for idx, num in enumerate(nums):

                # if(numMap[target - num]):
                if(numMap.setdefault(target - num, None)):
                    twoSolsSet.add((num, nums[numMap[target-num]]))

                numMap[num] = idx

            return twoSolsSet

        for idx, num in enumerate(nums):

            if(num not in dupes):

                tuplesForThreeSols = twoSum(-num)

                for (a, b) in tuplesForThreeSols:

                    theNums = [num, a, b]
                    theNumsSorted = sorted(theNums)
                    threeSolsSet.add(tuple(theNumsSorted))

                dupes.add(num)


        return threeSolsSet
    
    def threeSumII(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i == 0 or nums[i] != nums[i-1]:
                self.twoSumII(nums, i, res)

        return res
    
    def twoSumII(self, nums: List[int], i: int, res: List):
        lo, hi = i + 1, len(nums)-1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append((nums[i], nums[lo], nums[hi]))
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
    
        
if __name__ == "__main__":
    solution = Solution()

    i1 = [-1, 0, 1, 2, -1, 4]
    
    print(solution.threeSum(i1))
    print(solution.threeSumII(i1))


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i == 0 or nums[i - 1] != nums[i]:
#                 self.twoSumII(nums, i, res)
#         return res

#     def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
#         lo, hi = i + 1, len(nums) - 1
#         while (lo < hi):
#             sum = nums[i] + nums[lo] + nums[hi]
#             if sum < 0:
#                 lo += 1
#             elif sum > 0:
#                 hi -= 1
#             else:
#                 res.append([nums[i], nums[lo], nums[hi]])
#                 lo += 1
#                 hi -= 1
#                 while lo < hi and nums[lo] == nums[lo - 1]:
#                     lo += 1

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i == 0 or nums[i - 1] != nums[i]:
#                 self.twoSum(nums, i, res)
#         return res

#     def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
#         seen = set()
#         j = i + 1
#         while j < len(nums):
#             complement = -nums[i] - nums[j]
#             if complement in seen:
#                 res.append([nums[i], nums[j], complement])
#                 while j + 1 < len(nums) and nums[j] == nums[j + 1]:
#                     j += 1
#             seen.add(nums[j])
#             j += 1



# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res, dups = set(), set()
#         seen = {}
#         for i, val1 in enumerate(nums):
#             if val1 not in dups:
#                 dups.add(val1)
#                 for j, val2 in enumerate(nums[i+1:]):
#                     complement = -val1 - val2
#                     if complement in seen and seen[complement] == i:
#                         res.add(tuple(sorted((val1, val2, complement))))
#                     seen[val2] = i
#         return res