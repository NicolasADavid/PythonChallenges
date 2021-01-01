from typing import List

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        best = 0

        def getHeight(item):
            return item[0]
        def getWidth(item):
            return item[1]
        
        for h in heights:

            inheritWidth = 0
            
            # Discard items in the stack with a height exceeding h. Track best before discarding.
            while stack and getHeight(stack[-1]) >= h:

                item = stack.pop()

                #Track best
                best = max(best, getHeight(item) * (getWidth(item)+inheritWidth))

                #Track width being discarded
                inheritWidth += getWidth(item)

            #Add width to new item    
            stack.append((h, 1 + inheritWidth))

        inheritWidth = 0
        while stack:
            item = stack.pop()
            best = max(best, getHeight(item) * (getWidth(item) + inheritWidth))
            inheritWidth += getWidth(item)
        
        return best

if __name__ == "__main__":

    # Solution().largestRectangleArea
    Solution().largestRectangleArea([2,1,5,6,2,3])