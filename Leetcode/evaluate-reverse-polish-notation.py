from typing import List
import math

class Solution:

    ops = [
        '+',
        '-',
        '*',
        '/'
    ]


    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:

            if token not in self.ops:
                s.append(token)

            else:
                first, second = int(s.pop()), int(s.pop())

                ans = None

fix                if token == '+':
                    ans = second + first
                if token == '-':
                    ans = second - first
                if token == '*':
                    ans = second * first
                if token == '/':
                    ans = second / first
                    ans = math.floor(ans) if ans > 0 else math.ceil(ans)

                s.append(ans)

        return s.pop()


if __name__ == "__main__":
    s = Solution()
    # r = s.evalRPN(["2", "1", "+", "3", "*"])
    # print(r)

    r = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) # 22
    print(r)