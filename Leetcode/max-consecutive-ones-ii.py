from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        k = 1
        
        best = 0
        
        subs = 0

        slow = 0
        fast = -1

        while fast < len(nums) - 1:

            # Have exceeded limit of subs?
            if subs > k:
                # contract
                if nums[slow] == 0:
                    subs -= 1
                slow += 1
            else:
                # expand
                fast += 1
                if nums[fast] == 0:
                    subs += 1
                if subs <= k:
                    # track
                    best = max(best, fast - slow + 1)
        
        return best


        

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,0,1,1,0]))
    print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))