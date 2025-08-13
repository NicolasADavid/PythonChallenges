# Backtracking
# class Solution:
#     def canJumpFromPosition(self, position, nums):
#         if position == len(nums) - 1:
#             return True
#         furthestJump = min(position + nums[position], len(nums) - 1)
#         for nextPosition in range(position + 1, furthestJump + 1):
#             if self.canJumpFromPosition(nextPosition, nums):
#                 return True
#         return False

#     def canJump(self, nums):
#         return self.canJumpFromPosition(0, nums)


# DP topdown
class Solution:
    def __init__(self):
        self.memo = []
        self.nums = []

    def canJumpFromPosition(self, position):
        if self.memo[position] != -1:
            return self.memo[position] == 1
        furthestJump = min(position + self.nums[position], len(self.nums) - 1)
        for nextPosition in range(position + 1, furthestJump + 1):
            if self.canJumpFromPosition(nextPosition):
                self.memo[position] = 1
                return True
        self.memo[position] = 0
        return False

    def canJump(self, nums):
        self.nums = nums
        self.memo = [-1] * len(nums)  # -1 for unknown, 0 for bad, 1 for good
        self.memo[-1] = 1  # The last position is always "good"
        return self.canJumpFromPosition(0)
    
# DP Bottom-up
# class Solution(object):
#     def canJump(self, nums):
#         GOOD, BAD, UNKNOWN = 1, 0, -1
#         memo = [UNKNOWN] * len(nums)
#         memo[-1] = GOOD
#         for i in range(len(nums) - 2, -1, -1):
#             furthest_jump = min(i + nums[i], len(nums) - 1)
#             for j in range(i + 1, furthest_jump + 1):
#                 if memo[j] == GOOD:
#                     memo[i] = GOOD
#                     break
#         return memo[0] == GOOD

if __name__ == "__main__":
    assert Solution().canJump([2, 3, 1, 1, 4])
    assert not Solution().canJump([3, 2, 1, 0, 4])
    assert Solution().canJump([0])
    assert Solution().canJump([1, 0])
    assert Solution().canJump([2, 0])
    assert Solution().canJump([2, 5, 0, 0])