from typing import List

'''
Given an integer array nums of unique elements, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        answers = []

        def helper(options: List[int], selections: List[int], index):

            if index == len(options):
                answers.append(selections.copy())
                return

            # include option at index
            selections.append(options[index])
            helper(options, selections, index+1)

            # remove option
            selections.pop()

            # omit option at index
            helper(options, selections, index+1)

        helper(nums, [], 0)

        return answers
    
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output

    
    def subsets_slicing(self, nums):
        result = []

        # DFS function to generate subsets.
        def dfs(nums, path, result):
            result.append(path)

            # Iterate over remaining elements in nums
            for i in range(len(nums)):
                # Recursively call the dfs function with the remaining elements
                dfs(nums[i + 1:], path + [nums[i]], result)

        # Generate subsets, starting with an empty path.
        dfs(nums, [], result)
        return result
    
    def subsets_no_slice(self, nums):
        result = []
        n = len(nums)

        # DFS function to generate subsets.
        def dfs(start, path):
            # append the subset denoted by path
            result.append(path)
            
            # iterate over the indexes from 'start' to the end of the array
            for i in range(start, n):
                # dfs for the remaining part of the array
                dfs(i + 1, path + [nums[i]])

        # Generate subsets, starting with an empty path.
        dfs(0, [])
        return result
    

# print(Solution().subsets_slicing([1,2,3]))
print(Solution().subsets_no_slice([1,2,3]))
        