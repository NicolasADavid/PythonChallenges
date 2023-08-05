from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:
        l, r, best = 0, len(height) - 1, 0 

        while l < r:

            new = min(height[l], height[r]) * (r - l)

            best = max(best, new)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return best

if __name__ == "__main__":
    s = Solution()

    in1 = [1,8,6,2,5,4,8,3,7] #49
    print(s.maxArea(in1))