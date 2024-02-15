from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        best = window = 0
        r = -1
        l = 0
        
        if len(nums) < k:
            return 0
        
        # add k to window
        while r - l + 1 < k:
            r += 1
            window += nums[r]
        
        best = max(best, window/k)

        # slide window
        while r < len(nums) - 1:
            #subtract nums[l]
            #incr l
            window -= nums[l]
            l += 1

            #incr r
            #add nums[r]
            r += 1
            window += nums[r]

            #track best
            best = max(best, window/k)

        return best
        

if __name__ == "__main__":

    s = Solution()

    r = s.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)
    print(r)

    
    r = s.findMaxAverage(nums = [5], k = 1)
    print(r)