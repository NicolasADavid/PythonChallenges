from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max = 0
        l = 0
        r = len(height)-1

        while (l < r):

            new = min(height[l], height[r])*(r-l)

            if(new > max):
                max = new
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1

        return max 
                
if __name__ == "__main__":
    s = Solution()

    in1 = [1,8,6,2,5,4,8,3,7] #49
    print(s.maxArea(in1))