from typing import List
from collections import deque
from itertools import permutations
from itertools import combinations
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # return self.generateParenthesisBrute(n)
        return self.generateParenthesisSmart(n)
        # return self.generateParenthesisDivAndConquer(n)

    def generateParenthesisBrute(self, n: int) -> List[str]:

        q = deque([""])
        
        while len(q[0]) < n*2:
            next = q.popleft()
            q.append(next + "(")
            q.append(next + ")")
            
        out = [_  for _ in q if self.isValid(_)]

        ans = []
        for s in q:
            if self.isValid(s):
                ans.append(s)

        return out


    def generateParenthesisSmart(self, n: int) -> List[str]:
        out = []

        def backtrack(s: str, lcount: int, rcount: int) -> None:
            if len(s) == n*2:
                out.append(s)
                return
            if lcount < n:
                backtrack(s+"(", lcount + 1 , rcount)
            if rcount < lcount:
                backtrack(s+")", lcount , rcount + 1)

        backtrack("", 0, 0)

        return out

    def generateParenthesisDivAndConquer(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        
        answer = []
        for left_count in range(n):
            for left_string in self.generateParenthesisDivAndConquer(left_count):
                for right_string in self.generateParenthesisDivAndConquer(n - 1 - left_count):
                    answer.append("(" + left_string + ")" + right_string)
        
        return answer

    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if not stack:
                stack.append(c)
            else:
                top = stack[-1]
                
                if c == ")":
                    if top != "(":
                        return False
                    stack.pop()
                elif c == "]":
                    if top != "[":
                        return False
                    stack.pop()
                elif c == "}":
                    if top != "{":
                        return False
                    stack.pop()
                else:
                    stack.append(c)

        return not stack


print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))