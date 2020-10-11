from typing import List

class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     output = [[]]
        
    #     for num in nums:
    #         output += [curr + [num] for curr in output]
        
    #     return output

    # WRONG
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     output = []
    #     seen = set()

    #     # Pass in nums like [1, 2, 3]
    #     # Swap with idx each element past idx
    #         # [1, 2, 3]
    #         # [2, 1, 3]
    #         # [3, 2, 1]
    #     # Backtrack with idx + 1
    #     # When idx == target, append avail[-target:] to output    

    #     def backtrack(curr, target, idx):
    #         # check solution
    #         if idx == target:
    #             # [1, > 2, 3]
    #             # if curr[n-target:] not in seen:
    #             #     print("WARNING")    
    #             output.append(curr[:target])
    #             return

    #         # swap each el in curr after idx with el at idx
    #         for i in range(idx, len(curr)): #if idx = 1, len(curr) = 3, -> [1, 2, 3]
    #             #swap
    #             curr[idx], curr[i] = curr[i], curr[idx]
    #             #backtrack
    #             backtrack(curr, target, idx+1)
    #             #unswap
    #             curr[idx], curr[i] = curr[i], curr[idx]
        
    #     for i in range(len(nums)+1): # 0, 1, 2, 3
    #         backtrack(nums, i, 0)

    #     return output


    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # start with an empty list in the output
        output = [[]]
        
        # for each num, add num to every element in output
        for num in nums:
            # add to output
            # a list of every element in curr with num appended
            output += [curr + [num] for curr in output]
        
        return output
        
s = Solution()
print(s.subsets([1,2,3]))