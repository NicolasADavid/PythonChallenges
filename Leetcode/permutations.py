from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first = 0):

            # if first is at the end of nums, append to out a copy of what is in nums
            if first == n: out.append(nums[:])

            # for each num after first
            # swap num with first
            # backtrack with first+1
            # un-swap
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        out = []
        backtrack()
        return out

if __name__ == "__main__":
    s = Solution()
    input = [1,2,3]

    print(s.permute(input))