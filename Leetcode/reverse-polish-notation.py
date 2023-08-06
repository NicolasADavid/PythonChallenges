from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token in ["+", "-", "/", "*"]:

                val1 = int(stack.pop())
                val2 = int(stack.pop())

                if token == "+":
                    stack.append(val1 + val2)

                if token == "-":
                    stack.append(val2 - val1)

                if token == "/":
                    stack.append(int(val2 / val1))
                
                if token == "*":
                    stack.append(val1 * val2)
                    
            else:
                stack.append(token)

        return int(stack[-1])

if __name__ == "__main__":
    # print(Solution().evalRPN(["2","1","+","3","*"]))
    # print(Solution().evalRPN(["4","13","5","/","+"]))
    # print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(Solution().evalRPN(["4","3","-"]))