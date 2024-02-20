from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        slow = fast = 0
        best = 0
        ones = 0

        while fast < len(nums):
            if nums[fast] == 1:
                ones += 1
                best = max(best, ones)
            else:
                ones = 0
            fast += 1

        return best

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(s.findMaxConsecutiveOnes([1, 0, 1, 0, 1, 1,]))
    print(s.findMaxConsecutiveOnes([1, 0, 1, 0, 1,]))
    print(s.findMaxConsecutiveOnes([0, 0]))