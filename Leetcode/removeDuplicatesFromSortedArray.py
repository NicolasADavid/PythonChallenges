from typing import List

class Solution:

    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0

        i = 0
        for j in range(len(nums)):
            if(nums[j] != nums[i]):
                i+=1
                nums[i] = nums[j]

        return i+1
    
if __name__ == "__main__":
    # solution = Solution()
    arr1 = [1,2,2,3]
    r = Solution.removeDuplicates(arr1)
    print(arr1)
    print(r)
