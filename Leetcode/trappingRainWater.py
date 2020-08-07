from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        ans = 0
        size = len(height)

        leftMax = [0] * size
        rightMax = [0] * size

        ### find leftMax of each space

        # There is no left wall to the left of the leftmost space
        leftMax[0] = height[0]

        # Start at second to first 
        for i in range(1, size):
            # print(i)
            leftMax[i] = max(leftMax[i-1], height[i])

        ### find rightMax of each space

        # There is no right wall to the right of the rightmost space
        rightMax[size-1] = height[size-1]

        # Start at second to last 
        for i in reversed(range(size-1)):
            # print(i)
            rightMax[i] = max(rightMax[i+1], height[i])

        ### Add the water contained over each space
        for i in range(size):
            ans += min(leftMax[i], rightMax[i]) - height[i]

        return ans        

if __name__ == "__main__":
    s = Solution()
    in1 = list([0,1,0,2,1,0,1,3,2,1,2,1]) #6
    print(s.trap(in1))
