from typing import List

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:

    #     slow = fast = 0

    #     while(fast < len(nums)):

    #         #Put slow on a zero
    #         while(slow < len(nums) and nums[slow] != 0):
    #             slow += 1

    #         #Put fast on a non-zero
    #         while(fast < len(nums) and nums[fast] == 0):
    #             fast += 1

    #         #swap
    #         if(fast < len(nums) and slow < fast):
    #             nums[slow], nums[fast] = nums[fast], nums[slow]

    #         if(fast == len(nums) or slow == len(nums)):
    #             break

    #         fast += 1

    def moveZeroes(self, nums: List[int]) -> None:

        s = 0

        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[s], nums[i] = nums[i], nums[s]
                s += 1

        return nums

if __name__ == "__main__":
    s = Solution()

    in1 = [0,1,0,3,12]
    # in1 = [1,0]
    s.moveZeroes(in1)