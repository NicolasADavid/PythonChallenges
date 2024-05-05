from typing import List
from collections import deque
class Solution:
    def findPermutation(self, s: str) -> List[int]:

        n = len(s) + 1

        q = [x for x in range(1, n+1)]
        q.reverse()
        stack = []
        ans = []
        
        for c in s:
            stack.append(q.pop())
            if c == "I":
                while stack:
                    ans.append(stack.pop())
            else:
                pass
        else:
            stack.append(q.pop())
        
        while(stack):
            ans.append(stack.pop())

        return ans
        

if __name__ == "__main__":
    print(Solution().findPermutation("I"))
    print(Solution().findPermutation("DI"))